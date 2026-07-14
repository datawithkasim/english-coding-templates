# 🌀 M002 Week 1 — While Loop

**Topic:** Repeat Until a Wall · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

A while loop checks, runs the body, then checks again. It stops when the check is false.

---

## 1 · Trace the Loop 🔮

```python
while not agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
```

**The wall is 5 steps ahead. How many moves? When does the loop end?**

<div class="write-space"></div>

---

## 2 · Read the API 📖

| Call | What it does |
|------|--------------|
| `agent.detect(BLOCK, FORWARD)` | true if a wall is ahead |
| `agent.move(FORWARD, 1)` | step forward once |
| `agent.turn(RIGHT_TURN)` | turn right |

**Why check `not agent.detect(...)` and not `agent.detect(...)`?**

<div class="write-space short"></div>

---

## 3 · Spot the Bugs 🐛

**Bug A** — should move until the wall.

```python
while agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
```

**Fix it:**

<div class="write-space short"></div>

**Bug B** — should stop right at the wall, not crash.

```python
while not agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
```

**Fix it. Say why it crashed:**

<div class="write-space"></div>

---

## 4 · Write a Chat Command ✏️

Make `go` move the agent forward until a wall.

> Use `player.on_chat`, `while`, `agent.detect`, `agent.move`.

<div class="write-space"></div>

---

## 5 · Loop, Turn, Loop ✏️

Move to the wall, turn right, then move to the next wall.

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Show Your Work 📸🎥

Open your homework world. Use a while loop to drive the agent down the straight maze to the wall.

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
