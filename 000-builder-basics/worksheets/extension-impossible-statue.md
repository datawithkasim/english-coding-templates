# 🗿 Builder Basics — The Impossible Statue (Extension)

**Topic:** Place + Move, On and Off · **Course:** Builder Basics · **Type:** Extension Activity · **Time:** about 45 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable placing blocks and moving the agent.

---

## 1 · Read the World 🔍

Open the **Impossible Statue** world. It is a puzzle. Read the markers:

- 🟥 **Red blocks** — your **start** and **end** points.
- ⬛ **Crying obsidian** — **build** here. Every dark spot is a block to place.
- ⬜ **Glass** — a **trap**. Move through these spots but place **nothing**.

**In your own words, what is the puzzle asking you to do?**

<div class="write-space"></div>

**Walk the path with your eyes from the red start block to the red end block. How many blocks should you place, and how many spots should you skip?**

<div class="write-space"></div>

---

## 2 · The Big Idea: Place On / Place Off 💡

The agent moves in a straight line, but should **not** place a block on every step. Placing is **on** at obsidian spots and **off** at glass spots.

So your code mixes `move forward` with `place block down`, and sometimes `move forward` alone.

```
place block down
move forward
place block down
move forward
move forward
place block down
```

**Look at the code above. On which steps is placing ON? On which step is it OFF (a skipped spot)?**

<div class="write-space"></div>

**Why can't you just place a block on every single step?**

<div class="write-space"></div>

---

## 3 · Plan Your Path ✏️

Plan on paper first. Mark each spot in the row **B** (build — place a block) or **S** (skip — move past, no block).

> Example: B B S B S S B

**Write your row of B and S, in order from the red start to the red end:**

<div class="write-space"></div>

Turn your plan into agent commands. A **B** spot needs a place **and** a move; an **S** spot needs only a move.

**Write your commands:**

```
1.
2.
3.
4.
5.
6.
7.
8.
```

---

## 4 · Spot the Bug 🐛

Each code block should copy the statue, but is broken. Rewrite it, then explain the fix.

**Bug A** — The pattern should be: build, skip, build. (B S B)

```
place block down
place block down
move forward
move forward
place block down
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent placed a block on a glass (skip) spot. The pattern should be: build, skip, skip, build. (B S S B)

```
place block down
move forward
place block down
move forward
place block down
move forward
place block down
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 5 · Show Your Work 📸🎥

Now go to the Impossible Statue world and run your code. Match the crying obsidian exactly: place where it says build, leave the glass spots empty, and finish on the red end block.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Fill the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
