# 🧩 M002 Extension 4 — Worksheet (Beginner)

**Topic:** Add Two AND Conditions · **Course:** Maze Madness · **Level:** Extension (Beginner) · **Time:** about 35 minutes

This is a **challenge** for students who finished the weekly mazes. The agent already knows **four rules** for following redstone through a 3D maze. But it is **not finished** — at two spots it gets stuck because one redstone signal is not enough. You will look at each stuck spot, see **which two signals** are on, and add your own **AND** rule (two things true at once). Then get the agent to the goal.

---

## 1 · The Four Rules the Agent Knows 🎛️

Each rule checks **one** redstone signal and does **one** thing.

```
if redstone on the LEFT:
    turn RIGHT
if redstone on the RIGHT:
    turn LEFT
if redstone BELOW:
    move UP
if redstone ABOVE:
    move DOWN
```

**Draw a line to match each signal to its action. You will reuse these actions in your own rules.**

| Signal | | Action |
|---|---|---|
| redstone on the left | → | move up |
| redstone below | → | turn right |
| redstone above | → | turn left |
| redstone on the right | → | move down |

<div class="write-space short"></div>

---

## 2 · AND means BOTH 🧠

**AND** is true only when **both** things are true.

```
if redstone on the LEFT AND redstone BELOW:
    turn right
    move up
```

**(This is just an example.) There is redstone on the left, but NOT below. Is the AND true? Circle one:** yes · no

<div class="write-space short"></div>

**There is redstone on the left AND redstone below. Is the AND true? Circle one:** yes · no

<div class="write-space short"></div>

**When the AND is true, the agent does the action for _each_ signal — so it does TWO things. How many actions does an AND rule with two signals need?**

<div class="write-space short"></div>

---

## 3 · Look at the Stuck Spots 🔍

Open the **M002 Complete the Maze** world. Type `run`. The agent stops at **two** spots because two signals are on at once. Walk to each spot and look around the agent.

**Which signals are on at each stuck spot? Tick all you see.**

| | left | right | below | above |
|---|---|---|---|---|
| **Stuck spot 1** | | | | |
| **Stuck spot 2** | | | | |

<div class="write-space short"></div>

---

## 4 · Write Your Two AND Rules ✏️

Use the two signals you ticked for each spot, and the actions from the table in section 1.

**Stuck spot 1** — fill in the two signals and the two actions:

```
if redstone on the ______ AND redstone ______:
    ______________
    ______________
```

<div class="write-space short"></div>

**Stuck spot 2** — write the whole rule yourself:

<div class="write-space"></div>

---

## 5 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version. Circle what is different and write one short sentence about the bug.

**Pair A** — A rule should fire only when **both** signals are on.

```
# clean
if redstone on the LEFT AND redstone BELOW:
    turn right
    move up
```

```
# buggy
if redstone on the LEFT OR redstone BELOW:
    turn right
    move up
```

**What is wrong? With OR, how many of the two does the agent need?**

<div class="write-space short"></div>

**Pair B** — A rule with two signals needs **two** actions.

```
# clean
turn right
move up
```

```
# buggy
turn right
```

**What is wrong? What does the agent forget to do?**

<div class="write-space short"></div>

---

## 6 · Finish the Whole Maze 📸

Type `run` and watch the agent. The goal is to reach the **very end**. If it gets stuck, fix your AND rules and run again.

When the agent finishes, come back here. Send a photo or video of the agent at the goal, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The agent already knew four rules, like …
>
> At the first stuck spot the two signals were … and …
>
> An AND rule means the agent needs …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 7 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent solves the maze. Talk like you are teaching a friend. Try to use these words: **redstone**, **AND**, **both**, **turn**, **move up**.

> 1. Show the maze and the redstone.
> 2. Type `run` and show the agent following it.
> 3. Say out loud the two signals your AND rule needs.
> 4. Show the agent reaching the goal.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
