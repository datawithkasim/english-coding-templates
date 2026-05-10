"""W2 — Mixed-up rules + complex paths: 15 mazes.
Each maze has its OWN rule mapping for the 4 detection directions
(LEFT, RIGHT, UP, DOWN). Student must read the rule per maze.

DSL: F + L/R/U/D (4 detection-letter moves). Each move:
  1. Places redstone in the indicated direction relative to agent facing.
  2. Applies the per-maze rule's action.

Rules used (named for clarity):
  R0 STANDARD       LEFT->turn-right+fwd, RIGHT->turn-left+fwd, DOWN->up, UP->down  (W1)
  R1 SWAP_TURNS     LEFT->turn-LEFT+fwd,  RIGHT->turn-RIGHT+fwd, DOWN->up, UP->down
  R2 SWAP_VERTICAL  LEFT->turn-right+fwd, RIGHT->turn-left+fwd,  DOWN->down, UP->up
  R3 ALL_SWAP       LEFT->turn-LEFT+fwd,  RIGHT->turn-RIGHT+fwd, DOWN->down, UP->up
  R4 ROTATED        LEFT->up,             RIGHT->down,           DOWN->turn-left+fwd, UP->turn-right+fwd
"""
import pathlib
from _maze_lib import (DELTA, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

# ---- Rule definitions ----
# Action format: list of ops. Op kinds:
#   ("turn_right",), ("turn_left",), ("forward", n), ("up", n), ("down", n)

R0_STANDARD = {
    "name": "STANDARD",
    "desc": "L->turn right + fwd, R->turn left + fwd, D->up, U->down",
    "L": [("turn_right",), ("forward", 1)],
    "R": [("turn_left",), ("forward", 1)],
    "D": [("up", 1)],
    "U": [("down", 1)],
}
R1_SWAP_TURNS = {
    "name": "SWAP_TURNS",
    "desc": "L->turn LEFT + fwd, R->turn RIGHT + fwd, D->up, U->down",
    "L": [("turn_left",), ("forward", 1)],
    "R": [("turn_right",), ("forward", 1)],
    "D": [("up", 1)],
    "U": [("down", 1)],
}
R2_SWAP_VERTICAL = {
    "name": "SWAP_VERTICAL",
    "desc": "L->turn right + fwd, R->turn left + fwd, D->DOWN, U->UP",
    "L": [("turn_right",), ("forward", 1)],
    "R": [("turn_left",), ("forward", 1)],
    "D": [("down", 1)],
    "U": [("up", 1)],
}
R3_ALL_SWAP = {
    "name": "ALL_SWAP",
    "desc": "L->turn LEFT + fwd, R->turn RIGHT + fwd, D->DOWN, U->UP",
    "L": [("turn_left",), ("forward", 1)],
    "R": [("turn_right",), ("forward", 1)],
    "D": [("down", 1)],
    "U": [("up", 1)],
}
R4_ROTATED = {
    "name": "ROTATED",
    "desc": "L->UP 1, R->DOWN 1, D->turn LEFT + fwd, U->turn RIGHT + fwd",
    "L": [("up", 1)],
    "R": [("down", 1)],
    "D": [("turn_left",), ("forward", 1)],
    "U": [("turn_right",), ("forward", 1)],
}


# ---- 15 mazes with per-maze rule ----
MAZES = [
    # M1-3: standard rule, complex paths (W1 review + density)
    (1,  "Standard - dense weave",   "FFLFFRFFLFFUFFRFFDFFLFFRFFF",   R0_STANDARD),
    (2,  "Standard - climb tower",   "FFUFFLFFUFFRFFUFFLFFDFFRFFF",   R0_STANDARD),
    (3,  "Standard - 3D snake",      "FFRFFUFFLFFDFFRFFUFFLFFDFFF",   R0_STANDARD),

    # M4-6: turns swapped (LEFT->turn LEFT, RIGHT->turn RIGHT)
    (4,  "Swap turns - intro",       "FFLFFFRFFFLFFF",                R1_SWAP_TURNS),
    (5,  "Swap turns - weave",       "FFLFFRFFLFFRFFLFFRFFF",         R1_SWAP_TURNS),
    (6,  "Swap turns + 3D",          "FFLFFUFFRFFDFFLFFRFFF",         R1_SWAP_TURNS),

    # M7-9: vertical swapped (DOWN->down, UP->up)
    (7,  "Swap vertical - intro",    "FFUFFFDFFFLFFF",                R2_SWAP_VERTICAL),
    (8,  "Swap vertical + turns",    "FFUFFLFFDFFRFFLFFF",            R2_SWAP_VERTICAL),
    (9,  "Swap vertical - dense",    "FFUFFLFFUFFRFFDFFLFFDFFF",      R2_SWAP_VERTICAL),

    # M10-12: all 4 actions swapped
    (10, "All-swap intro",           "FFLFFRFFUFFDFFF",               R3_ALL_SWAP),
    (11, "All-swap dense",           "FFLFFUFFRFFDFFLFFUFFRFFDFFF",   R3_ALL_SWAP),
    (12, "All-swap boss",            "FFLFFRFFLFFRFFUFFDFFLFFRFFF",   R3_ALL_SWAP),

    # M13-15: rotated 90 degrees (L/R rows = vertical, U/D = turns)
    (13, "Rotated intro",            "FFLFFFRFFFLFFF",                R4_ROTATED),
    (14, "Rotated 3D mix",           "FFLFFRFFUFFDFFLFFRFFF",         R4_ROTATED),
    (15, "Rotated boss",             "FFLFFRFFLFFRFFUFFDFFUFFDFFF",   R4_ROTATED),
]


# Grid: 2 rows x 8 cols (M1-8 row 0, M9-15 row 1)
ROW_SPACING_X = 50
COL_SPACING_Z = 40


def grid_position(num):
    idx = num - 1
    row = idx // 8
    col = idx % 8
    x_off = 10 + row * ROW_SPACING_X
    z_off = -col * COL_SPACING_Z
    return x_off, z_off


HEADER = '''# Maze Madness — Week 2: Mixed-up Rules + Complex Paths (15 mazes)
# Each maze has its OWN detection->action rule. Read the comment above each
# build_maze_N function to see that maze's rule, then write solver accordingly.
#
# Rules used:
#   R0 STANDARD       L->turn-right+fwd, R->turn-left+fwd, D->up, U->down
#   R1 SWAP_TURNS     L->turn-LEFT+fwd,  R->turn-RIGHT+fwd, D->up, U->down
#   R2 SWAP_VERTICAL  L->turn-right+fwd, R->turn-left+fwd,  D->DOWN, U->UP
#   R3 ALL_SWAP       L->turn-LEFT+fwd,  R->turn-RIGHT+fwd, D->DOWN, U->UP
#   R4 ROTATED        L->UP, R->DOWN,    D->turn-LEFT+fwd, U->turn-RIGHT+fwd
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.
# Grid: 2 rows x 8 cols (M1-8 row 0 x=10, M9-15 row 1 x=60).


'''


def apply_action(action_seq, pos, f, path):
    for op in action_seq:
        kind = op[0]
        if kind == "turn_right":
            f = turn_right(f)
        elif kind == "turn_left":
            f = turn_left(f)
        elif kind == "forward":
            for _ in range(op[1]):
                pos = step(pos, f); path.append(pos)
        elif kind == "up":
            for _ in range(op[1]):
                pos = (pos[0], pos[1] + 1, pos[2]); path.append(pos)
        elif kind == "down":
            for _ in range(op[1]):
                pos = (pos[0], pos[1] - 1, pos[2]); path.append(pos)
    return pos, f


def trace(moves, rule):
    pos = (0, 0, 0); f = "+X"; path = [pos]; redstones = []
    for m in moves:
        if m == "F":
            pos = step(pos, f); path.append(pos)
        elif m == "L":
            redstones.append(step(pos, turn_left(f)))
            pos, f = apply_action(rule["L"], pos, f, path)
        elif m == "R":
            redstones.append(step(pos, turn_right(f)))
            pos, f = apply_action(rule["R"], pos, f, path)
        elif m == "U":
            redstones.append((pos[0], pos[1] + 1, pos[2]))
            pos, f = apply_action(rule["U"], pos, f, path)
        elif m == "D":
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos, f = apply_action(rule["D"], pos, f, path)
    return path, redstones, pos, f


def build_maze_body(num, name, moves, rule):
    x_off, z_off = grid_position(num)
    path, redstones, end, end_f = trace(moves, rule)
    path = [(x + x_off, y, z + z_off) for (x, y, z) in path]
    redstones = [(x + x_off, y, z + z_off) for (x, y, z) in redstones]
    end = (end[0] + x_off, end[1], end[2] + z_off)
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

    lines = [
        f"# M{num} - {name}",
        f"# RULE {rule['name']}: {rule['desc']}",
        f"# {len(redstones)} redstones, {len(path_set)} unique path cells",
        f"def build_maze_{num}():",
    ]
    # CARVE: explicit AIR at every path cell
    for p in sorted(path_set):
        lines.append(f"    blocks.place(AIR, pos({p[0]}, {p[1]}, {p[2]}))")
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
    lines.append(f'    player.say("M{num} rule: {rule["name"]} - {rule["desc"]}")')
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves, rule))
              for (num, name, moves, rule) in MAZES]
    out = write_builder(here, 2, HEADER, bodies,
                        ((2, -4, -320), (130, 15, 30)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves, rule) in MAZES:
        path, redstones, _, _ = trace(moves, rule)
        x_off, z_off = grid_position(num)
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d}) [{rule['name']:14s}]  {name:25s}  rs={len(redstones):2d}  path={len(path):3d}")


if __name__ == "__main__":
    main()
