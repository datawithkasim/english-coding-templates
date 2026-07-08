# 🏡 M000 Week 7 — English Worksheet (Intermediate)

**Topic:** Farm House (House + Adjacent Farm) · **Course:** Builder Basics · **Level:** Intermediate · **Time:** about 38 minutes

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
# Stage 1
[build house walls]
# Stage 2
walk to the spot beside the house
# Stage 3
[build farm patch]
```

**This plan has three stages. Why does the agent walk to a new spot in stage 2 before it builds the farm?**

<div class="write-space"></div>

```
set size to 3

repeat size times:
    repeat size times:
        place block down
        move forward
    turn right
```

**What shape does the agent leave on the ground, and how wide is it? Tell me what it is for in a farm house.**

<div class="write-space"></div>

```
move down by 2
turn right
repeat 4 times:
    move forward
turn left
```

**The agent just finished a house. Where is it going next, and why does it move down first?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block is broken. Read the goal first, then write one or two sentences on what is wrong and how to fix it. You don't need to rewrite the whole program.

**Bug A** — The agent should build the **house walls first**, then the **farm patch beside it**. Right now the two stages are in the wrong order.

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

**What is wrong, and how do you fix it?**

<div class="write-space"></div>

**Bug B** — The agent should **walk to the spot beside the house first**, and the farm should land on the **ground**, not on top of the house. Hint: look at where `move down by 2` happens.

```
repeat 3 times:
    repeat 3 times:
        place block down
        move forward
    turn right
move down by 2
```

**What is wrong, and how do you fix it?**

<div class="write-space"></div>

**Bug C** — The house walls and the farm patch should share the **same `size` number**, so changing one value changes both. Right now the sizes are hard-coded and do not match.

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

**What is wrong, and how do you fix it with one `size` variable?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Now switch to your homework world. Build your farm house — a small house with walls, plus a farm patch beside it on the ground. When you finish, come back here.

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
