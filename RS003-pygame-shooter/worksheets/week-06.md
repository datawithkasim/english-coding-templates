# 🚀 RS003 Week 6 — English Worksheet

**Topic:** A Fleet of Ships — Many Parameters · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week one function makes a whole **fleet of different ships**. You give `draw_ship` more parameters — position, colour, and size — so a single function can draw a small green scout, a big red boss ship, and a blue one, all at once.

> 🧠 Words to know: **parameter**, **argument**, **default value**, **keyword argument**, **scale (size)**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

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

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and compare the three ships

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

**Describe the three ships — their colour, size, and position:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

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

## 4 · Modify It 🔧

### 🎯 Line up five ships in different colours

Call `draw_ship` five times across the screen, each with a different colour.

**Write your five calls:**

<div class="write-space"></div>

### 🎯 Make the middle one the boss

Use the `size` parameter to make one ship clearly bigger than the rest.

**Write the call for your boss ship and the size you gave it:**

<div class="write-space"></div>

**Hint:** a `size` above 1 makes it bigger; below 1 makes it smaller. Spread the X values evenly so they do not overlap.

---

## 5 · Make It 📸

### 🎯 Build your own ship fleet

Build a program that:

1. has a `draw_ship(x, color, size)` function,
2. draws several ships in a row,
3. uses different colours and at least two different sizes.

Send a **photo or video** of your fleet, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I added parameters for …
>
> I gave `size` a default value so that …
>
> My boss ship is bigger because …
>
> I used `int(...)` to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your ship fleet. Talk through it like you are teaching someone. Try to use these words: **parameter**, **argument**, **default value**, **keyword argument**, **scale**.

> 1. Show your row of ships.
> 2. Read one function call out loud and name each argument.
> 3. Explain what the default value of `size` does.
> 4. Point at your boss ship and say what makes it bigger.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
