"""
_gen_maze_world_w5_6.py — Maze Madness Week 5+6 builder.

Output:
  - _builder_week5-6.py  (paste-into-MakeCode source)

Builds 15 mazes that introduce two new mechanics on top of W1-W4:

  W5: REDSTONE DOOR (iron block obstacle)
    Detection: agent.detect_block(IRON_BLOCK, FORWARD)
    Action:    agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
    (route around the closed door)

  W6: LEVER (interact to pass)
    Detection: agent.detect_block(LEVER, FORWARD)
    Action:    agent.interact(); agent.move(FORWARD, 1)
    (lever is a non-solid path block; interact then walk through)

Move-string DSL:
  F = forward, R = turn right + forward, L = turn left + forward
  U = up, D = down
  1..5 = ANDs (W3+W4)
  I = iron door (W5 new)
  V = lever (W6 new)

Solver priority:
  ANDs -> iron door -> lever -> singles (DOWN, UP, LEFT, RIGHT) -> forward
"""

import pathlib

FACINGS = ["+X", "+Z", "-X", "-Z"]
DELTA = {"+X": (1, 0, 0), "+Z": (0, 0, 1), "-X": (-1, 0, 0), "-Z": (0, 0, -1)}

X_OFFSET = 10
PILLAR_HEIGHT = 4


def turn_right(f):
    return FACINGS[(FACINGS.index(f) + 1) % 4]


def turn_left(f):
    return FACINGS[(FACINGS.index(f) - 1) % 4]


def step(p, f):
    dx, dy, dz = DELTA[f]
    return (p[0] + dx, p[1] + dy, p[2] + dz)


def trace(moves):
    pos = (0, 0, 0)
    f = "+X"
    path = [pos]
    redstones = []
    iron_doors = []
    levers = []
    for m in moves:
        if m == "F":
            pos = step(pos, f)
            path.append(pos)
        elif m == "R":
            redstones.append(step(pos, turn_left(f)))
            f = turn_right(f)
            pos = step(pos, f)
            path.append(pos)
        elif m == "L":
            redstones.append(step(pos, turn_right(f)))
            f = turn_left(f)
            pos = step(pos, f)
            path.append(pos)
        elif m == "U":
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2])
            path.append(pos)
        elif m == "D":
            redstones.append((pos[0], pos[1] + 1, pos[2]))
            pos = (pos[0], pos[1] - 1, pos[2])
            path.append(pos)
        elif m == "1":
            redstones.append(step(pos, turn_left(f)))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2])
            f = turn_right(f)
            path.append(pos)
        elif m == "2":
            redstones.append(step(pos, turn_right(f)))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2])
            f = turn_left(f)
            path.append(pos)
        elif m == "3":
            redstones.append(step(pos, f))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2])
            f = turn_right(turn_right(f))
            path.append(pos)
        elif m == "4":
            redstones.append(step(pos, turn_left(f)))
            redstones.append(step(pos, turn_right(f)))
            for _ in range(5):
                pos = (pos[0], pos[1] + 1, pos[2])
                path.append(pos)
        elif m == "5":
            redstones.append((pos[0], pos[1] + 1, pos[2]))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            back_f = turn_right(turn_right(f))
            for _ in range(2):
                pos = step(pos, back_f)
                path.append(pos)
            f = turn_right(f)
            for _ in range(2):
                pos = step(pos, f)
                path.append(pos)
        elif m == "I":  # iron door: block at f-step, agent turns right + forward
            iron_doors.append(step(pos, f))
            f = turn_right(f)
            pos = step(pos, f)
            path.append(pos)
        elif m == "V":  # lever at next path cell, agent interacts + forward through
            pos = step(pos, f)
            path.append(pos)
            levers.append(pos)
    return path, redstones, iron_doors, levers, pos, f


ANDS_WITH_REVISIT = {"5"}


def maze_geometry(num, name, moves, z_offset):
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
    lever_set = set(levers)

    overlap = path_set & redstone_set
    if overlap:
        print(f"WARN M{num} ({name}): redstone-path overlap at {overlap}")
    if iron_set & path_set:
        print(f"WARN M{num} ({name}): iron-path overlap at {iron_set & path_set}")
    if iron_set & redstone_set:
        print(f"WARN M{num} ({name}): iron-redstone overlap at {iron_set & redstone_set}")
    if len(path) != len(set(path)) and not (set(moves) & ANDS_WITH_REVISIT):
        dupes = [c for c in path if path.count(c) > 1]
        print(f"WARN M{num} ({name}): unexpected path self-overlap at {set(dupes)}")

    floor_set = set()
    for (px, py, pz) in path:
        fp = (px, py - 1, pz)
        if fp not in path_set and fp not in redstone_set and fp not in iron_set:
            floor_set.add(fp)

    wall_set = set()
    for (px, py, pz) in path:
        for (ddx, ddz) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, nz = px + ddx, pz + ddz
            for hy in [0, 1]:
                cell = (nx, py + hy, nz)
                if cell not in path_set:
                    wall_set.add(cell)
    wall_set -= redstone_set
    wall_set -= iron_set
    wall_set -= path_set
    wall_set.discard(diamond)

    start = path[0]
    for hy in [0, 1]:
        wall_set.discard((start[0] - 1, start[1] + hy, start[2]))

    spawn = (start[0], start[1] - 1, start[2])
    pillar = [(start[0], start[1] + 2 + i, start[2]) for i in range(PILLAR_HEIGHT)]

    return floor_set, wall_set, redstones, iron_doors, levers, spawn, diamond, len(set(path)), pillar


FLOOR_PALETTE = [
    "LIME_STAINED_GLASS",
    "CYAN_STAINED_GLASS",
    "RED_STAINED_GLASS",
    "YELLOW_STAINED_GLASS",
    "MAGENTA_STAINED_GLASS",
    "ORANGE_STAINED_GLASS",
    "PURPLE_STAINED_GLASS",
    "PINK_STAINED_GLASS",
    "GREEN_STAINED_GLASS",
    "BLUE_STAINED_GLASS",
    "LIGHT_BLUE_STAINED_GLASS",
    "BROWN_STAINED_GLASS",
    "GRAY_STAINED_GLASS",
    "LIGHT_GRAY_STAINED_GLASS",
    "WHITE_STAINED_GLASS",
]
SPAWN_BLOCK = "LIME_STAINED_GLASS"


def gen_maze_py(num, name, geom):
    floor_set, wall_set, redstones, iron_doors, levers, spawn, diamond, path_len, pillar = geom
    floor_block = FLOOR_PALETTE[(num - 1) % len(FLOOR_PALETTE)]
    lines = [
        f"# M{num} - {name}: rs={len(redstones)} iron={len(iron_doors)} lever={len(levers)} cells={path_len} floor={floor_block}",
        f"def build_maze_{num}():",
    ]
    for p in sorted(floor_set):
        lines.append(f"    blocks.place({floor_block}, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in sorted(wall_set):
        lines.append(f"    blocks.place(GLASS, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in redstones:
        lines.append(f"    blocks.place(REDSTONE_BLOCK, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in iron_doors:
        lines.append(f"    blocks.place(IRON_BLOCK, pos({p[0]}, {p[1]}, {p[2]}))")
        lines.append(f"    blocks.place(IRON_BLOCK, pos({p[0]}, {p[1] + 1}, {p[2]}))")
    for p in levers:
        lines.append(f"    blocks.place(LEVER, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place({SPAWN_BLOCK}, pos({spawn[0]}, {spawn[1]}, {spawn[2]}))")
    for p in pillar:
        lines.append(f"    blocks.place(GLOWSTONE, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place(DIAMOND_BLOCK, pos({diamond[0]}, {diamond[1]}, {diamond[2]}))")
    return "\n".join(lines) + "\n\n"


# Curriculum:
#   M1-M2: review (W1-W4 only)
#   M3-M5: introduce IRON DOOR (W5 mechanic)
#   M6-M8: introduce LEVER (W6 mechanic)
#   M9-M12: combine iron + lever
#   M13-M15: full mix incl. ANDs + singles
MAZES = [
    (1,  "Review singles (W1+W2)",    "FFRFFLFFUFFDFFRFFLFFF",          0),
    (2,  "Review ANDs (W3+W4)",       "FF1FFF2FFF3FFF",                 35),
    (3,  "Iron door intro",           "FFIFFFRFFLFFF",                  75),
    (4,  "Two iron doors",            "FFRFFIFFFLFFIFFRFFF",            115),
    (5,  "Iron + climb",              "FFUFFIFFFLFFRFFF",               160),
    (6,  "Lever intro",               "FFVFFFLFFRFFF",                  200),
    (7,  "Two levers",                "FFVFFRFFVFFLFFF",                235),
    (8,  "Lever + climb",             "FFUFFVFFFLFFVFFF",               275),
    (9,  "Iron + lever",              "FFIFFFVFFLFFRFFF",               320),
    (10, "Lever then iron",           "FFVFFIFFFRFFLFFF",               360),
    (11, "Iron + AND",                "FFIFFF1FFLFFRFFF",               400),
    (12, "Lever + AND",               "FFVFF2FFFRFFLFFF",               440),
    (13, "Iron + Lever + AND",        "FFIFFVFF3FFFLFFRFFF",            480),
    (14, "Tight mix",                 "FFRFFIFFVFFLFF1FFRFFF",          525),
    (15, "Final Boss: ALL types",     "FFIFFVFF1FFRFFLFF2FFIFFVFFUFFDFFF", 575),
]


HEADER_PY = '''# Maze Madness - Week 5+6: 15 Mazes with Iron Doors + Levers
# Auto-generated by _gen_maze_world_w5_6.py - do NOT edit by hand.
# Paste this whole file into MakeCode for Minecraft Education (Python).
# Stand on flat ground facing east (+X). Press Play.
# Chat:
#   build1   = build all 15 mazes (slow ~minute)
#   m1..m15  = build a single maze
#   clear    = wipe build zone
#
# Solution rule (student writes in homework, NOT here):
#   PRIORITY: ANDs first, then iron door, then lever, then singles, then forward.
#
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       # ANDs (W3+W4)
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
#       # New W5: iron door
#       elif agent.detect_block(IRON_BLOCK, FORWARD):
#           agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
#       # New W6: lever
#       elif agent.detect_block(LEVER, FORWARD):
#           agent.interact(); agent.move(FORWARD, 1)
#       # Singles (W1+W2)
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


'''


def build_py(geoms):
    body = HEADER_PY
    for (num, name, _, _), geom in geoms:
        body += gen_maze_py(num, name, geom)

    body += "def clear_zone():\n"
    body += "    blocks.fill(AIR, pos(2, -4, -15), pos(35, 15, 700), FillOperation.REPLACE)\n"
    body += "    blocks.fill(GRASS, pos(2, -5, -15), pos(35, -5, 700), FillOperation.REPLACE)\n\n\n"

    body += "def on_chat_build_all():\n    clear_zone()\n"
    for (num, _, _, _), _ in geoms:
        body += f"    build_maze_{num}()\n"
    body += '    player.say("15 mazes built. mazes 15 done!")\n'
    body += 'player.on_chat("build1", on_chat_build_all)\n\n\n'

    for (num, _, _, _), _ in geoms:
        body += f"def on_chat_m{num}():\n    build_maze_{num}()\n"
        body += f'player.on_chat("m{num}", on_chat_m{num})\n\n'

    body += "def on_chat_clr():\n    clear_zone()\n"
    body += 'player.on_chat("clear", on_chat_clr)\n'
    return body


def main():
    here = pathlib.Path(__file__).parent

    geoms = [(m, maze_geometry(m[0], m[1], m[2], m[3])) for m in MAZES]

    py_src = build_py(geoms)
    py_out = here / "_builder_week5-6.py"
    py_out.write_text(py_src, encoding="utf-8")
    print(f"Wrote {py_out} ({py_out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves, z_off), geom in geoms:
        floor_set, wall_set, redstones, iron_doors, levers, _, _, path_len, _ = geom
        print(f"  M{num:2d} z={z_off:3d}  {name:30s}  rs={len(redstones):2d}  iron={len(iron_doors):2d}  lever={len(levers):2d}  cells={path_len:3d}")


if __name__ == "__main__":
    main()
