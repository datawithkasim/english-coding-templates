# 🕹️ RS003 Week 7 — English Worksheet

**Topic:** Fly the Ship in Four Directions · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week your ship comes to life. It **flies** up, down, left, and right while you hold the arrow keys. You learn that the X axis goes across the screen and the Y axis goes down it — **left makes X smaller, right makes X bigger, up makes Y smaller, down makes Y bigger** — and that the ship is drawn wherever those two numbers say.

> 🧠 Words to know: **X axis**, **Y axis**, **key press**, **increase / decrease**, **speed**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
ship_x = CENTER_X
ship_y = HEIGHT - 100
SPEED = 5
ship_x -= SPEED
```

**Does `ship_x -= 5` move the ship left or right? Why?**

<div class="write-space"></div>

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:  ship_x -= SPEED
if keys[pygame.K_RIGHT]: ship_x += SPEED
if keys[pygame.K_UP]:    ship_y -= SPEED
if keys[pygame.K_DOWN]:  ship_y += SPEED
```

**What happens while you hold UP? What about holding DOWN? Why does UP make `ship_y` smaller?**

<div class="write-space"></div>

```python
pygame.draw.rect(screen, CYAN, (ship_x - 20, ship_y, 40, 50))
pygame.draw.polygon(screen, WHITE, [(ship_x, ship_y - 20), (ship_x - 20, ship_y), (ship_x + 20, ship_y)])
```

**The body and nose both use `ship_x` and `ship_y`. When you press a key, what moves?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and fly the ship

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SPACE = (10, 12, 40)
CYAN = (80, 220, 255)
WHITE = (255, 255, 255)
RED = (230, 60, 60)

ship_x = CENTER_X
ship_y = HEIGHT - 100
SPEED = 5

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  ship_x -= SPEED
    if keys[pygame.K_RIGHT]: ship_x += SPEED
    if keys[pygame.K_UP]:    ship_y -= SPEED
    if keys[pygame.K_DOWN]:  ship_y += SPEED

    screen.fill(SPACE)
    pygame.draw.rect(screen, CYAN, (ship_x - 20, ship_y, 40, 50))
    pygame.draw.polygon(screen, WHITE, [(ship_x, ship_y - 20), (ship_x - 20, ship_y), (ship_x + 20, ship_y)])
    pygame.draw.rect(screen, RED, (ship_x - 16, ship_y + 50, 8, 10))
    pygame.draw.rect(screen, RED, (ship_x + 8, ship_y + 50, 8, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Fly in all four directions. Describe how the ship moves for each arrow key:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — Pressing UP should move the ship up, but it moves **down** instead.

```python
if keys[pygame.K_UP]:
    ship_y += SPEED
```

**Hint:** up means Y gets smaller.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The ship should only move **while a key is held**, but it drifts to the right on its own without any key press.

```python
ship_x += SPEED
if keys[pygame.K_LEFT]:
    ship_x -= SPEED
```

**Hint:** the first line runs every loop no matter what.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The keys do nothing at all. The ship never moves.

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if keys[pygame.K_LEFT]:
        ship_x -= SPEED
```

**Hint:** `keys` was never asked for. You need `pygame.key.get_pressed()` outside the event loop.

**Write the fixed code (show where `keys` is set and used):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Change the flying speed

Try `SPEED = 2`, then `SPEED = 10`. Run each one.

**Write how the flying feels at slow speed versus fast speed:**

<div class="write-space"></div>

### 🎯 Move the whole ship together

Make sure every part of the ship — body, nose, and thrusters — uses `ship_x` and `ship_y`, so they all fly together.

**Write down two lines that use `ship_x` and `ship_y`:**

<div class="write-space"></div>

**Hint:** if one part forgets to use `ship_x` or `ship_y`, that part stays behind while the rest flies away.

---

## 5 · Make It 📸

### 🎯 Build a flying ship

Build a program where:

1. the ship flies in all four directions with the arrow keys,
2. all parts move together,
3. you can choose the flying speed with a `SPEED` constant.

Send a **video** (so the movement is visible), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made variables to hold the ship position called …
>
> Pressing LEFT changes `ship_x` by … and UP changes `ship_y` by …
>
> All the parts move together because they use …
>
> I set the speed to … because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while you fly the ship with the arrow keys. Talk through it like you are teaching someone. Try to use these words: **X axis**, **Y axis**, **key press**, **increase**, **speed**.

> 1. Show the ship flying in all four directions as you press keys.
> 2. Read your four `if keys[...]` lines out loud and say which way each moves.
> 3. Point at where the ship position is used to draw the body.
> 4. Change the SPEED live and show the difference.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your flying video to teacher on KakaoTalk.
