# 🔁 RS003 Week 11 — English Worksheet

**Topic:** Repeat with a For Loop · **Course:** Pygame Turret · **Time:** about 45 minutes

This week one short loop draws **many things**. A `for` loop with `range(N)` repeats N times, and by using the loop counter `i` you can spread stars across the sky or grass blades across the ground. Your scene gets a lot richer with very little code.

> 🧠 Words to know: **for loop**, **range**, **counter (`i`)**, **pattern**, **spacing**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
for i in range(5):
    x = 100 + (i * 150)
    pygame.draw.circle(screen, WHITE, (x, 100), 10)
```

**The loop runs 5 times. What are the X values for each circle? `i` is 0, 1, 2, 3, 4.**

<div class="write-space"></div>

```python
for i in range(20):
    x = i * 40 + 10
    pygame.draw.rect(screen, LIGHT_GREEN, (x, HEIGHT - 60, 6, 15))
```

**How many grass blades appear? How far apart is each one?**

<div class="write-space"></div>

```python
for i in range(5):
    pygame.draw.circle(screen, WHITE, (100, 100), 10)
```

**This loop never uses `i` in the position. What goes wrong with the picture?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and count the stars

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
SKY = (135, 206, 235)
DARK_GREEN = (0, 100, 0)
LIGHT_GREEN = (50, 150, 50)

screen.fill(SKY)

for i in range(5):
    x = 100 + (i * 150)
    pygame.draw.circle(screen, WHITE, (x, 100), 10)

pygame.draw.rect(screen, DARK_GREEN, (0, HEIGHT - 50, WIDTH, 50))
for i in range(20):
    x = i * 40 + 10
    pygame.draw.rect(screen, LIGHT_GREEN, (x, HEIGHT - 60, 6, 15))

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
```

**How many stars are in the sky? How many grass blades on the ground?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — This should draw 5 stars spread across the sky, but all 5 land on top of each other in one spot.

```python
for i in range(5):
    x = 100
    pygame.draw.circle(screen, WHITE, (x, 100), 10)
```

**Hint:** `x` is the same every time. Use `i` to spread them out.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should draw 10 grass blades, but only one appears.

```python
i = 0
x = i * 40 + 10
pygame.draw.rect(screen, LIGHT_GREEN, (x, HEIGHT - 60, 6, 15))
```

**Hint:** there is no loop at all — it only runs once.

**Write the fixed code using a for loop:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The stars are supposed to fit on screen, but some are drawn way off the right edge where you cannot see them.

```python
for i in range(20):
    x = i * 200
    pygame.draw.circle(screen, WHITE, (x, 100), 10)
```

**Hint:** `i * 200` gets bigger than the screen width very fast. Use a smaller gap or fewer stars.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Change how many and how far apart

Change `range(5)` to draw more stars, and change the spacing number so they fit nicely.

**Write the range and spacing you chose:**

<div class="write-space"></div>

### 🎯 Add the stars and grass to your turret game

Open your turret game from an earlier week and add a star loop and a grass loop to the background.

**Describe where you put the loops in your game loop and what changed on screen:**

<div class="write-space"></div>

**Hint:** draw the background loops **after** `screen.fill(...)` but **before** the turret, so the turret sits in front.

---

## 5 · Make It 📸

### 🎯 Fill your scene with a pattern

Build a scene that uses at least two `for` loops — for example stars in the sky and grass on the ground — added to your turret.

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

> 1. Show your stars and grass.
> 2. Read one for loop out loud and say how many times it runs.
> 3. Explain how `i` makes each item land in a different spot.
> 4. Change the count or spacing live and show the difference.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
