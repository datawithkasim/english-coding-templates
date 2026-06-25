# 💥 RS003 Week 10 — English Worksheet

**Topic:** Feedback When You Hit the Edge · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week is about **thinking and talking** about the code that makes the screen react when the ship hits a wall. The border flashes red and the scene shakes for a moment using **timer variables** that count down frame by frame and `random` to make a shake. You will read code, find bugs on paper, and explain the code you wrote in the lesson.

> 🧠 Words to know: **timer**, **flash**, **shake**, **offset**, **random**

---

## 1 · Predict 🔮

Read each piece of code. Write what you think it does. You are reading only — do not run anything.

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

```python
border_color = (255, 50, 50) if flash_timer > 0 else (60, 60, 90)
border_width = 6 if flash_timer > 0 else 2
```

**What colour and width is the border while `flash_timer` is above 0? What about when it is 0?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Find the problem on paper.

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

## 3 · Explain the Code 📖

Read this working example. It is the full program from your lesson. Answer the questions by reading the code — you do not need to run it.

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

**The line `if ship_x < 20 or ship_x > WIDTH - 20 ...` checks four things. What is it checking for?**

<div class="write-space"></div>

**When that check is true, which two timers get set, and what number do they get?**

<div class="write-space"></div>

**The four lines like `if ship_x < 20: ship_x = 20` keep the ship on screen. In your own words, what do they stop happening?**

<div class="write-space"></div>

**Why is `shake_x` added to both the rectangle and the polygon, instead of just one of them?**

<div class="write-space"></div>

**Near the bottom, both timers go down by 1 each loop. What would happen if you deleted those two `if` blocks?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the code **you** wrote in today's lesson. Record a short video on your phone. You can show the program running, then talk through your code like you are teaching someone. Try to use these words: **timer**, **flash**, **shake**, **offset**, **random**.

> 1. Fly into a wall and show the flash and shake.
> 2. Read your timer line out loud and say what 10 means.
> 3. Point at where the timer counts down each loop.
> 4. Show where the **offset** (shake) is added to the ship.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
