# 🏆 M002 Week 8 — English Worksheet

**Topic:** Capstone — 15×15×15 Cube Maze · **Course:** Maze Madness · **Time:** about 60 minutes

This is the **final project**. You design a 3D cube maze with redstone doors and levers, then write code that solves it on its own.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
A cube maze: 15 wide, 15 deep, 15 tall.
- multiple floors
- at least 1 redstone door
- at least 1 lever
- a clear start and finish
```

**Sketch (in words) one floor of your maze. Where is the start? Where is the goal?**

<div class="write-space"></div>

```
keep doing until at goal:
    if wall ahead OR closed door ahead:
        turn right
    otherwise if lever ahead:
        interact ahead
    otherwise:
        move forward
```

**This is one strategy. Name one type of maze where this will get stuck.**

<div class="write-space"></div>

```
function go_to_next_floor:
    while no stairs ahead:
        move forward
    move up by 1
```

**Why is it useful to have a function called `go_to_next_floor` in a 3D maze?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent must use `interact` only when there is a **lever** ahead — not on every step.

```
keep doing until at goal:
    interact ahead
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent should **stop** when it reaches the goal. Right now it keeps running forever.

```
keep doing forever:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — On a 3D maze the agent must also handle **going up to the next floor**. Right now the code only handles left/right/forward.

```
if wall ahead:
    turn right
otherwise:
    move forward
```

**Write the fixed code (add an "if stairs ahead" or similar):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now build your **final project**. Your maze must include:

- a **15 × 15 × 15** cube structure
- **more than one floor**
- at least **1 redstone door**
- at least **1 lever** the agent must flip
- a clear **start** and **finish**
- agent code that solves it on its own using `while` + `if/else` + `interact`

When you finish, come back here. Send a photo or video of the agent solving your maze, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My maze has … floors and … levers.
>
> The agent's strategy is …
>
> The hardest part of building the maze was …
>
> The hardest part of writing the code was …
>
> To fix it, I …
>
> The thing I am most proud of is …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs your maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **cube**, **floor**, **lever**, **door**, **strategy**.

> 1. Show the cube maze from outside, then from inside.
> 2. Point out the start, the goal, the door, and the lever.
> 3. Run your code and follow the agent all the way to the goal.
> 4. Read the most important loop in your code out loud and say what it does.
> 5. Say what you learned across the 8 weeks of this course.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk. This is the **last week** of Maze Madness — congratulations on finishing the full Minecraft track!
