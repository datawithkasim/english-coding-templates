# 🏆 M002 Week 8 — English Worksheet (Beginner)

**Topic:** Capstone — 20×20×20 Cube Maze · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 45 minutes

This is the **final project**. You design your own maze with a redstone door and a lever, then write code that solves it.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
Your maze needs:
- walls
- 1 redstone door
- 1 lever
- a start and a finish
```

**Sketch (in words) your maze. Where is the start? Where is the goal? Where is the lever?**

<div class="write-space"></div>

```
keep doing until at goal:
    if wall ahead:
        turn right
    otherwise if lever ahead:
        interact ahead
    otherwise:
        move forward
```

**The agent reaches the lever. What does it do? Circle one:** turn right · interact · move forward

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should `interact` only when there is a **lever** ahead.

```
# clean
if lever ahead:
    interact ahead
otherwise:
    move forward
```

```
# buggy
interact ahead
move forward
```

**What is wrong?**

<div class="write-space short"></div>

**Pair B** — The agent should **stop** when it reaches the goal.

```
# clean
keep doing until at goal:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

```
# buggy
keep doing forever:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**What is wrong? When does the buggy agent stop?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent should keep going **until it reaches the goal**. One part is missing. Fill it in using the word bank.

```
keep doing until ____________:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**Word bank:** `at goal` · `forever` · `wall ahead`

**Write the missing part:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now build your **final project**. Your maze needs:

- a **20 × 20 × 20** cube shape
- walls and a clear path
- **1 redstone door**
- **1 lever** the agent must flip
- a clear **start** and **finish**
- agent code that solves it using `if/otherwise` and `interact`

When you finish, come back here. Send a photo or video of the agent solving your maze, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My maze has …
>
> The agent's plan is …
>
> The thing I am most proud of is …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent runs your maze. Talk like you are teaching a friend. Try to use these words: **maze**, **lever**, **door**, **goal**.

> 1. Show the maze, the start, the door, and the lever.
> 2. Run your code and follow the agent to the goal.
> 3. Say what you learned in this course.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk. This is the **last week** of Maze Madness — congratulations!
