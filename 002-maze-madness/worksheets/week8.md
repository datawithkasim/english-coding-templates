# 🏆 M002 Week 8 — Final Cube Maze

**Topic:** Final Cube Maze · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

Design a 20×20×20 cube maze with redstone doors and levers, then write Python that solves it. It uses everything: loops, turns, AND/OR, 3D up/down, levers, and pistons.

---

## 1 · Predict 🔮

```python
while not at_goal:
    if agent.detect(BLOCK, FORWARD) or agent.detect(REDSTONE, FORWARD):
        agent.turn(RIGHT_TURN)
    elif agent.detect(REDSTONE, DOWN):
        agent.interact(DOWN)
    else:
        agent.move(FORWARD, 1)
```

**Name one maze shape where this strategy gets stuck.**

<div class="write-space"></div>

---

## 2 · Trace 🔍

```python
while not at_goal:
    if agent.detect(REDSTONE, FORWARD):
        agent.interact(FORWARD)
    elif agent.detect(BLOCK, FORWARD):
        agent.turn(RIGHT_TURN)
    elif agent.detect(BLOCK, UP):
        agent.move(UP, 1)
    else:
        agent.move(FORWARD, 1)
```

**Ahead: a lever, then open path, then a wall, then a block above. Write the action for each step.**

<div class="write-space"></div>

---

## 3 · Spot + Fix Bugs 🐛

**Bug A** — Must `interact` only when a lever is ahead, not every step.

```python
while not at_goal:
    agent.interact(FORWARD)
    if agent.detect(BLOCK, FORWARD):
        agent.turn(RIGHT_TURN)
    else:
        agent.move(FORWARD, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Bug B** — Must stop at the goal. This runs forever.

```python
while True:
    if agent.detect(BLOCK, FORWARD):
        agent.turn(RIGHT_TURN)
    else:
        agent.move(FORWARD, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Bug C** — On a 3D maze the agent must climb floors. This only handles left/right/forward.

```python
if agent.detect(BLOCK, FORWARD):
    agent.turn(RIGHT_TURN)
else:
    agent.move(FORWARD, 1)
```

**Fixed code (add a way to go up):**

<div class="write-space"></div>

---

## 4 · Write the Function 💻

Write a function that climbs to the next floor: move forward until a wall, then move up by 1.

```python
def go_to_next_floor():
```

<div class="write-space"></div>

---

## 5 · Wire the Chat 💬

Write one line so typing `solve` in chat runs your `solve_maze` function.

<div class="write-space short"></div>

---

## 6 · Show Your Work 📸🎥

Build your final project. Your maze must have:

- a **20 × 20 × 20** cube
- more than one floor
- at least 1 redstone door
- at least 1 lever the agent flips
- a clear start and finish
- agent code that solves it with `while` + `if/else` + `interact` + `agent.move(UP, 1)`

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
