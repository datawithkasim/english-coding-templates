# 🚧 RS003 Week 9 — English Worksheet

**Topic:** Keep the Ship Inside the Screen · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you stop the ship from flying off the screen on any side. You set a **minimum** and **maximum** for both X and Y, then use comparisons (`<`, `>`) to keep the ship inside all four walls. The trick of forcing a value back inside a range is called **clamping**.

> 🧠 Words to know: **minimum / maximum**, **compare (`<`, `>`)**, **clamp**, **boundary**, **limit**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
if ship_x < 20: ship_x = 20
if ship_x > WIDTH - 20: ship_x = WIDTH - 20
```

**These two lines run AFTER the ship moves. What do they do if the ship went too far left or too far right?**

<div class="write-space"></div>

```python
if ship_y < 20: ship_y = 20
if ship_y > HEIGHT - 60: ship_y = HEIGHT - 60
```

**These keep the ship inside the top and bottom. Why is the bottom limit `HEIGHT - 60` and not just `HEIGHT`?**

<div class="write-space"></div>

```python
pygame.draw.rect(screen, RED, (0, 0, WIDTH, HEIGHT), 3)
```

**A red rectangle outline is drawn around the whole edge of the screen. What does it show the player?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and hit the walls

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ship_x = CENTER_X
ship_y = HEIGHT - 100
SPEED = 5
RED = (230, 60, 60)

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

    if ship_x < 20: ship_x = 20
    if ship_x > WIDTH - 20: ship_x = WIDTH - 20
    if ship_y < 20: ship_y = 20
    if ship_y > HEIGHT - 60: ship_y = HEIGHT - 60

    screen.fill((10, 12, 40))
    pygame.draw.rect(screen, RED, (0, 0, WIDTH, HEIGHT), 3)
    pygame.draw.rect(screen, (80, 220, 255), (ship_x - 20, ship_y, 40, 50))
    pygame.draw.polygon(screen, (255, 255, 255), [(ship_x, ship_y - 20), (ship_x - 20, ship_y), (ship_x + 20, ship_y)])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Fly into each of the four walls. Where does the ship stop? What stops it?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The ship should not fly past the left wall, but it flies right off the left edge of the screen.

```python
if keys[pygame.K_LEFT]:
    ship_x -= SPEED
```

**Hint:** there is no clamp pulling the ship back if it goes past the left wall.

**Write the fixed code (add the left clamp):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The clamp is supposed to pull the ship back if it goes too far, but the comparisons are backwards so it teleports to the wrong wall.

```python
if ship_x > 20:
    ship_x = 20
if ship_x < WIDTH - 20:
    ship_x = WIDTH - 20
```

**Hint:** if the ship is **smaller** than 20 it went too far left. Check the directions.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The ship is clamped left and right, but it still flies off the **top** and **bottom** of the screen.

```python
if ship_x < 20: ship_x = 20
if ship_x > WIDTH - 20: ship_x = WIDTH - 20
```

**Hint:** there are only two clamps here. You need two more for `ship_y`.

**Write the fixed code (add the top and bottom clamps):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Make the play area smaller

Change the clamp numbers so the ship has a smaller space to fly in (for example keep it in the bottom half).

**Write the new clamp values you chose:**

<div class="write-space"></div>

### 🎯 Try the guard method instead of the clamp method

Right now the example lets the ship move freely, then clamps it back. Rewrite one direction so the ship only moves while it is still inside the wall (check `> 20` before moving).

**Write your guarded move lines:**

<div class="write-space"></div>

**Hint:** both methods keep the ship inside. The clamp lets it move first, then snaps it back if it went too far.

---

## 5 · Make It 📸

### 🎯 Build a ship that stays on screen

Build a program where:

1. the ship flies in all four directions,
2. it can never leave the screen on any side,
3. a red border shows where the limits are.

Send a **photo or video** showing the ship stopping at all four walls, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I set my clamp limits to …
>
> The ship stops on the left because …
>
> The ship stops at the bottom because …
>
> Clamping means …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while the ship hits all four walls. Talk through it like you are teaching someone. Try to use these words: **minimum**, **maximum**, **compare**, **clamp**, **boundary**.

> 1. Fly into the left and right walls and show it stop.
> 2. Fly into the top and bottom walls and show it stop.
> 3. Read one clamp line out loud and explain it.
> 4. Say what would happen with no limits at all.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
