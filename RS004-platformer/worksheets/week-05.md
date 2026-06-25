# 🪂 RS004 Week 5 — English Worksheet

**Topic:** Gravity & Jump · **Course:** Platformer Game · **Time:** about 45 minutes

This week is about **thinking through** how a player learns to **fall** and **jump**, and **explaining** the code you wrote in the live lesson. A `velocity_y` value grows every frame (gravity pulls down), and a jump gives it a sudden *negative* push (upward). The player can only jump when it is on the ground.

> Keep these words handy: **velocity**, **gravity**, **jump strength**, **on ground**, **accelerate**.

---

## 1 · Predict 🔮

Read each snippet and write what you think it does. Do not run anything — just think.

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

Each snippet is broken. On paper, write the fixed code, then explain why the original was wrong.

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

## 4 · Explain the Code 📖

Here is a working gravity-and-jump player, like the one from your lesson. Read it carefully, then answer the questions.

```python
GRAVITY = 0.7
JUMP_STRENGTH = -14
velocity_y = 0
on_ground = True

# inside the event loop
if event.key == pygame.K_SPACE and on_ground:
    velocity_y = JUMP_STRENGTH
    on_ground = False

# every frame
velocity_y = velocity_y + GRAVITY
player.y = player.y + velocity_y

if player.y >= HEIGHT - 50:
    player.y = HEIGHT - 50
    velocity_y = 0
    on_ground = True
```

**What does the line `velocity_y = velocity_y + GRAVITY` do every frame?**

<div class="write-space"></div>

**Why does a jump set `velocity_y` to a *negative* number instead of a positive one?**

<div class="write-space"></div>

**Right after a jump, `on_ground` becomes `False`. Why is that important?**

<div class="write-space"></div>

**What three things happen when `player.y >= HEIGHT - 50` is true?**

<div class="write-space"></div>

**If you deleted the line `velocity_y = 0` at the bottom, what would go wrong?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

In the live lesson you wrote your own gravity and jump code. Now explain *your* code in a short phone video. You may show it running. Try to use these words: **gravity**, **velocity**, **jump strength**, **on ground**, **land**.

> 1. Show your player falling and landing.
> 2. Read your gravity line out loud and explain what it does.
> 3. Show a jump from the ground and explain how the jump works.
> 4. Try to jump in mid-air, show it doesn't work, and say why.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
