# 🔂 M001 Week 4 — English Worksheet (Beginner)

**Topic:** Nested Loops · **Course:** Pyramid Problems · **Level:** Beginner · **Time:** about 30 minutes

A **nested loop** is a loop inside another loop. The inner loop builds one side; the outer loop repeats it for every side.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

**What shape does this make on the ground? Circle one:** line · square · tower

**How many sides does it have?**

<div class="write-space short"></div>

```
repeat 3 times:
    place block down
    move forward
```

**This is only the inner loop, on its own. What does it build? Circle one:** one side · a whole square

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should build a square: 4 sides, turning after each side.

```
# clean
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

```
# buggy
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
        turn right
```

**What is wrong? Look at where `turn right` sits.**

<div class="write-space short"></div>

**Pair B** — The agent should build a square with a nested loop, not just one line.

```
# clean
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

```
# buggy
repeat 3 times:
    place block down
    move forward
turn right
```

**What is wrong? How much of the square does the buggy code build?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent should build a square. After each side, it must turn. One line is missing. Fill it in using the word bank.

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    ____________
```

**Word bank:** `turn right` · `move up by 1` · `place block down`

**Write the missing line:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Build a **4×4 square floor** using a nested loop. When you finish, come back here.

Send a photo or video of your floor, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My outer loop repeated … times.
>
> My inner loop did …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and show your square. Talk like you are teaching a friend. Try to use these words: **nested loop**, **outer**, **inner**, **repeat**.

> 1. Show what your nested loop built.
> 2. Read the outer loop and the inner loop out loud.
> 3. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
