# 🧊 M002 Week 5 — English Worksheet

**Topic:** Mini Cube Puzzle · **Course:** Maze Madness · **Time:** about 45 minutes

This week you finish the **mini cube**. You already have starter code that builds part of the cube. Your job is to **keep it going** — add more decisions with conditionals, and leave a way out through the **top**.

> Two ways to finish — pick the one that fits you:
>
> - **Challenge:** add **2 more conditionals**, and make **one of them an `OR`**.
> - **Steady:** keep the same pattern the starter uses and **fill the whole cube**.
>
> Either way: the agent must **break a hole in the top** and climb out.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
repeat 5 times:
    place block
    move forward
```

**What shape does the agent leave behind? How long is it?**

<div class="write-space"></div>

```
if on the edge OR on the top layer:
    place block
otherwise:
    leave empty
```

**Only one condition needs to be true. Which spots get a block? Which stay empty?**

<div class="write-space"></div>

```
repeat for each layer:
    fill the layer
move up
if at the top:
    break block above
    climb out
```

**Describe in plain English what the agent does, from the first layer to climbing out.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent should place a block on **every edge** of the layer, then move up. Right now it moves up **before** finishing the layer.

```
place block
move up
place block
place block
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent should leave a block when it is on the **bottom layer** `OR` on an **outer wall**. Right now it only fills the bottom layer.

```
if on the bottom layer:
    place block
```

**Hint:** one condition is missing. Add the wall check with `OR`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — After the cube is full, the agent should **break the block above** and climb out the top. Right now it tries to climb **before** making the hole, so it gets stuck.

```
move up
break block above
```

**Hint:** make the hole first, then move into it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Finish the Cube 📸

Open this week's world. You will find the **mini cube starter** — some of the cube is already built. Finish it your way:

**Challenge path**

1. Keep the starter running.
2. Add **2 more conditionals** that decide where blocks go (for example: a different block on corners, or skip a spot to leave a pattern).
3. Make **one** of them use `OR` (for example: `if on a corner OR on the top → place glass`).
4. Make sure the agent **breaks a hole in the top** and climbs out.

**Steady path**

1. Keep the **same pattern** the starter uses.
2. Repeat it until the **whole cube is filled**.
3. Make sure the agent **breaks a hole in the top** and climbs out.

When you finish, come back here. Send a **photo or video** of the finished cube (and the hole in the top!), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I looked at the starter code and saw …
>
> To keep building, I …
>
> I used a conditional when …
>
> I made the hole in the top by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent builds the cube. Talk through it like you are teaching someone who has never seen it. Try to use these words: **cube**, **layer**, **conditional**, **OR**, **hole**.

> 1. Show the starter cube before you run your code.
> 2. Run your code and watch the cube fill up.
> 3. Read your conditional out loud and say what makes it run.
> 4. Show the agent breaking the hole in the top and climbing out.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
