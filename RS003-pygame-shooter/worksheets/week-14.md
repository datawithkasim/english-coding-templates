# 📊 RS003 Week 14 — English Worksheet

**Topic:** A HUD and Enemy Types · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week your game shows a **score and timer** on screen (a HUD) and has **several enemies** at once, each a different type. Each enemy is a dictionary with its own position, type, and points — aliens are worth 1 point and meteors are worth 3.

> 🧠 Words to know: **HUD**, **score**, **timer**, **list of dictionaries**, **enemy type**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
font = pygame.font.SysFont(None, 32)
score_text = font.render(f"Score: {score}", True, (255, 255, 255))
screen.blit(score_text, (10, 10))
```

**These three lines put text on screen. What does the player see in the top-left corner?**

<div class="write-space"></div>

```python
enemies = []
for i in range(3):
    kind = random.choice(["alien", "meteor"])
    points = 1 if kind == "alien" else 3
    enemies.append({"x": random.randint(150, WIDTH - 150), "y": 120, "type": kind, "points": points})
```

**How many enemies are made? What is different about each one?**

<div class="write-space"></div>

```python
score = score + hit["points"]
```

**Score goes up by the enemy's `points`. An alien is worth 1 and a meteor is worth 3. Which gives more points?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and watch the score

```python
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

RED = (230, 60, 60)
GREY = (120, 120, 140)

def new_enemy():
    kind = random.choice(["alien", "meteor"])
    points = 1 if kind == "alien" else 3
    return {"x": random.randint(150, WIDTH - 150), "y": 120, "type": kind, "points": points}

enemies = [new_enemy() for i in range(3)]

def draw_enemy(e):
    color = RED if e["type"] == "alien" else GREY
    pygame.draw.rect(screen, color, (e["x"] - 18, e["y"] - 18, 36, 36))

def draw_hud(score, time_left):
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Time: {time_left}", True, (255, 255, 255)), (WIDTH - 150, 10))

def get_aimed_enemy(ship_x):
    for e in enemies:
        if abs(ship_x - e["x"]) < 22:
            return e
    return None

ship_x = CENTER_X
ship_y = HEIGHT - 100
score = 0
start_time = pygame.time.get_ticks()
GAME_DURATION = 30000

running = True
while running:
    elapsed = pygame.time.get_ticks() - start_time
    time_left = max(0, (GAME_DURATION - elapsed) // 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hit = get_aimed_enemy(ship_x)
            if hit:
                score = score + hit["points"]
                new = new_enemy()
                hit["x"], hit["type"], hit["points"] = new["x"], new["type"], new["points"]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 100:
        ship_x -= 6
    if keys[pygame.K_RIGHT] and ship_x < WIDTH - 100:
        ship_x += 6

    screen.fill((10, 12, 40))
    for e in enemies:
        draw_enemy(e)
    pygame.draw.rect(screen, (80, 220, 255), (ship_x - 20, ship_y, 40, 50))
    pygame.draw.polygon(screen, (255, 255, 255), [(ship_x, ship_y - 20), (ship_x - 20, ship_y), (ship_x + 20, ship_y)])
    aimed = get_aimed_enemy(ship_x)
    laser_color = (255, 210, 40) if aimed else (230, 60, 60)
    pygame.draw.line(screen, laser_color, (ship_x, ship_y - 20), (ship_x, 120), 4)
    draw_hud(score, time_left)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Line up under an alien and press SPACE, then a meteor. Which gave you more points? What does the timer do?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The score is supposed to appear on screen, but the number never shows up.

```python
score_text = font.render(f"Score: {score}", True, (255, 255, 255))
```

**Hint:** rendering the text is not enough — it must be put on the screen.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Hitting a meteor should give more points than an alien, but every enemy gives the same score.

```python
score = score + 1
```

**Hint:** the score should depend on the enemy's type.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Pressing SPACE on empty space should do nothing, but the program crashes when you miss.

```python
hit = get_aimed_enemy(ship_x)
score = score + hit["points"]
```

**Hint:** when nothing is lined up, `hit` is `None`, and `None["points"]` is an error.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Add more enemies

Change `range(3)` so more enemies appear at once.

**Write the new number you chose and how the game feels with more enemies:**

<div class="write-space"></div>

### 🎯 Change the game length

Change `GAME_DURATION` to make the round longer or shorter (it is in milliseconds, so 30000 is 30 seconds).

**Write the new duration you chose and what 1000 milliseconds equals in seconds:**

<div class="write-space"></div>

**Hint:** keep the enemies inside `150` to `WIDTH - 150` so they never spawn off screen or under the HUD.

---

## 5 · Make It 📸

### 🎯 Build a scored shooting game

Build a program where:

1. several enemies appear at once,
2. a HUD shows score and time,
3. meteors are worth more than aliens,
4. missing does not crash the game.

Send a **video** of 30 seconds of play, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I stored my enemies as a list of …
>
> My HUD shows … in the corner.
>
> Meteors give more points because …
>
> I stopped misses from crashing by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of a full 30-second round. Talk through it like you are teaching someone. Try to use these words: **HUD**, **score**, **timer**, **dictionary**, **enemy type**.

> 1. Show the HUD with score and time changing.
> 2. Hit an alien and a meteor, and say the point difference.
> 3. Read the line that renders the score out loud.
> 4. Show what happens when you miss.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your 30-second play video to teacher on KakaoTalk.
