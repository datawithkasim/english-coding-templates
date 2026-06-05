# 🟥 RS004 Week 3 — English Worksheet

**Topic:** Player & Keyboard Movement · **Course:** Platformer Game · **Time:** about 45 minutes

This week a **player** appears — a rectangle you control with the **arrow keys**. You will learn `pygame.Rect` to track position, read held-down keys with `pygame.key.get_pressed()`, and stop the player from sliding off the screen.

> Keep these words handy: **Rect**, **position**, **`get_pressed()`**, **speed**, **boundary (edge)**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

```python
player = pygame.Rect(100, 500, 50, 50)
```

**What do the four numbers mean? Where on the screen is the player?**

<div class="write-space"></div>

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_RIGHT]:
    player.x = player.x + 5
```

**The right arrow is held down. What happens to the player each frame?**

<div class="write-space"></div>

```python
if player.x > WIDTH - player.width:
    player.x = WIDTH - player.width
```

**The player runs into the right wall. What does this code stop from happening?**

<div class="write-space"></div>

---

## 2 · Rect Reading 📐

A player is `pygame.Rect(100, 500, 50, 50)`. Fill in the blanks.

```
player.x       = ___
player.y       = ___
player.width   = ___
player.right   = ___   (hint: x + width)
player.bottom  = ___   (hint: y + height)
```

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — Arrow keys should move the player smoothly while held. Right now the player only moves on a brand-new key press, one step at a time.

```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player.x = player.x + 5
```

**Hint:** for *held* keys we use `pygame.key.get_pressed()`, not `KEYDOWN` events.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The player should stop at the left edge. Right now it disappears off the left side.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.x = player.x - 5
```

**Hint:** after moving, check if `player.x` went below 0 and pull it back.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Both arrows should work. Right now only the right arrow does anything.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_RIGHT]:
    player.x = player.x + 5
    if keys[pygame.K_LEFT]:
        player.x = player.x - 5
```

**Hint:** the left check is trapped *inside* the right check. They should be separate.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Tune the Feel 🛠️

Start from your working player. Change one thing at a time and note the effect.

1. Set `PLAYER_SPEED` to 2, then 10. Which feels best to you, and why?

<div class="write-space"></div>

2. Change the player's colour and size. Write what you picked.

<div class="write-space"></div>

3. **Stretch:** make the player start in the middle of the screen instead of the left. Which number did you change?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Put your player on top of last week's gradient sky. It should move left and right with the arrow keys and stop at both walls.

When it works, send a **photo or video**, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I made the player with `pygame.Rect(...)` which means …
>
> To move it, I used `get_pressed()` because …
>
> I stopped it leaving the screen by …
>
> The speed I chose was ___ because …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while you move the player around. Teach it to someone new. Try to use these words: **Rect**, **arrow keys**, **speed**, **edge**, **boundary**.

> 1. Show the player moving left and right.
> 2. Run into a wall and show it stops.
> 3. Read the boundary check out loud and explain it.
> 4. Show what happens when you change the speed.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
