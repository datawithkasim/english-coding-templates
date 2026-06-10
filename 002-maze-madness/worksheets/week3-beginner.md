# 🔀 M002 Week 3 — English Worksheet (Beginner)

**Topic:** AND Conditions — Two Things at Once · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 30 minutes

This week your agent checks **two things at the same time** using `AND`. With `AND`, the action only happens when **both** are true.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
if wall ahead AND wall on right:
    turn left
```

**There is a wall ahead but the right side is open. Does the agent turn? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
if wall ahead AND wall on right:
    turn left
```

**Now there is a wall ahead AND a wall on the right. Does the agent turn? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should turn left only at a **corner**: wall ahead AND wall on right.

```
# clean
if wall ahead AND wall on right:
    turn left
```

```
# buggy
if wall ahead:
    turn left
```

**What is wrong? When does the buggy agent turn too early?**

<div class="write-space short"></div>

**Pair B** — The two checks should be **different** — front and right.

```
# clean
if wall ahead AND wall on right:
    turn left
```

```
# buggy
if wall ahead AND wall ahead:
    turn left
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent should turn left only when **both** walls are there. One word is missing. Fill it in using the word bank.

```
if wall ahead ____ wall on right:
    turn left
```

**Word bank:** `AND` · `IF` · `THEN`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Solve the maze using an `AND` condition. When you finish, come back here.

Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I used **AND** when …
>
> Both conditions were true when …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent runs the maze. Talk like you are teaching a friend. Try to use these words: **AND**, **condition**, **both**, **true**.

> 1. Show the start of the maze, then run your code.
> 2. Read your `if … AND …` line out loud.
> 3. Say in your own words what **AND** means.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
