# 🎮 M004 Week 3 — English Worksheet

**Topic:** Sensing the World · **Course:** Functions & Games · **Time:** about 45 minutes

This week your agent **senses** the world before it acts. It can detect a block **ahead**, check what is **below**, and act differently for each block type.

---

## 1 · Predict 🔮

```
if agent detects block ahead:
    turn left
otherwise:
    move forward
```

**There is a stone wall right in front of the agent. What does it do? What if the path ahead is open?**

<div class="write-space"></div>

```
if block below is lava:
    place block below
    move forward
otherwise:
    move forward
```

**The agent is standing at the edge of a lava pool. What does it do before moving? Does it fall in?**

<div class="write-space"></div>

```
repeat 5 times:
    if block below is dirt:
        place flower
    if block below is sand:
        place cactus
    move forward
```

**The agent walks over: dirt, sand, dirt, stone, sand. What gets planted on each step?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below is broken. Rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — The agent should place a safe block when the block **below** is lava. But it never notices the lava under its feet and falls in.

```
if agent detects block ahead:
    place block below
move forward
```

**Hint:** the lava is **below**, but the check looks **ahead**.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent should plant a flower **only** when it is standing on dirt. But it plants a flower on **every** step, even on stone.

```
repeat 5 times:
    if block below is air OR block below is dirt:
        place flower
    move forward
```

**Hint:** above the ground, the block ahead of the agent is almost always air — so this check is almost always true.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The agent should cross the field safely: cover lava when it sees it, and walk when the ground is safe. But this code **only** handles the lava case — on safe ground the agent does nothing and gets stuck.

```
repeat 8 times:
    if block below is lava:
        place block below
        move forward
```

**Hint:** add an `otherwise` so the agent still moves on safe ground.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Switch to your homework world. Send your agent across the danger field: check the block **below** and the block **ahead**, and act differently for **two** block types.

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
