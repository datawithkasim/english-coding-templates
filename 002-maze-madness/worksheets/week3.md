# 🔀 M002 Week 3 — English Worksheet

**Topic:** AND Conditions — Two Things at Once · **Course:** Maze Madness · **Time:** about 45 minutes

This week your agent checks **two things at the same time** using `AND`. With `AND`, the action only happens when **both** conditions are true.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
if wall ahead AND wall on right:
    turn left
```

**Both conditions must be true. When does the agent turn left? When does it do nothing?**

<div class="write-space"></div>

```
if no wall ahead AND no wall below:
    move forward
```

**Both must be true to move. The path ahead is clear but there is a wall below — does the agent move?**

<div class="write-space"></div>

```
keep doing forever:
    if wall ahead AND wall on right:
        turn left
    otherwise:
        move forward
```

**The agent reaches a corner with walls on the front AND right. What does it do? What happens at an open path?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to turn left **only when** there is a wall ahead AND a wall on the right (a dead-end corner).

```
if wall ahead:
    turn left
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent should move forward only when the path ahead is clear AND the path on the left is also clear (a wide-open spot).

```
if no wall ahead:
    move forward
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — At a dead-end corner (wall ahead AND wall on right), the agent should turn left. Right now it turns left whenever there is **any** wall, so it spins in place too early.

```
if wall ahead AND wall ahead:
    turn left
```

**Hint:** the two checks should be **different** — front *and* right.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Solve the maze using at least one `AND` condition. When you finish, come back here.

Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I used **AND** when …
>
> Both conditions were true when …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs the maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **AND**, **condition**, **both**, **true**, **turn**.

> 1. Show the start of the maze, then run your code.
> 2. Read each `if … AND …` block out loud and say what makes it run.
> 3. Show one spot where the agent did **nothing** because only one condition was true.
> 4. Say in your own words what **AND** means.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
