# 🧩 M002 Extension 3 — Builder Challenge

**Topic:** Build a Maze + Write the Solution · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

This time **you** make the maze. Build one maze that runs through **6 zones**. Wire it with pistons and doors. Then write the code that drives the agent to the end.

Open **M002 EXT 3 — Cube World** and build inside it. Chat: `l` turns left, `r` turns right, `run` starts your solver, `rl` sends the agent back to start.

**Your maze needs at least:**

- **2 pistons** (each opens a wall when powered)
- **2 doors** (the agent opens them with `agent.interact(...)`)
- **4 AND** conditions in your code (`... and ...`)
- **1 OR** condition in your code (`... or ...`)

---

## 1 · Plan Your 6 Zones 🗺️

Your maze runs through **6 zones** in a row. The agent finishes one and walks into the next. Give each zone one job: a turn, a piston, or a door.

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

Build it in the world. Walk the path yourself first — make sure a person can reach the end. Tick each part.

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

Write the solver. Use a `while True` loop so it checks every step. Your code needs **4 AND** and **1 OR**.

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

Write your own checks for your maze. Add more `if` / `elif` until all 6 zones are covered. Mark each one `# AND` or `# OR`.

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

## 5 · Test, Finish, and Show 📸

Type `run` and watch. It will get stuck — that is normal. Find where it stops, fix the code or the maze, run again. Use `rl` to send it back. Keep going until the agent reaches the **GOAL** on its own.

Send a photo OR video of the agent at the goal. Then write 3 or 4 sentences with these starters.

> My maze runs through 6 zones. The trickiest zone was …
>
> I put my pistons in … and my doors in …
>
> I used an AND at … to make the agent …
>
> I needed an OR at … because …

<div class="write-space tall" style="min-height: 240px"></div>

**Plan your phone video.** Take a video on your phone (or a parent's phone). Show off your maze like a game designer. Write what you will say — you can read from it while filming.

> 1. Show the whole maze and point out the 6 zones.
> 2. Show each piston and each door, and say what it does.
> 3. Read one AND check out loud and say what it decides.
> 4. Type `run` and let the agent reach the goal.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
