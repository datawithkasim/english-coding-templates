# 🕹️ RS003 Week 7 — English Worksheet

**Topic:** Fly the Ship in Four Directions · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you think about how the ship **flies** up, down, left, and right while you hold the arrow keys. You read the code, predict what it does, fix broken code, and explain it in your own words — including the code you wrote in today's live lesson.

> 🧠 Words to know: **X axis**, **Y axis**, **key press**, **increase / decrease**, **speed**

---

## 1 · Predict 🔮

Read each piece of code. Write what you think it does. You do not run anything — just think it through.

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

```python
SPEED = 2
SPEED = 10
```

**One of these makes the ship fly slowly and one makes it fly fast. Which is which, and why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Write the fixed code, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Here is the full working program from this week. Read it carefully and answer the questions below. You do not need to run it.

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

**What do `ship_x` and `ship_y` hold, and what is the starting position of the ship?**

<div class="write-space"></div>

**What does `keys = pygame.key.get_pressed()` give you, and why is it inside the `while` loop?**

<div class="write-space"></div>

**Why does the same `ship_x` and `ship_y` appear in the body, the nose, and both thrusters?**

<div class="write-space"></div>

**What would change on screen if you set `SPEED = 10` instead of `5`?**

<div class="write-space"></div>

**Why is `screen.fill(SPACE)` called every loop before the ship is drawn?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own flying-ship code. Now explain **your own code** in a short phone video. You may show it running on screen. Talk through it like you are teaching someone, and try to use these words: **X axis**, **Y axis**, **key press**, **increase**, **speed**.

> 1. Show your ship flying in all four directions as you press the keys.
> 2. Read your four `if keys[...]` lines out loud and say which way each one moves the ship.
> 3. Point at where `ship_x` and `ship_y` are used to draw the ship.
> 4. Say what `SPEED` does and what number you chose.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
