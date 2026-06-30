# 🧩 M002 Extension 2 — Piston & Logic Maze

**Topic:** Two Pistons + AND Conditions · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 60 minutes

This is an **extension challenge** for students who finished the weekly mazes. The agent follows a **redstone trail** through a long maze. At some junctions it must check **two things at once** — an **AND** condition — to pick the right way. Twice along the path, a **lever powers a piston** that pulls a block back and opens the gate. Your job: drive the agent through the **whole maze**, start to finish.

Chat words: `l` turn left, `r` turn right, `run` start the solver, `rl` teleport the agent back to you.

---

## 1 · Read the Chat Commands 🎛️

Each block binds a **chat word** to an action.

```python
def on_chat():
    agent.turn(RIGHT_TURN)
player.on_chat("r", on_chat)
```

**What does the agent do when you type `r`?**

<div class="write-space short"></div>

```python
def on_chat():
    agent.teleport_to_player()
player.on_chat("rl", on_chat)
```

**You type `rl`. Where does the agent go, and when does that help in a long maze?**

<div class="write-space"></div>

**This maze has two pistons far apart. Why test the first half with `l` and `r` before you type `run`?**

<div class="write-space"></div>

---

## 2 · Trace the Solver 🔍

This loop runs when you type `run`. It follows the trail, makes AND decisions, and flips a lever at each piston gate.

```python
while True:
    agent.move(FORWARD, 1)
    if agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, AHEAD):
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, 1)
    elif agent.detect(BLOCK, AHEAD) and agent.detect(REDSTONE, RIGHT):
        agent.turn(RIGHT_TURN)
        agent.move(FORWARD, 1)
    elif agent.detect(BLOCK, AHEAD):
        agent.interact(AHEAD)
        agent.move(FORWARD, 1)
```

**The loop is `while True`. When does it stop on its own?**

<div class="write-space short"></div>

**First check: `detect(REDSTONE, LEFT) and detect(REDSTONE, AHEAD)`. Describe a spot in the maze where both are true.**

<div class="write-space"></div>

**The last `elif` is a piston gate: a block ahead, no redstone beside it. What does `agent.interact(AHEAD)` do, and why can the agent move forward right after?**

<div class="write-space"></div>

**Why does check order matter? What breaks if `elif agent.detect(BLOCK, AHEAD)` ran first, before the two AND checks?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block is broken. Read its goal, rewrite it, then explain the fix.

**Bug A** — Turn left **only when redstone is left AND ahead**. This turns on either one.

```python
if agent.detect(REDSTONE, LEFT) or agent.detect(REDSTONE, AHEAD):
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

**Bug B** — The solver should check on **every step** for the whole maze. This checks once and stops.

```python
agent.move(FORWARD, 1)
if agent.detect(BLOCK, AHEAD):
    agent.interact(AHEAD)
    agent.move(FORWARD, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

**Bug C** — At a piston gate, **flip the lever first**, then cross the gap. This walks forward before powering the piston, so it hits a closed wall.

```python
agent.move(FORWARD, 1)
agent.move(FORWARD, 1)
agent.interact(AHEAD)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

---

## 4 · Make It Your Own 🛠️

Open the **M002 EXT 2** world and run `run`. Now **change one thing** and predict before you test.

Pick **one** (or your own):

- Add a chat word `back` that turns the agent around (two right turns).
- Place a block (`agent.place(...)`) each time it flips a lever, so you can see how far it got.
- Add an `elif` for a junction where redstone is on the **right and ahead** at once.

**Which did you pick? Write the code.**

<div class="write-space tall" style="min-height: 200px"></div>

**Predict: what will happen?**

<div class="write-space short"></div>

**Test it. What actually happened?**

<div class="write-space"></div>

---

## 5 · Finish the Whole Maze 📸

Get the agent from **start to the very end** — past both piston gates and every junction. Run `run`, see where it sticks, fix, run again until it reaches the goal.

Send a photo or video of the agent at the goal, then explain. Use these starters — 4 to 6 sentences.

> The maze had two pistons, so the agent had to …
>
> At a junction I used an AND condition to …
>
> At a piston gate, the agent flipped the lever first because …
>
> The change I made in section 4 was …
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film on a phone while the agent solves the whole maze. Teach it like the viewer has never seen it. Try to use: **detect**, **redstone**, **trail**, **AND**, **piston**, **lever**, **loop**.

> 1. Show the maze and redstone trail before you start.
> 2. Type `run` and show the agent following the trail.
> 3. Read one AND check out loud and say what it decides.
> 4. Show the agent reaching a piston gate and flipping the lever.
> 5. Show it reaching the goal.

**Write what you will say. Plan it here first — read from it while filming.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
