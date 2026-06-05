# 👀 RS004 Week 4 — English Worksheet

**Topic:** Player Faces a Direction (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week your player gets a **face**. A `facing` variable remembers which way it last moved, and a `draw_player()` function uses it to put the eyes on the correct side. One function takes charge of *all* the drawing — that is **separation of concerns**.

> Keep these words handy: **facing**, **state variable**, **`draw_player()`**, **offset**, **separation of concerns**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

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

## 3 · Extend the Look 🛠️

Start from your working `draw_player()`. Add one idea at a time.

1. When the player is standing still (no key held), put the eye in the **middle**. How will you know it is standing still?

<div class="write-space"></div>

2. Add a second eye so the player has two. Where do you place the second one?

<div class="write-space"></div>

3. **Stretch:** make the body colour go darker while moving fast. What decides "fast"?

<div class="write-space"></div>

---

## 4 · Build & Show 📸

Design **your own** player character. It must clearly show which way it is facing when it moves.

When it works, send a **photo or video** showing it moving *both* ways, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I drew my player with `draw_player()` which is in charge of …
>
> The `facing` variable remembers …
>
> I made the eyes follow the body by …
>
> My character shows direction by …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video showing the player turning left and right. Teach it to someone new. Try to use these words: **facing**, **draw_player**, **offset**, **direction**, **function**.

> 1. Show the player facing right, then left.
> 2. Point at the `facing` variable and say when it changes.
> 3. Read the eye-position line out loud and explain the offset.
> 4. Show one design choice you made and why.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
