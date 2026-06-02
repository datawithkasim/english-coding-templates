# 🧱 M002 Week 7 — English Worksheet

**Topic:** Pistons and Mazes · **Course:** Maze Madness · **Time:** about 45 minutes

This week the maze uses **pistons**. A piston pushes or pulls a block when it gets a redstone signal. A **sticky piston** can pull a block back, opening a path. Your agent flips a lever to power a piston, then crosses the gap it opens.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
move forward
interact ahead
move forward
```

**The agent walks up to a lever, flips it, and a sticky piston pulls a block back. What happens to the path? Can the agent move forward now?**

<div class="write-space"></div>

```
if gap ahead:
    interact ahead
otherwise:
    move forward
```

**There is a gap in the floor with a piston bridge. What does the agent do at the gap? What does it do on solid ground?**

<div class="write-space"></div>

```
keep doing forever:
    if gap ahead:
        interact ahead
        move forward
    otherwise:
        move forward
```

**Describe in plain English what the agent is doing, step by step.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to **power the piston first**, then cross the gap it opens.

```
move forward
move forward
interact ahead
```

**Hint:** flip the lever *before* you reach the gap, not after.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent should only `interact` when there is a **gap** ahead. Right now it tries to flip a lever on every step.

```
keep doing forever:
    interact ahead
    move forward
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — A sticky piston holds the bridge **only while the lever is ON**. The agent must cross **before** turning the lever back off.

```
interact ahead
move forward
interact ahead
move forward
```

**Hint:** the second `interact` switches the lever OFF and the bridge disappears. Cross first.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. The maze has a **gap** (or a blocked path) and a **piston** that opens it when powered. Write code that:

1. moves the agent to the lever,
2. flips it (`interact`) so the piston opens the path,
3. crosses while the path is open,
4. reaches the goal.

When you finish, come back here. Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I walked the agent to …
>
> I powered the piston by …
>
> Once the path opened, the agent …
>
> The hardest part was …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs the maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **piston**, **redstone**, **signal**, **gap**, **bridge**.

> 1. Show the gap (or blocked path) and the piston in the maze.
> 2. Run your code and show the agent powering the piston and crossing.
> 3. Read your code out loud and say which line opens the path.
> 4. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
