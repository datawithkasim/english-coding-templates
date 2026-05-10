"""W6 — Lever Interaction: 15 mazes adding LEVER block.
DSL adds: V = lever at next forward path cell. Action: agent.interact() + forward 1.
All previous mechanics still apply.
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

MAZES = [
    (1,  "Review (W1-W5)",          "FFRFFLFFUFFDFFIFFRFFF",          0),
    (2,  "Lever intro",             "FFVFFFLFFRFFF",                  35),
    (3,  "Two levers",              "FFVFFRFFVFFLFFF",                70),
    (4,  "Lever + climb",           "FFUFFVFFFLFFRFFF",               110),
    (5,  "Lever + descent",         "FFDFFVFFFLFFRFFF",               150),
    (6,  "Lever x3",                "FFVFFRFFVFFLFFVFFRFFF",          190),
    (7,  "Lever + iron",            "FFVFFIFFFLFFRFFF",               235),
    (8,  "Iron + lever combo",      "FFIFFVFFFRFFLFFF",               275),
    (9,  "Lever + AND 1",           "FFVFFF1FFLFFRFFF",               315),
    (10, "Lever + AND 2",           "FFVFFF2FFRFFLFFF",               355),
    (11, "Lever + AND 3",           "FFVFFF3FFRFFLFFF",               395),
    (12, "Lever x4",                "FFVFFRFFVFFLFFVFFRFFVFFLFFF",    435),
    (13, "Lever + iron + AND",      "FFVFFIFFF1FFLFFRFFF",            490),
    (14, "Tight lever mix",         "FFVFFIFFVFFLFF1FFRFFF",          535),
    (15, "Boss: lever + all",       "FFVFFIFF1FF2FFVFFRFFLFFUFFDFFF", 585),
]

HEADER = '''# Maze Madness — Week 6: Lever Interaction (레버로 도어 열기)
# 15 mazes adding LEVER blocks. Agent interacts with lever to pass.
#
# New rule:
#   LEVER FORWARD -> agent.interact(); agent.move(FORWARD, 1)
#
# Solver: ANDs FIRST -> iron door -> LEVER -> singles -> forward.
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.


'''


def trace(moves):
    pos = (0, 0, 0)
    f = "+X"
    path = [pos]
    redstones = []
    iron_doors = []
    levers = []
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
    out = write_builder(here, 6, HEADER, bodies,
                        ((2, -4, -15), (35, 15, 700)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
