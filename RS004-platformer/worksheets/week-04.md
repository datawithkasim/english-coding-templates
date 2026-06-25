# 👀 RS004 Week 4 — English Worksheet

**Topic:** Player Faces a Direction (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week your player gets a **face**. A `facing` variable remembers which way it last moved, and a `draw_player()` function uses it to put the eyes on the correct side. One function takes charge of *all* the drawing — that is **separation of concerns**. This worksheet is for thinking about and explaining that code, not for building it here.

> Keep these words handy: **facing**, **state variable**, **`draw_player()`**, **offset**, **separation of concerns**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think will happen.

```python
facing = "right"
if keys[pygame.K_LEFT]:
    player.x -= PLAYER_SPEED
    facing = "left"
```

**The player moves left. What does `facing` become? What if it moves right next?**

<div class="write-space"></div>

```python
body_color = (220, 50, 50) if facing == "right" else (180, 30, 30)
```

**This is a one-line `if`/`else`. What colour is the body when facing left?**

<div class="write-space"></div>

```python
if facing == "right":
    eye_x = rect.x + 35
else:
    eye_x = rect.x + 15
```

**Why is the eye further right (`+35`) when facing right?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Write the fixed code on paper, then explain why the original was wrong.

**Bug A** — The eyes should follow the player as it moves. Right now the eyes stay frozen in one spot while the body slides away.

```python
def draw_player(rect, facing):
    pygame.draw.rect(screen, (220, 50, 50), rect)
    pygame.draw.circle(screen, (255, 255, 255), (135, 215), 6)
```

**Hint:** the eye position is hard-coded as `(135, 215)`. It should be built from `rect.x`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The body colour should change with direction, but it is always the same red.

```python
def draw_player(rect, facing):
    body_color = (220, 50, 50)
    pygame.draw.rect(screen, body_color, rect)
```

**Hint:** `facing` is passed in but never used. Make the colour depend on it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `facing` should update when the player moves, but it never changes from its starting value.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.x -= PLAYER_SPEED
if keys[pygame.K_RIGHT]:
    player.x += PLAYER_SPEED
```

**Hint:** each movement should also set `facing`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Here is a working `draw_player()` that puts the eye on the correct side and changes colour with direction.

```python
def draw_player(rect, facing):
    body_color = (220, 50, 50) if facing == "right" else (180, 30, 30)
    pygame.draw.rect(screen, body_color, rect)

    if facing == "right":
        eye_x = rect.x + 35
    else:
        eye_x = rect.x + 15
    eye_y = rect.y + 15
    pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 6)
```

Read it carefully and answer:

**Why does `draw_player()` take `facing` as one of its inputs?**

<div class="write-space"></div>

**The first line uses a one-line `if`/`else`. What two colours can `body_color` become, and what decides which one?**

<div class="write-space"></div>

**The eye uses `rect.x + 35` or `rect.x + 15`. Why is the eye built from `rect.x` instead of a fixed number like `135`?**

<div class="write-space"></div>

**`eye_y` is always `rect.y + 15`. Why does the up/down position stay the same when the left/right position changes?**

<div class="write-space"></div>

**This one function draws the body AND the eye. Why is keeping all the drawing in one place (separation of concerns) helpful?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the code **you wrote in today's lesson**. Record a short video on your phone — you may show your player turning left and right while it runs. Try to use these words: **facing**, **draw_player**, **offset**, **direction**, **function**.

> 1. Show your player facing right, then left.
> 2. Point at your `facing` variable and say when it changes.
> 3. Read your eye-position line out loud and explain the offset.
> 4. Show one choice you made in your code and why.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
