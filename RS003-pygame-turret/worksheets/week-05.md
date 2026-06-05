# 🔫 RS003 Week 5 — English Worksheet

**Topic:** Add the Gun with a Function · **Course:** Pygame Turret · **Time:** about 45 minutes

This week you add a **gun barrel** to your turret and wrap the whole turret in a **function** called `draw_turret`. Then you give the function a **parameter** so you can draw the same turret at any X position you like.

> 🧠 Words to know: **function**, **define (`def`)**, **call**, **parameter**, **line (barrel)**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
def draw_turret():
    pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 30, HEIGHT - 80, 60, 40))
    pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 80), (CENTER_X, HEIGHT - 140), 8)
```

**This defines a function but does not run it yet. What two shapes will it draw when it IS called?**

<div class="write-space"></div>

```python
screen.fill(SKY)
draw_turret()
pygame.display.flip()
```

**Now the function is called. When does the turret actually appear?**

<div class="write-space"></div>

```python
def draw_turret(x):
    pygame.draw.rect(screen, DARK_GREEN, (x - 30, HEIGHT - 80, 60, 40))

draw_turret(200)
draw_turret(400)
draw_turret(600)
```

**The function now takes `x`. How many turrets appear, and where?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and find the barrel

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SKY = (135, 206, 235)
DARK_GREEN = (0, 100, 0)
GRAY = (80, 80, 80)
BLACK = (0, 0, 0)

def draw_turret():
    pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 30, HEIGHT - 80, 60, 40))
    pygame.draw.circle(screen, BLACK, (CENTER_X, HEIGHT - 80), 10)
    pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 80), (CENTER_X, HEIGHT - 150), 10)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SKY)
    draw_turret()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Where does the barrel point? What two points does the `line` connect?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The turret function is written but nothing appears on screen.

```python
def draw_turret():
    pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 30, HEIGHT - 80, 60, 40))

screen.fill(SKY)
pygame.display.flip()
```

**Hint:** a function only runs when you **call** it.

**Write the fixed code (show the loop body):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The barrel is supposed to stand **up** from the base. Right now it lies flat sideways.

```python
pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 80), (CENTER_X + 60, HEIGHT - 80), 10)
```

**Hint:** to go up, the second point needs a **smaller** Y, not a bigger X.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should draw three turrets at 200, 400, and 600, but Python gives an error about a missing argument.

```python
def draw_turret(x):
    pygame.draw.rect(screen, DARK_GREEN, (x - 30, HEIGHT - 80, 60, 40))

draw_turret()
```

**Hint:** the function needs an `x` value when you call it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Give the function a position parameter

Change `draw_turret()` so it takes an `x`, and use `x` everywhere the position appears instead of `CENTER_X`.

**Write your new function header line (the `def ...` line):**

<div class="write-space"></div>

### 🎯 Draw a whole row of turrets

Call your function three times with different X values to make a row.

**Write the three calls you used:**

<div class="write-space"></div>

**Hint:** `draw_turret(200)` draws one turret centred at X = 200. Change the number for each one.

---

## 5 · Make It 📸

### 🎯 Build a turret you can place anywhere

Build a program that:

1. has a `draw_turret(x)` function with a base, a pivot, and a barrel,
2. is called inside the game loop,
3. draws at least one turret on screen.

Send a **photo or video** of your turret, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I wrapped my turret in a function called …
>
> I gave it a parameter so that …
>
> The barrel points up because the second point has …
>
> To draw more than one turret, I …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your turret. Talk through it like you are teaching someone. Try to use these words: **function**, **define**, **call**, **parameter**, **barrel**.

> 1. Show your turret with its barrel.
> 2. Read your `def draw_turret(x)` line out loud and explain the parameter.
> 3. Point at where you **call** the function.
> 4. Change the X value live and show the turret move.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
