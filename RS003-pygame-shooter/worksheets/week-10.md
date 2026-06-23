# 💥 RS003 Week 10 — English Worksheet

**Topic:** Feedback When You Hit the Edge · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week the screen edge **reacts**. When the ship slams into a wall, the border flashes red and the whole scene shakes for a moment. You learn to use **timer variables** that count down frame by frame, and `random` to make a shake.

> 🧠 Words to know: **timer**, **flash**, **shake**, **offset**, **random**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
flash_timer = 0
if ship_x > WIDTH - 20:
    ship_x = WIDTH - 20
    flash_timer = 10
```

**When the ship hits the right wall, `flash_timer` is set to 10. What might 10 mean here?**

<div class="write-space"></div>

```python
if flash_timer > 0:
    flash_timer = flash_timer - 1
```

**This runs every loop. How long does `flash_timer` stay above 0 after being set to 10?**

<div class="write-space"></div>

```python
shake_x = random.randint(-5, 5) if shake_timer > 0 else 0
pygame.draw.rect(screen, CYAN, (ship_x - 20 + shake_x, ship_y, 40, 50))
```

**While the shake timer is running, `shake_x` is a small random number. What does adding it to every position do?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and slam the wall

```python
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ship_x = CENTER_X
ship_y = HEIGHT - 100
SPEED = 6
flash_timer = 0
shake_timer = 0

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

    if ship_x < 20 or ship_x > WIDTH - 20 or ship_y < 20 or ship_y > HEIGHT - 60:
        flash_timer = 10
        shake_timer = 10
    if ship_x < 20: ship_x = 20
    if ship_x > WIDTH - 20: ship_x = WIDTH - 20
    if ship_y < 20: ship_y = 20
    if ship_y > HEIGHT - 60: ship_y = HEIGHT - 60

    shake_x = random.randint(-5, 5) if shake_timer > 0 else 0
    shake_y = random.randint(-5, 5) if shake_timer > 0 else 0

    screen.fill((10, 12, 40))
    border_color = (255, 50, 50) if flash_timer > 0 else (60, 60, 90)
    border_width = 6 if flash_timer > 0 else 2
    pygame.draw.rect(screen, border_color, (0, 0, WIDTH, HEIGHT), border_width)
    pygame.draw.rect(screen, (80, 220, 255), (ship_x - 20 + shake_x, ship_y + shake_y, 40, 50))
    pygame.draw.polygon(screen, (255, 255, 255), [(ship_x + shake_x, ship_y - 20 + shake_y), (ship_x - 20 + shake_x, ship_y + shake_y), (ship_x + 20 + shake_x, ship_y + shake_y)])
    pygame.display.flip()

    if flash_timer > 0:
        flash_timer = flash_timer - 1
    if shake_timer > 0:
        shake_timer = shake_timer - 1

    clock.tick(60)

pygame.quit()
```

**Slam into a wall. Describe what flashes and what shakes, and how long it lasts:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The border should flash for a moment then go back to grey, but once it flashes it stays red forever.

```python
if ship_x > WIDTH - 20:
    ship_x = WIDTH - 20
    flash_timer = 10
```

**Hint:** the timer is set but never counts down.

**Write the fixed code (show where the timer goes down):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The screen should only shake when you hit a wall, but it shakes all the time even in the middle.

```python
shake_x = random.randint(-5, 5)
```

**Hint:** only shake while the shake timer is running.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The shake should move the whole ship together, but right now the nose jumps around while the body stays still, so they come apart.

```python
pygame.draw.rect(screen, CYAN, (ship_x - 20, ship_y, 40, 50))
pygame.draw.polygon(screen, WHITE, [(ship_x + shake_x, ship_y - 20), (ship_x - 20 + shake_x, ship_y), (ship_x + 20 + shake_x, ship_y)])
```

**Hint:** the body does not have the shake offset added.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Tune the shake strength and length

Change `random.randint(-5, 5)` to a bigger range, and change the timer from 10 to a bigger or smaller number.

**Write the shake range and timer length you chose, and how it feels:**

<div class="write-space"></div>

### 🎯 Design your own hit feedback

Replace or add to the flash with your own idea — a flash of the whole screen, a colour change on the ship, anything visual.

**Describe your feedback idea and the timer that controls it:**

<div class="write-space"></div>

**Hint:** any feedback works the same way — set a timer to a number on the hit, count it down each loop, and do something special while it is above 0.

---

## 5 · Make It 📸

### 🎯 Build a ship that reacts to walls

Build a program where:

1. the ship is clamped to the screen,
2. hitting a wall flashes the border,
3. hitting a wall shakes the scene for a moment,
4. everything shakes together.

Send a **video** showing a wall hit, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made a timer that …
>
> When the ship hits a wall, I set the timer to …
>
> Each loop the timer goes down by …
>
> The shake uses random numbers to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video showing a wall hit and the reaction. Talk through it like you are teaching someone. Try to use these words: **timer**, **flash**, **shake**, **offset**, **random**.

> 1. Fly into a wall and show the flash and shake.
> 2. Read your timer line out loud and say what 10 means.
> 3. Point at where the timer counts down.
> 4. Show your own feedback idea.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your wall-hit video to teacher on KakaoTalk.
