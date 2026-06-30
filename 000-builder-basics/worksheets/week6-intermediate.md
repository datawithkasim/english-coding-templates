# 🪣 M000 Week 6 — English Worksheet (Intermediate)

**Topic:** Building a Well · **Course:** Builder Basics · **Level:** Intermediate · **Time:** about 38 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
repeat 3 times:
    destroy block down
    move down by 1
```

**What does the agent do, and how deep is the hole?**

<div class="write-space"></div>

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

**What shape does the agent leave on the ground? How many blocks total?**

<div class="write-space"></div>

---

## 2 · Find the Bug 🐛

Each block below was meant to do one thing, but it is broken. The goal is written for you first. Read it, circle the line that causes the problem, then write one sentence about what is wrong.

**Bug A** — Goal: dig **3 blocks straight down** to make the well hole. After each `destroy`, the agent must step down into the hole.

```
repeat 3 times:
    destroy block down
```

**Which line is missing, and why does that break the dig?**

<div class="write-space short"></div>

**Bug B** — Goal: build the square wall **first**, then dig the hole. Think about where the agent ends up after it digs.

```
repeat 3 times:
    destroy block down
    move down by 1
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

**What is in the wrong order, and what problem does that cause?**

<div class="write-space short"></div>

---

## 3 · Fix the Code ✏️

The agent is supposed to build the **4 sides** of a 3×3 square wall around the well. Right now it only builds **one side** because the outer loop is missing.

```
repeat 3 times:
    place block down
    move forward
    turn right
```

> Hint: a square has 4 sides. You need to repeat "3 blocks, then turn" four times.

**Write the fixed code:**

<div class="write-space"></div>

**Why does your fix make a full square?**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Build a **well** — a 3×3 square wall on top, and a hole **3 or 4 blocks deep** inside it. When you finish, come back here.

Send a photo or video of your well, then explain what you did. Use these sentence starters — write 3 or 4 sentences.

> First, I built the square wall by …
>
> Then I dug down by …
>
> The well is … blocks wide and … blocks deep.
>
> The hardest part was …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you walk the camera around your well. Talk through it like you are teaching someone who has never seen it. Try to use these words: **square**, **wall**, **dig**, **destroy**, **deep**.

> 1. Show the well from outside, then look down inside it.
> 2. Read the wall loop and the dig loop out loud and say what each one does.
> 3. Say how wide the wall is and how deep the well goes.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
