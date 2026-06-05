# 🧩 RS003 Week 13 — English Worksheet

**Topic:** A Second Function · **Course:** Pygame Turret · **Time:** about 45 minutes

This week you split your game into **several small functions** — one for the ground, one for the turret, one for a target, one for the aim marker. The functions work together by sharing the gun's X position, and the marker changes colour when the aim lines up with the target.

> 🧠 Words to know: **function**, **call**, **share a value**, **target**, **marker**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 50, WIDTH, 50))

def draw_turret(gun_x):
    ...

draw_ground()
draw_turret(CENTER_X)
```

**`draw_ground` takes no input but `draw_turret` takes a `gun_x`. Why does only one of them need a value?**

<div class="write-space"></div>

```python
def draw_marker(gun_x):
    distance = abs(gun_x - TARGET_X)
    color = YELLOW if distance < 20 else RED
    pygame.draw.circle(screen, color, (gun_x, HEIGHT - 200), 8)
```

**`abs(gun_x - TARGET_X)` is how far the aim is from the target. When does the marker turn yellow?**

<div class="write-space"></div>

```python
draw_ground()
draw_target()
draw_turret(gun_x)
draw_marker(gun_x)
```

**Four functions are called in a row. Which one is drawn last, and what does that mean for what sits in front?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and line up the target

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SKY = (135, 206, 235)
GREEN = (0, 100, 0)
GRAY = (80, 80, 80)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

TARGET_X = 600
TARGET_Y = HEIGHT - 200

def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 50, WIDTH, 50))

def draw_turret(gun_x):
    pygame.draw.rect(screen, GREEN, (CENTER_X - 30, HEIGHT - 90, 60, 40))
    pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 90), (gun_x, HEIGHT - 200), 10)

def draw_target():
    pygame.draw.circle(screen, BLACK, (TARGET_X, TARGET_Y), 25)
    pygame.draw.circle(screen, RED, (TARGET_X, TARGET_Y), 18)
    pygame.draw.circle(screen, YELLOW, (TARGET_X, TARGET_Y), 8)

def draw_marker(gun_x):
    distance = abs(gun_x - TARGET_X)
    color = YELLOW if distance < 20 else RED
    pygame.draw.circle(screen, color, (gun_x, HEIGHT - 200), 8)

gun_x = CENTER_X
SPEED = 5
MIN_X, MAX_X = 100, WIDTH - 100

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gun_x > MIN_X:
        gun_x -= SPEED
    if keys[pygame.K_RIGHT] and gun_x < MAX_X:
        gun_x += SPEED

    screen.fill(SKY)
    draw_ground()
    draw_target()
    draw_turret(gun_x)
    draw_marker(gun_x)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Aim slowly toward the target. What happens to the marker colour as you get close?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The marker should follow the gun, but it is stuck in the centre and never moves.

```python
def draw_marker():
    pygame.draw.circle(screen, RED, (CENTER_X, HEIGHT - 200), 8)
```

**Hint:** the marker needs the gun's position passed in.

**Write the fixed code (the whole function):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The target should sit **behind** the marker, but right now the target circle covers the marker so you cannot see when you are aiming on it.

```python
draw_ground()
draw_turret(gun_x)
draw_marker(gun_x)
draw_target()
```

**Hint:** whatever is drawn last sits on top.

**Write the fixed code (calls in the right order):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The marker is supposed to turn yellow only when the aim is **close** to the target, but it is yellow everywhere.

```python
distance = gun_x - TARGET_X
color = YELLOW if distance < 20 else RED
```

**Hint:** without `abs`, a big negative distance is also "less than 20".

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Move the target somewhere new

Change `TARGET_X` so the target sits in a different spot, then aim at it.

**Write the new TARGET_X you chose:**

<div class="write-space"></div>

### 🎯 Add a fourth function of your own

Write one more small function — for example `draw_score()` or `draw_clouds()` — and call it in the loop.

**Write your function name and what it draws:**

<div class="write-space"></div>

**Hint:** a function is just a name for a group of drawing lines. If it needs a changing value (like the gun position), pass it in as a parameter.

---

## 5 · Make It 📸

### 🎯 Build a game split into functions

Build a program where:

1. the ground, turret, target, and marker are each their own function,
2. the functions share the gun's position,
3. the marker changes colour when you aim on the target.

Send a **photo or video** of your aimed-on target, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I split my code into functions for …
>
> The functions share the gun position by …
>
> The marker turns yellow when …
>
> I used `abs(...)` to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while you aim onto the target. Talk through it like you are teaching someone. Try to use these words: **function**, **call**, **share**, **target**, **marker**.

> 1. Show the marker turning yellow on the target.
> 2. Read your function names out loud and say what each one draws.
> 3. Explain how the gun position is shared between functions.
> 4. Point at the line that decides the marker colour.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
