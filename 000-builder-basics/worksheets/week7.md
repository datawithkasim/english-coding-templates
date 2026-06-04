# 🏡 M000 Week 7 — English Worksheet

**Topic:** Farm House (House + Adjacent Farm) · **Course:** Builder Basics · **Time:** about 45 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build your farm house — small house with walls and roof, plus a farm patch beside it. Try making the farm bigger (5×5) **or** add a path between the house and farm. When you finish, come back here.

Send a photo or video of your farm house, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I built the house walls by …
>
> Then I built the roof by …
>
> To get to the farm spot, the agent had to …
>
> The farm patch is … blocks wide.
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera around your farm house. Talk through it like you are teaching someone who has never seen it. Try to use these words: **walls**, **roof**, **farm**, **patch**, **stage**.

> 1. Show the house, then walk over to the farm patch.
> 2. Read your house loops and farm loops out loud and say what each stage does.
> 3. Show one bug you hit and how you fixed it.
> 4. Say how big the house is and how big the farm is.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
