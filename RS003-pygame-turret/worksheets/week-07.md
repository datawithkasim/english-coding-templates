# ⬅️➡️ RS003 Week 7 — English Worksheet

**Topic:** Move the Gun Left and Right · **Course:** Pygame Turret · **Time:** about 45 minutes

This week your turret comes to life. The barrel **aims** left and right while you hold the arrow keys. You learn that the X axis goes across the screen — **left makes X smaller, right makes X bigger** — and that the base stays still while only the gun moves.

> 🧠 Words to know: **X axis**, **key press**, **arrow key**, **increase / decrease**, **speed**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
gun_x = CENTER_X
SPEED = 5
gun_x -= SPEED
```

**Does `gun_x -= 5` move the gun left or right? Why?**

<div class="write-space"></div>

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    gun_x -= SPEED
if keys[pygame.K_RIGHT]:
    gun_x += SPEED
```

**What happens while you hold the LEFT key? What about holding RIGHT?**

<div class="write-space"></div>

```python
pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 30, HEIGHT - 80, 60, 40))
pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 80), (gun_x, HEIGHT - 200), 10)
```

**The base uses `CENTER_X` but the barrel tip uses `gun_x`. When you press a key, which part moves and which part stays still?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and aim the barrel

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SKY = (135, 206, 235)
DARK_GREEN = (0, 100, 0)
GRAY = (80, 80, 80)
BLACK = (0, 0, 0)

gun_tip_x = CENTER_X
SPEED = 5

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        gun_tip_x -= SPEED
    if keys[pygame.K_RIGHT]:
        gun_tip_x += SPEED

    screen.fill(SKY)
    pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 30, HEIGHT - 80, 60, 40))
    pygame.draw.circle(screen, BLACK, (CENTER_X, HEIGHT - 80), 10)
    pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 80), (gun_tip_x, HEIGHT - 200), 10)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Hold LEFT, then RIGHT. Describe how the barrel tip moves and what stays still:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — Pressing RIGHT should move the barrel right, but it moves **left** instead.

```python
if keys[pygame.K_RIGHT]:
    gun_tip_x -= SPEED
```

**Hint:** right means X gets bigger.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The barrel should only move **while a key is held**, but it drifts on its own without any key press.

```python
gun_tip_x += SPEED
if keys[pygame.K_LEFT]:
    gun_tip_x -= SPEED
```

**Hint:** the first line runs every loop no matter what.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The keys do nothing at all. The barrel never moves.

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if keys[pygame.K_LEFT]:
        gun_tip_x -= SPEED
```

**Hint:** `keys` was never asked for. You need `pygame.key.get_pressed()` outside the event loop.

**Write the fixed code (show where `keys` is set and used):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Change the aiming speed

Try `SPEED = 2`, then `SPEED = 10`. Run each one.

**Write how the aiming feels at slow speed versus fast speed:**

<div class="write-space"></div>

### 🎯 Keep the base still, move only the gun

Make sure your base rectangle uses `CENTER_X` and only the barrel tip uses `gun_tip_x`.

**Write down which line uses `CENTER_X` and which line uses `gun_tip_x`:**

<div class="write-space"></div>

**Hint:** the base is bolted to the ground. Only the moving end of the barrel should follow `gun_tip_x`.

---

## 5 · Make It 📸

### 🎯 Build an aiming turret

Build a program where:

1. the barrel aims left and right with the arrow keys,
2. the base stays still,
3. you can choose the aiming speed with a `SPEED` constant.

Send a **video** (so the movement is visible), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made a variable to hold the barrel position called …
>
> Pressing LEFT changes it by … and RIGHT by …
>
> The base stays still because it uses …
>
> I set the speed to … because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while you aim the turret with the arrow keys. Talk through it like you are teaching someone. Try to use these words: **X axis**, **key press**, **arrow key**, **increase**, **speed**.

> 1. Show the barrel aiming left and right as you press keys.
> 2. Read your two `if keys[...]` lines out loud and say which way each moves.
> 3. Point at the line that keeps the base still.
> 4. Change the SPEED live and show the difference.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your aiming video to teacher on KakaoTalk.
