# 🕹️ M002 Week 6 — English Worksheet

**Topic:** Lever Interaction — Opening Doors · **Course:** Maze Madness · **Time:** about 45 minutes

This week your agent **flips a lever** to open a closed redstone door, then walks through.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
move forward
interact ahead
move forward
```

**The agent moves up to a lever, flips it, then moves forward. What happens to the door?**

<div class="write-space"></div>

```
interact ahead
move forward
move forward
```

**There is no lever in front of the agent. What happens?**

<div class="write-space"></div>

```
while no lever ahead:
    move forward
interact ahead
turn right
move forward
move forward
```

**Describe in plain English what the agent is doing, step by step.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to **flip the lever first**, then walk through the now-open door.

```
move forward
move forward
interact ahead
```

**Hint:** the lever is at the first wall. Flip it before passing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Before flipping a lever, the agent should be **right in front of it**.

```
while no lever ahead:
    move forward
    interact ahead
```

**Hint:** the agent is interacting on every step, even when there is no lever.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — After flipping the lever, the agent should **turn around** and go back through the door.

```
interact ahead
move forward
```

**Hint:** the door is behind the agent, not in front.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. The maze has a **lever** that opens a **closed door**. Write code that:

1. moves the agent to the lever,
2. flips it (`interact`),
3. moves on through the now-open door,
4. reaches the goal.

When you finish, come back here. Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I walked the agent to …
>
> I used `interact` to …
>
> Once the door opened, the agent …
>
> The hardest part was …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs the maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **lever**, **interact**, **flip**, **door**, **open**.

> 1. Show the closed door and the lever in the maze.
> 2. Run your code and show the agent flipping the lever.
> 3. Read your code out loud and say which line opens the door.
> 4. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
