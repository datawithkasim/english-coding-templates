# 🦊 RS004 Week 6 — English Worksheet

**Topic:** Coyote Time + Double Jump (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week your jump feels like a *real* game. **Coyote time** lets the player jump for a few frames *after* leaving the edge. A **double jump** gives one extra jump in the air. You will track how many jumps were used and reset them on landing.

> Keep these words handy: **coyote time**, **double jump**, **jumps used**, **was on ground**, **reset**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

## 4 · Tune the Polish 🛠️

Start from your working coyote + double jump. Change one thing at a time.

1. Set `COYOTE_FRAMES` to 1, then to 12. What feels too short? Too forgiving?

<div class="write-space"></div>

2. Make `DOUBLE_JUMP_STRENGTH` weaker, then equal to the first jump. Which feels right?

<div class="write-space"></div>

3. **Stretch:** add a tiny particle burst (a few small circles) when the double jump fires. Where will you create them?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Tune **your own** jump polish: coyote time + double jump that feel good to you.

When it works, send a **photo or video** showing a single jump, a double jump, and a coyote jump, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, coyote time lets the player jump after leaving an edge by …
>
> The double jump works because `jumps_used` …
>
> I reset the jumps when …
>
> The values I tuned were …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video showing all three jumps. Teach it to someone new. Try to use these words: **coyote time**, **double jump**, **jumps used**, **reset**, **air**.

> 1. Show a normal jump from the ground.
> 2. Show a double jump in the air.
> 3. Run off a ledge and jump late — show coyote time working.
> 4. Read the line that resets jumps on landing and explain it.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
