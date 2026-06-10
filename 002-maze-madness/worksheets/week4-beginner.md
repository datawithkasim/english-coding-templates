# 🔂 M002 Week 4 — English Worksheet (Beginner)

**Topic:** AND and OR Conditions — Smarter Decisions · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 30 minutes

Last week your agent used `AND` (both true). This week you add `OR`:

- `AND` → the action happens **only when both** are true.
- `OR` → the action happens **when at least one** is true.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
if wall ahead AND wall on right:
    turn left
```

**Wall ahead, but the right is open. Does the agent turn? Circle one:** yes · no

<div class="write-space short"></div>

```
if no wall ahead OR no wall below:
    move forward
```

**The path ahead is blocked, but the path below is open. Does the agent move? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should turn left **only** at a corner (wall ahead AND wall on right).

```
# clean
if wall ahead AND wall on right:
    turn left
```

```
# buggy
if wall ahead OR wall on right:
    turn left
```

**What is wrong? When does the buggy agent turn too often?**

<div class="write-space short"></div>

**Pair B** — The agent should move when **either** path is clear.

```
# clean
if no wall ahead OR no wall below:
    move forward
```

```
# buggy
if no wall ahead AND no wall below:
    move forward
```

**What is wrong? When does the buggy agent get stuck?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent should move when **at least one** path is open. One word is missing. Fill it in using the word bank.

```
if no wall ahead ____ no wall below:
    move forward
```

**Word bank:** `OR` · `AND` · `NOT`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Solve the maze using an `OR` condition. When you finish, come back here.

Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I used **OR** when …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent runs the maze. Talk like you are teaching a friend. Try to use these words: **AND**, **OR**, **both**, **either**.

> 1. Show the start of the maze, then run your code.
> 2. Read your `if … OR …` line out loud.
> 3. Say in your own words how **AND** is different from **OR**.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
