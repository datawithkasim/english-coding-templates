"""W3 — AND Conditions: 15 mazes introducing 5 AND-condition rules.
DSL: F, L, R, U, D, 1, 2, 3, 4, 5.
ANDs:
  1 = L+D -> up + R turn
  2 = R+D -> up + L turn
  3 = F+D -> up + 180
  4 = L+R -> up 5
  5 = U+D -> back 2 + R turn + forward 2
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

MAZES = [
    (1,  "Review singles",         "FFRFFLFFUFFDFFRFFLFFF",          0),
    (2,  "AND 1 only (L+D)",       "FF1FFFRFFLFFF",                  35),
    (3,  "AND 2 only (R+D)",       "FF2FFFLFFRFFF",                  60),
    (4,  "AND 3 only (F+D)",       "FF3FFFRFFLFFF",                  85),
    (5,  "AND 4 only (L+R up5)",   "FF4FFFRFFF",                     110),
    (6,  "AND 5 only (U+D back)",  "FFFF5FFFLFFF",                   140),
    (7,  "ANDs 1+2",               "FF1FFF2FFF",                     180),
    (8,  "ANDs 2+3",               "FF2FFF3FFF",                     215),
    (9,  "ANDs 3+4",               "FF3FFF4FF",                      250),
    (10, "ANDs 4+5",               "FF4FFF5FFF",                     290),
    (11, "ANDs 5+1+2",             "FFF5FFF1FFF2FFF",                340),
    (12, "ANDs 1+4+5",             "FFF1FFF4FFF5FFF",                400),
    (13, "ANDs 2+4+1",             "FFF2FFF4FFF1FFF",                460),
    (14, "ANDs 3+5+2",             "FFF3FFFFF5FFF2FFF",              520),
    (15, "Final: ALL ANDs + W1+W2","FF1FF2FF3FF4FF5FFRFFLFFUFFDFFF", 600),
]

HEADER = '''# Maze Madness — Week 3: AND Conditions (두 가지 신호 동시 인식)
# 5 AND-condition rules introduced progressively. Singles still apply.
#
# AND rules:
#   RS LEFT + DOWN  -> move UP 1, turn RIGHT
#   RS RIGHT + DOWN -> move UP 1, turn LEFT
#   RS FWD + DOWN   -> move UP 1, turn 180
#   RS LEFT + RIGHT -> move UP 5
#   RS UP + DOWN    -> move BACK 2, turn RIGHT, move FORWARD 2
#
# Solver: ANDs FIRST, then singles, then forward.
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.


'''

ANDS_REVISIT = {"5"}


def trace(moves):
    pos = (0, 0, 0)
    f = "+X"
    path = [pos]
    redstones = []
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
        elif m == "4":
            redstones.append(step(pos, turn_left(f)))
            redstones.append(step(pos, turn_right(f)))
            for _ in range(5):
                pos = (pos[0], pos[1]+1, pos[2]); path.append(pos)
        elif m == "5":
            redstones.append((pos[0], pos[1]+1, pos[2]))
            redstones.append((pos[0], pos[1]-1, pos[2]))
            back_f = turn_right(turn_right(f))
            for _ in range(2):
                pos = step(pos, back_f); path.append(pos)
            f = turn_right(f)
            for _ in range(2):
                pos = step(pos, f); path.append(pos)
    return path, redstones, pos, f


def build_maze_body(num, name, moves, z_offset):
    path, redstones, end, end_f = trace(moves)
    path = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in path]
    redstones = [(x + X_OFFSET, y, z + z_offset) for (x, y, z) in redstones]
    end = (end[0] + X_OFFSET, end[1], end[2] + z_offset)
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

    lines = [f"# M{num} - {name}: {len(redstones)} RS",
             f"def build_maze_{num}():"]
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


def main():
    here = pathlib.Path(__file__).parent
    bodies = [(num, build_maze_body(num, name, moves, z))
              for (num, name, moves, z) in MAZES]
    out = write_builder(here, 3, HEADER, bodies,
                        ((2, -4, -15), (35, 15, 700)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
