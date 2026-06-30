# 🔴 M002 Week 6 — Redstone & Levers

**Topic:** Redstone Levers · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

This week the maze has **redstone levers**. The agent detects redstone, flips a lever with `interact` to open a closed redstone door, then walks through to clear the maze.

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

Each block is broken. Write the fixed code, then say why.

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

The agent starts in the maze. Somewhere ahead is a lever. Write code that walks to the lever, flips it, and walks through the open door.

```python
def run():
    # your code here


player.on_chat("go", run)
```

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Finish the Maze 📸

Open your homework world. The maze has a **lever** that opens a **closed door**. Write code that:

1. moves the agent to the lever,
2. flips it with `interact`,
3. walks through the open door,
4. reaches the goal.

Send a photo or video of the agent at the end. Then write 4 to 6 sentences.

> First, I walked the agent to …
>
> I used `interact` to …
>
> Once the door opened, the agent …
>
> The hardest part was …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 7 · Record Your Walkthrough 🎥

Film the agent running the maze on a phone. Teach it like the viewer has never seen it. Use these words: **lever**, **interact**, **flip**, **door**, **open**.

> 1. Show the closed door and the lever.
> 2. Run your code. Show the agent flip the lever.
> 3. Read your code out loud. Say which line opens the door.
> 4. Show one bug you hit and how you fixed it.

**Plan what you will say before you record. You can read it while filming.**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
