# 🏎️ RS003 Week 8 — English Worksheet

**Topic:** Variable Speed — Hold Shift to Go Fast · **Course:** Pygame Turret · **Time:** about 45 minutes

This week you make the aiming **feel good**. The barrel speeds up while you hold **Shift**, and when you let go of the arrow keys it slowly coasts to a stop with **friction**. You learn about a **velocity** variable that builds up and slows down.

> 🧠 Words to know: **velocity**, **acceleration**, **friction**, **max speed**, **Shift key**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
velocity_x = 0
ACCEL = 0.5
velocity_x += ACCEL
gun_tip_x = gun_tip_x + int(velocity_x)
```

**`velocity_x` keeps growing while you hold a key. What happens to the barrel's movement — does it move at a steady speed or get faster?**

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

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and feel the coast

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

gun_tip_x = CENTER_X
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

    gun_tip_x = gun_tip_x + int(velocity_x)

    screen.fill((135, 206, 235))
    pygame.draw.rect(screen, (0, 100, 0), (CENTER_X - 30, HEIGHT - 80, 60, 40))
    pygame.draw.line(screen, (80, 80, 80), (CENTER_X, HEIGHT - 80), (gun_tip_x, HEIGHT - 200), 10)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Hold RIGHT, then let go. Does the barrel stop instantly or coast? Now hold Shift and aim. What changes?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The barrel should coast to a stop when you let go, but instead it keeps sliding forever.

```python
if keys[pygame.K_LEFT]:
    velocity_x -= ACCEL
if keys[pygame.K_RIGHT]:
    velocity_x += ACCEL
gun_tip_x += int(velocity_x)
```

**Hint:** nothing slows the velocity down when no key is held.

**Write the fixed code (add the friction step):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The barrel is supposed to have a top speed, but holding a key for a long time makes it shoot across the screen far too fast.

```python
if keys[pygame.K_RIGHT]:
    velocity_x += ACCEL
gun_tip_x += int(velocity_x)
```

**Hint:** the velocity is never capped at a maximum.

**Write the fixed code (add the speed limit):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The program crashes because Pygame is given a position with a decimal point.

```python
gun_tip_x = gun_tip_x + velocity_x
pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 80), (gun_tip_x, HEIGHT - 200), 10)
```

**Hint:** velocity is a decimal; screen positions must be whole numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Tune the friction

Try `FRICTION = 0.5`, then `0.85`, then `0.99`. Run each one and let go after aiming.

**Write how each friction value feels (which one is slippery, which one is grippy):**

<div class="write-space"></div>

### 🎯 Make Shift mode look different

Add a visual change while Shift is held — for example, make the barrel a different colour.

**Describe what you changed and which key state triggers it:**

<div class="write-space"></div>

**Hint:** you already know `keys[pygame.K_LSHIFT]`. Use it to pick a colour the same way the code picks `max_v`.

---

## 5 · Make It 📸

### 🎯 Build a turret with feel

Build a program where:

1. the barrel speeds up while held (acceleration),
2. it coasts to a stop when released (friction),
3. Shift gives a faster top speed,
4. it never crashes from decimal positions.

Send a **video** comparing normal aiming and Shift aiming, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I added a velocity variable that …
>
> Acceleration makes the barrel …
>
> Friction makes it … when I let go.
>
> Holding Shift changes the top speed to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video showing normal aiming and Shift aiming. Talk through it like you are teaching someone. Try to use these words: **velocity**, **acceleration**, **friction**, **max speed**, **Shift**.

> 1. Aim slowly, then hold Shift and aim fast.
> 2. Let go of the keys and show the barrel coasting.
> 3. Read your friction line out loud and say what 0.85 does.
> 4. Show the difference between two friction values you tried.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your normal/Shift comparison video to teacher on KakaoTalk.
