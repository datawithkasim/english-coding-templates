# 🚀 RS003 Week 6 — English Worksheet

**Topic:** A Fleet of Ships — Many Parameters · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week is about thinking and talking about code, not typing it in the app. One function makes a whole **fleet of different ships**: you give `draw_ship` more parameters — position, colour, and size — so a single function can draw a small green scout, a big red boss ship, and a blue one, all at once. You will predict, debug, and explain code, then explain the code you wrote in today's lesson.

> 🧠 Words to know: **parameter**, **argument**, **default value**, **keyword argument**, **scale (size)**

---

## 1 · Predict 🔮

Read each piece of code. Do not run anything — just write what you think will happen.

```python
def draw_ship(x, body_color, size=1):
    ...
```

**This function takes three parameters. Which one has a default value, and what does that mean when you call the function?**

<div class="write-space"></div>

```python
draw_ship(200, GREEN, size=0.8)
draw_ship(400, RED, size=1.2)
draw_ship(600, BLUE, size=0.8)
```

**Three ships are drawn. Which one is the biggest? Which one is in the middle?**

<div class="write-space"></div>

```python
w = int(40 * size)
```

**If `size` is 1.2, what does `int(40 * size)` work out to? Why is `int(...)` needed?**

<div class="write-space"></div>

```python
draw_ship(400, RED)
```

**Here `size` is left out. What size will this ship be, and how do you know?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken.

**Bug A** — This should draw a ship in any colour, but every ship comes out the same colour no matter what you pass in.

```python
def draw_ship(x, body_color, size=1):
    pygame.draw.rect(screen, GREEN, (x - 20, HEIGHT - 120, 40, 50))
```

**Hint:** the function ignores its own `body_color` parameter.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should make a ship 1.2 times bigger, but Python crashes with an error about needing a whole number.

```python
w = 40 * size
pygame.draw.rect(screen, body_color, (x, HEIGHT - 120, w, 50))
```

**Hint:** `40 * 1.2` is a decimal. Pygame sizes must be whole numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — You want most ships to stay normal size without typing `size=1` every time, but right now leaving size out causes an error.

```python
def draw_ship(x, body_color, size):
    ...

draw_ship(400, RED)
```

**Hint:** give `size` a default value so it can be left out.

**Write the fixed code (just the `def` line):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working example carefully. You do not need to run it — just answer the questions about how it works.

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SPACE = (10, 12, 40)
WHITE = (255, 255, 255)
GREEN = (60, 200, 120)
RED = (230, 60, 60)
BLUE = (80, 140, 255)

def draw_ship(x, body_color, size=1):
    w = int(40 * size)
    h = int(50 * size)
    nose = int(20 * size)
    y = HEIGHT - 120
    pygame.draw.rect(screen, body_color, (x - w // 2, y, w, h))
    pygame.draw.polygon(screen, WHITE, [(x, y - nose), (x - w // 2, y), (x + w // 2, y)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SPACE)
    draw_ship(200, GREEN, size=0.8)
    draw_ship(400, RED, size=1.2)
    draw_ship(600, BLUE, size=0.8)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**What are the three parameters of `draw_ship`, and which one has a default value?**

<div class="write-space"></div>

**Look at `w = int(40 * size)`. Why does a bigger `size` make a wider ship?**

<div class="write-space"></div>

**In `draw_ship(400, RED, size=1.2)`, name each argument and say which parameter it goes to.**

<div class="write-space"></div>

**Why can the same `draw_ship` function draw three different ships? What changes each time?**

<div class="write-space"></div>

**The `pygame.draw.polygon` line draws the white nose. How does it use `size` to stay the right shape?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own ship-fleet code. Record a short video on your phone explaining that code in your own words. You may show your fleet running on screen. Try to use these words: **parameter**, **argument**, **default value**, **keyword argument**, **scale**.

> 1. Show your row of ships.
> 2. Read one of your function calls out loud and name each argument.
> 3. Explain what the default value of `size` does in your code.
> 4. Point at your boss ship and say what makes it bigger.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
