# 🏎️ RS003 Week 8 — English Worksheet

**Topic:** Variable Speed — Hold Shift to Boost · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week is about how the flying **feels good**. You will think about and explain the code that makes the ship speed up while you hold **Shift**, and slowly coast to a stop with **friction**, like drifting through space. You learn about a **velocity** variable that builds up and slows down.

> 🧠 Words to know: **velocity**, **acceleration**, **friction**, **max speed**, **Shift key**

---

## 1 · Predict 🔮

Read each piece of code. Just by reading it, write what you think will happen.

```python
velocity_x = 0
ACCEL = 0.5
velocity_x += ACCEL
ship_x = ship_x + int(velocity_x)
```

**`velocity_x` keeps growing while you hold a key. What happens to the ship's movement — does it move at a steady speed or get faster?**

<div class="write-space"></div>

```python
if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
    velocity_x = velocity_x * FRICTION   # FRICTION = 0.85
```

**When you let go of both keys, the velocity is multiplied by 0.85 every loop. What does that do over time?**

<div class="write-space"></div>

```python
max_v = MAX_SPEED_FAST if keys[pygame.K_LSHIFT] else MAX_SPEED
```

**What does holding Shift change about the top speed?**

<div class="write-space"></div>

```python
if velocity_x > max_v:
    velocity_x = max_v
if velocity_x < -max_v:
    velocity_x = -max_v
```

**If `velocity_x` tries to grow past `max_v`, what do these lines do to it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Write the fixed code, then explain why the original was wrong.

**Bug A** — The ship should coast to a stop when you let go, but instead it keeps sliding forever.

```python
if keys[pygame.K_LEFT]:
    velocity_x -= ACCEL
if keys[pygame.K_RIGHT]:
    velocity_x += ACCEL
ship_x += int(velocity_x)
```

**Hint:** nothing slows the velocity down when no key is held.

**Write the fixed code (add the friction step):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The ship is supposed to have a top speed, but holding a key for a long time makes it shoot across the screen far too fast.

```python
if keys[pygame.K_RIGHT]:
    velocity_x += ACCEL
ship_x += int(velocity_x)
```

**Hint:** the velocity is never capped at a maximum.

**Write the fixed code (add the speed limit):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The program crashes because Pygame is given a position with a decimal point.

```python
ship_x = ship_x + velocity_x
pygame.draw.rect(screen, CYAN, (ship_x - 20, ship_y, 40, 50))
```

**Hint:** velocity is a decimal; screen positions must be whole numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this full program. It makes the ship speed up, coast, and boost. Answer the questions by reading only — you do not need to run it.

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ship_x = CENTER_X
ship_y = HEIGHT - 100
velocity_x = 0
ACCEL = 0.5
MAX_SPEED = 8
MAX_SPEED_FAST = 16
FRICTION = 0.85

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    max_v = MAX_SPEED_FAST if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) else MAX_SPEED

    if keys[pygame.K_LEFT]:
        velocity_x -= ACCEL
    if keys[pygame.K_RIGHT]:
        velocity_x += ACCEL

    if velocity_x > max_v:
        velocity_x = max_v
    if velocity_x < -max_v:
        velocity_x = -max_v

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        velocity_x = velocity_x * FRICTION

    ship_x = ship_x + int(velocity_x)

    screen.fill((10, 12, 40))
    pygame.draw.rect(screen, (80, 220, 255), (ship_x - 20, ship_y, 40, 50))
    pygame.draw.polygon(screen, (255, 255, 255), [(ship_x, ship_y - 20), (ship_x - 20, ship_y), (ship_x + 20, ship_y)])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Which line makes the ship speed up when you press RIGHT, and how does it change `velocity_x`?**

<div class="write-space"></div>

**What does the line `max_v = MAX_SPEED_FAST if ... else MAX_SPEED` decide, and what makes it pick the fast number?**

<div class="write-space"></div>

**The line `velocity_x = velocity_x * FRICTION` only runs when no arrow key is held. Why is that the right time to slow the ship down?**

<div class="write-space"></div>

**Why does the code use `int(velocity_x)` instead of just `velocity_x` when changing `ship_x`?**

<div class="write-space"></div>

**`velocity_x` can become a negative number. What does a negative velocity make the ship do?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own ship-with-feel code. Now explain it. Record a short phone video. You may show your ship running while you talk. Try to use these words: **velocity**, **acceleration**, **friction**, **max speed**, **Shift**.

> 1. Show your ship flying slowly, then hold Shift and fly fast.
> 2. Let go of the keys and show the ship coasting to a stop.
> 3. Point to your friction line and say what 0.85 does.
> 4. Explain how your code stops the ship going past the max speed.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
