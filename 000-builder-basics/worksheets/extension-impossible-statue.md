# 🗿 Builder Basics — The Impossible Statue (Extension)

**Topic:** Place + Move, On and Off · **Course:** Builder Basics · **Type:** Extension Activity · **Time:** about 45 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable placing blocks and moving the agent.

---

## 1 · Read the World 🔍

Open the **Impossible Statue** world. Someone left you a puzzle. Before you write any code, read the markers:

- 🟥 **Red blocks** — your **start** point and your **end** point. The agent begins on one and must finish on the other.
- ⬛ **Crying obsidian** — this is the shape you must **build**. Every crying obsidian spot is a block you need to place.
- ⬜ **Glass** — a **trap**. You must move through these spots but place **nothing** here. Leave them empty.

**In your own words, what is the puzzle asking you to do?**

<div class="write-space"></div>

**Walk the path with your eyes from the red start block to the red end block. How many blocks should you place, and how many spots should you skip?**

<div class="write-space"></div>

---

## 2 · The Big Idea: Place On / Place Off 💡

The agent moves in a straight line, but it should **not** place a block on every step. On the obsidian spots, placing is **on**. On the glass spots, placing is **off**.

So your code is a mix: `move forward`, and sometimes `place block down`, and sometimes just `move forward` with no place.

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

Before you build in the world, write the plan on paper first. Imagine the row of spots from start to end. Mark each spot with **B** (build — place a block) or **S** (skip — move past, no block).

> Example: B B S B S S B

**Write your row of B and S, in order from the red start to the red end:**

<div class="write-space"></div>

Now turn that plan into agent commands. Remember: a **B** spot needs a place **and** a move; an **S** spot needs only a move.

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

Each code block was meant to copy the statue, but it is broken. Read the goal, then rewrite it so it works. Then explain the fix.

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

## 5 · Build the Statue 📸

Now go to the Impossible Statue world and run your code. Match the crying obsidian exactly: place where it says build, leave the glass spots empty, and finish on the red end block.

When it looks right, send a photo or video. Then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I read the markers and saw …
>
> My plan was … (B and S)
>
> I used the command … to place, and I left the skip spots empty by …
>
> The hardest part was …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and teach someone how you solved the puzzle. Try to use these words: **place**, **skip**, **move forward**, **start**, **end**, **pattern**.

> 1. Point to the red start and red end blocks.
> 2. Show the crying obsidian shape you copied.
> 3. Show one glass spot you skipped and explain why you placed nothing there.
> 4. Read your commands out loud and say which ones are "place on" and which are "skip".

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
