# 🏘️ M000 Week 8 — English Worksheet

**Topic:** Build a Village (Final Project) · **Course:** Builder Basics · **Time:** about 60 minutes

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
set size to 5
set height to 3

repeat height times:
    repeat 4 times:
        repeat size times:
            place block down
            move forward
        turn right
    move up by 1
```

**Which part of the village is this — house, well, or farm house?**

<div class="write-space"></div>

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
repeat 3 times:
    destroy block down
    move down by 1
```

**Which part of the village is this?**

<div class="write-space"></div>

```
# Stage 1
[house walls + roof]
# Stage 2
move to next spot
[well]
# Stage 3
move to next spot
[farm house]
```

**This is the skeleton for the whole village. What does the agent need between each stage?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block is broken. Read what it should do, rewrite it, then explain why the original was wrong.

**Bug A** — The village should have **a house with a roof, a well, and a farm house** — three structures, side by side.

```
# House
[house walls + roof code]
# Well
[well code]
```

**Hint:** something is missing. Rewrite the skeleton to include all three structures.

**Write the fixed skeleton:**

<div class="write-space"></div>

**What was missing? Why does the full version work?**

<div class="write-space"></div>

**Bug B** — Between each structure, the agent must **walk to a new spot** so the next structure doesn't land on top of the last one.

```
# House
[house walls + roof]
# Well
[well code]
# Farm house
[farm house code]
```

**Hint:** add the missing "move to next spot" steps. You don't need to write the full house/well/farm code — write where the agent should walk between stages.

**Write the fixed skeleton:**

<div class="write-space"></div>

**Why was the original wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The house roof should sit on top of the walls, but in this code the agent stays on the ground after the walls.

```
repeat height times:
    repeat 4 times:
        repeat size times:
            place block down
            move forward
        turn right
# now place the roof
repeat size times:
    repeat size times:
        place block down
        move forward
```

**Hint:** the agent finishes the walls on the ground. Where should it go before placing the roof?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Switch to your homework world and build your village — **a house with a roof, a well, and a farm house**. If you have time, add a standalone farm too.

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
