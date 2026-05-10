"""W1-W4 combined: 35-maze progressive curriculum.

Difficulty ramp:
  M1-4   simple L/R turns only (RS LEFT -> turn right, RS RIGHT -> turn left)
  M5-8   add U/D singles (RS DOWN -> up, RS UP -> down)
  M9-13  dense L+R+U+D mix (singles in any combination)
  M14-19 OR conditions (S = side-OR, T = vertical-OR; split paths)
  M20-24 AND conditions (1-3: L+D, R+D, F+D)
  M25-29 advanced ANDs (4 = up5, 5 = back+turn+forward) + mixed paths
  M30-35 boss tier: long mazes mixing every mechanic

Solver priority (student writes once, applies to all):
  ANDs (1-5) -> ORs (S, T) -> singles (D, U, L, R) -> default forward.

DSL: F, R, L, U, D, 1, 2, 3, 4, 5, S, T.
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start)

# Grid layout: 4 rows (forward +X) x 10 cols (left -Z from player facing east).
# Row spacing = 50 in X, col spacing = 40 in Z (negative direction = left).
ROW_SPACING_X = 50
COL_SPACING_Z = 40
GRID_X_BASE = 10  # first row at x=10 (10 blocks east of player)


def grid_position(num):
    """Return (x_offset, z_offset) for maze 1..35 in 4x10 grid."""
    idx = num - 1
    row = idx // 10           # 0..3
    col = idx % 10            # 0..9
    x_off = GRID_X_BASE + row * ROW_SPACING_X
    z_off = -col * COL_SPACING_Z  # mazes spread to player's LEFT
    return x_off, z_off


# (num, name, moves) — z/x derived from grid_position(num)
MAZES = [
    # M1-4 — simple L/R only
    (1,  "L turn intro",            "FFLFFF"),
    (2,  "R turn intro",            "FFRFFF"),
    (3,  "L then R",                "FFLFFRFFF"),
    (4,  "R then L",                "FFRFFLFFF"),

    # M5-8 — add U/D singles
    (5,  "First climb (U)",         "FFUFFFLFFF"),
    (6,  "First descent (D)",       "FFDFFFRFFF"),
    (7,  "Climb + turn",            "FFRFFUFFLFFF"),
    (8,  "Descent + turn",          "FFLFFDFFRFFF"),

    # M9-13 — dense L+R+U+D
    (9,  "All 4 singles",           "FFRFFUFFLFFDFFRFFF"),
    (10, "Climb weave",             "FFUFFLFFUFFRFFUFFF"),

    # M11-13 wrap to row 1 (forward from player)
    (11, "Drop weave",              "FFDFFRFFDFFLFFDFFF"),
    (12, "Long L/R snake",          "FFRFFLFFRFFLFFRFFLFFF"),
    (13, "Zigzag 3D",               "FFUFFRFFDFFLFFUFFRFFDFFF"),

    # M14-19 — OR conditions
    (14, "OR side intro (S)",       "FFSFFFLFFF"),
    (15, "OR vertical intro (T)",   "FFTFFFRFFF"),
    (16, "Two side-ORs",            "FFSFFFSFFLFFRFFF"),
    (17, "Side + vertical OR",      "FFSFFTFFLFFRFFF"),
    (18, "Triple side-ORs",         "FFSFFRFFSFFLFFSFFF"),
    (19, "OR + singles",            "FFRFFSFFUFFTFFLFFF"),

    # M20-24 — AND conditions (1-3)
    (20, "AND #1 (L+D)",            "FF1FFFLFFRFFF"),
    (21, "AND #2 (R+D)",            "FF2FFFLFFRFFF"),
    (22, "AND #3 (F+D)",            "FF3FFFRFFLFFF"),
    (23, "ANDs 1+2",                "FF1FFF2FFLFFF"),
    (24, "AND + singles",           "FFRFF1FFLFFUFFRFFF"),

    # M25-29 — advanced ANDs (4, 5) + mixes
    (25, "AND #4 (L+R up5)",        "FF4FFFRFFLFFF"),
    (26, "AND #5 (U+D back)",       "FFFF5FFFLFFRFFF"),
    (27, "ANDs 1+4+5 mix",          "FFF1FFF4FFF5FFLFFF"),
    (28, "ANDs 2+3 + OR",           "FFF2FFF3FFSFFRFFF"),
    (29, "Tight ANDs",              "FFF1FFF2FFF3FFLFFF"),

    # M30-35 — full mix, advanced
    (30, "Full singles + ANDs",     "FFRFFLFFUFFDFF1FF2FF3FFRFFF"),
    (31, "ORs + ANDs combo",        "FFSFFTFF1FF2FFRFFLFFF"),
    (32, "Long 3D climb mix",       "FFUFFRFFUFFLFFUFFDFFRFFLFFUFFDFFF"),
    (33, "Snake + OR + AND",        "FFRFFSFFLFFTFF1FFRFFLFFUFFDFFF"),
    (34, "AND 4+5 + OR mix",        "FFFFSFF4FFTFF5FFLFFRFFF"),
    (35, "Final Boss (all types)",  "FFRFFLFFUFFDFF1FF2FF3FF4FF5FFSFFTFFLFFRFFF"),
]


HEADER = '''# Maze Madness — Weeks 1-4 Combined: 35 Progressive Mazes
# Auto-generated. One world covers W1 (turns), W2 (3D), W3 (AND), W4 (OR).
#
# Solver priority — student writes ONCE, applies to all 35 mazes:
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       # ANDs FIRST (most specific):
#       if agent.detect_block(REDSTONE_BLOCK, LEFT) and agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(UP, 1); agent.turn(RIGHT_TURN)
#       elif agent.detect_block(REDSTONE_BLOCK, RIGHT) and agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(UP, 1); agent.turn(LEFT_TURN)
#       elif agent.detect_block(REDSTONE_BLOCK, FORWARD) and agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(UP, 1); agent.turn(RIGHT_TURN); agent.turn(RIGHT_TURN)
#       elif agent.detect_block(REDSTONE_BLOCK, LEFT) and agent.detect_block(REDSTONE_BLOCK, RIGHT):
#           agent.move(UP, 5)
#       elif agent.detect_block(REDSTONE_BLOCK, UP) and agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(BACK, 2); agent.turn(RIGHT_TURN); agent.move(FORWARD, 2)
#       # ORs:
#       elif agent.detect_block(REDSTONE_BLOCK, LEFT) or agent.detect_block(REDSTONE_BLOCK, RIGHT):
#           agent.move(FORWARD, 2)
#       elif agent.detect_block(REDSTONE_BLOCK, UP) or agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.turn(RIGHT_TURN); agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
#       # Singles:
#       elif agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(UP, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, UP):
#           agent.move(DOWN, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, LEFT):
#           agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, RIGHT):
#           agent.turn(LEFT_TURN); agent.move(FORWARD, 1)
#       else:
#           agent.move(FORWARD, 1)
#
# Stand facing east (+X). Chat: build1 / m1..m35 / clear.
#
# Grid layout: 35 mazes arranged in a 4-row x 10-col grid.
#   Row direction: +X (forward from player; rows 50 blocks apart)
#   Col direction: -Z (left of player facing east; cols 40 blocks apart)
#   Row 0 (M1-10):  x=10,  cols z=0..-360
#   Row 1 (M11-20): x=60,  cols z=0..-360
#   Row 2 (M21-30): x=110, cols z=0..-360
#   Row 3 (M31-35): x=160, cols z=0..-160


'''


def trace(moves):
    pos = (0, 0, 0); f = "+X"; path = [pos]; redstones = []
    s_count, t_count = 0, 0
    for m in moves:
        if m == "F":
            pos = step(pos, f); path.append(pos)
        elif m == "R":
            redstones.append(step(pos, turn_left(f)))
            f = turn_right(f); pos = step(pos, f); path.append(pos)
        elif m == "L":
            redstones.append(step(pos, turn_right(f)))
            f = turn_left(f); pos = step(pos, f); path.append(pos)
        elif m == "U":
            redstones.append((pos[0], pos[1]-1, pos[2]))
            pos = (pos[0], pos[1]+1, pos[2]); path.append(pos)
        elif m == "D":
            redstones.append((pos[0], pos[1]+1, pos[2]))
            pos = (pos[0], pos[1]-1, pos[2]); path.append(pos)
        elif m == "1":
            redstones.append(step(pos, turn_left(f)))
            redstones.append((pos[0], pos[1]-1, pos[2]))
            pos = (pos[0], pos[1]+1, pos[2]); f = turn_right(f); path.append(pos)
        elif m == "2":
            redstones.append(step(pos, turn_right(f)))
            redstones.append((pos[0], pos[1]-1, pos[2]))
            pos = (pos[0], pos[1]+1, pos[2]); f = turn_left(f); path.append(pos)
        elif m == "3":
            redstones.append(step(pos, f))
            redstones.append((pos[0], pos[1]-1, pos[2]))
            pos = (pos[0], pos[1]+1, pos[2]); f = turn_right(turn_right(f)); path.append(pos)
        elif m == "4":
            redstones.append(step(pos, turn_left(f)))
            redstones.append(step(pos, turn_right(f)))
            for _ in range(5):
                pos = (pos[0], pos[1]+1, pos[2]); path.append(pos)
        elif m == "5":
            redstones.append((pos[0], pos[1]+1, pos[2]))
            redstones.append((pos[0], pos[1]-1, pos[2]))
            back_f = turn_right(turn_right(f))
            for _ in range(2):
                pos = step(pos, back_f); path.append(pos)
            f = turn_right(f)
            for _ in range(2):
                pos = step(pos, f); path.append(pos)
        elif m == "S":
            if s_count % 2 == 0:
                redstones.append(step(pos, turn_left(f)))
            else:
                redstones.append(step(pos, turn_right(f)))
            s_count += 1
            pos = step(pos, f); path.append(pos)
            pos = step(pos, f); path.append(pos)
        elif m == "T":
            if t_count % 2 == 0:
                redstones.append((pos[0], pos[1]+1, pos[2]))
            else:
                redstones.append((pos[0], pos[1]-1, pos[2]))
            t_count += 1
            f = turn_right(turn_right(f))
            pos = step(pos, f); path.append(pos)
    return path, redstones, pos, f


def build_maze_body(num, name, moves):
    x_off, z_off = grid_position(num)
    path, redstones, end, end_f = trace(moves)
    path = [(x + x_off, y, z + z_off) for (x, y, z) in path]
    redstones = [(x + x_off, y, z + z_off) for (x, y, z) in redstones]
    end = (end[0] + x_off, end[1], end[2] + z_off)
    dx, dy, dz = DELTA[end_f]
    diamond = (end[0] + dx, end[1] + dy, end[2] + dz)

    path_set = set(path)
    redstone_set = set(redstones)
    floor_set = floor_for_path(path_set, [redstone_set])
    wall_set = wall_set_for_path(path_set, [redstone_set])
    wall_set.discard(diamond)
    start = path[0]
    open_entry(wall_set, start)
    spawn = (start[0], start[1] - 1, start[2])
    pillar = pillar_for_start(start)
    floor_block = FLOOR_PALETTE[(num - 1) % 15]

    lines = [f"# M{num} - {name}: {len(redstones)} RS",
             f"def build_maze_{num}():"]
    for p in sorted(floor_set):
        lines.append(f"    blocks.place({floor_block}, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in sorted(wall_set):
        lines.append(f"    blocks.place(GLASS, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in redstones:
        lines.append(f"    blocks.place(REDSTONE_BLOCK, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place({SPAWN_BLOCK}, pos({spawn[0]}, {spawn[1]}, {spawn[2]}))")
    for p in pillar:
        lines.append(f"    blocks.place(GLOWSTONE, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place(DIAMOND_BLOCK, pos({diamond[0]}, {diamond[1]}, {diamond[2]}))")
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    out_lines = [HEADER]
    for (num, name, moves) in MAZES:
        out_lines.append(build_maze_body(num, name, moves))

    # Grid bounds: 4 rows in +X (10..220), 10 cols in -Z (0..-380), with buffer
    out_lines.append("def clear_zone():")
    out_lines.append("    blocks.fill(AIR, pos(2, -4, -420), pos(225, 15, 30), FillOperation.REPLACE)")
    out_lines.append("    blocks.fill(GRASS, pos(2, -5, -420), pos(225, -5, 30), FillOperation.REPLACE)\n\n")

    out_lines.append("def on_chat_build_all():")
    out_lines.append("    clear_zone()")
    for (num, _, _) in MAZES:
        out_lines.append(f"    build_maze_{num}()")
    out_lines.append('    player.say("35 mazes built. 미로 35개 완성!")')
    out_lines.append('player.on_chat("build1", on_chat_build_all)\n\n')

    for (num, _, _) in MAZES:
        out_lines.append(f"def on_chat_m{num}():")
        out_lines.append(f"    build_maze_{num}()")
        out_lines.append(f'player.on_chat("m{num}", on_chat_m{num})\n')

    out_lines.append("\ndef on_chat_clr():")
    out_lines.append("    clear_zone()")
    out_lines.append('player.on_chat("clear", on_chat_clr)')

    py_src = "\n".join(out_lines)
    out_path = here / "_builder_weeks1to4.py"
    out_path.write_text(py_src, encoding="utf-8")
    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves) in MAZES:
        path, redstones, _, _ = trace(moves)
        x_off, z_off = grid_position(num)
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d})  {name:30s}  rs={len(redstones):2d}  path={len(path):3d}")


if __name__ == "__main__":
    main()
