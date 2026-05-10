"""W4 — OR Conditions with split paths: 10 mazes.

At each split point:
  - Two parallel walkable corridors fork left and right
  - Both converge at the same cell ahead
  - One redstone placed on either LEFT or RIGHT side (alternates per move)

OR rule:
  RS LEFT or RS RIGHT  ->  agent.move(FORWARD, 4)
  (agent walks straight through; the forks are visible alternatives the
   player can also walk; either way reaches the same convergence cell)

DSL: F (forward) + a (split point, OR-LR).
Plus L/R for turn variations in later mazes.

Each maze has an entry corridor of 4 cells leading INTO the start (so the
start is at the end of an approach path, not in the middle of a wall).
"""
import pathlib
from _maze_lib import (DELTA, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)


SPLIT_LEN = 3   # parallel fork length (cells beyond pos before convergence)
SPLIT_TOTAL = SPLIT_LEN + 1   # forward steps action takes through main path
ENTRY_LEN = 4   # cells of approach corridor before maze start


def trace(moves):
    """Trace path. 'a' = LR split section. Returns
    (agent_path, fork_extras, redstones, end, end_facing)."""
    pos = (0, 0, 0); f = "+X"
    agent_path = [pos]
    fork_extras = []
    redstones = []
    a_count = 0

    for m in moves:
        if m == "F":
            pos = step(pos, f); agent_path.append(pos)
        elif m == "L":
            redstones.append(step(pos, turn_right(f)))
            f = turn_left(f); pos = step(pos, f); agent_path.append(pos)
        elif m == "R":
            redstones.append(step(pos, turn_left(f)))
            f = turn_right(f); pos = step(pos, f); agent_path.append(pos)
        elif m == "a":
            # Place RS on LEFT or RIGHT (alternating)
            if a_count % 2 == 0:
                rs_pos = step(pos, turn_left(f))
            else:
                rs_pos = step(pos, turn_right(f))
            a_count += 1
            redstones.append(rs_pos)

            left_dir = turn_left(f)
            right_dir = turn_right(f)

            # Left fork: turn_left side, parallel SPLIT_LEN cells, then back
            for i in range(SPLIT_LEN + 1):
                cx = pos[0] + DELTA[f][0] * i + DELTA[left_dir][0]
                cy = pos[1]
                cz = pos[2] + DELTA[f][2] * i + DELTA[left_dir][2]
                fork_extras.append((cx, cy, cz))

            # Right fork: turn_right side, parallel SPLIT_LEN cells
            for i in range(SPLIT_LEN + 1):
                cx = pos[0] + DELTA[f][0] * i + DELTA[right_dir][0]
                cy = pos[1]
                cz = pos[2] + DELTA[f][2] * i + DELTA[right_dir][2]
                fork_extras.append((cx, cy, cz))

            # Agent's actual path: forward SPLIT_TOTAL cells (main path)
            for _ in range(SPLIT_TOTAL):
                pos = step(pos, f); agent_path.append(pos)

    return agent_path, fork_extras, redstones, pos, f


# (num, name, moves)
MAZES = [
    (1,  "Single split (intro)",          "FFaFFF"),
    (2,  "Single split + L turn",         "FFaFFLFFF"),
    (3,  "Two splits",                    "FFaFFaFFF"),
    (4,  "Splits + R turn",               "FFaFFRFFaFFF"),
    (5,  "Three splits",                  "FFaFFaFFaFFF"),
    (6,  "Splits + L+R turns",            "FFaFFLFFaFFRFFaFFF"),
    (7,  "Four splits",                   "FFaFFaFFaFFaFFF"),
    (8,  "Long mix splits + turns",       "FFaFFRFFaFFLFFaFFRFFaFFF"),
    (9,  "Five splits weave",             "FFaFFLFFaFFRFFaFFLFFaFFRFFaFFF"),
    (10, "Boss: 6 splits + many turns",   "FFaFFLFFaFFRFFaFFRFFaFFLFFaFFRFFaFFF"),
]


# Grid: 1 row x 10 cols, cols spaced wider for split width
ROW_SPACING_X = 60
COL_SPACING_Z = 60   # wider since splits add z-extent +/-1


def grid_position(num):
    idx = num - 1
    row = idx // 10
    col = idx % 10
    x_off = 10 + ENTRY_LEN + row * ROW_SPACING_X   # leave room for entry corridor
    z_off = -col * COL_SPACING_Z
    return x_off, z_off


HEADER = '''# Maze Madness — Week 4: OR Conditions with Split Paths (10 mazes)
# Each split point shows TWO parallel walkable forks converging back to main.
# Agent uses OR rule to decide same action regardless of which side has RS.
#
# OR rule:
#   if agent.detect_block(REDSTONE_BLOCK, LEFT) or agent.detect_block(REDSTONE_BLOCK, RIGHT):
#       agent.move(FORWARD, 4)
#
# Each maze starts at the end of a 4-cell entry corridor (approach path
# behind the GLOWSTONE start pillar). Walk down the corridor onto the lime
# spawn block, run code, and the agent solves the maze.
#
# Stand facing east (+X). Chat: build1 / m1..m10 / clear.


'''


def build_maze_body(num, name, moves):
    x_off, z_off = grid_position(num)
    agent_path, fork_extras, redstones, end, end_f = trace(moves)
    agent_path = [(x + x_off, y, z + z_off) for (x, y, z) in agent_path]
    fork_extras = [(x + x_off, y, z + z_off) for (x, y, z) in fork_extras]
    redstones = [(x + x_off, y, z + z_off) for (x, y, z) in redstones]
    end = (end[0] + x_off, end[1], end[2] + z_off)
    dx, dy, dz = DELTA[end_f]
    diamond = (end[0] + dx, end[1] + dy, end[2] + dz)

    start = agent_path[0]

    # Entry corridor: ENTRY_LEN cells in -X direction behind start
    entry_cells = []
    for i in range(1, ENTRY_LEN + 1):
        entry_cells.append((start[0] - i, start[1], start[2]))

    # Combined path set for geometry (all walkable air cells)
    path_set = set(agent_path) | set(fork_extras) | set(entry_cells)
    redstone_set = set(redstones)
    floor_set = floor_for_path(path_set, [redstone_set])
    wall_set = wall_set_for_path(path_set, [redstone_set])
    wall_set.discard(diamond)
    # Open behind entry corridor's far end so player can step in
    entry_far = (start[0] - ENTRY_LEN, start[1], start[2])
    for hy in [0, 1]:
        wall_set.discard((entry_far[0] - 1, entry_far[1] + hy, entry_far[2]))

    spawn = (start[0], start[1] - 1, start[2])
    pillar = pillar_for_start(start)
    floor_block = FLOOR_PALETTE[(num - 1) % 15]

    lines = [
        f"# M{num} - {name}",
        f"# Splits: {moves.count('a')}, redstones: {len(redstones)}, agent path: {len(agent_path)}",
        f"def build_maze_{num}():",
    ]
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
    lines.append(f'    player.say("M{num}: OR L|R -> forward 4")')
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves))
              for (num, name, moves) in MAZES]
    out = write_builder(here, 4, HEADER, bodies,
                        ((2, -10, -620), (90, 25, 30)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves) in MAZES:
        ap, fk, rs, _, _ = trace(moves)
        x_off, z_off = grid_position(num)
        splits = moves.count("a")
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d})  {name:35s}  splits={splits}  rs={len(rs)}  agent_path={len(ap)}  fork_extras={len(fk)}")


if __name__ == "__main__":
    main()
