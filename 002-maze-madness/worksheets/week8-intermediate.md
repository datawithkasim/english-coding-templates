# 🏆 M002 Week 8 — Final Cube Maze

**Topic:** Final Cube Maze · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

Final week! Build a 3D cube maze with a door and a lever, then write code that solves it.

---

## 1 · Predict 🔮

```
keep going until at goal:
    if wall ahead OR closed door ahead:
        turn right
    else if lever ahead:
        interact
    else:
        move forward
```

**Name one maze where this gets stuck.**

<div class="write-space"></div>

---

## 2 · Trace 🔍

```
keep going until at goal:
    if lever ahead:
        interact
    else if wall ahead:
        turn right
    else:
        move forward
```

**Agent sees a lever, then open path, then a wall. What does it do each step?**

<div class="write-space"></div>

---

## 3 · Fill the Blanks ✏️

This loop should solve the maze.

```
keep going until at goal:
    if wall ahead:
        agent.turn(________)
    else:
        agent.move(FORWARD, ____)
```

**Word bank:** `LEFT_TURN` · `RIGHT_TURN` · `1`

<div class="write-space"></div>

---

## 4 · One Bug 🐛

This must use `interact` **only** when a lever is ahead. It interacts on every step.

```
keep going until at goal:
    interact
    if wall ahead:
        turn right
    else:
        move forward
```

**Write the fixed code.**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

---

## 5 · Show Your Work 📸🎥

Build your final maze:

- **20 × 20 × 20** cube
- more than one floor
- 1 redstone door
- 1 lever the agent flips
- start and finish
- code with `while` + `if/else` + `interact` (use `agent.move(UP, 1)` for floors)

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
