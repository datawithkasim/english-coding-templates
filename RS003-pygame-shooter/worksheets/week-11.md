# 🔁 RS003 Week 11 — English Worksheet

**Topic:** Repeat with a For Loop · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week one short loop draws **many things**. A `for` loop with `range(N)` repeats N times, and by using the loop counter `i` you can spread a **row of enemies** across the top of the screen or scatter stars across the background. Your scene gets a lot richer with very little code.

> 🧠 Words to know: **for loop**, **range**, **counter (`i`)**, **pattern**, **spacing**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
for i in range(5):
    x = 100 + (i * 150)
    pygame.draw.rect(screen, RED, (x - 18, 60, 36, 36))
```

**The loop runs 5 times. What are the X values for each enemy? `i` is 0, 1, 2, 3, 4.**

<div class="write-space"></div>

```python
for i in range(40):
    x = i * 20 + 10
    pygame.draw.circle(screen, WHITE, (x, 30), 2)
```

**How many stars appear along the top? How far apart is each one?**

<div class="write-space"></div>

```python
for i in range(5):
    pygame.draw.rect(screen, RED, (100, 60, 36, 36))
```

**This loop never uses `i` in the position. What goes wrong with the picture?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and count the enemies

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SPACE = (10, 12, 40)
WHITE = (255, 255, 255)
RED = (230, 60, 60)

screen.fill(SPACE)

for i in range(40):
    x = i * 20 + 10
    pygame.draw.circle(screen, WHITE, (x, 30), 2)

for i in range(5):
    x = 100 + (i * 150)
    pygame.draw.rect(screen, RED, (x - 18, 80, 36, 36))

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
```

**How many enemies are in the row? How many stars along the top?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — This should draw 5 enemies spread across the top, but all 5 land on top of each other in one spot.

```python
for i in range(5):
    x = 100
    pygame.draw.rect(screen, RED, (x - 18, 80, 36, 36))
```

**Hint:** `x` is the same every time. Use `i` to spread them out.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should draw 10 stars, but only one appears.

```python
i = 0
x = i * 20 + 10
pygame.draw.circle(screen, WHITE, (x, 30), 2)
```

**Hint:** there is no loop at all — it only runs once.

**Write the fixed code using a for loop:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The enemies are supposed to fit on screen, but some are drawn way off the right edge where you cannot see them.

```python
for i in range(20):
    x = i * 200
    pygame.draw.rect(screen, RED, (x - 18, 80, 36, 36))
```

**Hint:** `i * 200` gets bigger than the screen width very fast. Use a smaller gap or fewer enemies.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Change how many and how far apart

Change `range(5)` to draw more enemies, and change the spacing number so they fit nicely.

**Write the range and spacing you chose:**

<div class="write-space"></div>

### 🎯 Add the enemies and stars to your shooter

Open your ship program from an earlier week and add a star loop to the background and a row of enemies across the top.

**Describe where you put the loops in your game loop and what changed on screen:**

<div class="write-space"></div>

**Hint:** draw the background loops **after** `screen.fill(...)` but **before** the ship, so the ship sits in front.

---

## 5 · Make It 📸

### 🎯 Fill your scene with a pattern

Build a scene that uses at least two `for` loops — for example a row of enemies across the top and stars in the background — added to your ship.

Send a **photo or video** of your richer scene, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I used a for loop to draw …
>
> The counter `i` helped me spread them out by …
>
> I chose the spacing … so that …
>
> My second loop draws …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your patterned scene. Talk through it like you are teaching someone. Try to use these words: **for loop**, **range**, **counter**, **pattern**, **spacing**.

> 1. Show your row of enemies and your stars.
> 2. Read one for loop out loud and say how many times it runs.
> 3. Explain how `i` makes each item land in a different spot.
> 4. Change the count or spacing live and show the difference.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
