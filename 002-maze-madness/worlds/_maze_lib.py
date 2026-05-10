"""
_maze_lib.py — shared maze-generation helpers for week 1-8 generators.

All week generators import from here:
    from _maze_lib import (FACINGS, DELTA, X_OFFSET, PILLAR_HEIGHT,
                            FLOOR_PALETTE, SPAWN_BLOCK,
                            turn_right, turn_left, step,
                            wall_set_for_path, write_builder)
"""

FACINGS = ["+X", "+Z", "-X", "-Z"]
DELTA = {"+X": (1, 0, 0), "+Z": (0, 0, 1), "-X": (-1, 0, 0), "-Z": (0, 0, -1)}

X_OFFSET = 10
PILLAR_HEIGHT = 4
SPAWN_BLOCK = "LIME_STAINED_GLASS"

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


def turn_right(f):
    return FACINGS[(FACINGS.index(f) + 1) % 4]


def turn_left(f):
    return FACINGS[(FACINGS.index(f) - 1) % 4]


def step(p, f):
    dx, dy, dz = DELTA[f]
    return (p[0] + dx, p[1] + dy, p[2] + dz)


def wall_set_for_path(path_set, exclude_sets=()):
    """Compute glass walls for given path cells (horizontal neighbors at hy=0,1)."""
    wall_set = set()
    for (px, py, pz) in path_set:
        for (ddx, ddz) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, nz = px + ddx, pz + ddz
            for hy in [0, 1]:
                cell = (nx, py + hy, nz)
                if cell not in path_set:
                    wall_set.add(cell)
    for ex in exclude_sets:
        wall_set -= ex
    wall_set -= path_set
    return wall_set


def floor_for_path(path_set, exclude_sets=()):
    """Compute floor cells (y-1 of each path cell) excluding any cells in exclude_sets."""
    floor_set = set()
    for (px, py, pz) in path_set:
        fp = (px, py - 1, pz)
        if fp not in path_set and not any(fp in ex for ex in exclude_sets):
            floor_set.add(fp)
    return floor_set


def open_entry(wall_set, start):
    """Remove walls behind start cell (default initial facing is +X, so back is -X)."""
    for hy in [0, 1]:
        wall_set.discard((start[0] - 1, start[1] + hy, start[2]))
    return wall_set


def pillar_for_start(start):
    """4-block GLOWSTONE pillar above start cell."""
    return [(start[0], start[1] + 2 + i, start[2]) for i in range(PILLAR_HEIGHT)]


def gen_blocks_lines(places):
    """places: list of (block_name, (x,y,z)) tuples → list of MakeCode-Python lines."""
    return [f"    blocks.place({b}, pos({p[0]}, {p[1]}, {p[2]}))" for (b, p) in places]


def write_builder(here, week, header, body_per_maze, clear_zone_bounds, num_mazes):
    """
    Write _builder_weekN.py with header + each maze's body + chat handlers.
    body_per_maze: list of (num, body_str)
    clear_zone_bounds: ((x0,y0,z0), (x1,y1,z1)) for both AIR fill and GRASS fill ground.
    """
    out = []
    out.append(header)
    for num, body in body_per_maze:
        out.append(body)

    (x0, y0, z0), (x1, y1, z1) = clear_zone_bounds
    out.append("def clear_zone():")
    out.append(f"    blocks.fill(AIR, pos({x0}, {y0}, {z0}), pos({x1}, {y1}, {z1}), FillOperation.REPLACE)")
    out.append(f"    blocks.fill(GRASS, pos({x0}, -5, {z0}), pos({x1}, -5, {z1}), FillOperation.REPLACE)\n\n")

    out.append("def on_chat_build_all():")
    out.append("    clear_zone()")
    for num, _ in body_per_maze:
        out.append(f"    build_maze_{num}()")
    out.append('    player.say("Mazes built. 미로 완성!")')
    out.append('player.on_chat("build1", on_chat_build_all)\n\n')

    for num, _ in body_per_maze:
        out.append(f"def on_chat_m{num}():")
        out.append(f"    build_maze_{num}()")
        out.append(f'player.on_chat("m{num}", on_chat_m{num})\n')

    out.append("\ndef on_chat_clr():")
    out.append("    clear_zone()")
    out.append('player.on_chat("clear", on_chat_clr)')

    py_src = "\n".join(out)
    out_path = here / f"_builder_week{week}.py"
    out_path.write_text(py_src, encoding="utf-8")
    return out_path
