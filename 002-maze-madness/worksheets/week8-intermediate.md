# 🏆 M002 Week 8 — Final Cube Maze

**Topic:** Final Cube Maze · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

Last week. Build a 3D cube maze with a door and a lever. Write code that solves it on its own.

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

This loop should solve the maze. Fill in the two blanks.

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

This must use `interact` **only** when a lever is ahead. Right now it interacts every step.

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

## 5 · Build It 📸 + Video Plan 🎥

Build your final maze:

- **20 × 20 × 20** cube
- more than one floor
- 1 redstone door
- 1 lever the agent flips
- start and finish
- code with `while` + `if/else` + `interact` (use `agent.move(UP, 1)` for floors)

Send a photo or video of the agent at the goal. Write 3-4 sentences.

> My maze has … floors and … levers.
>
> The agent's strategy is …
>
> The hardest part was …
>
> I am proud of …

<div class="write-space"></div>

**Phone video plan.** Use these words: **cube**, **floor**, **lever**, **door**, **strategy**.

> 1. Show the cube outside, then inside.
> 2. Point to the start, goal, door, and lever.
> 3. Run your code to the goal.
> 4. Read your main loop out loud and say what it does.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
