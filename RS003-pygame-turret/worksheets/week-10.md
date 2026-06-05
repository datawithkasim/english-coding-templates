# 💥 RS003 Week 10 — English Worksheet

**Topic:** Feedback When You Hit the Wall · **Course:** Pygame Turret · **Time:** about 45 minutes

This week the boundary **reacts**. When the aim slams into a wall, the line flashes red and the screen shakes for a moment. You learn to use **timer variables** that count down frame by frame, and `random` to make a shake.

> 🧠 Words to know: **timer**, **flash**, **shake**, **offset**, **random**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
flash_timer = 0
if gun_tip_x > MAX_X:
    gun_tip_x = MAX_X
    flash_timer = 10
```

**When the gun hits the right wall, `flash_timer` is set to 10. What might 10 mean here?**

<div class="write-space"></div>

```python
if flash_timer > 0:
    flash_timer = flash_timer - 1
```

**This runs every loop. How long does `flash_timer` stay above 0 after being set to 10?**

<div class="write-space"></div>

```python
shake_x = random.randint(-5, 5) if shake_timer > 0 else 0
pygame.draw.rect(screen, GREEN, (CENTER_X - 30 + shake_x, HEIGHT - 80, 60, 40))
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

MIN_X = 50
MAX_X = WIDTH - 50
gun_tip_x = CENTER_X
SPEED = 6
flash_timer = 0
shake_timer = 0

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

    if gun_tip_x < MIN_X:
        gun_tip_x = MIN_X
        flash_timer = 10
        shake_timer = 10
    if gun_tip_x > MAX_X:
        gun_tip_x = MAX_X
        flash_timer = 10
        shake_timer = 10

    shake_x = random.randint(-5, 5) if shake_timer > 0 else 0
    shake_y = random.randint(-5, 5) if shake_timer > 0 else 0

    screen.fill((135, 206, 235))
    line_color = (255, 50, 50) if flash_timer > 0 else (180, 180, 180)
    line_width = 6 if flash_timer > 0 else 2
    pygame.draw.line(screen, line_color, (MIN_X + shake_x, 0), (MIN_X + shake_x, HEIGHT), line_width)
    pygame.draw.line(screen, line_color, (MAX_X + shake_x, 0), (MAX_X + shake_x, HEIGHT), line_width)
    pygame.draw.rect(screen, (0, 100, 0), (CENTER_X - 30 + shake_x, HEIGHT - 80 + shake_y, 60, 40))
    pygame.draw.line(screen, (80, 80, 80), (CENTER_X + shake_x, HEIGHT - 80 + shake_y), (gun_tip_x + shake_x, HEIGHT - 200 + shake_y), 10)
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

**Bug A** — The wall should flash for a moment then go back to grey, but once it flashes it stays red forever.

```python
if gun_tip_x > MAX_X:
    gun_tip_x = MAX_X
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

**Bug C** — The shake should move everything together, but right now the barrel jumps around while the base stays still, so they come apart.

```python
pygame.draw.rect(screen, GREEN, (CENTER_X - 30, HEIGHT - 80, 60, 40))
pygame.draw.line(screen, GRAY, (CENTER_X + shake_x, HEIGHT - 80), (gun_tip_x + shake_x, HEIGHT - 200), 10)
```

**Hint:** the base does not have the shake offset added.

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

Replace or add to the flash with your own idea — a flash of the whole screen, a colour change on the barrel, anything visual.

**Describe your feedback idea and the timer that controls it:**

<div class="write-space"></div>

**Hint:** any feedback works the same way — set a timer to a number on the hit, count it down each loop, and do something special while it is above 0.

---

## 5 · Make It 📸

### 🎯 Build a turret that reacts to walls

Build a program where:

1. the aim is clamped to the screen,
2. hitting a wall flashes the boundary,
3. hitting a wall shakes the scene for a moment,
4. everything shakes together.

Send a **video** showing a wall hit, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made a timer that …
>
> When the gun hits a wall, I set the timer to …
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

> 1. Aim into a wall and show the flash and shake.
> 2. Read your timer line out loud and say what 10 means.
> 3. Point at where the timer counts down.
> 4. Show your own feedback idea.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your wall-hit video to teacher on KakaoTalk.
