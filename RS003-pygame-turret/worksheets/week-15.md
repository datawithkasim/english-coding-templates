# 🎮 RS003 Week 15 — English Worksheet

**Topic:** Put It All Together — Shoot with Space · **Course:** Pygame Turret · **Time:** about 45 minutes

This week everything you have learned comes together into one **playable mini game**. Constants, for loops, functions, key movement, range limits, a random target, and a score — all in a single program. Press SPACE to shoot; a hit scores a point and spawns a new target.

> 🧠 Words to know: **integrate**, **hit detection**, **respawn**, **score**, **random target**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    if abs(gun_x - target_x) < 25:
        score += 1
        target_x = random.randint(MIN_X + 50, MAX_X - 50)
```

**Pressing SPACE checks one thing before scoring. What has to be true to earn a point?**

<div class="write-space"></div>

```python
def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 50, WIDTH, 50))
    for i in range(20):
        pygame.draw.rect(screen, (50, 150, 50), (i * 40 + 10, HEIGHT - 60, 6, 15))
```

**This function uses a for loop from week 11 inside a function from week 13. What does it draw?**

<div class="write-space"></div>

```python
target_x = random.randint(MIN_X + 50, MAX_X - 50)
```

**After a hit, this runs. Where can the new target appear, and why not right at the edges?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and score a point

```python
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
SPEED = 5
MIN_X = 100
MAX_X = WIDTH - 100

SKY = (135, 206, 235)
GREEN = (0, 100, 0)
GRAY = (80, 80, 80)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turret Mini Game")
font = pygame.font.SysFont(None, 40)

def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 50, WIDTH, 50))
    for i in range(20):
        pygame.draw.rect(screen, (50, 150, 50), (i * 40 + 10, HEIGHT - 60, 6, 15))

def draw_turret(gun_x):
    pygame.draw.rect(screen, GREEN, (CENTER_X - 30, HEIGHT - 90, 60, 40))
    pygame.draw.line(screen, GRAY, (CENTER_X, HEIGHT - 90), (gun_x, HEIGHT - 200), 10)

def draw_target(tx, ty):
    pygame.draw.circle(screen, BLACK, (tx, ty), 25)
    pygame.draw.circle(screen, RED, (tx, ty), 18)
    pygame.draw.circle(screen, YELLOW, (tx, ty), 8)

def draw_marker(gun_x, tx):
    color = YELLOW if abs(gun_x - tx) < 25 else RED
    pygame.draw.circle(screen, color, (gun_x, HEIGHT - 200), 8)

def draw_score(score):
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))

gun_x = CENTER_X
target_x = random.randint(MIN_X + 50, MAX_X - 50)
target_y = HEIGHT - 200
score = 0

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if abs(gun_x - target_x) < 25:
                score += 1
                target_x = random.randint(MIN_X + 50, MAX_X - 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gun_x > MIN_X:
        gun_x -= SPEED
    if keys[pygame.K_RIGHT] and gun_x < MAX_X:
        gun_x += SPEED

    screen.fill(SKY)
    draw_ground()
    draw_target(target_x, target_y)
    draw_turret(gun_x)
    draw_marker(gun_x, target_x)
    draw_score(score)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Aim onto the target so the marker turns yellow, then press SPACE. What happens to the score and the target?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — You should only score when the marker is on the target, but pressing SPACE anywhere adds a point.

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    score += 1
    target_x = random.randint(MIN_X + 50, MAX_X - 50)
```

**Hint:** the hit check is missing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — After a hit, the target should jump to a new spot, but it stays in the same place and you can score forever without moving.

```python
if abs(gun_x - target_x) < 25:
    score += 1
```

**Hint:** the target is never moved after a hit.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Holding SPACE is supposed to fire once per press, but right now it racks up huge scores instantly when aimed on a target.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE] and abs(gun_x - target_x) < 25:
    score += 1
    target_x = random.randint(MIN_X + 50, MAX_X - 50)
```

**Hint:** `get_pressed` is true every frame the key is down. A `KEYDOWN` event fires once per press.

**Write the fixed code (use the event instead):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Make the target easier or harder to hit

Change the `< 25` hit distance. A bigger number is more forgiving; a smaller number needs precise aim.

**Write the value you chose and whether it made the game easier or harder:**

<div class="write-space"></div>

### 🎯 Add one feature from an earlier week

Bring back something you built before — twinkling stars, the boundary lines, the Shift speed boost — into the final game.

**Write which feature you added and which week it came from:**

<div class="write-space"></div>

**Hint:** you already wrote that code. Copy the part you need and place it in the right spot in the game loop.

---

## 5 · Make It 📸

### 🎯 Build your full mini game

Build a program that:

1. uses constants, a for loop, and functions,
2. moves the aim with keys and stays on screen,
3. has a random target and a score,
4. respawns the target after each hit.

Send a **photo or video** of you scoring, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I brought together my … from earlier weeks.
>
> A point is scored when …
>
> After a hit, the target …
>
> The feature I am most proud of is …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of you playing and scoring. Talk through it like you are teaching someone. Try to use these words: **integrate**, **hit detection**, **respawn**, **score**, **random**.

> 1. Aim onto the target and score a point.
> 2. Read the hit-detection line out loud and explain it.
> 3. Point at where the target respawns.
> 4. Name two earlier-week ideas you can see in this game.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your scoring video to teacher on KakaoTalk.
