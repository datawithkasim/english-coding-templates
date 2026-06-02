# 🔂 M002 Week 4 — English Worksheet

**Topic:** AND and OR Conditions — Smarter Decisions · **Course:** Maze Madness · **Time:** about 45 minutes

Last week your agent used `AND` (both true). This week you add `OR` (**either** one true) and use them **together** in the same maze.

- `AND` → the action happens **only when both** conditions are true.
- `OR` → the action happens **when at least one** condition is true.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
if wall ahead AND wall on right:
    turn left
```

**Both must be true. The agent has a wall ahead but an open path on the right — does it turn left?**

<div class="write-space"></div>

```
if no wall ahead OR no wall below:
    move forward
```

**Only one needs to be true. The path ahead is blocked but the path below is open — does the agent move?**

<div class="write-space"></div>

```
keep doing forever:
    if wall ahead AND wall on right:
        turn left
    otherwise if no wall ahead OR no wall on left:
        move forward
    otherwise:
        turn right
```

**The agent reaches a corner with walls on the front AND right. What does it do? At an open junction, which branch runs?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent should turn left **only when** there is a wall ahead AND a wall on the right (a dead-end corner). Right now it turns at *any* wall.

```
if wall ahead OR wall on right:
    turn left
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent should move forward when **either** the path ahead is clear OR the path below is clear.

```
if no wall ahead AND no wall below:
    move forward
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — At a fork the agent should **turn right if it can** (path on the right), otherwise turn left. Right now the order is wrong, so it always turns left first.

```
if no wall on left:
    turn left
otherwise if no wall on right:
    turn right
```

**Hint:** check the right side first.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Solve the maze using **both** an `AND` condition and an `OR` condition. When you finish, come back here.

Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I used **AND** when …
>
> I used **OR** when …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs the maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **AND**, **OR**, **condition**, **both**, **either**.

> 1. Show the start of the maze, then run your code.
> 2. Read each `if … AND …` and `if … OR …` block out loud and say what makes it run.
> 3. Show one bug you hit and how you fixed it.
> 4. Say in your own words how **AND** is different from **OR**.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
