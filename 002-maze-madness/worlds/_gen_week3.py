"""W3 — AND Conditions: 10 mazes.

  M1-5: progressive intro of 5 ANDs (M1 only AND#1, M2 #1+#2, ..., M5 all 5).
  M6-10: mixed-rule variants — same AND detections, different agent actions.

DSL: F + 1/2/3/4/5 + L/R/U/D singles for filler.

Standard AND detections (all mazes share these — student detects same way):
  AND #1: RS LEFT  + RS DOWN
  AND #2: RS RIGHT + RS DOWN
  AND #3: RS FWD   + RS DOWN
  AND #4: RS LEFT  + RS RIGHT
  AND #5: RS UP    + RS DOWN

Standard actions (M1-5):
  #1 -> move up 1, turn right
  #2 -> move up 1, turn left
  #3 -> move up 1, turn 180
  #4 -> move up 5
  #5 -> move back 2, turn right, move forward 2

Mixed-rule variants (M6-10) reassign the AND actions; rule documented per maze.
"""
import pathlib
from _maze_lib import (DELTA, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

# ---- Standard AND action set ----
ACT_STD = {
    "1": [("up", 1), ("turn_right",)],
    "2": [("up", 1), ("turn_left",)],
    "3": [("up", 1), ("turn_right",), ("turn_right",)],
    "4": [("up", 5)],
    "5": [("back", 2), ("turn_right",), ("forward", 2)],
}

# ---- Variant AND action sets (mixed rules for M6-10) ----
ACT_V1_TURNS_SWAPPED = {
    # AND#1 and #2 swap turn directions
    "1": [("up", 1), ("turn_left",)],
    "2": [("up", 1), ("turn_right",)],
    "3": [("up", 1), ("turn_right",), ("turn_right",)],
    "4": [("up", 5)],
    "5": [("back", 2), ("turn_right",), ("forward", 2)],
}
ACT_V2_DOWN_INSTEAD = {
    # All "up" moves become "down" — vertical inverted
    "1": [("down", 1), ("turn_right",)],
    "2": [("down", 1), ("turn_left",)],
    "3": [("down", 1), ("turn_right",), ("turn_right",)],
    "4": [("down", 5)],
    "5": [("forward", 2), ("turn_left",), ("forward", 2)],
}
ACT_V3_BIGGER = {
    # Up moves are 3 instead of 1; AND#4 is up 8 instead of 5
    "1": [("up", 3), ("turn_right",)],
    "2": [("up", 3), ("turn_left",)],
    "3": [("up", 3), ("turn_right",), ("turn_right",)],
    "4": [("up", 8)],
    "5": [("back", 3), ("turn_right",), ("forward", 3)],
}
ACT_V4_FORWARD_LEAP = {
    # ANDs that turn drop the turn — just move up + forward
    "1": [("up", 1), ("forward", 2)],
    "2": [("up", 1), ("forward", 2)],
    "3": [("up", 2), ("forward", 1)],
    "4": [("up", 5), ("forward", 1)],
    "5": [("forward", 4)],
}


def detect_redstones_for_and(m, pos, f):
    """Return list of redstone cells for given AND move at pos/facing."""
    if m == "1":
        return [step(pos, turn_left(f)), (pos[0], pos[1] - 1, pos[2])]
    if m == "2":
        return [step(pos, turn_right(f)), (pos[0], pos[1] - 1, pos[2])]
    if m == "3":
        return [step(pos, f), (pos[0], pos[1] - 1, pos[2])]
    if m == "4":
        return [step(pos, turn_left(f)), step(pos, turn_right(f))]
    if m == "5":
        return [(pos[0], pos[1] + 1, pos[2]), (pos[0], pos[1] - 1, pos[2])]
    return []


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


def trace(moves, action_set):
    """action_set: dict mapping '1'..'5' to action_seq."""
    pos = (0, 0, 0); f = "+X"; path = [pos]; redstones = []
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
        elif m in "12345":
            redstones.extend(detect_redstones_for_and(m, pos, f))
            pos, f = apply_action(action_set[m], pos, f, path)
    return path, redstones, pos, f


# (num, name, moves, action_set, rule_label)
MAZES = [
    # M1-5: progressive standard ANDs
    (1,  "AND #1 only (L+D)",         "FF1FFFLFFRFFF",                  ACT_STD, "STD #1 only"),
    (2,  "ANDs #1 + #2",              "FF1FFF2FFLFFRFFF",               ACT_STD, "STD #1+#2"),
    (3,  "ANDs #1 + #2 + #3",         "FF1FFF2FFF3FFLFFRFFF",           ACT_STD, "STD #1+#2+#3"),
    (4,  "ANDs #1-4",                 "FF1FFF2FFF3FF4FFLFFF",           ACT_STD, "STD #1-#4"),
    (5,  "All 5 ANDs",                "FF1FFF2FFF3FF4FFFF5FFLFFRFFF",   ACT_STD, "STD #1-#5"),

    # M6-10: mixed-rule variants
    (6,  "Variant: turns swapped",    "FF1FFF2FFF3FFLFFRFFF",           ACT_V1_TURNS_SWAPPED, "V1 turns swapped (#1=up+turn LEFT, #2=up+turn RIGHT)"),
    (7,  "Variant: down instead",     "FF1FFF2FFF3FF4FFFLFFRFFF",       ACT_V2_DOWN_INSTEAD,  "V2 vertical inverted (all up -> down; #4 = down 5; #5 = fwd 2 + turn left + fwd 2)"),
    (8,  "Variant: bigger jumps",     "FF1FFF2FFF3FFF4FFFFF5FFLFFRFFF", ACT_V3_BIGGER,        "V3 bigger jumps (up 3 not 1; #4 = up 8; #5 = back 3 + turn right + fwd 3)"),
    (9,  "Variant: forward leap",     "FF1FFF2FFF3FF4FFF5FFLFFRFFF",    ACT_V4_FORWARD_LEAP,  "V4 forward leaps (no turns; up + forward)"),
    (10, "Final: revert to standard", "FF1FF2FF3FF4FFF5FFLFFRFFUFFDFFF",ACT_STD,              "STD final boss — all 5 ANDs + singles"),
]


# Grid: 1 row x 10 cols
ROW_SPACING_X = 50
COL_SPACING_Z = 45


def grid_position(num):
    idx = num - 1
    row = idx // 10
    col = idx % 10
    x_off = 10 + row * ROW_SPACING_X
    z_off = -col * COL_SPACING_Z
    return x_off, z_off


HEADER = '''# Maze Madness — Week 3: AND Conditions (10 mazes)
# M1-5 introduce the 5 ANDs progressively (standard actions).
# M6-9 mix up the AND actions (detection same, agent action different per maze).
# M10 reverts to standard for review.
#
# Standard ANDs:
#   #1: RS LEFT + DOWN  -> move UP 1, turn RIGHT
#   #2: RS RIGHT + DOWN -> move UP 1, turn LEFT
#   #3: RS FWD + DOWN   -> move UP 1, turn 180
#   #4: RS LEFT + RIGHT -> move UP 5
#   #5: RS UP + DOWN    -> move BACK 2, turn RIGHT, move FORWARD 2
#
# Each maze chat-prints its rule when built so student knows which to use.
# Stand facing east (+X). Chat: build1 / m1..m10 / clear.


'''


def build_maze_body(num, name, moves, action_set, rule_label):
    x_off, z_off = grid_position(num)
    path, redstones, end, end_f = trace(moves, action_set)
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
        f"# Rule: {rule_label}",
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
    safe_label = rule_label.replace('"', "'")
    lines.append(f'    player.say("M{num}: {safe_label}")')
    return "\n".join(lines) + "\n\n"


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves, aset, label))
              for (num, name, moves, aset, label) in MAZES]
    out = write_builder(here, 3, HEADER, bodies,
                        ((2, -10, -460), (75, 25, 30)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")

    print("\nMaze summary:")
    for (num, name, moves, aset, label) in MAZES:
        path, redstones, _, _ = trace(moves, aset)
        x_off, z_off = grid_position(num)
        print(f"  M{num:2d} grid({x_off:3d},{z_off:5d})  {name:25s}  rs={len(redstones):2d}  path={len(path):3d}")


if __name__ == "__main__":
    main()
