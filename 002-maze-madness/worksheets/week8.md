# 🏆 M002 Week 8 — Final Cube Maze

**Topic:** Final Cube Maze · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

This is the final project. Design a 20×20×20 cube maze with redstone doors and levers, then write Python that solves it on its own. It combines everything: loops, turns, AND/OR, 3D up/down, levers, and pistons.

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

## 6 · Build It 📸

Build your final project. Your maze must have:

- a **20 × 20 × 20** cube
- more than one floor
- at least 1 redstone door
- at least 1 lever the agent flips
- a clear start and finish
- agent code that solves it with `while` + `if/else` + `interact` + `agent.move(UP, 1)`

Send a photo or video of the agent reaching the goal. Then write 4-6 sentences.

> My maze has … floors and … levers.
>
> The agent's strategy is …
>
> The hardest part of building was …
>
> The hardest part of the code was …
>
> To fix it, I …
>
> I am most proud of …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 7 · Record Your Walkthrough 🎥

Film on your phone while the agent runs. Teach it like the viewer has never seen it. Use these words: **cube**, **floor**, **lever**, **door**, **strategy**.

> 1. Show the cube from outside, then inside.
> 2. Point out the start, goal, door, and lever.
> 3. Run your code and follow the agent to the goal.
> 4. Read your most important loop out loud and say what it does.
> 5. Say what you learned across the 8 weeks.

**Plan what you will say below. Read from it while filming.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
