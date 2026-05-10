"""W1 — Simple L/R/U/D singles: 15 mazes.
DSL: F, L, R, U, D (no ANDs, no ORs).

Signpost rules (consistent across all 15 mazes):
  RS on LEFT  -> turn RIGHT, forward 1
  RS on RIGHT -> turn LEFT,  forward 1
  RS DOWN     -> move UP 1   (climb)
  RS UP       -> move DOWN 1 (drop)
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

# (num, name, moves) — z derived from grid_position(num)
MAZES = [
    (1,  "L turn intro",       "FFLFFF"),
    (2,  "R turn intro",       "FFRFFF"),
    (3,  "L then R",           "FFLFFRFFF"),
    (4,  "R then L",           "FFRFFLFFF"),
    (5,  "First climb (U)",    "FFUFFFLFFF"),
    (6,  "First descent (D)",  "FFDFFFRFFF"),
    (7,  "Climb + turn",       "FFRFFUFFLFFF"),
    (8,  "Descent + turn",     "FFLFFDFFRFFF"),
    (9,  "All 4 singles",      "FFRFFUFFLFFDFFRFFF"),
    (10, "Climb weave",        "FFUFFLFFUFFRFFUFFF"),
    (11, "Drop weave",         "FFDFFRFFDFFLFFDFFF"),
    (12, "L/R snake",          "FFRFFLFFRFFLFFRFFF"),
    (13, "Climb tower",        "FFUFFUFFRFFLFFDFFDFFRFFF"),
    (14, "Long descent",       "FFDFFDFFLFFRFFUFFUFFLFFRFFF"),
    (15, "3D snake boss",      "FFRFFUFFLFFDFFRFFUFFLFFDFFF"),
]


# Grid: 2 rows x 8 cols (last row 7 mazes for 15 total)
ROW_SPACING_X = 50
COL_SPACING_Z = 40


def grid_position(num):
    """Return (x_offset, z_offset) for maze 1..15. Row 0: M1-8, Row 1: M9-15."""
    idx = num - 1
    row = idx // 8        # 0..1
    col = idx % 8         # 0..7
    x_off = 10 + row * ROW_SPACING_X
    z_off = -col * COL_SPACING_Z
    return x_off, z_off


HEADER = '''# Maze Madness — Week 1: Simple L/R/U/D Singles (15 mazes)
# Auto-generated. NO AND/OR conditions; only single-redstone signposts.
#
# Signpost rules:
#   RS on LEFT  -> turn RIGHT, forward 1
#   RS on RIGHT -> turn LEFT,  forward 1
#   RS DOWN     -> move UP 1
#   RS UP       -> move DOWN 1
#
# Solver:
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       if agent.detect_block(REDSTONE_BLOCK, DOWN):
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
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.
#
# Grid layout: 2 rows x 8 cols (last row 7 mazes).
#   Row 0 (M1-8):  x=10,  cols z=0..-280
#   Row 1 (M9-15): x=60,  cols z=0..-240


'''


def trace(moves):
    pos = (0, 0, 0); f = "+X"; path = [pos]; redstones = []
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

    lines = [f"# M{num} - {name}: {len(redstones)} redstones",
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
    bodies = [(num, build_maze_body(num, name, moves))
              for (num, name, moves) in MAZES]
    out = write_builder(here, 1, HEADER, bodies,
                        ((2, -4, -320), (130, 12, 30)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves) in MAZES:
        path, redstones, _, _ = trace(moves)
        x_off, z_off = grid_position(num)
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d})  {name:25s}  rs={len(redstones):2d}  path={len(path):3d}")


if __name__ == "__main__":
    main()
