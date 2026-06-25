# 🧱 RS004 Week 7 — English Worksheet

**Topic:** Platform Collision · **Course:** Platformer Game · **Time:** about 45 minutes

This week you think about how a player can **land on platforms**. You read code that keeps platforms in a **list**, checks each one with `colliderect()`, and only lands when the player is falling *down* onto the top of a platform. Then you explain the collision code from today's lesson in your own words.

> Keep these words handy: **platform**, **list**, **`colliderect()`**, **land**, **falling (vy > 0)**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think will happen.

```python
platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(200, 450, 120, 20),
]
for plat in platforms:
    pygame.draw.rect(screen, BROWN, plat)
```

**How many platforms get drawn? What does the `for` loop do here?**

<div class="write-space"></div>

```python
if player.colliderect(plat) and velocity_y > 0:
    player.bottom = plat.top
    velocity_y = 0
    on_ground = True
```

**Why check `velocity_y > 0`? What does `player.bottom = plat.top` do?**

<div class="write-space"></div>

```python
on_ground = False
for plat in platforms:
    if player.colliderect(plat) and velocity_y > 0:
        ...
```

**Why is `on_ground` set to `False` *before* the loop, every frame?**

<div class="write-space"></div>

---

## 2 · Why `velocity_y > 0`? 🤔

The player can touch a platform while moving up *or* down. We only want to land when moving **down**.

**What would go wrong if we removed the `velocity_y > 0` check and the player jumped up through a platform?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Read it, write the fixed code on paper, then explain why the original was wrong.

**Bug A** — The player should land on every platform. Right now it only ever lands on the first one.

```python
plat = platforms[0]
if player.colliderect(plat) and velocity_y > 0:
    player.bottom = plat.top
    velocity_y = 0
    on_ground = True
```

**Hint:** we check only one platform. How do we check *all* of them?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The player should stand on top of a platform. Right now it sinks halfway into it.

```python
for plat in platforms:
    if player.colliderect(plat) and velocity_y > 0:
        velocity_y = 0
        on_ground = True
```

**Hint:** nothing snaps the player's bottom to the platform top.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `on_ground` should be `True` only when actually standing on something. Right now it gets stuck `True` even after the player walks off a platform into the air.

```python
on_ground = True
for plat in platforms:
    if player.colliderect(plat) and velocity_y > 0:
        player.bottom = plat.top
        velocity_y = 0
```

**Hint:** start each frame assuming the player is *not* on the ground.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working collision code carefully, then answer the questions about it.

```python
platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(200, 450, 120, 20),
]

on_ground = False
for plat in platforms:
    if player.colliderect(plat) and velocity_y > 0:
        player.bottom = plat.top
        velocity_y = 0
        on_ground = True
```

**Why are the platforms kept in a list instead of separate variables?**

<div class="write-space"></div>

**What does `for plat in platforms:` do on each pass through the loop?**

<div class="write-space"></div>

**What does `player.colliderect(plat)` return, and how is it used in the `if`?**

<div class="write-space"></div>

**What does the line `player.bottom = plat.top` do to the player's position?**

<div class="write-space"></div>

**Why is `on_ground = False` written before the loop instead of inside it?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Today in your live lesson you wrote collision code for your player. Record a short phone video explaining the code **you** wrote. You may show it running. Try to use these words: **platform**, **list**, **colliderect**, **land**, **falling**.

> 1. Point to where you keep your platforms in a list.
> 2. Read your collision check out loud and explain `velocity_y > 0`.
> 3. Show the player landing on a platform, then walking off and falling.
> 4. Explain one part of the code that was tricky for you.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
