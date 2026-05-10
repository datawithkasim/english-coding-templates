"""W4 — OR Conditions (single path) + 2 simple ANDs: 10 mazes.

Single path mazes (no forks). 3 OR rules + 2 AND multi-step rules.

OR rules (each places RS at one of two detection sides, alternating per move):
  p: RS LEFT or RIGHT  -> agent.move(UP, 1)
  q: RS UP or DOWN     -> agent.move(LEFT, 1)
  r: RS FWD or BACK    -> agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
     (RS placed at FORWARD only — BACK cell is always prior path)

AND rules (multi-step jumps; placement avoids action-geometry collision):
  1: RS LEFT AND RIGHT -> agent.move(UP, 5)
  2: RS UP   AND DOWN  -> agent.move(LEFT, 5)

Solver order (ANDs first, then ORs, then default):
  if detect(LEFT) and detect(RIGHT):  move UP 5
  elif detect(UP) and detect(DOWN):   move LEFT 5
  elif detect(LEFT) or detect(RIGHT): move UP 1
  elif detect(UP) or detect(DOWN):    move LEFT 1
  elif detect(FORWARD) or detect(BACK): turn RIGHT + forward 1
  else: forward 1
"""
import pathlib
from _maze_lib import (DELTA, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)


ENTRY_LEN = 4


def trace(moves):
    pos = (0, 0, 0); f = "+X"
    path = [pos]
    redstones = []
    p_count = 0; q_count = 0
    for m in moves:
        if m == "F":
            pos = step(pos, f); path.append(pos)
        elif m == "L":   # turn left + forward (single, RS at RIGHT)
            redstones.append(step(pos, turn_right(f)))
            f = turn_left(f); pos = step(pos, f); path.append(pos)
        elif m == "R":   # turn right + forward (single, RS at LEFT)
            redstones.append(step(pos, turn_left(f)))
            f = turn_right(f); pos = step(pos, f); path.append(pos)
        elif m == "U":   # move up (single, RS at DOWN)
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2]); path.append(pos)
        elif m == "D":   # move down (single, RS at UP)
            redstones.append((pos[0], pos[1] + 1, pos[2]))
            pos = (pos[0], pos[1] - 1, pos[2]); path.append(pos)
        elif m == "p":   # OR L|R -> up 1
            if p_count % 2 == 0:
                redstones.append(step(pos, turn_left(f)))
            else:
                redstones.append(step(pos, turn_right(f)))
            p_count += 1
            pos = (pos[0], pos[1] + 1, pos[2]); path.append(pos)
        elif m == "q":   # OR U|D -> move LEFT 1 (no facing change)
            if q_count % 2 == 0:
                redstones.append((pos[0], pos[1] + 1, pos[2]))
            else:
                redstones.append((pos[0], pos[1] - 1, pos[2]))
            q_count += 1
            pos = step(pos, turn_left(f)); path.append(pos)
        elif m == "r":   # OR F|B -> turn right + forward 1 (RS at FORWARD only)
            redstones.append(step(pos, f))
            f = turn_right(f); pos = step(pos, f); path.append(pos)
        elif m == "1":   # AND L+R -> move UP 5
            redstones.append(step(pos, turn_left(f)))
            redstones.append(step(pos, turn_right(f)))
            for _ in range(5):
                pos = (pos[0], pos[1] + 1, pos[2]); path.append(pos)
        elif m == "2":   # AND U+D -> move LEFT 5
            redstones.append((pos[0], pos[1] + 1, pos[2]))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            for _ in range(5):
                pos = step(pos, turn_left(f)); path.append(pos)
    return path, redstones, pos, f


# (num, name, moves)
MAZES = [
    (1,  "OR p only (L|R -> up)",          "FFpFFF"),
    (2,  "OR p chained",                   "FFpFFpFFRFFF"),
    (3,  "OR q only (U|D -> left)",        "FFqFFF"),
    (4,  "OR q chained",                   "FFqFFqFFLFFF"),
    (5,  "OR r only (F|B -> turn R)",      "FFFrFFFLFFF"),
    (6,  "OR p + q mix",                   "FFpFFqFFRFFpFFF"),
    (7,  "OR p + q + r mix",               "FFpFFqFFrFFFLFFF"),
    (8,  "AND 1 (L+R -> UP 5)",            "FF1FFF"),
    (9,  "AND 2 (U+D -> LEFT 5)",          "FF2FFRFFF"),
    (10, "Boss: ORs + both ANDs",          "FFpFF1FFqFF2FFrFFFLFFF"),
]


# Grid: 1 row x 10 cols
ROW_SPACING_X = 60
COL_SPACING_Z = 50


def grid_position(num):
    idx = num - 1
    row = idx // 10
    col = idx % 10
    x_off = 10 + ENTRY_LEN + row * ROW_SPACING_X
    z_off = -col * COL_SPACING_Z
    return x_off, z_off


HEADER = '''# Maze Madness — Week 4: OR conditions + multi-step ANDs (10 mazes)
# Single path mazes. 3 OR rules + 2 AND multi-step rules.
#
# OR rules:
#   RS LEFT or RIGHT     -> agent.move(UP, 1)
#   RS UP or DOWN        -> agent.move(LEFT, 1)
#   RS FORWARD or BACK   -> agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
#
# AND multi-step rules (these MUST be checked first — they share signals
# with OR rules but are more specific):
#   RS LEFT AND RIGHT    -> agent.move(UP, 5)
#   RS UP   AND DOWN     -> agent.move(LEFT, 5)
#
# Solver:
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       if agent.detect_block(REDSTONE_BLOCK, LEFT) and agent.detect_block(REDSTONE_BLOCK, RIGHT):
#           agent.move(UP, 5)
#       elif agent.detect_block(REDSTONE_BLOCK, UP) and agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(LEFT, 5)
#       elif agent.detect_block(REDSTONE_BLOCK, LEFT) or agent.detect_block(REDSTONE_BLOCK, RIGHT):
#           agent.move(UP, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, UP) or agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(LEFT, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, FORWARD) or agent.detect_block(REDSTONE_BLOCK, BACK):
#           agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
#       else:
#           agent.move(FORWARD, 1)
#
# Each maze has a 4-cell entry corridor leading INTO the start.
# Stand facing east (+X). Chat: build1 / m1..m10 / clear.


'''


def build_maze_body(num, name, moves):
    x_off, z_off = grid_position(num)
    path, redstones, end, end_f = trace(moves)
    path = [(x + x_off, y, z + z_off) for (x, y, z) in path]
    redstones = [(x + x_off, y, z + z_off) for (x, y, z) in redstones]
    end = (end[0] + x_off, end[1], end[2] + z_off)
    dx, dy, dz = DELTA[end_f]
    diamond = (end[0] + dx, end[1] + dy, end[2] + dz)

    start = path[0]
    entry_cells = [(start[0] - i, start[1], start[2]) for i in range(1, ENTRY_LEN + 1)]

    path_set = set(path) | set(entry_cells)
    redstone_set = set(redstones)

    # Sanity: warn if any redstone overlaps path
    overlap = path_set & redstone_set
    if overlap:
        print(f"WARN M{num}: rs/path overlap at {overlap}")

    floor_set = floor_for_path(path_set, [redstone_set])
    wall_set = wall_set_for_path(path_set, [redstone_set])
    wall_set.discard(diamond)
    entry_far = (start[0] - ENTRY_LEN, start[1], start[2])
    for hy in [0, 1]:
        wall_set.discard((entry_far[0] - 1, entry_far[1] + hy, entry_far[2]))

    spawn = (start[0], start[1] - 1, start[2])
    pillar = pillar_for_start(start)
    floor_block = FLOOR_PALETTE[(num - 1) % 15]

    lines = [
        f"# M{num} - {name}",
        f"# {len(redstones)} redstones, {len(path_set)} path cells (incl. entry)",
        f"def build_maze_{num}():",
    ]
    for p in sorted(path_set):
        lines.append(f"    blocks.place(AIR, pos({p[0]}, {p[1]}, {p[2]}))")
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
    lines.append(f'    player.say("M{num}: {name}")')
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves))
              for (num, name, moves) in MAZES]
    out = write_builder(here, 4, HEADER, bodies,
                        ((2, -10, -520), (90, 25, 30)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves) in MAZES:
        path, rs, _, _ = trace(moves)
        x_off, z_off = grid_position(num)
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d})  rs={len(rs):2d}  path={len(path):3d}  | {name}")


if __name__ == "__main__":
    main()
