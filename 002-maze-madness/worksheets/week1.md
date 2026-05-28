# 🔁 M002 Week 1 — English Worksheet

**Topic:** While Loops — Move Until You Hit a Wall · **Course:** Maze Madness · **Time:** about 45 minutes

This week your agent uses a **while loop** to keep moving forward until it hits a wall.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
while no wall ahead:
    move forward
```

**When does the agent stop? Why?**

<div class="write-space"></div>

```
move forward
move forward
move forward
```

**How is this different from the while loop above? What if the wall is only 2 steps away?**

<div class="write-space"></div>

```
while no wall ahead:
    move forward
turn right
while no wall ahead:
    move forward
```

**The agent finishes the first while loop. What happens next?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to keep moving forward **until** it hits a wall.

```
while wall ahead:
    move forward
```

**Hint:** the condition is backwards.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent is supposed to move forward step by step. Right now it only checks the wall **once**, before moving 10 steps no matter what.

```
if no wall ahead:
    move forward
    move forward
    move forward
    move forward
    move forward
    move forward
    move forward
    move forward
    move forward
    move forward
```

**Write the fixed code using a while loop:**

<div class="write-space"></div>

**Why was it wrong? Why does your while loop work better?**

<div class="write-space"></div>

**Bug C** — The agent is supposed to stop **right in front** of the wall, not crash into it.

```
while no wall ahead:
    move forward
    move forward
```

**Hint:** the agent moves twice before checking again.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Use a **while loop** to move the agent from the start of the straight maze all the way to the wall. When you finish, come back here.

Send a photo or video of the agent reaching the wall, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I read the maze and noticed …
>
> My while loop checked …
>
> The agent stopped because …
>
> The hardest part was …
>
> To fix it, I …
>
> A while loop is useful because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs the maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **while**, **loop**, **detect**, **wall**, **forward**.

> 1. Show the start of the maze, then run your code.
> 2. Read your while loop out loud and say what makes it stop.
> 3. Show one bug you hit and how you fixed it.
> 4. Say why a while loop is better than writing `move forward` many times.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
