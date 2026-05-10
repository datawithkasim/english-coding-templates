"""
_gen_maze_world_w3_4.py — Maze Madness Week 3+4 builder.

Outputs:
  - _builder_week-3.py + _builder_week-4.py   (paste-ready Python source)
  - ../blocks/week-3.mkcd + week-4.mkcd        (full MakeCode projects)

Adds AND-conditions on top of W1+W2's single-redstone rules:

  Singles (W1+W2):
    RS DOWN   -> move UP 1
    RS UP     -> move DOWN 1
    RS LEFT   -> turn RIGHT, forward 1
    RS RIGHT  -> turn LEFT, forward 1

  ANDs (W3+W4 new):
    RS LEFT  + DOWN -> move UP 1, turn RIGHT
    RS RIGHT + DOWN -> move UP 1, turn LEFT
    RS FWD   + DOWN -> move UP 1, turn RIGHT twice (180)
    RS LEFT  + RIGHT -> move UP 5
    RS UP    + DOWN  -> move BACK 2, turn RIGHT, forward 2

Move-string DSL:
  F = forward, R = turn right + forward, L = turn left + forward
  U = up, D = down
  1 = AND L+D, 2 = AND R+D, 3 = AND F+D, 4 = AND L+R, 5 = AND U+D
"""

import json
import pathlib
import zipfile

FACINGS = ["+X", "+Z", "-X", "-Z"]
DELTA = {"+X": (1, 0, 0), "+Z": (0, 0, 1), "-X": (-1, 0, 0), "-Z": (0, 0, -1)}

X_OFFSET = 10  # build 10 blocks east of player so player isn't engulfed
PILLAR_HEIGHT = 4  # GLOWSTONE pillar above start cell for visibility


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
        elif m == "1":  # AND L+D -> up 1, turn right
            redstones.append(step(pos, turn_left(f)))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2])
            f = turn_right(f)
            path.append(pos)
        elif m == "2":  # AND R+D -> up 1, turn left
            redstones.append(step(pos, turn_right(f)))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2])
            f = turn_left(f)
            path.append(pos)
        elif m == "3":  # AND F+D -> up 1, turn 180
            redstones.append(step(pos, f))
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2])
            f = turn_right(turn_right(f))
            path.append(pos)
        elif m == "4":  # AND L+R -> up 5
            redstones.append(step(pos, turn_left(f)))
            redstones.append(step(pos, turn_right(f)))
            for _ in range(5):
                pos = (pos[0], pos[1] + 1, pos[2])
                path.append(pos)
        elif m == "5":  # AND U+D -> back 2, turn right, forward 2
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
    return path, redstones, pos, f


# Moves where path cell revisits are EXPECTED (back-tracking ANDs).
ANDS_WITH_REVISIT = {"5"}


def maze_geometry(num, name, moves, z_offset):
    path, redstones, end, end_f = trace(moves)

    path = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in path]
    redstones = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in redstones]
    end = (end[0] + X_OFFSET, end[1], end[2] + z_offset)

    dx, dy, dz = DELTA[end_f]
    diamond = (end[0] + dx, end[1] + dy, end[2] + dz)

    path_set = set(path)
    redstone_set = set(redstones)

    overlap = path_set & redstone_set
    if overlap:
        print(f"WARN M{num} ({name}): redstone-path overlap at {overlap}")
    if len(path) != len(set(path)) and not (set(moves) & ANDS_WITH_REVISIT):
        dupes = [c for c in path if path.count(c) > 1]
        print(f"WARN M{num} ({name}): unexpected path self-overlap at {set(dupes)}")

    floor_set = set()
    for (px, py, pz) in path:
        fp = (px, py - 1, pz)
        if fp not in path_set and fp not in redstone_set:
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
    wall_set -= path_set
    wall_set.discard(diamond)

    start = path[0]
    for hy in [0, 1]:
        wall_set.discard((start[0] - 1, start[1] + hy, start[2]))

    spawn = (start[0], start[1] - 1, start[2])
    pillar = [(start[0], start[1] + 2 + i, start[2]) for i in range(PILLAR_HEIGHT)]
    return floor_set, wall_set, redstones, spawn, diamond, len(set(path)), pillar


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
    floor_set, wall_set, redstones, spawn, diamond, path_len, pillar = geom
    floor_block = FLOOR_PALETTE[(num - 1) % len(FLOOR_PALETTE)]
    lines = [
        f"# M{num} — {name}: {len(redstones)} redstones, {path_len} unique path cells, floor={floor_block}",
        f"def build_maze_{num}():",
    ]
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


def gen_maze_ts(num, name, geom):
    floor_set, wall_set, redstones, spawn, diamond, path_len, pillar = geom
    floor_block = FLOOR_PALETTE[(num - 1) % len(FLOOR_PALETTE)]
    lines = [
        f"// M{num} — {name}: {len(redstones)} redstones, {path_len} unique path cells, floor={floor_block}",
        f"function build_maze_{num} () {{",
    ]
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
    lines.append("}")
    return "\n".join(lines) + "\n\n"


# Curriculum:
#   M1: review — all W1+W2 conditions, no ANDs
#   M2-M6: ONE AND each (cycle 1->2->3->4->5)
#   M7-M10: TWO ANDs each
#   M11-M14: THREE ANDs each
#   M15: ALL 5 ANDs + W1+W2 singles (boss)
MAZES = [
    (1,  "Review (all W1+W2)",            "FFRFFLFFUFFDFFRFFLFFF",            0),
    (2,  "AND #1: L+D -> up + R turn",     "FF1FFFRFFLFFF",                    25),
    (3,  "AND #2: R+D -> up + L turn",     "FF2FFFLFFRFFF",                    50),
    (4,  "AND #3: F+D -> up + 180",        "FF3FFFRFFLFFF",                    75),
    (5,  "AND #4: L+R -> up 5",            "FF4FFFRFFF",                       100),
    (6,  "AND #5: U+D -> back+R+fwd",      "FFFF5FFFLFFF",                     130),
    (7,  "ANDs #1 + #2",                  "FF1FFF2FFF",                       170),
    (8,  "ANDs #2 + #3",                  "FF2FFF3FFF",                       210),
    (9,  "ANDs #3 + #4",                  "FF3FFF4FF",                        250),
    (10, "ANDs #4 + #5",                  "FF4FFF5FFF",                       290),
    (11, "ANDs #5 + #1 + #2",             "FFF5FFF1FFF2FFF",                  340),
    (12, "ANDs #1 + #4 + #5",             "FFF1FFF4FFF5FFF",                  400),
    (13, "ANDs #2 + #4 + #1",             "FFF2FFF4FFF1FFF",                  460),
    (14, "ANDs #3 + #5 + #2",             "FFF3FFFFF5FFF2FFF",                520),
    (15, "Final Boss: ALL ANDs + W1+W2",  "FF1FF2FF3FF4FF5FFRFFLFFUFFDFFF",   600),
]


HEADER_PY = '''# Maze Madness — Week 3+4: 15 Mazes with AND-conditions
# Auto-generated by _gen_maze_world_w3_4.py — do NOT edit by hand.
# Paste this whole file into MakeCode for Minecraft Education (Python), or open the .mkcd.
# Stand on flat ground facing east (+X). Press Play.
# Chat:
#   build1   = build all 15 mazes (slow — ~minute)
#   m1..m15  = build a single maze
#   clear    = wipe build zone
#
# Solution rule (student writes in homework, NOT here):
#   PRIORITY: ANDs FIRST, then singles, then forward.
#
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       # ANDs first
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
#       # Singles
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

HEADER_TS = '''// Maze Madness — Week 3+4: 15 Mazes with AND-conditions
// Auto-generated by _gen_maze_world_w3_4.py — do NOT edit by hand.


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
    body += '    player.say("15 mazes built. 미로 15개 완성!")\n'
    body += 'player.on_chat("build1", on_chat_build_all)\n\n\n'

    for (num, _, _, _), _ in geoms:
        body += f"def on_chat_m{num}(): build_maze_{num}()\n"
        body += f'player.on_chat("m{num}", on_chat_m{num})\n\n'

    body += "def on_chat_clr(): clear_zone()\n"
    body += 'player.on_chat("clear", on_chat_clr)\n'
    return body


def build_ts(geoms):
    body = HEADER_TS
    for (num, name, _, _), geom in geoms:
        body += gen_maze_ts(num, name, geom)

    body += "function clear_zone () {\n"
    body += "    blocks.fill(AIR, pos(2, -4, -15), pos(35, 15, 700), FillOperation.Replace)\n"
    body += "    blocks.fill(GRASS, pos(2, -5, -15), pos(35, -5, 700), FillOperation.Replace)\n"
    body += "}\n\n"

    body += 'player.onChat("build1", function () {\n'
    body += "    clear_zone()\n"
    for (num, _, _, _), _ in geoms:
        body += f"    build_maze_{num}()\n"
    body += '    player.say("15 mazes built. 미로 15개 완성!")\n'
    body += "})\n\n"

    for (num, _, _, _), _ in geoms:
        body += f'player.onChat("m{num}", function () {{ build_maze_{num}() }})\n'
    body += '\nplayer.onChat("clear", function () { clear_zone() })\n'
    return body


PXT_JSON = {
    "name": "Maze Madness — Week 3+4",
    "description": "15 mazes with AND-conditions (W3+W4). 미로 3-4주차 월드 빌더.",
    "dependencies": {"core": "*", "Minecraft": "*"},
    "files": ["main.blocks", "main.ts", "main.py", "README.md"],
    "preferredEditor": "pyprj",
    "targetVersions": {"target": "1.0.0", "targetId": "minecraftedu"},
}

MAIN_BLOCKS = '<xml xmlns="https://developers.google.com/blockly/xml"></xml>'

README_MD = '''# Maze Madness — Week 3+4 World Builder

미로 3-4주차 월드 빌더 — adds AND-condition mazes on top of W1+W2 rules.

## New AND-conditions

| Sensors detected | Agent action |
|------------------|--------------|
| RS LEFT + DOWN | move UP 1, turn RIGHT |
| RS RIGHT + DOWN | move UP 1, turn LEFT |
| RS FORWARD + DOWN | move UP 1, turn RIGHT twice (180) |
| RS LEFT + RIGHT | move UP 5 |
| RS UP + DOWN | move BACK 2, turn RIGHT, move FORWARD 2 |

**Priority:** Check ANDs FIRST in the `if/elif` chain, then singles, then default forward.

## Curriculum

| # | Theme | ANDs |
|---|-------|------|
| 1 | Review (all W1+W2 singles) | none |
| 2 | AND #1 only — L+D | 1 |
| 3 | AND #2 only — R+D | 1 |
| 4 | AND #3 only — F+D | 1 |
| 5 | AND #4 only — L+R | 1 |
| 6 | AND #5 only — U+D | 1 |
| 7 | #1 + #2 | 2 |
| 8 | #2 + #3 | 2 |
| 9 | #3 + #4 | 2 |
| 10 | #4 + #5 | 2 |
| 11 | #5 + #1 + #2 | 3 |
| 12 | #1 + #4 + #5 | 3 |
| 13 | #2 + #4 + #1 | 3 |
| 14 | #3 + #5 + #2 | 3 |
| 15 | Final Boss — ALL 5 ANDs + W1+W2 | 5+ |

## Usage

1. Open in MakeCode for Minecraft Education.
2. Press Play, connect to flat world.
3. Stand facing east (+X).
4. Chat: `m1`–`m15` for single, `build1` for all, `clear` to wipe.

## Materials

- Floor: rotating colored stained glass per maze
- Walls + ceiling: clear `GLASS`
- Spawn: `LIME_STAINED_GLASS` (entry behind it is OPEN)
- **Start pillar**: 4-block `GLOWSTONE` tower above each start (visible from far)
- Goal: `DIAMOND_BLOCK`
- Signposts: `REDSTONE_BLOCK`

## Build position

Mazes build **10 blocks east** of player position so the build does not engulf
the player. Stand still, type `build1`, then walk/teleport agent to the
glowstone start pillar.
'''


def main():
    here = pathlib.Path(__file__).parent

    geoms = [(m, maze_geometry(m[0], m[1], m[2], m[3])) for m in MAZES]

    py_src = build_py(geoms)
    ts_src = build_ts(geoms)

    for week in (3, 4):
        py_out = here / f"_builder_week-{week}.py"
        py_out.write_text(py_src, encoding="utf-8")
        print(f"Wrote {py_out} ({py_out.stat().st_size} bytes)")

        mkcd_out = here.parent / "blocks" / f"week-{week}.mkcd"
        mkcd_out.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(mkcd_out, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("pxt.json", json.dumps(PXT_JSON, indent=2))
            z.writestr("main.py", py_src)
            z.writestr("main.ts", ts_src)
            z.writestr("main.blocks", MAIN_BLOCKS)
            z.writestr("README.md", README_MD)
        print(f"Wrote {mkcd_out} ({mkcd_out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves, z_off), geom in geoms:
        floor_set, wall_set, redstones, _, _, path_len, _ = geom
        print(f"  M{num:2d} z={z_off:3d}  {name:35s}  rs={len(redstones):2d}  cells={path_len:3d}  walls={len(wall_set):3d}")


if __name__ == "__main__":
    main()
