# 🎮 M004 Week 3 — English Worksheet

**Topic:** Sensing the World · **Course:** Functions & Games · **Time:** about 45 minutes

This week your agent **senses** the world before it acts. It can detect a block **ahead**, check what is **below**, and do something different for each block type — like stopping before lava.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

**Bug C** — The agent should cross the field safely: cover lava when it sees it, and just walk when the ground is safe. But this code **only** handles the lava case — on safe ground the agent does nothing and gets stuck.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Send your agent across the danger field: it must check the block **below** at least once and the block **ahead** at least once, and act differently for at least two block types. When you finish, come back here.

Send a photo or video of the agent crossing safely, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My agent detected …
>
> When the block below was …, my agent …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent crosses the field. Talk through it like you are teaching someone who has never seen it. Try to use these words: **detect**, **below**, **ahead**, **condition**, **otherwise**.

> 1. Show the danger field, then run your code.
> 2. Read each `if … detects …` block out loud and say what makes it run.
> 3. Show one moment where the agent acted **differently** because of what it sensed.
> 4. Say in your own words why the agent checks **before** it moves.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
