"""W4 — OR Conditions: 15 mazes introducing OR-condition rules.
DSL adds:
  S = side-OR signpost. RS placed on EITHER LEFT or RIGHT (alternating
      L for even-index S, R for odd). Action: move FORWARD 2 (skip ahead).
  T = top/bottom-OR signpost. RS placed on EITHER UP or DOWN (alternating).
      Action: turn RIGHT 2 (180), move FORWARD 1 (reverse direction).

Rules taught:
  RS LEFT or RIGHT  -> move FORWARD 2
  RS UP or DOWN     -> turn 180, move FORWARD 1

Singles, ANDs from W1-W3 still apply. Solver order:
  ANDs first -> ORs next -> singles -> forward.
"""
import pathlib
from _maze_lib import (DELTA, X_OFFSET, FLOOR_PALETTE, SPAWN_BLOCK,
                       turn_right, turn_left, step,
                       wall_set_for_path, floor_for_path, open_entry,
                       pillar_for_start, write_builder)

MAZES = [
    (1,  "Review (W1-W3 mix)",     "FFRFFLFFUFFDFFRFFF",          0),
    (2,  "OR side intro",          "FFSFFFLFFRFFF",               30),
    (3,  "Two side-ORs",           "FFSFFFSFFLFFF",               60),
    (4,  "Side-OR + R",            "FFSFFRFFSFFLFFF",             95),
    (5,  "OR vertical intro",      "FFTFFFLFFRFFF",               130),
    (6,  "Two vertical-ORs",       "FFTFFFTFFRFFF",               165),
    (7,  "Side + vertical OR",     "FFSFFTFFLFFRFFF",             200),
    (8,  "OR + AND",               "FFSFF1FFTFFRFFF",             240),
    (9,  "OR + climb",             "FFUFFSFFLFFTFFRFFF",          280),
    (10, "Side-OR triple",         "FFSFFRFFSFFLFFSFFF",          325),
    (11, "Vertical-OR triple",     "FFTFFRFFTFFLFFTFFF",          370),
    (12, "Mix S+T+1+2",            "FFSFF1FFTFF2FFLFFRFFF",       415),
    (13, "Mix S+T+3+4",            "FFSFFTFF3FF4FFRFFF",          465),
    (14, "Tight OR+AND",           "FFSTSTFFRFFLFFF",             510),
    (15, "Boss: ORs+ANDs+singles", "FFSFFTFF1FF2FFRFFLFFUFFDFFF", 555),
]

HEADER = '''# Maze Madness — Week 4: OR Conditions (여러 신호 중 하나만)
# OR rules: any one of multiple signals triggers same action.
#
# OR rules:
#   RS LEFT  or  RIGHT  -> move FORWARD 2 (skip ahead)
#   RS UP    or  DOWN   -> turn RIGHT_TURN twice (180), move FORWARD 1
#
# Solver: ANDs FIRST, then ORs, then singles, then forward.
#
# Stand facing east (+X). Chat: build1 / m1..m15 / clear.


'''

ANDS_REVISIT = {"5"}


def trace(moves):
    pos = (0, 0, 0)
    f = "+X"
    path = [pos]
    redstones = []
    s_count = 0   # alternates side for S
    t_count = 0   # alternates vertical for T
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
        elif m == "S":  # side-OR: RS on left (even) or right (odd)
            if s_count % 2 == 0:
                redstones.append(step(pos, turn_left(f)))
            else:
                redstones.append(step(pos, turn_right(f)))
            s_count += 1
            # action: forward 2
            pos = step(pos, f); path.append(pos)
            pos = step(pos, f); path.append(pos)
        elif m == "T":  # vertical-OR: RS above (even) or below (odd)
            if t_count % 2 == 0:
                redstones.append((pos[0], pos[1]+1, pos[2]))
            else:
                redstones.append((pos[0], pos[1]-1, pos[2]))
            t_count += 1
            # action: turn 180, forward 1
            f = turn_right(turn_right(f))
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
    out = write_builder(here, 4, HEADER, bodies,
                        ((2, -4, -15), (40, 15, 650)), len(MAZES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
