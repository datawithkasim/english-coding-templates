# ✏️ RS004 Week 10 — English Worksheet

**Topic:** Paper to Code (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week you design a level **on paper first**, then turn it into coordinates and into code. You will measure how far and how high your player can jump, so every platform is actually reachable.

> Keep these words handy: **sketch**, **coordinate (x, y)**, **jump height**, **jump distance**, **reachable**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

## 2 · Measure Your Jump 📏

Before you design, find out your player's real limits. Run your week 9 game and test.

```
1. Stand on the ground and jump straight up.
   Highest platform you can land on is about ___ pixels above.

2. Run and jump across a flat gap.
   Widest gap you can clear is about ___ pixels.
```

<div class="write-space"></div>

**Why must you know these numbers *before* you place platforms?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is a *level design* mistake. Read what's wrong, then rewrite the coordinates so the level works. Explain your fix.

**Bug A** — The second platform is meant to be reachable, but it is 300 pixels above the first — too high to jump.

```python
MY_LEVEL = [
    (0, 580, 250, 20),
    (300, 280, 100, 20),
]
```

**Hint:** max jump height is about 140 pixels. Lower the gap.

**Write the fixed coordinates:**

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

**Write the fixed level:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · From Sketch to Coordinates 🛠️

Do this in order.

1. On paper, sketch a level: a start, 5–8 platforms, and a finish at the top. Take a photo when done.

<div class="write-space"></div>

2. For each platform in your sketch, write its `(x, y, width, height)`. Read coordinates off your drawing.

<div class="write-space tall" style="min-height: 200px"></div>

3. **Stretch:** add a secret platform reachable only by a hard jump. Where is it?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Turn your paper sketch into a playable level. Tune it so it is challenging but fair — aim for about 1 success in 5 tries.

Send **your paper sketch photo and a full play-through video**, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I sketched my level with …
>
> I measured my jump and found I can reach about ___ pixels high and ___ wide.
>
> To turn the sketch into code, I …
>
> The hardest jump in my level is …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of a full clear of your hand-designed level. Teach it to someone new. Try to use these words: **sketch**, **coordinate**, **jump height**, **reachable**, **difficulty**.

> 1. Show your paper sketch next to the running game.
> 2. Point at one platform and read its coordinates.
> 3. Show the hardest jump and whether you cleared it.
> 4. Reach the finish.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your paper sketch + your walkthrough video to teacher on KakaoTalk.
