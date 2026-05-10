"""W1 — While Loops: 15 straight corridors of varying length.
Solver: while not detect(DIAMOND_BLOCK, FORWARD): move(FORWARD, 1)
"""
import pathlib
from _maze_lib import (X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

# (num, name, length, z_offset)
MAZES = [
    (1,  "5블록 / Length 5",   5,   0),
    (2,  "7블록 / Length 7",   7,   20),
    (3,  "10블록 / Length 10", 10,  40),
    (4,  "12블록 / Length 12", 12,  60),
    (5,  "15블록 / Length 15", 15,  85),
    (6,  "18블록 / Length 18", 18,  110),
    (7,  "22블록 / Length 22", 22,  140),
    (8,  "25블록 / Length 25", 25,  170),
    (9,  "30블록 / Length 30", 30,  205),
    (10, "35블록 / Length 35", 35,  245),
    (11, "40블록 / Length 40", 40,  290),
    (12, "45블록 / Length 45", 45,  340),
    (13, "50블록 / Length 50", 50,  395),
    (14, "60블록 / Length 60", 60,  455),
    (15, "80블록 / Length 80", 80,  525),
]

HEADER = '''# Maze Madness — Week 1: While Loops (벽까지 자동 이동)
# 15 straight corridors of varying length. Agent walks forward until DIAMOND.
#
# Solver:
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       agent.move(FORWARD, 1)
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.
# Maze builds 10 blocks east of player.


'''


def build_maze_body(num, name, length, z_offset):
    path_set = set((X_OFFSET + i, 0, z_offset) for i in range(length))
    floor_set = floor_for_path(path_set)
    end_x = X_OFFSET + length - 1
    diamond = (end_x + 1, 0, z_offset)
    wall_set = wall_set_for_path(path_set)
    wall_set.discard(diamond)
    start = (X_OFFSET, 0, z_offset)
    open_entry(wall_set, start)
    spawn = (start[0], -1, z_offset)
    pillar = pillar_for_start(start)
    floor_block = FLOOR_PALETTE[(num - 1) % 15]

    lines = [f"# M{num} - {name}", f"def build_maze_{num}():"]
    for p in sorted(floor_set):
        lines.append(f"    blocks.place({floor_block}, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in sorted(wall_set):
        lines.append(f"    blocks.place(GLASS, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place({SPAWN_BLOCK}, pos({spawn[0]}, {spawn[1]}, {spawn[2]}))")
    for p in pillar:
        lines.append(f"    blocks.place(GLOWSTONE, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place(DIAMOND_BLOCK, pos({diamond[0]}, {diamond[1]}, {diamond[2]}))")
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, length, z))
              for (num, name, length, z) in MAZES]
    out = write_builder(here, 1, HEADER, bodies,
                        ((2, -4, -10), (110, 8, 620)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
