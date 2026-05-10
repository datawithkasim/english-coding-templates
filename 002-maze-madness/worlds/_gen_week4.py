"""W4 — OR Conditions: 15 mazes.

  M1-5  introduce 5 OR rules progressively (one new OR per maze, accumulating).
  M6-10 mixed-rule variants — same OR detections, different actions.
  M11-15 combined ORs + singles + boss tier.

5 standard ORs (each = "EITHER signal triggers SAME action"):
  OR a: RS LEFT or RIGHT     -> move FORWARD 2
  OR b: RS UP or DOWN        -> turn 180, move FORWARD 1
  OR c: RS LEFT or DOWN      -> move UP 2
  OR d: RS RIGHT or UP       -> move DOWN 2
  OR e: RS FORWARD or DOWN   -> turn LEFT, move FORWARD 2

For each OR move the generator alternates which detection direction gets the
redstone (so the same maze tests both sides, validating student's OR usage).

DSL: F + a/b/c/d/e (OR moves) + L/R/U/D (singles for filler).
"""
import pathlib
from _maze_lib import (DELTA, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)


def detect_position(direction, pos, f):
    if direction == "LEFT":    return step(pos, turn_left(f))
    if direction == "RIGHT":   return step(pos, turn_right(f))
    if direction == "UP":      return (pos[0], pos[1] + 1, pos[2])
    if direction == "DOWN":    return (pos[0], pos[1] - 1, pos[2])
    if direction == "FORWARD": return step(pos, f)
    raise ValueError(direction)


# ---- Standard OR rule set ----
OR_STD = {
    "a": {"dirs": ["LEFT", "RIGHT"],    "action": [("forward", 2)],
          "desc": "L|R -> fwd 2"},
    "b": {"dirs": ["UP", "DOWN"],       "action": [("turn_right",), ("turn_right",), ("forward", 1)],
          "desc": "U|D -> 180 + fwd 1"},
    "c": {"dirs": ["LEFT", "DOWN"],     "action": [("up", 2)],
          "desc": "L|D -> up 2"},
    "d": {"dirs": ["RIGHT", "UP"],      "action": [("down", 2)],
          "desc": "R|U -> down 2"},
    "e": {"dirs": ["FORWARD", "DOWN"],  "action": [("turn_left",), ("forward", 2)],
          "desc": "F|D -> turn left + fwd 2"},
}

# ---- Variant OR rule sets (mixed-rule mazes) ----
OR_V1_BIGGER_JUMPS = {
    "a": {"dirs": ["LEFT", "RIGHT"],    "action": [("forward", 4)],
          "desc": "L|R -> fwd 4 (V1 bigger)"},
    "b": {"dirs": ["UP", "DOWN"],       "action": [("turn_right",), ("turn_right",), ("forward", 3)],
          "desc": "U|D -> 180 + fwd 3 (V1 bigger)"},
    "c": {"dirs": ["LEFT", "DOWN"],     "action": [("up", 4)],
          "desc": "L|D -> up 4 (V1 bigger)"},
    "d": {"dirs": ["RIGHT", "UP"],      "action": [("down", 4)],
          "desc": "R|U -> down 4 (V1 bigger)"},
    "e": {"dirs": ["FORWARD", "DOWN"],  "action": [("turn_left",), ("forward", 4)],
          "desc": "F|D -> turn left + fwd 4 (V1 bigger)"},
}
OR_V2_INVERTED = {
    "a": {"dirs": ["LEFT", "RIGHT"],    "action": [("turn_right",), ("turn_right",), ("forward", 2)],
          "desc": "L|R -> 180 + fwd 2 (V2 reverse)"},
    "b": {"dirs": ["UP", "DOWN"],       "action": [("forward", 2)],
          "desc": "U|D -> fwd 2 (V2 reverse)"},
    "c": {"dirs": ["LEFT", "DOWN"],     "action": [("down", 2)],
          "desc": "L|D -> DOWN 2 (V2 reverse)"},
    "d": {"dirs": ["RIGHT", "UP"],      "action": [("up", 2)],
          "desc": "R|U -> UP 2 (V2 reverse)"},
    "e": {"dirs": ["FORWARD", "DOWN"],  "action": [("turn_right",), ("forward", 2)],
          "desc": "F|D -> turn RIGHT + fwd 2 (V2 reverse)"},
}


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
        elif kind == "back":
            back_f = turn_right(turn_right(f))
            for _ in range(op[1]):
                pos = step(pos, back_f); path.append(pos)
    return pos, f


def trace(moves, or_set):
    pos = (0, 0, 0); f = "+X"; path = [pos]; redstones = []
    or_counters = {}
    for m in moves:
        if m == "F":
            pos = step(pos, f); path.append(pos)
        elif m == "L":
            redstones.append(step(pos, turn_right(f)))
            f = turn_left(f); pos = step(pos, f); path.append(pos)
        elif m == "R":
            redstones.append(step(pos, turn_left(f)))
            f = turn_right(f); pos = step(pos, f); path.append(pos)
        elif m == "U":
            redstones.append((pos[0], pos[1] - 1, pos[2]))
            pos = (pos[0], pos[1] + 1, pos[2]); path.append(pos)
        elif m == "D":
            redstones.append((pos[0], pos[1] + 1, pos[2]))
            pos = (pos[0], pos[1] - 1, pos[2]); path.append(pos)
        elif m in or_set:
            rule = or_set[m]
            n = or_counters.get(m, 0)
            direction = rule["dirs"][n % 2]   # alternate which side gets RS
            or_counters[m] = n + 1
            redstones.append(detect_position(direction, pos, f))
            pos, f = apply_action(rule["action"], pos, f, path)
    return path, redstones, pos, f


# (num, name, moves, or_set, label)
MAZES = [
    # M1-5: progressive intro of 5 ORs (standard rules)
    (1,  "OR a only (L|R)",          "FFaFFFLFFRFFF",                OR_STD, "STD a only"),
    (2,  "ORs a + b",                 "FFaFFbFFFLFFRFFF",             OR_STD, "STD a+b"),
    (3,  "ORs a + b + c",             "FFaFFbFFcFFFLFFRFFF",          OR_STD, "STD a+b+c"),
    (4,  "ORs a..d",                  "FFaFFbFFcFFdFFLFFRFFF",        OR_STD, "STD a-d"),
    (5,  "All 5 ORs",                 "FFaFFbFFcFFdFFeFFLFFRFFF",     OR_STD, "STD a-e"),

    # M6-10: variant rules
    (6,  "Variant: bigger jumps (a)", "FFaFFFaFFFLFFRFFF",            OR_V1_BIGGER_JUMPS, "V1 bigger jumps a"),
    (7,  "Variant: bigger (a+b+c)",   "FFaFFbFFcFFFLFFRFFF",          OR_V1_BIGGER_JUMPS, "V1 bigger jumps a+b+c"),
    (8,  "Variant: inverted (a+b)",   "FFaFFbFFLFFRFFF",              OR_V2_INVERTED,     "V2 inverted a+b"),
    (9,  "Variant: inverted (c+d)",   "FFcFFdFFLFFRFFF",              OR_V2_INVERTED,     "V2 inverted c+d"),
    (10, "Variant: inverted all",     "FFaFFbFFcFFdFFeFFLFFRFFF",     OR_V2_INVERTED,     "V2 inverted a-e"),

    # M11-15: combined ORs + singles + boss tier
    (11, "Mix: ORs + L/R turns",      "FFaFFRFFbFFLFFcFFRFFF",        OR_STD, "STD mix ORs + turns"),
    (12, "Mix: ORs + U/D",            "FFaFFUFFcFFDFFbFFRFFF",        OR_STD, "STD mix ORs + vertical"),
    (13, "Long mix",                  "FFaFFRFFbFFLFFcFFUFFdFFDFFFLFFRFFF", OR_STD, "STD long mix"),
    (14, "Variant boss (V1)",         "FFaFFbFFcFFdFFeFFRFFLFFF",     OR_V1_BIGGER_JUMPS, "V1 boss"),
    (15, "Final boss (STD all)",      "FFaFFRFFbFFLFFcFFUFFdFFDFFeFFRFFLFFF", OR_STD, "STD final boss"),
]


# Grid: 2 rows x 8 cols (M1-8 row 0, M9-15 row 1)
ROW_SPACING_X = 60
COL_SPACING_Z = 50


def grid_position(num):
    idx = num - 1
    row = idx // 8
    col = idx % 8
    x_off = 10 + row * ROW_SPACING_X
    z_off = -col * COL_SPACING_Z
    return x_off, z_off


HEADER = '''# Maze Madness — Week 4: OR Conditions (15 mazes)
# M1-5: introduce 5 OR rules progressively.
# M6-10: mixed-rule variants (same OR detections, different actions).
# M11-15: combined ORs + singles + boss.
#
# Standard ORs (M1-5, M11-13, M15):
#   a: RS LEFT or RIGHT     -> move FORWARD 2
#   b: RS UP or DOWN        -> turn 180, move FORWARD 1
#   c: RS LEFT or DOWN      -> move UP 2
#   d: RS RIGHT or UP       -> move DOWN 2
#   e: RS FORWARD or DOWN   -> turn LEFT, move FORWARD 2
#
# Each maze chat-prints its rule when built so student knows which to use.
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.
# Grid: 2 rows x 8 cols (M1-8 row 0 x=10, M9-15 row 1 x=70).


'''


def build_maze_body(num, name, moves, or_set, label):
    x_off, z_off = grid_position(num)
    path, redstones, end, end_f = trace(moves, or_set)
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
        f"# Rule: {label}",
        f"# {len(redstones)} redstones, {len(path_set)} unique path cells",
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
    safe_label = label.replace('"', "'")
    lines.append(f'    player.say("M{num}: {safe_label}")')
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves, or_set, label))
              for (num, name, moves, or_set, label) in MAZES]
    out = write_builder(here, 4, HEADER, bodies,
                        ((2, -10, -420), (140, 25, 30)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves, or_set, label) in MAZES:
        path, redstones, _, _ = trace(moves, or_set)
        x_off, z_off = grid_position(num)
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d})  {name:30s}  rs={len(redstones):2d}  path={len(path):3d}")


if __name__ == "__main__":
    main()
