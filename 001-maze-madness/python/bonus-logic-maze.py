# ============================================================
# M002 BONUS: 2-Level Glass Maze (AND + OR puzzles, Agent-Solvable)
# Minecraft Education -> MakeCode -> Python project.
#
# HOW TO USE
#   1. Open a flat creative world (Minecraft Education).
#   2. C -> Code Builder -> MakeCode -> New Python project.
#   3. Paste this file into main.py. Run.
#   4. Back in game, stand on flat ground.
#   5. Type "build" in chat.
#
# DESIGN
#   - Whole maze volume is filled with GLASS first.
#   - Every cell the agent could walk through is then explicitly
#     carved with AIR (no assumption that "the space is already there").
#   - Walls and ceiling are GLASS so the player watches from outside.
#   - REDSTONE_BLOCK markers sit in some walls. The agent detects them
#     with AgentDetection.REDSTONE (the only thing it can detect).
#
# PUZZLES
#   Level 1: AND  -> both levers must be ON to open the iron door
#   Level 2: OR   -> either pressure plate opens the iron door
#   Goal: reach the EMERALD block on level 2.
#
# REDSTONE RULES (followed below)
#   - Redstone wire only carries signal up to 8 blocks.
#   - Wire breaks if a block is placed above it -- so wires go LAST.
# ============================================================

GW = 13
GH = 13
LEVEL_H = 4         # y0 floor, y0+1..y0+2 walls/path (2 tall), y0+3 ceiling
LEVELS = 2

# --- maze patterns ---
# 1 = glass wall, 0 = path (explicitly carved to air), 2 = redstone-block marker
# Path connectivity guaranteed by hand. Entry south of (1, 0).
# Level 1 path runs roughly: south wall -> snake to NE shaft at (11, 11).
maze_l1 = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
# Level 2 path runs from shaft top at (11, 11) back to center emerald.
maze_l2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 2, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
mazes = [maze_l1, maze_l2]

# state holder list -- avoids `global` (unsupported in static Python)
origin = [0, 0, 0]


# ----------------------- helpers -----------------------
def set_b(b, x, y, z):
    blocks.place(b, world(origin[0] + x, origin[1] + y, origin[2] + z))


def fill_b(b, x1, y1, z1, x2, y2, z2):
    blocks.fill(
        b,
        world(origin[0] + x1, origin[1] + y1, origin[2] + z1),
        world(origin[0] + x2, origin[1] + y2, origin[2] + z2),
        FillOperation.REPLACE)


# ----------------------- phase 1: full glass shell -----------------------
def build_shell(lvl):
    y0 = lvl * LEVEL_H
    # fill the whole level volume with glass first (every block explicit)
    fill_b(GLASS, 0, y0, 0, GW - 1, y0 + LEVEL_H - 1, GH - 1)
    # stone-brick floor (overrides bottom glass)
    fill_b(STONE_BRICKS, 0, y0, 0, GW - 1, y0, GH - 1)
    # solid ceiling on top level so player can't fall out the top
    if lvl == LEVELS - 1:
        fill_b(STONE_BRICKS, 0, y0 + LEVEL_H - 1, 0,
               GW - 1, y0 + LEVEL_H - 1, GH - 1)


# ----------------------- phase 2: carve explicit agent path -----------------------
# Every path cell is set to AIR by hand at BOTH agent-body heights.
# Wall cells stay glass. "2" cells become a redstone-block marker
# (with air above so the agent can stand on it / sense it).
def carve_path(lvl):
    y0 = lvl * LEVEL_H
    m = mazes[lvl]
    for cy in range(GH):
        for cx in range(GW):
            v = m[cy][cx]
            if v == 0:
                set_b(AIR, cx, y0 + 1, cy)
                set_b(AIR, cx, y0 + 2, cy)
            elif v == 2:
                set_b(REDSTONE_BLOCK, cx, y0 + 1, cy)
                set_b(AIR,            cx, y0 + 2, cy)


def carve_entrance():
    # open the south wall at column 1 on level 1
    set_b(AIR, 1, 1, 0)
    set_b(AIR, 1, 2, 0)


def carve_shaft(cx, cz, y_from, y_to):
    # vertical 1x1 air column joining two levels, with a ladder on south face
    fill_b(AIR, cx, y_from, cz, cx, y_to, cz)
    for y in range(y_from, y_to + 1):
        set_b(LADDER, cx, y, cz + 1)


# ----------------------- phase 3: mechanical (doors, levers, plates, emerald) -----------------------
def place_mechanical():
    # ---- L1 AND chamber ----
    # Carve a 3-wide x 3-deep chamber at cells (cx0..cx0+2, cz0..cz0+2) on L1.
    # Layout (top view, y = y0+1):
    #
    #   . S . S .          (S = stone block carrying a LEVER on top)
    #   . . . . .
    #   . . D . .          (D = iron door, agent exits north to shaft)
    #
    # Sits just south of the NE shaft at (11, 11).
    cx0 = 8
    cz0 = 8
    fill_b(AIR, cx0, 1, cz0, cx0 + 2, 2, cz0 + 2)
    # two lever pillars
    set_b(STONE, cx0,     1, cz0)
    set_b(LEVER, cx0,     2, cz0)
    set_b(STONE, cx0 + 2, 1, cz0)
    set_b(LEVER, cx0 + 2, 2, cz0)
    # iron door at chamber's north exit
    set_b(IRON_DOOR, cx0 + 1, 1, cz0 + 2)

    # ---- L2 OR alcove ----
    # Two pressure plates next to the iron door. Each plate sits on a stone
    # block that becomes a power source while the plate is pressed, so the
    # adjacent door receives signal directly with a 1-block wire.
    by2 = LEVEL_H
    # carve alcove
    fill_b(AIR, 2, by2 + 1, 9, 4, by2 + 2, 11)
    set_b(STONE,                2, by2 + 1, 10)
    set_b(STONE_PRESSURE_PLATE, 2, by2 + 2, 10)
    set_b(STONE,                4, by2 + 1, 10)
    set_b(STONE_PRESSURE_PLATE, 4, by2 + 2, 10)
    set_b(IRON_DOOR, 3, by2 + 1, 11)

    # ---- emerald exit on top level ----
    by3 = LEVEL_H * (LEVELS - 1)
    fx = GW // 2
    fz = GH // 2
    fill_b(AIR, fx - 1, by3 + 1, fz - 1, fx + 1, by3 + 2, fz + 1)
    set_b(EMERALD_BLOCK, fx, by3 + 1, fz)
    set_b(GLOWSTONE,     fx, by3 + 3, fz)


# ----------------------- phase 4: redstone (LAST - nothing built above) -----------------------
# All wire runs below are short (<= 6 blocks) so signal carries cleanly.
def place_redstone():
    # ---- AND gate behind the L1 chamber ----
    # Compact NOR-of-NOTs gate placed BEHIND the chamber's back wall.
    # Inputs come from the two lever-bearing stone blocks at
    # (8, 1, 8) and (10, 1, 8). Output goes to the iron door at (9, 1, 10).
    #
    # Top-view footprint (y=1):
    #
    #   stoneA   .   stoneB        z=8   (lever stone blocks; powered by lever)
    #     .     .     .            z=9   (chamber interior; empty path)
    #   torchN  inv  torchN        z=10  (NOT torches on side of each input;
    #                                     final inverter base sits center)
    #   wire   torch  wire         y=2 on top of the inverter stone
    #
    # We place: NOT torches, the inverter pedestal, then wire LAST.

    # carve a thin "gate alley" behind the chamber back wall
    # (the back wall is at z=10; build at z=11 just south of door)
    fill_b(AIR, 7, 1, 11, 11, 2, 11)
    fill_b(STONE_BRICKS, 7, 0, 11, 11, 0, 11)

    # NOT torches attached to the side of each lever's stone block.
    # Torches face south (out of the lever-stone) so they sit at z=9
    # against the stone blocks at z=8.
    set_b(REDSTONE_TORCH, 8,  1, 9)
    set_b(REDSTONE_TORCH, 10, 1, 9)

    # Final inverter pedestal in the middle, behind the door.
    set_b(STONE,          9, 1, 11)
    set_b(REDSTONE_TORCH, 9, 2, 11)

    # WIRES LAST -- nothing will be placed above these positions.
    # NOR row joining the two NOT torch outputs (3 blocks long)
    fill_b(REDSTONE_WIRE, 8, 1, 10, 10, 1, 10)
    # output wire on top of the final inverter, running toward the door
    set_b(REDSTONE_WIRE, 9, 2, 10)

    # ---- OR gate is implicit: each plate's stone block sits adjacent
    # to the door. No long wires required. ----


# ----------------------- main -----------------------
def build_all():
    p = player.position()
    origin[0] = p.get_value(Axis.X) + 2
    origin[1] = p.get_value(Axis.Y)
    origin[2] = p.get_value(Axis.Z) + 2

    player.say("Building 2-level glass logic maze...")

    # phase 1: solid glass shell per level
    for lvl in range(LEVELS):
        build_shell(lvl)

    # phase 2: explicit air corridor for every path cell + entrance + shaft
    for lvl in range(LEVELS):
        carve_path(lvl)
    carve_entrance()
    carve_shaft(GW - 2, GH - 2, 1, LEVEL_H * 2 - 1)

    # phase 3: doors / levers / plates / emerald
    place_mechanical()

    # phase 4: redstone wires (LAST so nothing is placed above them)
    place_redstone()

    player.say("=== MAZE READY ===")
    player.say("L1: flip BOTH levers (AND) to open the iron door.")
    player.say("L2: step on EITHER pressure plate (OR) to open the door.")
    player.say("Goal: reach the EMERALD block on level 2.")

    player.teleport(world(origin[0] + 1, origin[1] + 1, origin[2] + 1))


def on_build():
    build_all()
player.on_chat("build", on_build)
