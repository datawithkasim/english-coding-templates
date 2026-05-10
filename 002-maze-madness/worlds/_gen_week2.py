"""W2 — 3D Movement (L+R+U+D): 15 mazes adding vertical signposts.
Solver:
  while not detect(DIAMOND, FORWARD):
    if RS DOWN: move UP 1
    elif RS UP: move DOWN 1
    elif RS LEFT: turn RIGHT, forward 1
    elif RS RIGHT: turn LEFT, forward 1
    else: forward 1
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

# DSL: F, L, R, U, D.
MAZES = [
    (1,  "Review L+R",          "FFLFFFRFFF",                                 0),
    (2,  "First climb (U)",     "FFUFFFLFFF",                                 25),
    (3,  "First descent (D)",   "FFDFFFRFFF",                                 50),
    (4,  "L+R+U",               "FFRFFUFFLFFF",                               75),
    (5,  "L+R+D",               "FFLFFDFFRFFF",                               100),
    (6,  "All 4 types",         "FFRFFUFFLFFDFFRFFF",                         130),
    (7,  "Climb weave",         "FFUFFLFFUFFRFFUFFF",                         165),
    (8,  "Descent weave",       "FFDFFRFFDFFLFFDFFF",                         200),
    (9,  "Up-down weave",       "FFUFFDFFUFFDFFRFFF",                         235),
    (10, "Mix all types",       "FFRFFUFFLFFDFFRFFLFFUFFF",                   270),
    (11, "Long mix",            "FFRFFLFFUFFDFFRFFLFFUFFDFFRFFF",             315),
    (12, "Tight mix",           "FRFLFUFRFLFDFRFLFFF",                        365),
    (13, "Climb tower",         "FFUFFUFFRFFLFFDFFDFFLFFRFFF",                400),
    (14, "Long descent",        "FFDFFDFFLFFRFFUFFUFFRFFLFFF",                445),
    (15, "Boss: 3D snake",      "FFRFFUFFLFFDFFRFFUFFLFFDFFRFFUFFLFFDFFF",    490),
]

HEADER = '''# Maze Madness — Week 2: 3D Movement (L+R+U+D)
# 15 mazes adding vertical (UP/DOWN) signposts to W1's L+R turns.
#
# Signpost rules:
#   RS DOWN  -> move UP 1     (climb)
#   RS UP    -> move DOWN 1   (drop)
#   RS LEFT  -> turn RIGHT, forward 1
#   RS RIGHT -> turn LEFT,  forward 1
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


def build_maze_body(num, name, moves, z_offset):
    path, redstones, end, end_f = trace(moves)
    path = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in path]
    redstones = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in redstones]
    end = (end[0] + X_OFFSET, end[1], end[2] + z_offset)
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
                        ((2, -4, -15), (40, 15, 600)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
