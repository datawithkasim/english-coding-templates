# 🧩 M002 Extension 1 — Redstone Trail Solver

**Topic:** Redstone Trail Solver (3D Cube Maze) · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 60 minutes

This is an **extension challenge** for students who finished the weekly mazes. The agent solves a **3D cube maze** on its own. It reads a **redstone trail** above, below, left, right and ahead, then decides what to do at every step. You drive it with chat: `l` turns left, `r` turns right, `run` starts the solver, `rl` teleports it back to you.

---

## 1 · Read the Chat Commands 🎛️

Each block binds a **chat word** to an action. Type the word, the agent runs the code.

```
def turn_left():
    agent.turn(LEFT_TURN)
player.on_chat("l", turn_left)
```

**What does the agent do when you type `l`?**

<div class="write-space short"></div>

```
def go_back():
    agent.teleport_to_player()
player.on_chat("rl", go_back)
```

**You type `rl`. Where does the agent go? When is that useful?**

<div class="write-space"></div>

**Why bind small helpers (`l`, `r`, `rl`) _before_ you write the big `run` solver?**

<div class="write-space"></div>

---

## 2 · Trace the Solver 🔍

This loop runs when you type `run`. It checks redstone in different directions and reacts.

```
while True:
    agent.move(FORWARD, 1)
    if agent.detect(REDSTONE, DOWN) and agent.detect(REDSTONE, RIGHT):
        agent.move(FORWARD, 1)
        agent.interact(LEFT)
    elif agent.detect(BLOCK, RIGHT) and agent.detect(REDSTONE, LEFT):
        agent.move(FORWARD, 1)
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, 1)
    elif agent.detect(REDSTONE, DOWN):
        agent.move(UP, 1)
    elif agent.detect(REDSTONE, UP):
        agent.move(DOWN, 4)
```

**`while True` keeps going. When does it stop on its own?**

<div class="write-space short"></div>

**In your own words: what does `detect(REDSTONE, DOWN)` tell the agent?**

<div class="write-space"></div>

**The maze is 3D. Which two lines move the agent between floors? What does each do?**

<div class="write-space"></div>

**Why does the order of the `if` / `elif` checks matter? What changes if the `elif agent.detect(REDSTONE, DOWN)` check came _first_?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block is broken. Read what it should do, rewrite it, then explain the fix.

**Bug A** — The solver should keep going until the maze is done, checking the trail every step.

```
agent.move(FORWARD, 1)
if agent.detect(REDSTONE, DOWN):
    agent.move(UP, 1)
```

**Hint:** this checks only once. What wraps a block so it repeats?

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — When there is redstone **down and right**, step forward, then flip a lever on the **left**.

```
if agent.detect(REDSTONE, DOWN) or agent.detect(REDSTONE, RIGHT):
    agent.interact(LEFT)
```

**Hint:** "down **and** right" — both must be true. Move forward before you interact.

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Write a Branch ✍️

Add one more `elif` to the solver. When there is redstone straight **ahead**, the agent should turn **right** and move forward.

**Write the branch:**

<div class="write-space"></div>

**In one line: where in the loop should this go, and why?**

<div class="write-space short"></div>

---

## 5 · Make It Your Own 🛠️

Open the extension world and run the solver with `run`. Change **one thing**, predict, then test.

Pick **one** (or your own):

- Add a `back` command that turns the agent around (two right turns).
- Change `agent.move(DOWN, 4)` to a new number and watch where it lands.
- Add an `elif` that reacts to redstone straight **ahead**.

**Which change? Write the code.**

<div class="write-space tall" style="min-height: 200px"></div>

**Predict:** what will happen?

<div class="write-space short"></div>

**Test it.** What actually happened? If it surprised you, why?

<div class="write-space"></div>

---

## 6 · Finish the Maze 📸

When the agent finishes the cube maze, come back. Send a photo OR video of the agent at the goal, then explain. Write 4 to 6 sentences.

> The maze was 3D, so the agent had to …
>
> The redstone trail told the agent to …
>
> I used `detect` to …
>
> The change I made was …
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 7 · Record Your Walkthrough 🎥

Film the agent solving the maze on your phone. Talk through it like you are teaching someone new. Try these words: **detect**, **redstone**, **trail**, **loop**, **3D**, **elif**.

> 1. Show the cube maze and the redstone trail before you start.
> 2. Type `run` and show the agent following the trail.
> 3. Read one `if` / `elif` line out loud and say what it decides.
> 4. Show the change you made and what it did.

**Write what you will say.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
