# 🧩 M002 Extension 1 — Redstone Trail Solver

**Topic:** Redstone Trail Solver (3D Cube Maze) · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

The agent solves a **3D cube maze** on its own. It reads a **redstone trail** above, below, left, right and ahead, then picks a move. You drive it with chat: `l` turns left, `r` turns right, `run` starts it, `rl` brings it back.

---

## 1 · Read the Chat Commands 🎛️

A chat word binds to an action. Type the word, the agent runs the code.

```
def turn_left():
    agent.turn(LEFT_TURN)
player.on_chat("l", turn_left)
```

**You type `l`. What does the agent do?**

<div class="write-space short"></div>

```
def go_back():
    agent.teleport_to_player()
player.on_chat("rl", go_back)
```

**You type `rl`. Where does the agent go? When is that handy?**

<div class="write-space"></div>

---

## 2 · Trace the Solver 🔍

This loop runs when you type `run`.

```
while True:
    agent.move(FORWARD, 1)
    if agent.detect(REDSTONE, DOWN):
        agent.move(UP, 1)
    elif agent.detect(REDSTONE, UP):
        agent.move(DOWN, 4)
```

**`while True` keeps going. The maze is 3D. Which line moves the agent up a floor?**

<div class="write-space short"></div>

**Which line moves it down? How far?**

<div class="write-space short"></div>

**In one short sentence: what does `detect(REDSTONE, DOWN)` tell the agent?**

<div class="write-space"></div>

---

## 3 · Fill the Blanks ✏️

The agent should step forward, then go **up** when there is redstone **below** it. Fill the blanks.

```
agent.move(________, 1)
if agent.detect(REDSTONE, ________):
    agent.move(________, 1)
```

**Word bank:** `FORWARD` · `DOWN` · `UP`

<div class="write-space"></div>

---

## 4 · Spot the Bug 🐛

This should **keep going** and check the trail on every step.

```
agent.move(FORWARD, 1)
if agent.detect(REDSTONE, DOWN):
    agent.move(UP, 1)
```

**Hint:** it only checks once. What wraps a block so it repeats?

**Write the fix:**

<div class="write-space"></div>

**One line: why was it wrong?**

<div class="write-space short"></div>

---

## 5 · Finish + Film 📸🎥

Open the world. Type `run`. Let the agent reach the goal.

Send a photo OR video of the agent at the goal. Write 3 or 4 sentences.

> The maze was 3D, so the agent had to …
>
> The redstone trail told the agent to …
>
> I used `detect` to …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

**Phone video plan.** Film the agent solving the maze. Talk like you teach a friend. Try these words: **detect**, **redstone**, **trail**, **loop**, **3D**.

> 1. Show the maze and the redstone trail.
> 2. Type `run` and show the agent following it.
> 3. Say one spot where the agent went up or down.

**Write what you will say:**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
