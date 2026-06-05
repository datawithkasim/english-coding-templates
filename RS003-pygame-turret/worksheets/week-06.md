# 🎯 RS003 Week 6 — English Worksheet

**Topic:** Three Different Turrets — Many Parameters · **Course:** Pygame Turret · **Time:** about 45 minutes

This week one function makes **many different turrets**. You give `draw_turret` more parameters — position, colour, and size — so a single function can draw a small green turret, a big red boss turret, and a blue one, all at once.

> 🧠 Words to know: **parameter**, **argument**, **default value**, **keyword argument**, **scale (size)**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
def draw_turret(x, base_color, size=1):
    ...
```

**This function takes three parameters. Which one has a default value, and what does that mean when you call the function?**

<div class="write-space"></div>

```python
draw_turret(200, GREEN, size=0.8)
draw_turret(400, RED, size=1.2)
draw_turret(600, BLUE, size=0.8)
```

**Three turrets are drawn. Which one is the biggest? Which one is in the middle?**

<div class="write-space"></div>

```python
w = int(60 * size)
```

**If `size` is 1.2, what does `int(60 * size)` work out to? Why is `int(...)` needed?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and compare the three turrets

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SKY = (135, 206, 235)
GROUND = (95, 60, 30)
GRAY = (80, 80, 80)
GREEN = (0, 100, 0)
RED = (150, 30, 30)
BLUE = (30, 60, 150)

def draw_turret(x, base_color, size=1):
    w = int(60 * size)
    h = int(40 * size)
    barrel = int(60 * size)
    pygame.draw.rect(screen, base_color, (x - w // 2, HEIGHT - 50 - h, w, h))
    pygame.draw.circle(screen, (0, 0, 0), (x, HEIGHT - 50 - h), 8)
    pygame.draw.line(screen, GRAY, (x, HEIGHT - 50 - h), (x, HEIGHT - 50 - h - barrel), int(8 * size))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SKY)
    pygame.draw.rect(screen, GROUND, (0, HEIGHT - 50, WIDTH, 50))
    draw_turret(200, GREEN, size=0.8)
    draw_turret(400, RED, size=1.2)
    draw_turret(600, BLUE, size=0.8)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Describe the three turrets — their colour, size, and position:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — This should draw a turret in any colour, but every turret comes out the same colour no matter what you pass in.

```python
def draw_turret(x, base_color, size=1):
    pygame.draw.rect(screen, GREEN, (x - 30, HEIGHT - 50, 60, 40))
```

**Hint:** the function ignores its own `base_color` parameter.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should make a turret 1.2 times bigger, but Python crashes with an error about needing a whole number.

```python
w = 60 * size
pygame.draw.rect(screen, base_color, (x, HEIGHT - 50, w, 40))
```

**Hint:** `60 * 1.2` is a decimal. Pygame sizes must be whole numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — You want most turrets to stay normal size without typing `size=1` every time, but right now leaving size out causes an error.

```python
def draw_turret(x, base_color, size):
    ...

draw_turret(400, RED)
```

**Hint:** give `size` a default value so it can be left out.

**Write the fixed code (just the `def` line):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Line up five turrets in different colours

Call `draw_turret` five times across the screen, each with a different colour.

**Write your five calls:**

<div class="write-space"></div>

### 🎯 Make the middle one the boss

Use the `size` parameter to make one turret clearly bigger than the rest.

**Write the call for your boss turret and the size you gave it:**

<div class="write-space"></div>

**Hint:** a `size` above 1 makes it bigger; below 1 makes it smaller. Spread the X values evenly so they do not overlap.

---

## 5 · Make It 📸

### 🎯 Build your own turret line-up

Build a program that:

1. has a `draw_turret(x, color, size)` function,
2. draws several turrets in a row,
3. uses different colours and at least two different sizes.

Send a **photo or video** of your line-up, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I added parameters for …
>
> I gave `size` a default value so that …
>
> My boss turret is bigger because …
>
> I used `int(...)` to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your turret line-up. Talk through it like you are teaching someone. Try to use these words: **parameter**, **argument**, **default value**, **keyword argument**, **scale**.

> 1. Show your row of turrets.
> 2. Read one function call out loud and name each argument.
> 3. Explain what the default value of `size` does.
> 4. Point at your boss turret and say what makes it bigger.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
