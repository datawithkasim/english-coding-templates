"""W8 — Final Boss: 15x15x15 Redstone Cube Maze.
DSL combines ALL mechanics: F R L U D 1 2 3 4 5 S T I V.
15 ramp-up mazes culminating in a fully 3D cube challenge.
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

MAZES = [
    (1,  "Singles + ANDs review",        "FFRFFLFFUFFDFF1FF2FFRFFF",                 0),
    (2,  "ORs review",                    "FFSFFTFFRFFLFFF",                          40),
    (3,  "Iron + lever review",           "FFIFFVFFRFFLFFF",                          80),
    (4,  "Mix singles+iron+lever",        "FFRFFIFFLFFVFFRFFF",                       120),
    (5,  "ANDs + iron",                   "FF1FFIFF2FFRFFLFFF",                       165),
    (6,  "ORs + lever",                   "FFSFFVFFTFFLFFF",                          210),
    (7,  "AND+OR+iron+lever",             "FF1FFSFFIFFVFFRFFF",                       250),
    (8,  "Triple ANDs",                   "FF1FF2FF3FFLFFRFFF",                       295),
    (9,  "Triple ORs",                    "FFSFFTFFSFFTFFLFFF",                       340),
    (10, "Iron x3 + lever x3",            "FFIFFVFFIFFVFFIFFVFFLFFF",                 385),
    (11, "ANDs+ORs+iron+lever",           "FF1FFSFF2FFIFFTFFVFFLFFF",                 435),
    (12, "AND 4 (up5) + iron + lever",    "FFRFF4FFIFFVFFLFFF",                       490),
    (13, "AND 5 (back) + ORs",            "FFFF5FFSFFTFFLFFF",                        555),
    (14, "Climb 3D + all",                "FFUFFIFFVFFUFF1FF2FFLFFRFFF",              610),
    (15, "Cube boss: 15x15x15 mix",       "FF1FF2FF3FFSFFTFFIFFVFFRFFLFFUFFDFF1FFF",  675),
]

HEADER = '''# Maze Madness — Week 8: Final Boss / 15x15x15 Redstone Cube Maze
# 15 ramp-up mazes culminating in a fully 3D cube combining all mechanics.
# Mechanics: singles (R/L/U/D) + ANDs (1-5) + ORs (S/T) + iron (I) + lever (V).
#
# Solver order (priority):
#   ANDs FIRST -> ORs -> iron door -> lever -> singles -> forward.
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.


'''


def trace(moves):
    pos = (0, 0, 0); f = "+X"; path = [pos]
    redstones, iron_doors, levers = [], [], []
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
        elif m == "I":
            iron_doors.append(step(pos, f))
            f = turn_right(f); pos = step(pos, f); path.append(pos)
        elif m == "V":
            pos = step(pos, f); path.append(pos); levers.append(pos)
    return path, redstones, iron_doors, levers, pos, f


def build_maze_body(num, name, moves, z_offset):
    path, redstones, iron_doors, levers, end, end_f = trace(moves)
    path = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in path]
    redstones = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in redstones]
    iron_doors = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in iron_doors]
    levers = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in levers]
    end = (end[0] + X_OFFSET, end[1], end[2] + z_offset)
    dx, dy, dz = DELTA[end_f]
    diamond = (end[0] + dx, end[1] + dy, end[2] + dz)

    path_set = set(path)
    redstone_set = set(redstones)
    iron_set = set(iron_doors)
    floor_set = floor_for_path(path_set, [redstone_set, iron_set])
    wall_set = wall_set_for_path(path_set, [redstone_set, iron_set])
    wall_set.discard(diamond)
    start = path[0]
    open_entry(wall_set, start)
    spawn = (start[0], start[1] - 1, start[2])
    pillar = pillar_for_start(start)
    floor_block = FLOOR_PALETTE[(num - 1) % 15]

    lines = [f"# M{num} - {name}: rs={len(redstones)} iron={len(iron_doors)} lever={len(levers)}",
             f"def build_maze_{num}():"]
    for p in sorted(floor_set):
        lines.append(f"    blocks.place({floor_block}, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in sorted(wall_set):
        lines.append(f"    blocks.place(GLASS, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in redstones:
        lines.append(f"    blocks.place(REDSTONE_BLOCK, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in iron_doors:
        lines.append(f"    blocks.place(IRON_BLOCK, pos({p[0]}, {p[1]}, {p[2]}))")
        lines.append(f"    blocks.place(IRON_BLOCK, pos({p[0]}, {p[1]+1}, {p[2]}))")
    for p in levers:
        lines.append(f"    blocks.place(LEVER, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place({SPAWN_BLOCK}, pos({spawn[0]}, {spawn[1]}, {spawn[2]}))")
    for p in pillar:
        lines.append(f"    blocks.place(GLOWSTONE, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place(DIAMOND_BLOCK, pos({diamond[0]}, {diamond[1]}, {diamond[2]}))")
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves, z))
              for (num, name, moves, z) in MAZES]
    out = write_builder(here, 8, HEADER, bodies,
                        ((2, -4, -20), (45, 20, 800)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
