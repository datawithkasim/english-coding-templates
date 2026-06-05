# 🧱 RS004 Week 7 — English Worksheet

**Topic:** Platform Collision · **Course:** Platformer Game · **Time:** about 45 minutes

This week your player can **land on platforms**. You keep platforms in a **list**, check each one with `colliderect()`, and only land when the player is falling *down* onto the top of a platform.

> Keep these words handy: **platform**, **list**, **`colliderect()`**, **land**, **falling (vy > 0)**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

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

## 4 · Refactor & Extend 🛠️

Start from your working collision code.

1. Move the collision check into a function `handle_collisions(player, vy, platforms)` that returns the new `vy` and `on_ground`. Why is a function cleaner here?

<div class="write-space"></div>

2. Add a fifth platform that can only be reached with a jump. Write its `Rect` values.

<div class="write-space"></div>

3. **Stretch:** mark the highest platform with a "finish" colour. Which platform did you choose?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Add platforms to your jumping player. Place several so the player can hop up from one to the next.

When it works, send a **photo or video** of the player climbing the platforms, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I kept my platforms in a list so that …
>
> `colliderect()` checks whether …
>
> I only land when `velocity_y > 0` because …
>
> `player.bottom = plat.top` makes the player …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of the player jumping across platforms. Teach it to someone new. Try to use these words: **platform**, **list**, **colliderect**, **land**, **falling**.

> 1. Show the player landing on a platform.
> 2. Jump up to a higher platform.
> 3. Read your collision check out loud and explain `velocity_y > 0`.
> 4. Walk off a platform and show the player falls again.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
