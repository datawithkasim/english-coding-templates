# 🧩 M002 Extension — Worksheet (Beginner)

**Topic:** Redstone Trail Solver (3D Cube Maze) · **Course:** Maze Madness · **Level:** Extension (Beginner) · **Time:** about 35 minutes

This is a **challenge** for students who finished the weekly mazes. The agent follows a **redstone trail** through a maze that goes **up and down**, not just flat. You start it with a chat word: type `run`.

---

## 1 · Read the Chat Commands 🎛️

A chat command binds a **word** to an action. When you type that word in chat, the agent does it.

```
when you type "l":
    agent turns left
```

**You type `l`. What does the agent do? Circle one:** turns left · turns right · jumps

<div class="write-space short"></div>

```
when you type "rl":
    agent teleports back to you
```

**You type `rl`. Where does the agent go? Circle one:** to the goal · back to you · nowhere

<div class="write-space short"></div>

---

## 2 · Follow the Trail 🔍

The agent reads redstone around it and follows the trail. Read each line and answer.

```
if redstone is below me:
    move up
```

**There is redstone under the agent. What does it do? Circle one:** move up · move down · stop

<div class="write-space short"></div>

```
if redstone is above me:
    move down
```

**This maze is 3D. Which way does the agent go here? Circle one:** up · down

<div class="write-space short"></div>

**The agent follows the redstone like a path. In one short sentence, what is the redstone for?**

<div class="write-space short"></div>

---

## 3 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should **keep going** until the maze is done.

```
# clean
keep doing forever:
    move forward
    if redstone is below me:
        move up
```

```
# buggy
move forward
if redstone is below me:
    move up
```

**What is wrong? How many times does the buggy agent check the trail?**

<div class="write-space short"></div>

---

## 4 · Fill the Gap ✏️

The agent should go **up** when there is redstone below it. One word is missing. Fill it in from the word bank.

```
if redstone is below me:
    move ____
```

**Word bank:** `up` · `down` · `left`

**Write the missing word:**

<div class="write-space short"></div>

---

## 5 · Tell Me What You Built 📸

Open the extension world. Type `run` and watch the agent follow the redstone trail to the goal. When it finishes, come back here.

Send a photo or video of the agent at the goal, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The maze was 3D, so the agent went …
>
> The redstone trail told the agent to …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent solves the maze. Talk like you are teaching a friend. Try to use these words: **redstone**, **trail**, **up**, **down**, **3D**.

> 1. Show the maze and the redstone trail.
> 2. Type `run` and show the agent following it.
> 3. Say one place where the agent went up or down.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
