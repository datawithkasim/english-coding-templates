# 🧩 M002 Extension 3 — Builder Challenge

**Topic:** Design a Maze + Write the Solution · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 60 minutes

This time you are the maze maker. Design one maze that **stretches through 6 zones**, wire it with pistons and doors, then write the **solution code** that drives the agent to the end.

Open **M002 EXT 3 — Cube World** and build inside it. Drive the agent with chat: `l` turns left, `r` turns right, `run` starts your solver, `rl` teleports the agent back to you.

**Your maze must include:**

- **2 pistons** (each opens a wall or path when powered)
- **2 doors** (the agent opens them with `agent.interact(...)`)
- **4 AND conditions** in your solution (`... and ...`)
- **1 OR condition** in your solution (`... or ...`)

Tick off each part as you go.

---

## 1 · Design Your 6 Zones 🗺️

Your maze runs through **6 zones** in a row. Give each zone one job: a turn, a piston, a door, or a junction that checks two things.

**Sketch your 6 zones.** Write each zone number and what makes it tricky.

<div class="write-space tall" style="min-height: 240px"></div>

**Where go your 2 pistons? Which zones, and what does each open?**

<div class="write-space"></div>

**Where go your 2 doors? What is behind each one?**

<div class="write-space"></div>

---

## 2 · Build the Maze 🧱

Build it in the world. Walk it yourself first (no code) to check a person can reach the end, then tick each part as you place it.

> ☐ Zone 1 built
>
> ☐ Zone 2 built
>
> ☐ Zone 3 built
>
> ☐ Zone 4 built
>
> ☐ Zone 5 built
>
> ☐ Zone 6 built
>
> ☐ Piston #1 placed and tested
>
> ☐ Piston #2 placed and tested
>
> ☐ Door #1 placed
>
> ☐ Door #2 placed
>
> ☐ A clear START block and a clear GOAL block

**What broke while you built it? What did you change?**

<div class="write-space"></div>

---

## 3 · Write the Solution 💻

Write the **solver** with a `while True` loop so it checks every step. It needs **4 AND conditions and 1 OR condition.**

Fill in this shape for **your** maze.

```python
while True:
    agent.move(FORWARD, 1)

    # a junction — turn only when BOTH things are true  (AND)
    if agent.detect(BLOCK, LEFT) and agent.detect(REDSTONE, AHEAD):
        agent.turn(LEFT_TURN)

    # a door OR a piston gate — handle either one  (OR)
    elif agent.detect(BLOCK, AHEAD) or agent.detect(REDSTONE, RIGHT):
        agent.interact(AHEAD)
        agent.move(FORWARD, 1)
```

**Write your full solution here.** Add `if` / `elif` until it covers all 6 zones, marking each AND with `# AND` and each OR with `# OR`.

<div class="write-space tall" style="min-height: 360px"></div>

---

## 4 · Count Your Logic ✅

Go back through your solution and **count.** Write the number, then copy one real line as proof.

**How many AND conditions? (need 4)**

<div class="write-space short"></div>

**Copy one AND line:**

<div class="write-space short"></div>

**How many OR conditions? (need 1)**

<div class="write-space short"></div>

**Copy your OR line:**

<div class="write-space short"></div>

**Why did that spot need OR instead of AND? What two things is it checking for?**

<div class="write-space"></div>

---

## 5 · Spot and Fix the Bugs 🐞

Read each, say what goes wrong, then write the fix.

```python
# Should turn left only when a wall is on the left AND redstone is ahead.
if agent.detect(BLOCK, LEFT) or agent.detect(REDSTONE, AHEAD):
    agent.turn(LEFT_TURN)
```

**What is wrong, and what is the fixed line?**

<div class="write-space"></div>

```python
# Should open a door ahead, then step through it.
elif agent.detect(BLOCK, AHEAD):
    agent.move(FORWARD, 1)
    agent.interact(AHEAD)
```

**What is wrong, and what is the fixed code?**

<div class="write-space"></div>

---

## 6 · Show Your Work 📸🎥

Type `run` and watch. It sticks — find the spot, fix your code or maze, `rl` to reset, then run until it reaches the **GOAL**.

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
