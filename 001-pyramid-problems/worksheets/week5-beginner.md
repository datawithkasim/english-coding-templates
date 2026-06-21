# 🔺 M001 Week 5 — English Worksheet (Beginner)

**Topic:** First Pyramid · **Course:** Pyramid Problems · **Level:** Beginner · **Time:** about 30 minutes

The agent walks around a **square** and drops blocks as it walks. Stack squares that get **smaller** and you get a pyramid.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
set f to 4
place on move ON
repeat 4 times:
    move forward by f
    turn left
```

**What shape does the agent draw? Circle one:** line · square · circle

**How many sides does it draw? Circle one:** 1 · 3 · 4

<div class="write-space short"></div>

```
set f to 5
repeat 3 times:
    [draw one square]
    move up by 1
    change f by -2
```

**The sides go 5, then …, then … Circle one:** 5 · 3 · 1 → 5 · 4 · 3

**Which square is biggest — bottom or top?**

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent must draw a closed **square**.

```
# clean
place on move ON
repeat 4 times:
    move forward by f
    turn left
```

```
# buggy
place on move ON
repeat 4 times:
    move forward by f
```

**What is wrong? What shape does the buggy code draw instead?**

<div class="write-space short"></div>

**Pair B** — Each new layer should be **2 smaller** than the one below.

```
# clean
[draw one square]
move up by 1
change f by -2
```

```
# buggy
[draw one square]
move up by 1
change f by 2
```

**What is wrong? Does the buggy tower get smaller or bigger as it goes up?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

Each square must sit one block **higher** than the last. One line is missing. Fill it in using the word bank.

```
set f to 5
repeat 3 times:
    [draw one square]
    ____________
    change f by -2
```

**Word bank:** `move up by 1` · `move down by 1` · `turn left`

**Write the missing line:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Run your `pyra` command to build a pyramid. If the agent gets stuck or faces the wrong way, use your helper commands — `1` turns it left, `r` turns it right, `r1` brings it back to you.

Send a photo or video of your pyramid, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The bottom square has sides … blocks long.
>
> Each new layer gets smaller by …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and walk the camera around your pyramid. Talk like you are teaching a friend. Try to use these words: **square**, **side**, **layer**, **shrink**.

> 1. Walk around the pyramid and show all 4 sides.
> 2. Say the side length of each layer from bottom to top.
> 3. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
