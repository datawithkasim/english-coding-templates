"""
_gen_maze_world.py — generates Maze Madness Week 1 builder.

Outputs:
  - _builder_week-1.py            (paste-friendly Python source)
  - ../blocks/week-1.mkcd          (full MakeCode for Minecraft Education project)

Each maze is described by a "move string" the agent's solution will follow.
Move characters:
  F = forward  (no redstone)
  R = turn right + forward  (redstone signpost on agent's LEFT)
  L = turn left + forward   (redstone signpost on agent's RIGHT)
  U = move up              (redstone signpost BELOW)
  D = move down            (redstone signpost ABOVE)

Run: python _gen_maze_world.py
"""

import json
import pathlib
import zipfile

FACINGS = ["+X", "+Z", "-X", "-Z"]
DELTA = {"+X": (1, 0, 0), "+Z": (0, 0, 1), "-X": (-1, 0, 0), "-Z": (0, 0, -1)}


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
        elif m == "R":
            redstones.append(step(pos, turn_left(f)))   # rs on LEFT
            f = turn_right(f)
            pos = step(pos, f)
        elif m == "L":
            redstones.append(step(pos, turn_right(f)))  # rs on RIGHT
            f = turn_left(f)
            pos = step(pos, f)
        elif m == "U":
            redstones.append((pos[0], pos[1] - 1, pos[2]))  # rs BELOW
            pos = (pos[0], pos[1] + 1, pos[2])
        elif m == "D":
            redstones.append((pos[0], pos[1] + 1, pos[2]))  # rs ABOVE
            pos = (pos[0], pos[1] - 1, pos[2])
        path.append(pos)
    return path, redstones, pos, f


def maze_geometry(num, name, moves, z_offset):
    """Return (floor_set, wall_set, redstones, spawn, diamond) for one maze."""
    path, redstones, end, end_f = trace(moves)

    path = [(x, y, z + z_offset) for (x, y, z) in path]
    redstones = [(x, y, z + z_offset) for (x, y, z) in redstones]
    end = (end[0], end[1], end[2] + z_offset)

    dx, dy, dz = DELTA[end_f]
    diamond = (end[0] + dx, end[1] + dy, end[2] + dz)

    path_set = set(path)
    redstone_set = set(redstones)

    overlap = path_set & redstone_set
    if overlap:
        print(f"WARN M{num} ({name}): redstone-path overlap at {overlap}")
    if len(path) != len(set(path)):
        dupes = [c for c in path if path.count(c) > 1]
        print(f"WARN M{num} ({name}): self-overlap path cells: {set(dupes)}")

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

    # Open entry behind start (start always faces +X, so back = -X)
    start = path[0]
    for hy in [0, 1]:
        wall_set.discard((start[0] - 1, start[1] + hy, start[2]))

    # Down-move clearance: cell directly below every redstone-up signpost
    # (descent target) must be air. Already excluded via path_set, but verify.
    for (rx, ry, rz) in redstones:
        # If this redstone is ABOVE a path cell (rs at pos+1, descent trigger):
        below = (rx, ry - 2, rz)
        if (rx, ry - 1, rz) in path_set and below in floor_set:
            print(f"WARN M{num} ({name}): floor blocks descent at {below}")
            floor_set.discard(below)

    spawn = (start[0], start[1] - 1, start[2])

    return floor_set, wall_set, redstones, spawn, diamond, len(path)


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
    floor_set, wall_set, redstones, spawn, diamond, path_len = geom
    floor_block = FLOOR_PALETTE[(num - 1) % len(FLOOR_PALETTE)]
    lines = [
        f"# M{num} — {name}: {len(redstones)} redstones, {path_len} path cells, floor={floor_block}",
        f"def build_maze_{num}():",
    ]
    for p in sorted(floor_set):
        lines.append(f"    blocks.place({floor_block}, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in sorted(wall_set):
        lines.append(f"    blocks.place(GLASS, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in redstones:
        lines.append(f"    blocks.place(REDSTONE_BLOCK, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place({SPAWN_BLOCK}, pos({spawn[0]}, {spawn[1]}, {spawn[2]}))")
    lines.append(f"    blocks.place(DIAMOND_BLOCK, pos({diamond[0]}, {diamond[1]}, {diamond[2]}))")
    return "\n".join(lines) + "\n\n"


def gen_maze_ts(num, name, geom):
    floor_set, wall_set, redstones, spawn, diamond, path_len = geom
    floor_block = FLOOR_PALETTE[(num - 1) % len(FLOOR_PALETTE)]
    lines = [
        f"// M{num} — {name}: {len(redstones)} redstones, {path_len} path cells, floor={floor_block}",
        f"function build_maze_{num} () {{",
    ]
    for p in sorted(floor_set):
        lines.append(f"    blocks.place({floor_block}, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in sorted(wall_set):
        lines.append(f"    blocks.place(GLASS, pos({p[0]}, {p[1]}, {p[2]}))")
    for p in redstones:
        lines.append(f"    blocks.place(REDSTONE_BLOCK, pos({p[0]}, {p[1]}, {p[2]}))")
    lines.append(f"    blocks.place({SPAWN_BLOCK}, pos({spawn[0]}, {spawn[1]}, {spawn[2]}))")
    lines.append(f"    blocks.place(DIAMOND_BLOCK, pos({diamond[0]}, {diamond[1]}, {diamond[2]}))")
    lines.append("}")
    return "\n".join(lines) + "\n\n"


# Maze definitions: (num, name, moves, z_offset)
# Curriculum:
#   M1: only L (left turns only)
#   M2: L + R (both turn types)
#   M3: L + R + U (adds vertical up)
#   M4: L + R + U + D (all 4 redstone types)
#   M5+: progressively more redstone detection points
MAZES = [
    (1,  "Only Lefts",          "FFLFFFLFFFLFF",                                              0),
    (2,  "Lefts + Rights",      "FFRFFLFFRFFLFFF",                                            30),
    (3,  "Add Up",              "FFRFFLFFUFFRFFLFFF",                                         60),
    (4,  "All 4 Types",         "FFRFFLFFUFFRFFDFFLFFF",                                      90),
    (5,  "Mix 7 RS",            "FFRFFLFFUFFRFFDFFLFFRFFF",                                   120),
    (6,  "Snake Drill",         "FFLFFRFFLFFRFFLFFRFFLFFF",                                   160),
    (7,  "3D Snake Begin",      "FFRFFUFFLFFDFFRFFUFFLFFD",                                   200),
    (8,  "Climbing Snake",      "FFLFFUFFRFFUFFLFFUFFRFFF",                                   240),
    (9,  "Drop Snake",          "FFRFFDFFLFFDFFRFFDFFLFFF",                                   280),
    (10, "Tight Mix",           "FRFLFUFRFLFDFRFLFUFLFDFRFLFFF",                              320),
    (11, "Long Mix",            "FFRFFLFFUFFRFFLFFDFFRFFLFFUFFRFFLFFD",                       360),
    (12, "Big 3D Snake",        "FFRFFUFFLFFDFFRFFUFFLFFDFFRFFUFFLFFDFFF",                    410),
    (13, "Dense Turns",         "FRFLFRFLFRFLFUFRFLFDFRFLFRFLFUFRFLFDFFF",                    460),
    (14, "Mega Weave",          "FRFLFUFRFLFDFRFLFUFRFLFDFRFLFUFRFLFDFFF",                    510),
    (15, "Final Boss",          "FFRFFLFFUFFRFFLFFDFFRFFLFFUFFRFFLFFDFFRFFLFFUFFRFFLFFDFFF",  570),
]


HEADER_PY = '''# Maze Madness — Week 1: 15 Glass + Redstone Mazes
# Auto-generated by _gen_maze_world.py — do NOT edit by hand. Regenerate via the .py file.
# Paste this whole file into MakeCode for Minecraft Education (Python), or open the .mkcd.
# Stand on flat ground facing east (+X). Press Play.
# Chat:
#   build1   = build all 15 mazes (slow — ~minute)
#   m1..m15  = build a single maze
#   clear    = wipe build zone
#
# Solution rule (student writes in homework, NOT here):
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       if agent.detect_block(REDSTONE_BLOCK, DOWN):    agent.move(UP, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, LEFT):  agent.turn(RIGHT_TURN); agent.move(FORWARD, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, RIGHT): agent.turn(LEFT_TURN);  agent.move(FORWARD, 1)
#       elif agent.detect_block(REDSTONE_BLOCK, UP):    agent.move(DOWN, 1)
#       else:                                            agent.move(FORWARD, 1)


'''

HEADER_TS = '''// Maze Madness — Week 1: 15 Glass + Redstone Mazes
// Auto-generated by _gen_maze_world.py — do NOT edit by hand.


'''


def build_py(geoms):
    body = HEADER_PY
    for (num, name, _, _), geom in geoms:
        body += gen_maze_py(num, name, geom)

    body += "def clear_zone():\n"
    body += "    blocks.fill(AIR, pos(-8, -4, -8), pos(20, 8, 650), FillOperation.REPLACE)\n"
    body += "    blocks.fill(GRASS, pos(-8, -5, -8), pos(20, -5, 650), FillOperation.REPLACE)\n\n\n"

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
    body += "    blocks.fill(AIR, pos(-8, -4, -8), pos(20, 8, 650), FillOperation.Replace)\n"
    body += "    blocks.fill(GRASS, pos(-8, -5, -8), pos(20, -5, 650), FillOperation.Replace)\n"
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
    "name": "Maze Madness — Week 1",
    "description": "15 glass + redstone mazes for Week 1. 미로 1주차 월드 빌더.",
    "dependencies": {"core": "*", "Minecraft": "*"},
    "files": ["main.blocks", "main.ts", "main.py", "README.md"],
    "preferredEditor": "pyprj",
    "targetVersions": {"target": "1.0.0", "targetId": "minecraftedu"},
}

MAIN_BLOCKS = '<xml xmlns="https://developers.google.com/blockly/xml"></xml>'

README_MD = '''# Maze Madness — Week 1 World Builder

미로 1주차 월드 빌더 / Week 1 world builder for Maze Madness curriculum.

15 glass-walled mazes with redstone signposts. Agent solves by detecting `REDSTONE_BLOCK` neighbours.

## 사용법 / Usage

1. Open in MakeCode for Minecraft Education.
2. Press Play → connect to your world.
3. In game, stand on flat ground facing east (+X).
4. Type one of these in chat:
   - `build1` — build all 15 mazes (~1 minute)
   - `m1` … `m15` — build a single maze
   - `clear` — wipe build area

## Maze Index — Progressive Curriculum

| # | Name | Redstones | Teaches |
|---|------|-----------|---------|
| 1 | Only Lefts | 3 L | RIGHT-side detection only |
| 2 | Lefts + Rights | 2L + 2R | LEFT + RIGHT detection |
| 3 | Add Up | L+R+U | + DOWN-direction detection (climb up) |
| 4 | All 4 Types | L+R+U+D | full sensor set |
| 5 | Mix 7 RS | 7 mixed | combine all 4 types |
| 6 | Snake Drill | 7 L/R | turn density |
| 7 | 3D Snake Begin | 8 L+R+U+D | 3D weave start |
| 8 | Climbing Snake | 7 L+U | climb endurance |
| 9 | Drop Snake | 7 R+D | descent endurance |
| 10 | Tight Mix | 10 mixed | dense detection points |
| 11 | Long Mix | 12 mixed | endurance |
| 12 | Big 3D Snake | 12 mixed | 3D endurance |
| 13 | Dense Turns | 14 mixed | very dense |
| 14 | Mega Weave | 14 mixed | dense 3D |
| 15 | Final Boss | 18 mixed | full mastery |

## Materials

- Floor: rotating `*_STAINED_GLASS` color (one per maze, 15 colors)
- Walls + ceiling: clear `GLASS` (visible for video demos)
- Spawn marker: `LIME_STAINED_GLASS` (under start cell — entry behind it is OPEN for teleport)
- Goal: `DIAMOND_BLOCK` (one step beyond final cell)
- Signposts: `REDSTONE_BLOCK` (LEFT = turn right, RIGHT = turn left, BELOW = up, ABOVE = down)

## Solution Pattern

Student writes (in their homework, not here):

```python
while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
    if agent.detect_block(REDSTONE_BLOCK, DOWN):
        agent.move(UP, 1)
    elif agent.detect_block(REDSTONE_BLOCK, LEFT):
        agent.turn(RIGHT_TURN)
        agent.move(FORWARD, 1)
    elif agent.detect_block(REDSTONE_BLOCK, RIGHT):
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, 1)
    elif agent.detect_block(REDSTONE_BLOCK, UP):
        agent.move(DOWN, 1)
    else:
        agent.move(FORWARD, 1)
```
'''


def main():
    here = pathlib.Path(__file__).parent

    geoms = [(m, maze_geometry(m[0], m[1], m[2], m[3])) for m in MAZES]

    py_src = build_py(geoms)
    ts_src = build_ts(geoms)

    # Emit both week-1 and week-2 — same world serves both weeks
    # (W1 = while loops to wall, W2 = turning at walls; same maze geometry)
    for week in (1, 2):
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
        floor_set, wall_set, redstones, _, _, path_len = geom
        print(f"  M{num:2d} z={z_off:3d}  {name:20s}  rs={len(redstones):2d}  path={path_len:3d}  walls={len(wall_set):3d}")


if __name__ == "__main__":
    main()
