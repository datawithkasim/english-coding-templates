# 🔁 RS003 Week 11 — English Worksheet

**Topic:** Repeat with a For Loop · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week is about **thinking about and explaining code**. One short loop can draw **many things**. A `for` loop with `range(N)` repeats N times, and by using the loop counter `i` you can spread a **row of enemies** across the top of the screen or scatter stars across the background. You will read loops, fix broken ones, and explain the code you wrote with your teacher in the lesson.

> 🧠 Words to know: **for loop**, **range**, **counter (`i`)**, **pattern**, **spacing**

---

## 1 · Predict 🔮

Read each piece of code. Write what you think will happen in your head — no need to run anything.

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

```python
for i in range(5):
    x = 100 + (i * 150)
    pygame.draw.rect(screen, RED, (x - 18, 80, 36, 36))
```

**This draws a row of enemies near the top. Where on screen does the first enemy land, and where does the last one land?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken.

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

## 3 · Explain the Code 📖

Here is a working example. Read it carefully and answer the questions about it. You do not need to run it.

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

**How many times does the first `for` loop run, and what does each turn of the loop draw?**

<div class="write-space"></div>

**In the second loop, how many enemies are drawn, and how does `i` change where each one lands?**

<div class="write-space"></div>

**Why do the stars get drawn before the enemies? What would happen if the enemy loop came first?**

<div class="write-space"></div>

**What does `screen.fill(SPACE)` do, and why is it at the top before the loops?**

<div class="write-space"></div>

**What do you think `pygame.time.wait(3000)` does to the picture on screen?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's lesson you wrote your own loop code with your teacher. Now explain that code in a short phone video. You may show your scene running while you talk. Try to use these words: **for loop**, **range**, **counter**, **pattern**, **spacing**.

> 1. Show the code you wrote in the lesson and what appears on screen.
> 2. Read one for loop out loud and say how many times it runs.
> 3. Explain how the counter `i` makes each item land in a different spot.
> 4. Say what spacing you used and why it fits on screen.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
