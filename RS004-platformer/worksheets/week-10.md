# ✏️ RS004 Week 10 — English Worksheet

**Topic:** Paper to Code (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week you think about how a level is designed: how coordinates place each platform, and how jump height and jump distance decide what is reachable. You will read level code, find a design mistake on paper, and explain the code you wrote in your live lesson.

> Keep these words handy: **sketch**, **coordinate (x, y)**, **jump height**, **jump distance**, **reachable**.

---

## 1 · Predict 🔮

Read each snippet and write what you think it means.

```python
# JUMP_STRENGTH = -14, GRAVITY = 0.7
# max jump height ≈ 14² / (2 × 0.7) = 140 pixels
```

**If your player is on a platform, roughly how high can the next platform be and still be reachable?**

<div class="write-space"></div>

```python
MY_LEVEL = [
    (0, 580, 250, 20),
    (350, 520, 100, 20),
]
```

**The first platform ends at x = 250. The next starts at x = 350. How wide is the gap to jump?**

<div class="write-space"></div>

```python
START_X, START_Y = 50, 540
FINISH_X, FINISH_Y = 450, 220
```

**Where does the player begin, and where is the goal? Lower `y` is higher on screen.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is a *level design* mistake. Read what's wrong, then rewrite the coordinates so the level works. Explain your fix.

**Bug A** — The second platform is meant to be reachable, but it is 300 pixels above the first — too high to jump.

```python
MY_LEVEL = [
    (0, 580, 250, 20),
    (300, 280, 100, 20),
]
```

**Hint:** max jump height is about 140 pixels. Lower the gap.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The finish marker is floating in empty space with no platform under or near it, so the player can never reach it.

```python
MY_LEVEL = [
    (0, 580, 250, 20),
    (350, 520, 100, 20),
]
FINISH = (700, 100, 50, 40)
```

**Hint:** add a platform near the finish, within jump range of the last one.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

This is a working level. Each platform is `(x, y, width, height)`. The player starts low and climbs to the finish at the top.

```python
START_X, START_Y = 50, 540

MY_LEVEL = [
    (0, 580, 250, 20),
    (350, 520, 100, 20),
    (520, 430, 100, 20),
    (350, 330, 100, 20),
]

FINISH = (380, 280, 50, 40)
```

**What do the first two numbers in each platform tuple mean?**

<div class="write-space"></div>

**The gap from the first platform (ends at x = 250) to the second (starts at x = 350) is 100 pixels. Is that within jump distance? How do you know?**

<div class="write-space"></div>

**The player must climb from y = 580 up to the finish at y = 280. Why is a higher platform written with a *smaller* y number?**

<div class="write-space"></div>

**Look at the last platform `(350, 330, 100, 20)` and the finish `(380, 280, 50, 40)`. Why is the finish placed there and not somewhere far away?**

<div class="write-space"></div>

**If you wanted to make this level harder, which one number would you change, and why?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the level **you wrote in today's live lesson** in a short phone video. You may show it running. Try to use these words: **sketch**, **coordinate**, **jump height**, **reachable**, **difficulty**.

> 1. Show your code and point at your `MY_LEVEL` platforms.
> 2. Read the coordinates of one platform out loud and say where it sits.
> 3. Show the hardest jump and explain why it is still reachable.
> 4. Say one thing you would change to adjust the difficulty.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
