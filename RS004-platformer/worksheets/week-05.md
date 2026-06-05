# 🪂 RS004 Week 5 — English Worksheet

**Topic:** Gravity & Jump · **Course:** Platformer Game · **Time:** about 45 minutes

This week your player learns to **fall** and **jump**. A `velocity_y` value grows every frame (gravity pulls down), and a jump gives it a sudden *negative* push (upward). The player can only jump when it is on the ground.

> Keep these words handy: **velocity**, **gravity**, **jump strength**, **on ground**, **accelerate**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

```python
velocity_y = velocity_y + GRAVITY
player.y = player.y + velocity_y
```

**Each frame `velocity_y` grows. Does the player fall faster or slower as time goes on?**

<div class="write-space"></div>

```python
if event.key == pygame.K_SPACE and on_ground:
    velocity_y = JUMP_STRENGTH   # JUMP_STRENGTH = -14
```

**`velocity_y` becomes -14. In Pygame, smaller `y` is higher on screen. So the player goes …?**

<div class="write-space"></div>

```python
if player.y >= HEIGHT - 50:
    player.y = HEIGHT - 50
    velocity_y = 0
    on_ground = True
```

**The player hits the floor. Why set `velocity_y = 0`? Why set `on_ground = True`?**

<div class="write-space"></div>

---

## 2 · Trace the Fall 📉

`GRAVITY = 0.7`. The player starts at rest (`velocity_y = 0`). Fill in `velocity_y` after each frame.

```
start:    velocity_y = 0
frame 1:  velocity_y = ___
frame 2:  velocity_y = ___
frame 3:  velocity_y = ___
```

<div class="write-space"></div>

**In your own words, why does the player speed up as it falls?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — The player should fall, but it just sits in the air doing nothing.

```python
velocity_y = 0
player.y = player.y + velocity_y
```

**Hint:** gravity is never added, so `velocity_y` stays 0 forever.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The player should only jump when on the ground. Right now it can jump forever in mid-air ("flying").

```python
if event.key == pygame.K_SPACE:
    velocity_y = JUMP_STRENGTH
```

**Hint:** add a condition so the jump only happens when `on_ground` is true.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When the player lands, it should be able to jump again. Right now it lands but can never jump a second time.

```python
if player.y >= HEIGHT - 50:
    player.y = HEIGHT - 50
    velocity_y = 0
```

**Hint:** something needs to flip back to `True` on landing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Tune the Jump 🛠️

Start from your working jump. Change values one at a time and write down the feel.

1. Try `GRAVITY = 0.3`, then `GRAVITY = 1.2`. What changes about the fall?

<div class="write-space"></div>

2. Try `JUMP_STRENGTH = -8`, then `-20`. What changes about the jump height?

<div class="write-space"></div>

3. **Stretch:** add a `MAX_FALL` cap so the player never falls faster than a set speed. Why might that help?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Add gravity and a spacebar jump to last week's player. It must fall, land, and jump again from the ground.

When it works, send a **photo or video** of a jump, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, gravity works by adding `GRAVITY` to …
>
> A jump is just `velocity_y` becoming a negative number, which means …
>
> The player can only jump when …
>
> The `GRAVITY` and `JUMP_STRENGTH` values I liked best were …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video showing a jump and a landing. Teach it to someone new. Try to use these words: **gravity**, **velocity**, **jump strength**, **on ground**, **land**.

> 1. Show the player falling and landing.
> 2. Show a jump from the ground.
> 3. Read the gravity line out loud and explain it.
> 4. Try to jump in mid-air and show that it doesn't work — say why.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
