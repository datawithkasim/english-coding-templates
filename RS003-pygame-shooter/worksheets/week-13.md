# 🧩 RS003 Week 13 — English Worksheet

**Topic:** Many Cooperating Functions · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week your game was split into **several small functions** — one for the starfield, one for the ship, one for an enemy, one for the aiming laser. In this worksheet you will read that code, think about what it does, and explain it in your own words. The laser changes colour when the ship lines up under the enemy.

> 🧠 Words to know: **function**, **call**, **share a value**, **enemy**, **laser**

---

## 1 · Predict 🔮

Read each piece of code and write what you think will happen. You do not run anything — just read and think.

```python
def draw_stars():
    for i in range(40):
        pygame.draw.circle(screen, WHITE, (i * 20 + 10, 30), 2)

def draw_ship(ship_x):
    ...

draw_stars()
draw_ship(CENTER_X)
```

**`draw_stars` takes no input but `draw_ship` takes a `ship_x`. Why does only one of them need a value?**

<div class="write-space"></div>

```python
def draw_laser(ship_x):
    distance = abs(ship_x - ENEMY_X)
    color = YELLOW if distance < 20 else RED
    pygame.draw.line(screen, color, (ship_x, HEIGHT - 120), (ship_x, ENEMY_Y), 4)
```

**`abs(ship_x - ENEMY_X)` is how far the ship is from the enemy. When does the laser turn yellow?**

<div class="write-space"></div>

```python
draw_stars()
draw_enemy()
draw_ship(ship_x)
draw_laser(ship_x)
```

**Four functions are called in a row. Which one is drawn last, and what does that mean for what sits in front?**

<div class="write-space"></div>

```python
draw_ship(ship_x)
draw_laser(ship_x)
```

**Both functions are given the same `ship_x`. How do these two functions share the ship's position?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Write the fixed code, then explain why the original was wrong.

**Bug A** — The laser should follow the ship, but it is stuck in the centre and never moves.

```python
def draw_laser():
    pygame.draw.line(screen, RED, (CENTER_X, HEIGHT - 140), (CENTER_X, ENEMY_Y), 4)
```

**Hint:** the laser needs the ship's position passed in.

**Write the fixed code (the whole function):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The ship should sit **in front of** the laser, but right now the laser is drawn last and covers the ship.

```python
draw_stars()
draw_enemy()
draw_ship(ship_x)
draw_laser(ship_x)
```

**Hint:** whatever is drawn last sits on top.

**Write the fixed code (calls in the right order):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The laser is supposed to turn yellow only when the ship is **close** to lined up, but it is yellow everywhere.

```python
distance = ship_x - ENEMY_X
color = YELLOW if distance < 20 else RED
```

**Hint:** without `abs`, a big negative distance is also "less than 20".

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working program carefully. You do not run it — just read it and answer the questions about it.

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
YELLOW = (255, 210, 40)

ENEMY_X = 600
ENEMY_Y = 120

def draw_stars():
    for i in range(40):
        pygame.draw.circle(screen, WHITE, (i * 20 + 10, 30), 2)

def draw_ship(ship_x):
    pygame.draw.rect(screen, CYAN, (ship_x - 20, HEIGHT - 120, 40, 50))
    pygame.draw.polygon(screen, WHITE, [(ship_x, HEIGHT - 140), (ship_x - 20, HEIGHT - 120), (ship_x + 20, HEIGHT - 120)])

def draw_enemy():
    pygame.draw.rect(screen, RED, (ENEMY_X - 18, ENEMY_Y - 18, 36, 36))

def draw_laser(ship_x):
    distance = abs(ship_x - ENEMY_X)
    color = YELLOW if distance < 20 else RED
    pygame.draw.line(screen, color, (ship_x, HEIGHT - 140), (ship_x, ENEMY_Y), 4)

ship_x = CENTER_X
SPEED = 5
MIN_X, MAX_X = 100, WIDTH - 100

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > MIN_X:
        ship_x -= SPEED
    if keys[pygame.K_RIGHT] and ship_x < MAX_X:
        ship_x += SPEED

    screen.fill(SPACE)
    draw_stars()
    draw_enemy()
    draw_laser(ship_x)
    draw_ship(ship_x)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Which four functions does this program have, and what does each one draw?**

<div class="write-space"></div>

**How does `draw_laser` know where the ship is right now?**

<div class="write-space"></div>

**Inside the loop, `draw_laser(ship_x)` is called before `draw_ship(ship_x)`. Why does that order matter?**

<div class="write-space"></div>

**The `MIN_X` and `MAX_X` lines keep `ship_x` between 100 and 700. What would go wrong if they were missing?**

<div class="write-space"></div>

**The line `color = YELLOW if distance < 20 else RED` decides the laser colour. In plain words, what does this line say?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own code that splits the game into functions. Now record a short video on your phone explaining **the code you wrote**. You may show your result running while you talk. Try to use these words: **function**, **call**, **share**, **enemy**, **laser**.

> 1. Read your function names out loud and say what each one draws.
> 2. Explain how the ship position is **shared** between your functions.
> 3. Point at the line that decides the laser colour, and say when it turns yellow.
> 4. Show the laser lining up under the enemy if you can.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
