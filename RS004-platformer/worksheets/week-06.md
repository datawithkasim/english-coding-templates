# 🦊 RS004 Week 6 — English Worksheet

**Topic:** Coyote Time + Double Jump (Explain) · **Course:** Platformer Game · **Time:** about 45 minutes

This week your jump feels like a *real* game. **Coyote time** lets the player jump for a few frames *after* leaving the edge. A **double jump** gives one extra jump in the air. In this worksheet you will think about how the code tracks how many jumps were used and resets them on landing, then explain the code you wrote in the live lesson.

> Keep these words handy: **coyote time**, **double jump**, **jumps used**, **was on ground**, **reset**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think happens.

```python
if was_on_ground and not on_ground:
    coyote_time = COYOTE_FRAMES
```

**`was_on_ground` is last frame, `on_ground` is now. When exactly does this line run?**

<div class="write-space"></div>

```python
if (on_ground or coyote_time > 0) and jumps_used == 0:
    velocity_y = JUMP_STRENGTH
    jumps_used = 1
```

**The player just ran off a ledge but `coyote_time` is 4. Can it still jump? Why?**

<div class="write-space"></div>

```python
elif jumps_used == 1:
    velocity_y = DOUBLE_JUMP_STRENGTH
    jumps_used = 2
```

**The player already jumped once and is in the air. What does pressing jump do now?**

<div class="write-space"></div>

---

## 2 · Trace the Jumps 🔢

Walk through `jumps_used` as the player plays. Start standing on the ground.

```
on ground:        jumps_used = ___
press jump:        jumps_used = ___
press jump again:  jumps_used = ___
press jump again:  jumps_used = ___  (does it jump? ___)
lands on ground:   jumps_used = ___
```

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — After landing, the player should get its jumps back. Right now it lands but can never jump again.

```python
on_ground = False
if player.y >= HEIGHT - 50:
    player.y = HEIGHT - 50
    velocity_y = 0
    on_ground = True
```

**Hint:** `jumps_used` needs to reset to 0 on landing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Coyote time should count *down* each frame and run out. Right now it stays the same forever, so the player can jump from the air any time.

```python
if was_on_ground and not on_ground:
    coyote_time = COYOTE_FRAMES
```

**Hint:** somewhere you need to lower `coyote_time` by 1 each frame while it is above 0.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The double jump should only fire once. Right now the player keeps double-jumping endlessly.

```python
if event.key == pygame.K_SPACE:
    if on_ground or coyote_time > 0:
        velocity_y = JUMP_STRENGTH
    else:
        velocity_y = DOUBLE_JUMP_STRENGTH
```

**Hint:** nothing counts the jumps. Use `jumps_used` to block a third jump.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Here is a working version of coyote time + double jump. Read it carefully, then answer the questions.

```python
# each frame, before checking input
if was_on_ground and not on_ground:
    coyote_time = COYOTE_FRAMES
if coyote_time > 0:
    coyote_time -= 1

# when the player presses jump
if event.key == pygame.K_SPACE:
    if (on_ground or coyote_time > 0) and jumps_used == 0:
        velocity_y = JUMP_STRENGTH
        jumps_used = 1
    elif jumps_used == 1:
        velocity_y = DOUBLE_JUMP_STRENGTH
        jumps_used = 2

# when the player lands
if player.y >= HEIGHT - 50:
    player.y = HEIGHT - 50
    velocity_y = 0
    on_ground = True
    jumps_used = 0
```

**What does `coyote_time -= 1` do, and why does the player lose coyote time after a few frames?**

<div class="write-space"></div>

**Why does the first jump check `jumps_used == 0` instead of just `on_ground`?**

<div class="write-space"></div>

**When does `jumps_used` become 2, and what stops a third jump from happening?**

<div class="write-space"></div>

**Which line gives the player their jumps back, and when does it run?**

<div class="write-space"></div>

**How does `coyote_time > 0` let the player jump just after leaving an edge?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the coyote time + double jump code **you wrote in today's lesson**. Record a short video on your phone. You may show your game running. Try to use these words: **coyote time**, **double jump**, **jumps used**, **reset**, **air**.

> 1. Show a normal jump from the ground and point to the line that starts it.
> 2. Show a double jump in the air and read the part that uses `jumps_used`.
> 3. Run off a ledge and jump late — show coyote time working.
> 4. Read the line that resets jumps on landing and explain it.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
