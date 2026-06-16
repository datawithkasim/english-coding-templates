# 🧩 M002 Extension 2 — Worksheet (Beginner)

**Topic:** Two Pistons + AND Conditions · **Course:** Maze Madness · **Level:** Extension (Beginner) · **Time:** about 35 minutes

This is a **challenge** for students who finished the weekly mazes. The agent follows a **redstone trail**. Sometimes it must check **two things at once** (this is called **AND**). Twice in the maze it flips a **lever** to power a **piston** that opens the way. Your goal: get the agent through the **whole maze**.

---

## 1 · Read the Chat Commands 🎛️

A chat command binds a **word** to an action. When you type that word in chat, the agent does it.

```
when you type "r":
    agent turns right
```

**You type `r`. What does the agent do? Circle one:** turns left · turns right · jumps

<div class="write-space short"></div>

```
when you type "rl":
    agent teleports back to you
```

**You type `rl`. Where does the agent go? Circle one:** to the goal · back to you · nowhere

<div class="write-space short"></div>

---

## 2 · AND means BOTH 🔍

**AND** is true only when **both** things are true. Read each line and answer.

```
if redstone on left AND redstone ahead:
    turn left
```

**There is redstone on the left, but NOT ahead. Does the agent turn left? Circle one:** yes · no

<div class="write-space short"></div>

**There is redstone on the left AND redstone ahead. Does the agent turn left? Circle one:** yes · no

<div class="write-space short"></div>

```
if block ahead:
    flip the lever
    move forward
```

**A block is in the way (a piston gate). What does the agent do first? Circle one:** flip the lever · move back · stop

<div class="write-space short"></div>

---

## 3 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should turn left only when there is redstone on the left **AND** ahead.

```
# clean
if redstone on left AND redstone ahead:
    turn left
```

```
# buggy
if redstone on left OR redstone ahead:
    turn left
```

**What is wrong? With OR, how many of the two does the agent need?**

<div class="write-space short"></div>

**Pair B** — At a piston gate the agent should flip the lever **first**, then cross.

```
# clean
flip the lever
move forward
move forward
```

```
# buggy
move forward
move forward
flip the lever
```

**What is wrong? What does the agent hit if the lever is not flipped yet?**

<div class="write-space short"></div>

---

## 4 · Fill the Gap ✏️

The agent should turn left only when **both** are true. One word is missing. Fill it in from the word bank.

```
if redstone on left ____ redstone ahead:
    turn left
```

**Word bank:** `AND` · `OR` · `NOT`

**Write the missing word:**

<div class="write-space short"></div>

---

## 5 · Finish the Whole Maze 📸

Open the **M002 EXT 2** world. Type `run` and watch the agent. The goal is to reach the **very end** — past both pistons. If it gets stuck, fix it and run again.

When the agent finishes, come back here. Send a photo or video of the agent at the goal, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The maze had two pistons, so the agent had to …
>
> An AND check means the agent needs …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent solves the whole maze. Talk like you are teaching a friend. Try to use these words: **redstone**, **AND**, **piston**, **lever**.

> 1. Show the maze and the redstone trail.
> 2. Type `run` and show the agent following it.
> 3. Show the agent flipping a lever to open a piston.
> 4. Show it reaching the goal.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
