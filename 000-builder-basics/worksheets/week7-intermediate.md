# 🏡 M000 Week 7 — English Worksheet (Intermediate)

**Topic:** Farm House (House + Adjacent Farm) · **Course:** Builder Basics · **Level:** Intermediate · **Time:** about 38 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read the goal first, then write one or two sentences saying what is wrong and how you would fix it. You do not need to rewrite the whole program — just explain the fix clearly.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build your farm house — a small house with walls, plus a farm patch beside it on the ground. When you finish, come back here.

Send a photo or video of your farm house, then explain what you did. Use these sentence starters — write 3 or 4 sentences.

> First, I built the house walls by …
>
> To get to the farm spot, the agent had to …
>
> The farm patch is … blocks wide.
>
> The hardest part was …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera around your farm house. Talk through it like you are teaching a friend who has never seen it. Try to use these words: **walls**, **farm**, **patch**, **stage**.

> 1. Show the house, then walk over to the farm patch.
> 2. Say what stage 1 and stage 2 do.
> 3. Show one bug you hit and how you fixed it.
> 4. Say how big the house is and how big the farm is.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
