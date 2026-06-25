# 🚀 RS003 Week 5 — English Worksheet

**Topic:** Wrap the Ship in a Function · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you think about how a spaceship gets wrapped in a **function** called `draw_ship`, and how a **parameter** lets you draw the same ship at any X position. You read the code, predict it, fix it, and explain it in your own words.

> 🧠 Words to know: **function**, **define (`def`)**, **call**, **parameter**, **polygon (nose)**

---

## 1 · Predict 🔮

Read each piece of code. Just by reading it, write what you think will happen. Do not run anything.

```python
def draw_ship():
    pygame.draw.rect(screen, CYAN, (CENTER_X - 20, HEIGHT - 80, 40, 50))
    pygame.draw.polygon(screen, WHITE, [(CENTER_X, HEIGHT - 100), (CENTER_X - 20, HEIGHT - 80), (CENTER_X + 20, HEIGHT - 80)])
```

**This defines a function but does not run it yet. What two shapes will it draw when it IS called?**

<div class="write-space"></div>

```python
screen.fill(SPACE)
draw_ship()
pygame.display.flip()
```

**Now the function is called. When does the ship actually appear?**

<div class="write-space"></div>

```python
def draw_ship(x):
    pygame.draw.rect(screen, CYAN, (x - 20, HEIGHT - 80, 40, 50))

draw_ship(200)
draw_ship(400)
draw_ship(600)
```

**The function now takes `x`. How many ships appear, and where?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Read it, write the fixed code, then explain why the original was wrong.

**Bug A** — The ship function is written but nothing appears on screen.

```python
def draw_ship():
    pygame.draw.rect(screen, CYAN, (CENTER_X - 20, HEIGHT - 80, 40, 50))

screen.fill(SPACE)
pygame.display.flip()
```

**Hint:** a function only runs when you **call** it.

**Write the fixed code (show the loop body):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The nose is supposed to point **up** from the body. Right now its tip is below the body so it points down.

```python
pygame.draw.polygon(screen, WHITE, [(CENTER_X, HEIGHT - 60), (CENTER_X - 20, HEIGHT - 80), (CENTER_X + 20, HEIGHT - 80)])
```

**Hint:** to point up, the tip point needs a **smaller** Y than the two base points.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should draw a ship at X = 400, but Python gives an error about a missing argument.

```python
def draw_ship(x):
    pygame.draw.rect(screen, CYAN, (x - 20, HEIGHT - 80, 40, 50))

draw_ship()
```

**Hint:** the function needs an `x` value when you call it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this whole program carefully. Then answer the questions about it in your own words. You do not need to run it.

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

def draw_ship():
    pygame.draw.rect(screen, CYAN, (CENTER_X - 20, HEIGHT - 80, 40, 50))
    pygame.draw.polygon(screen, WHITE, [(CENTER_X, HEIGHT - 100), (CENTER_X - 20, HEIGHT - 80), (CENTER_X + 20, HEIGHT - 80)])
    pygame.draw.rect(screen, RED, (CENTER_X - 16, HEIGHT - 30, 8, 10))
    pygame.draw.rect(screen, RED, (CENTER_X + 8, HEIGHT - 30, 8, 10))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SPACE)
    draw_ship()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**What does the word `def` tell Python to do on the `draw_ship` line?**

<div class="write-space"></div>

**Inside `draw_ship`, which line draws the nose? Where does the nose point, and what three points does the `polygon` connect?**

<div class="write-space"></div>

**The two `RED` rectangles are the thrusters. How can you tell from the code that there are two of them?**

<div class="write-space"></div>

**Which single line inside the loop *calls* the function so the ship actually gets drawn?**

<div class="write-space"></div>

**If you deleted the line `draw_ship()` from the loop but kept the `def draw_ship()` block, what would you see on screen and why?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own `draw_ship` code. Now record a short video on your phone explaining the code **you** wrote. You may show it running. Try to use these words: **function**, **define**, **call**, **parameter**, **nose**.

> 1. Show your ship and point at its nose.
> 2. Read your `def draw_ship(x)` line out loud and explain what the parameter does.
> 3. Point at the line where you **call** the function.
> 4. Explain what changes when you give a different X value.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
