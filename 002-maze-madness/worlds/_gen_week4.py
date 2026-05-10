"""W4 — OR Conditions with split paths: 10 mazes, 4 OR rule types.

OR rules — each with its own split geometry (two parallel walkable forks
converging at the same cell). Action is the same (forward 4) regardless of
which detection direction has the redstone.

  OR a: RS LEFT or RIGHT     -> forward 4   (forks LEFT and RIGHT)
  OR b: RS UP or DOWN        -> forward 4   (forks UP and DOWN, vertical)
  OR c: RS LEFT or DOWN      -> forward 4   (one fork LEFT, one fork DOWN)
  OR d: RS RIGHT or UP       -> forward 4   (one fork RIGHT, one fork UP)

Solver:
  while not detect(DIAMOND, FORWARD):
      if detect(RS, LEFT) or detect(RS, RIGHT):
          agent.move(FORWARD, 4)
      elif detect(RS, UP) or detect(RS, DOWN):
          agent.move(FORWARD, 4)
      elif detect(RS, LEFT) or detect(RS, DOWN):
          agent.move(FORWARD, 4)
      elif detect(RS, RIGHT) or detect(RS, UP):
          agent.move(FORWARD, 4)
      else:
          agent.move(FORWARD, 1)

Each maze has a 4-cell entry corridor leading INTO the start.
"""
import pathlib
from _maze_lib import (DELTA, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)


SPLIT_LEN = 3
SPLIT_TOTAL = SPLIT_LEN + 1
ENTRY_LEN = 4


def fork_cells(rule_name, pos, f):
    """Return list of cells for both forks of given OR rule.
    Each fork = (length+1) cells parallel to main path."""
    cells = []
    if rule_name == "a":   # L|R: forks at perpendicular sides
        side_dirs = [turn_left(f), turn_right(f)]
        for sd in side_dirs:
            base = step(pos, sd)
            cells.append(base)
            cur = base
            for _ in range(SPLIT_LEN):
                cur = step(cur, f); cells.append(cur)
    elif rule_name == "b":  # U|D: vertical forks
        for dy in [1, -1]:
            base = (pos[0], pos[1] + dy, pos[2])
            cells.append(base)
            cur = base
            for _ in range(SPLIT_LEN):
                cur = step(cur, f); cells.append(cur)
    elif rule_name == "c":  # L|D: left fork + down fork
        # Left fork
        base = step(pos, turn_left(f))
        cells.append(base); cur = base
        for _ in range(SPLIT_LEN):
            cur = step(cur, f); cells.append(cur)
        # Down fork
        base = (pos[0], pos[1] - 1, pos[2])
        cells.append(base); cur = base
        for _ in range(SPLIT_LEN):
            cur = step(cur, f); cells.append(cur)
    elif rule_name == "d":  # R|U: right fork + up fork
        base = step(pos, turn_right(f))
        cells.append(base); cur = base
        for _ in range(SPLIT_LEN):
            cur = step(cur, f); cells.append(cur)
        base = (pos[0], pos[1] + 1, pos[2])
        cells.append(base); cur = base
        for _ in range(SPLIT_LEN):
            cur = step(cur, f); cells.append(cur)
    return cells


def rs_position(rule_name, side_idx, pos, f):
    """Return redstone position. side_idx 0 or 1 picks first or second
    detection direction of the OR rule."""
    if rule_name == "a":
        return step(pos, turn_left(f)) if side_idx == 0 else step(pos, turn_right(f))
    if rule_name == "b":
        return (pos[0], pos[1] + 1, pos[2]) if side_idx == 0 else (pos[0], pos[1] - 1, pos[2])
    if rule_name == "c":
        return step(pos, turn_left(f)) if side_idx == 0 else (pos[0], pos[1] - 1, pos[2])
    if rule_name == "d":
        return step(pos, turn_right(f)) if side_idx == 0 else (pos[0], pos[1] + 1, pos[2])
    raise ValueError(rule_name)


def trace(moves):
    pos = (0, 0, 0); f = "+X"
    agent_path = [pos]
    fork_extras = []
    redstones = []
    counters = {"a": 0, "b": 0, "c": 0, "d": 0}

    for m in moves:
        if m == "F":
            pos = step(pos, f); agent_path.append(pos)
        elif m == "L":
            redstones.append(step(pos, turn_right(f)))
            f = turn_left(f); pos = step(pos, f); agent_path.append(pos)
        elif m == "R":
            redstones.append(step(pos, turn_left(f)))
            f = turn_right(f); pos = step(pos, f); agent_path.append(pos)
        elif m in counters:
            n = counters[m]; counters[m] = n + 1
            redstones.append(rs_position(m, n % 2, pos, f))
            fork_extras.extend(fork_cells(m, pos, f))
            for _ in range(SPLIT_TOTAL):
                pos = step(pos, f); agent_path.append(pos)

    return agent_path, fork_extras, redstones, pos, f


# (num, name, moves)
MAZES = [
    (1,  "OR a (L|R) — 1 split",            "FFaFFF"),
    (2,  "OR a — 2 splits",                  "FFaFFaFFF"),
    (3,  "OR b (U|D) — 1 split",             "FFbFFF"),
    (4,  "OR b — 2 splits",                  "FFbFFbFFF"),
    (5,  "OR c (L|D) — 1 split",             "FFcFFF"),
    (6,  "OR d (R|U) — 1 split",             "FFdFFF"),
    (7,  "ORs a + b combo",                  "FFaFFbFFaFFbFFF"),
    (8,  "ORs c + d combo",                  "FFcFFdFFcFFdFFF"),
    (9,  "All 4 ORs (a+b+c+d)",              "FFaFFbFFcFFdFFF"),
    (10, "Boss: many splits + L/R turns",    "FFaFFLFFbFFRFFcFFLFFdFFRFFaFFbFFF"),
]


# Grid: 1 row x 10 cols (extra wide due to b/d vertical forks)
ROW_SPACING_X = 60
COL_SPACING_Z = 60


def grid_position(num):
    idx = num - 1
    row = idx // 10
    col = idx % 10
    x_off = 10 + ENTRY_LEN + row * ROW_SPACING_X
    z_off = -col * COL_SPACING_Z
    return x_off, z_off


HEADER = '''# Maze Madness — Week 4: OR Conditions with Split Paths (10 mazes)
# 4 OR rules, each placing redstone on EITHER of two detection sides.
# Both sides trigger the SAME action (forward 4) — that is the OR.
#
# OR a: RS LEFT or RIGHT  -> forward 4  (forks left + right)
# OR b: RS UP or DOWN     -> forward 4  (forks up + down, vertical)
# OR c: RS LEFT or DOWN   -> forward 4  (forks left + down)
# OR d: RS RIGHT or UP    -> forward 4  (forks right + up)
#
# Solver:
#   while not agent.detect_block(DIAMOND_BLOCK, FORWARD):
#       if agent.detect_block(REDSTONE_BLOCK, LEFT) or agent.detect_block(REDSTONE_BLOCK, RIGHT):
#           agent.move(FORWARD, 4)
#       elif agent.detect_block(REDSTONE_BLOCK, UP) or agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(FORWARD, 4)
#       elif agent.detect_block(REDSTONE_BLOCK, LEFT) or agent.detect_block(REDSTONE_BLOCK, DOWN):
#           agent.move(FORWARD, 4)
#       elif agent.detect_block(REDSTONE_BLOCK, RIGHT) or agent.detect_block(REDSTONE_BLOCK, UP):
#           agent.move(FORWARD, 4)
#       else:
#           agent.move(FORWARD, 1)
#
# Each maze has a 4-cell entry corridor leading into the GLOWSTONE start.


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

    entry_cells = [(start[0] - i, start[1], start[2]) for i in range(1, ENTRY_LEN + 1)]

    path_set = set(agent_path) | set(fork_extras) | set(entry_cells)
    redstone_set = set(redstones)
    floor_set = floor_for_path(path_set, [redstone_set])
    wall_set = wall_set_for_path(path_set, [redstone_set])
    wall_set.discard(diamond)
    entry_far = (start[0] - ENTRY_LEN, start[1], start[2])
    for hy in [0, 1]:
        wall_set.discard((entry_far[0] - 1, entry_far[1] + hy, entry_far[2]))

    spawn = (start[0], start[1] - 1, start[2])
    pillar = pillar_for_start(start)
    floor_block = FLOOR_PALETTE[(num - 1) % 15]

    rule_count = {c: moves.count(c) for c in "abcd" if c in moves}
    summary = " ".join(f"{c}={n}" for c, n in rule_count.items())

    lines = [
        f"# M{num} - {name}",
        f"# Splits: {summary}, redstones: {len(redstones)}",
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
    lines.append(f'    player.say("M{num}: {name}")')
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
        rules = "".join(c for c in "abcd" if c in moves)
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d})  rules=[{rules:4s}]  agent={len(ap):2d}  forks={len(fk):2d}  rs={len(rs):2d}  | {name}")


if __name__ == "__main__":
    main()
