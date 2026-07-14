# 🏡 M000 Week 7 — English Worksheet

**Topic:** Farm House (House + Adjacent Farm) · **Course:** Builder Basics · **Time:** about 45 minutes

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
set size to 3
set height to 2

repeat height times:
    repeat 4 times:
        repeat size times:
            place block down
            move forward
        turn right
    move up by 1
```

**What does the agent build? How tall is it?**

<div class="write-space"></div>

```
set size to 3

repeat size times:
    repeat size times:
        place block down
        move forward
    turn right
    move forward
    turn right
    repeat size times:
        move forward
    turn left
    turn left
```

**What shape does the agent leave on the ground? What is it for in a farm house?**

<div class="write-space"></div>

```
move down by 2
turn right
repeat 4 times:
    move forward
turn left
```

**The agent just finished a house. Where is it going next?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block is broken. Read what it should do, rewrite it, then explain why the original was wrong.

**Bug A** — The agent is supposed to build the **house walls first**, then the **farm patch beside it** (two clear stages).

```
# Stage 1: farm patch
repeat 3 times:
    repeat 3 times:
        place block down
        move forward
    turn right
# Stage 2: house walls
repeat 2 times:
    repeat 4 times:
        repeat 3 times:
            place block down
            move forward
        turn right
    move up by 1
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was the order wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent is supposed to walk to the spot beside the house, **then** build the farm patch. The farm should land on the ground, not on top of the house.

```
repeat 3 times:
    repeat 3 times:
        place block down
        move forward
    turn right
move down by 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The agent is supposed to use the **same `size` variable** for the house walls and the farm patch, so changing one number changes both.

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
# farm patch
repeat 5 times:
    repeat 5 times:
        place block down
        move forward
    turn right
```

**Write the fixed code using one `size` variable:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Switch to your homework world and build your farm house — small house with walls and roof, plus a farm patch beside it. Try making the farm bigger (5×5) **or** add a path between the house and farm.

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
