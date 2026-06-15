# 🧊 M003 Week 6 — English Worksheet

**Topic:** Building Things in 3D — Boxes & Rooms · **Course:** 3D Coordinates · **Time:** about 45 minutes

This week one command builds a whole box. `fill` takes **two corner coordinates** — `(x, y, z)` to `(x, y, z)` — and fills everything between them. Remember: **y is height**. Fill with stone to make a solid box, then fill the inside with **air** to make a room you can walk into.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine it happening, write what you think you will see.

```
fill stone from (0, 0, 0) to (4, 3, 4)
```

**One command, two corners. Is the box solid or hollow? How tall is it — look at the middle number.**

<div class="write-space"></div>

```
fill stone from (0, 0, 0) to (4, 3, 4)
fill air from (1, 1, 1) to (3, 2, 3)
```

**The second line fills the inside with air. What is left after both lines run? Could you stand inside it?**

<div class="write-space"></div>

```
fill stone from (0, 0, 0) to (4, 3, 4)
fill air from (1, 1, 1) to (3, 2, 3)
fill air from (2, 1, 0) to (2, 2, 0)
```

**The third line removes blocks from the front wall, starting at height 1. What did we just make? Can you walk in now?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should build a solid stone box from corner **(0, 0, 0)** up to corner **(4, 3, 4)**. Right now nothing fills.

```
fill stone from (4, 3, 4) to (0, 0, 0)
```

**Hint:** `fill` wants the **small** corner first, then the big corner.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should build a **room** you can stand inside. Right now it is a solid block of stone — there is no inside at all.

```
fill stone from (0, 0, 0) to (6, 4, 6)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The room should have a **doorway** you can walk through. Right now the doorway floats in the middle of the wall, one block above the ground.

```
fill stone from (0, 0, 0) to (6, 4, 6)
fill air from (1, 1, 1) to (5, 3, 5)
fill air from (3, 2, 0) to (3, 3, 0)
```

**Hint:** look at the **y** numbers in the last line. The floor inside the room is at height 0, so your feet stand at height 1.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build a **hollow room** with at least one **doorway**: fill a stone box, fill the inside with air, then cut the doorway. When you finish, come back here.

Send a photo or video of you standing inside your room, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My two corners were ( … , … , … ) and ( … , … , … ) because …
>
> To make it hollow, I …
>
> My doorway starts at height … so that …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your room in the world. Talk through it like you are teaching someone who has never seen `fill`. Try to use these words: **fill**, **corner**, **hollow**, **air**, **doorway**.

> 1. Show your room from outside, then run your code in a fresh spot.
> 2. Point at your two corners and say their coordinates out loud.
> 3. Walk through the doorway and stand inside — say which line made the inside hollow.
> 4. Say in your own words why `fill air` is just as useful as `fill stone`.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
