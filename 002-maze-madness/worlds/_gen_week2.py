"""W2 — Turning at Walls: 15 mazes with L/R turns (no vertical, no ANDs).
Solver:
  while not detect(DIAMOND, FORWARD):
    if RS LEFT: turn RIGHT
    elif RS RIGHT: turn LEFT
    move FORWARD 1
"""
import pathlib
from _maze_lib import (FACINGS, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

# DSL: F, L, R only.
MAZES = [
    (1,  "1 turn (L)",       "FFFLFFF",                            0),
    (2,  "1 turn (R)",       "FFFRFFF",                            25),
    (3,  "2 turns L+R",      "FFLFFRFFF",                          50),
    (4,  "3 turns",          "FFRFFLFFRFFF",                       75),
    (5,  "4 turns",          "FFLFFRFFLFFRFFF",                    105),
    (6,  "5 turns",          "FFRFFLFFRFFLFFRFFF",                 140),
    (7,  "6 turns",          "FFLFFRFFLFFRFFLFFRFFF",              175),
    (8,  "7 turns",          "FFRFFLFFRFFLFFRFFLFFRFFF",           210),
    (9,  "8 turns dense",    "FRFLFRFLFRFLFRFLFFF",                250),
    (10, "9 turns long",     "FFRFFLFFRFFLFFRFFLFFRFFLFFRFFF",     285),
    (11, "10 turns weave",   "FFLFFRFFLFFRFFLFFRFFLFFRFFLFFRFFF",  330),
    (12, "11 turns drift",   "FRFLFRFLFRFLFRFLFRFLFFFLFRFFF",      375),
    (13, "12 turns tight",   "FRLRLRLRLRLRLRLRLFFF",               420),
    (14, "13 turns mix",     "FFRFFLFLFRFRFLFLFRFRFLFLFRFFF",      465),
    (15, "14 turns boss",    "FRFLFRFLFRFLFRFLFRFLFRFLFRFLFFF",    520),
]

HEADER = '''# Maze Madness — Week 2: Turning at Walls (방향 전환)
# 15 mazes with L+R redstone turn signs (no vertical, no ANDs).
#
# Signpost rules:
#   RS on LEFT  -> turn RIGHT, forward 1
#   RS on RIGHT -> turn LEFT,  forward 1
#
# Solver:
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       if agent.detect_block(REDSTONE_BLOCK, LEFT):
#           agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, RIGHT):
#           agent.turn(LEFT_TURN); agent.move(FORWARD, 1)
#       else:
#           agent.move(FORWARD, 1)
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.
# Maze builds 10 blocks east of player.


'''


def trace(moves):
    pos = (0, 0, 0)
    f = "+X"
    path = [pos]
    redstones = []
    for m in moves:
        if m == "F":
            pos = step(pos, f); path.append(pos)
        elif m == "R":
            redstones.append(step(pos, turn_left(f)))
            f = turn_right(f); pos = step(pos, f); path.append(pos)
        elif m == "L":
            redstones.append(step(pos, turn_right(f)))
            f = turn_left(f); pos = step(pos, f); path.append(pos)
    return path, redstones, pos, f


def build_maze_body(num, name, moves, z_offset):
    path, redstones, end, end_f = trace(moves)
    path = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in path]
    redstones = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in redstones]
    end = (end[0] + X_OFFSET, end[1], end[2] + z_offset)
    from _maze_lib import DELTA
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
    bodies = [(num, build_maze_body(num, name, moves, z))
              for (num, name, moves, z) in MAZES]
    out = write_builder(here, 2, HEADER, bodies,
                        ((2, -4, -15), (35, 8, 600)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
