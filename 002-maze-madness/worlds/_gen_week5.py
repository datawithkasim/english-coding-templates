"""W5 — Redstone Doors (Iron Door obstacle): 15 mazes.
DSL adds: I = iron door at next forward cell. Action: turn RIGHT, forward 1.
Singles + ANDs from W1-W3 still apply (no ORs in W5).
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

MAZES = [
    (1,  "Review (W1-W3)",       "FFRFFLFFUFFDFFRFFF",          0),
    (2,  "Iron door intro",      "FFIFFFRFFLFFF",               30),
    (3,  "Two iron doors",       "FFRFFIFFFLFFIFFRFFF",         60),
    (4,  "Iron + climb",         "FFUFFIFFFLFFRFFF",            100),
    (5,  "Iron + descent",       "FFDFFIFFFRFFLFFF",            140),
    (6,  "Iron x3",              "FFIFFRFFIFFLFFIFFRFFF",       180),
    (7,  "Iron + AND 1",         "FFIFFF1FFLFFRFFF",            225),
    (8,  "Iron + AND 2",         "FFIFFF2FFLFFRFFF",            265),
    (9,  "Iron + AND 3",         "FFIFFF3FFRFFLFFF",            305),
    (10, "Iron + AND 4 (up5)",   "FFRFFIFFF4FFRFFF",            345),
    (11, "Iron + AND 5",         "FFFFIFFF5FFFLFFF",            385),
    (12, "Iron x4",              "FFIFFLFFIFFRFFIFFLFFIFFRFFF", 430),
    (13, "Iron + climb + RS",    "FFUFFIFFLFFIFFDFFRFFF",       485),
    (14, "Tight iron mix",       "FFRFFIFFLFFIFF1FFRFFF",       525),
    (15, "Boss: iron + all",     "FFIFF1FF2FF3FFIFFRFFLFFUFFDFFF", 575),
]

HEADER = '''# Maze Madness — Week 5: Redstone Doors / Iron Block obstacle
# 15 mazes adding IRON_BLOCK doors. Agent routes around closed doors.
#
# New rule:
#   IRON_BLOCK FORWARD -> turn RIGHT_TURN, move FORWARD 1 (route around)
#
# Solver: ANDs FIRST -> iron door -> singles -> forward.
# (No ORs in W5; ORs introduced separately in W4.)
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.


'''


def trace(moves):
    pos = (0, 0, 0)
    f = "+X"
    path = [pos]
    redstones = []
    iron_doors = []
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
        elif m == "I":
            iron_doors.append(step(pos, f))
            f = turn_right(f); pos = step(pos, f); path.append(pos)
    return path, redstones, iron_doors, pos, f


def build_maze_body(num, name, moves, z_offset):
    path, redstones, iron_doors, end, end_f = trace(moves)
    path = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in path]
    redstones = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in redstones]
    iron_doors = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in iron_doors]
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

    lines = [f"# M{num} - {name}: rs={len(redstones)} iron={len(iron_doors)}",
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
    lines.append(f"    blocks.place({SPAWN_BLOCK}, pos({spawn[0]}, {spawn[1]}, {spawn[2]}))")
    for p in pillar:
        lines.append(f"    blocks.place(GLOWSTONE, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place(DIAMOND_BLOCK, pos({diamond[0]}, {diamond[1]}, {diamond[2]}))")
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves, z))
              for (num, name, moves, z) in MAZES]
    out = write_builder(here, 5, HEADER, bodies,
                        ((2, -4, -15), (35, 15, 700)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
