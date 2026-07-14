# 🧩 M002 Extension 1 — Redstone Trail Solver

**Topic:** Redstone Trail Solver (3D Cube Maze) · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

The agent solves a **3D cube maze** on its own by reading a **redstone trail** all around it. Drive it with chat: `l` left, `r` right, `run` starts it, `rl` brings it back.

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

**What does `detect(REDSTONE, DOWN)` tell the agent?**

<div class="write-space"></div>

---

## 3 · Fill the Blanks ✏️

The agent should step forward, then go **up** when there is redstone **below** it.

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

## 5 · Show Your Work 📸🎥

Open the world and type `run`. Let the agent reach the goal.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
