# 🧩 M002 Extension 3 — Builder Challenge

**Topic:** Design a Maze + Write the Solution · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 60 minutes

This is the big **builder challenge**. This time you are not solving someone else's maze — **you are the maze maker.** Design one maze that **stretches through 6 zones**, wire it with pistons and doors, then write the **solution code** that drives the agent all the way to the end.

Open **M002 EXT 3 — Cube World** and build inside it. Drive the agent with chat: `l` turns left, `r` turns right, `run` starts your solver, `rl` teleports the agent back to you.

**Your maze must include at least:**

- **2 pistons** (each opens a wall or path when powered)
- **2 doors** (the agent opens them with `agent.interact(...)`)
- **4 AND conditions** in your solution (`... and ...`)
- **1 OR condition** in your solution (`... or ...`)

Keep this page beside you — tick off each part as you go.

---

## 1 · Design Your 6 Zones 🗺️

A great maze is **planned before it is built.** Your maze runs through **6 zones** in a row — the agent finishes one and walks straight into the next. Give each zone one job: a turn, a piston, a door, or a junction where the agent must check two things.

**Sketch your 6 zones.** Write each zone number and what makes it tricky.

<div class="write-space tall" style="min-height: 240px"></div>

**Where go your 2 pistons? Which zones, and what does each open?**

<div class="write-space"></div>

**Where go your 2 doors? What is behind each one?**

<div class="write-space"></div>

---

## 2 · Build the Maze 🧱

Build it in the world. Walk the path yourself first (no code) and make sure a person can get from start to end. Tick each part as you place it.

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

Write the **solver** — the code that gets the agent through your whole maze. Use a `while True` loop so it checks on every step. Your solution needs **at least 4 AND conditions and 1 OR condition.**

Here is the shape to start from. Fill it in for **your** maze.

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

**Write your full solution here.** Add more `if` / `elif` checks until it covers all 6 zones. Mark each AND with `# AND` and your OR with `# OR` so you can count them.

<div class="write-space tall" style="min-height: 360px"></div>

---

## 4 · Count Your Logic ✅

Go back through your solution and **count.** Write the number, then copy one real line as proof.

**How many AND conditions? (need at least 4)**

<div class="write-space short"></div>

**Copy one AND line:**

<div class="write-space short"></div>

**How many OR conditions? (need at least 1)**

<div class="write-space short"></div>

**Copy your OR line:**

<div class="write-space short"></div>

**Why did that spot need OR instead of AND? What two things is it checking for?**

<div class="write-space"></div>

---

## 5 · Spot and Fix the Bugs 🐞

These two lines are buggy. Read each, say what goes wrong, then write the fix.

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

## 6 · Test It and Finish 📸

Type `run` and watch the agent. It will get stuck somewhere — that is normal. Find where it stops, fix that part of your code or your maze, and run it again. Use `rl` to send it back between tries. Keep going until the agent reaches the **GOAL** all by itself.

When the agent finishes your maze on its own, send a photo OR video of the agent at the goal, then explain. Write 5 to 7 sentences with these starters.

> My maze runs through 6 zones. The trickiest zone was …
>
> I put my 2 pistons in … because …
>
> The agent opens my doors with `agent.interact(...)`, which works because …
>
> I used an AND condition at … to make the agent …
>
> I needed an OR condition at … because …
>
> The agent kept getting stuck at … until I …
>
> If I built a version 2, I would add …

<div class="write-space tall" style="min-height: 360px"></div>

---

## 7 · Present Your Maze 🎥

You built this maze, so you are the expert. Take a video on your phone (or a parent's phone) and **present your maze like a designer showing off their game.** Try to use these words: **zone**, **piston**, **door**, **detect**, **AND**, **OR**, **loop**.

> 1. Show the whole maze from the start and point out the 6 zones.
> 2. Show each piston and each door, and say what it does.
> 3. Read one AND check from your code out loud and say what decision it makes.
> 4. Read your OR check and say why it needed OR.
> 5. Type `run` and let the agent solve your maze to the goal.

**Plan your video here first** — you can read from it while filming.

<div class="write-space tall" style="min-height: 360px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
