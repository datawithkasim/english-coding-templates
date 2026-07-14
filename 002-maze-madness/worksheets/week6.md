# 🔴 M002 Week 6 — Redstone & Levers

**Topic:** Redstone Levers · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

The maze has **redstone levers**. The agent detects redstone, flips a lever with `interact` to open the door, then walks through to clear the maze.

---

## 1 · The API 📖

| Code | What it does |
| --- | --- |
| `agent.detect(REDSTONE, FORWARD)` | True if redstone is ahead |
| `agent.interact(...)` | flip the lever in front |
| `agent.move(FORWARD, 1)` | step one block |
| `agent.turn(RIGHT_TURN)` | turn right |
| `player.on_chat("go", run)` | run code on chat word |

---

## 2 · Predict 🔮

```python
agent.move(FORWARD, 1)
agent.interact(...)
agent.move(FORWARD, 1)
```

**The agent reaches a lever and flips it. What happens to the door?**

<div class="write-space short"></div>

```python
agent.interact(...)
agent.move(FORWARD, 1)
agent.move(FORWARD, 1)
```

**There is no lever in front. What happens?**

<div class="write-space short"></div>

---

## 3 · Trace the Code 🔍

```python
while not agent.detect(REDSTONE, FORWARD):
    agent.move(FORWARD, 1)
agent.interact(...)
agent.turn(RIGHT_TURN)
agent.move(FORWARD, 1)
agent.move(FORWARD, 1)
```

**Describe what the agent does, step by step, in plain English.**

<div class="write-space"></div>

---

## 4 · Spot and Fix the Bugs 🐛

Write the fixed code, then say why.

**Bug A** — Flip the lever **first**, then walk through the open door. The lever is at the first wall.

```python
agent.move(FORWARD, 1)
agent.move(FORWARD, 1)
agent.interact(...)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

**Bug B** — Walk **up to** the lever, then flip it **once**. This flips on every step.

```python
while not agent.detect(REDSTONE, FORWARD):
    agent.move(FORWARD, 1)
    agent.interact(...)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

**Bug C** — After flipping, the agent must **turn around** and go back through the door. The door is behind it.

```python
agent.interact(...)
agent.move(FORWARD, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

---

## 5 · Write the Code ✍️

Somewhere ahead is a lever. Write code that walks to it, flips it, and walks through the open door.

```python
def run():
    # your code here


player.on_chat("go", run)
```

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Show Your Work 📸🎥

Open your homework world. The maze has a **lever** that opens a **closed door**. Write code that:

1. moves the agent to the lever,
2. flips it with `interact`,
3. walks through the open door,
4. reaches the goal.

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
