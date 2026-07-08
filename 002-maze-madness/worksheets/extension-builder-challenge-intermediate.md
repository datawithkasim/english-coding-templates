# 🧩 M002 Extension 3 — Builder Challenge

**Topic:** Build a Maze + Write the Solution · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

This time **you** make the maze. Build one that runs through **6 zones**, wired with pistons and doors, then write the code that drives the agent to the end.

Open **M002 EXT 3 — Cube World** and build inside it. Chat: `l` turns left, `r` turns right, `run` starts your solver, `rl` sends the agent back to start.

**Your maze needs:**

- **2 pistons** (each opens a wall when powered)
- **2 doors** (the agent opens them with `agent.interact(...)`)
- **4 AND** conditions in your code (`... and ...`)
- **1 OR** condition in your code (`... or ...`)

---

## 1 · Plan Your 6 Zones 🗺️

Your maze runs through **6 zones** in a row. Give each zone one job: a turn, a piston, or a door.

> Zone 1: …
>
> Zone 2: …
>
> Zone 3: …
>
> Zone 4: …
>
> Zone 5: …
>
> Zone 6: …

<div class="write-space"></div>

Which 2 zones get a piston, and what does each open? Which 2 get a door?

<div class="write-space"></div>

---

## 2 · Build the Maze 🧱

Build it in the world. Walk it yourself first to check a person can reach the end, then tick each part.

> ☐ Zone 1   ☐ Zone 2   ☐ Zone 3   ☐ Zone 4   ☐ Zone 5   ☐ Zone 6
>
> ☐ Piston #1 tested   ☐ Piston #2 tested
>
> ☐ Door #1   ☐ Door #2
>
> ☐ A clear START block and GOAL block

What broke while you built it? What did you change?

<div class="write-space short"></div>

---

## 3 · Write the Solution 💻

Write the solver with a `while True` loop so it checks every step. Your code needs **4 AND** and **1 OR**.

```python
while True:
    agent.move(FORWARD, 1)

    # turn only when BOTH are true  (AND)
    if agent.detect(BLOCK, LEFT) and agent.detect(REDSTONE, AHEAD):
        agent.turn(LEFT_TURN)

    # a door OR a piston gate  (OR)
    elif agent.detect(BLOCK, AHEAD) or agent.detect(REDSTONE, RIGHT):
        agent.interact(AHEAD)
        agent.move(FORWARD, 1)
```

Add more `if` / `elif` until all 6 zones are covered. Mark each one `# AND` or `# OR`.

<div class="write-space tall" style="min-height: 280px"></div>

How many AND checks did you write? How many OR?

<div class="write-space short"></div>

---

## 4 · Find the Bug 🐞

This code should turn left at a junction. It turns at the wrong time.

```python
if agent.detect(BLOCK, LEFT) or agent.detect(REDSTONE, AHEAD):
    agent.turn(LEFT_TURN)
```

The agent should turn only when **both** are true. Write the fixed line.

<div class="write-space short"></div>

---

## 5 · Show Your Work 📸🎥

Type `run` and watch. It sticks — find the spot, fix the code or maze, `rl` to reset, then run until it reaches the **GOAL**.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Fill the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
