# 📊 RS003 Week 14 — English Worksheet

**Topic:** A HUD and Many Targets · **Course:** Pygame Turret · **Time:** about 45 minutes

This week your game shows a **score and timer** on screen (a HUD) and has **several targets** at once. Each target is a dictionary with its own position, size, and colour, and smaller targets are worth more points.

> 🧠 Words to know: **HUD**, **score**, **timer**, **list of dictionaries**, **render text**

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
targets = []
for i in range(3):
    targets.append({"x": random.randint(150, WIDTH - 150), "y": HEIGHT - 200, "size": random.choice([15, 25, 35])})
```

**How many targets are made? What is different about each one?**

<div class="write-space"></div>

```python
score = score + (50 // hit["size"])
```

**Score goes up by `50 // size`. A small target has size 15, a big one has size 35. Which gives more points?**

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

targets = []
for i in range(3):
    targets.append({"x": random.randint(150, WIDTH - 150), "y": HEIGHT - 200, "size": random.choice([15, 25, 35]), "color": random.choice([(255, 50, 50), (50, 255, 50), (255, 200, 50)])})

def draw_target(t):
    pygame.draw.circle(screen, (0, 0, 0), (t["x"], t["y"]), t["size"] + 3)
    pygame.draw.circle(screen, t["color"], (t["x"], t["y"]), t["size"])

def draw_hud(score, time_left):
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Time: {time_left}", True, (255, 255, 255)), (WIDTH - 150, 10))

def get_aimed_target(gun_x):
    for t in targets:
        if abs(gun_x - t["x"]) < t["size"]:
            return t
    return None

gun_x = CENTER_X
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
            hit = get_aimed_target(gun_x)
            if hit:
                score = score + (50 // hit["size"])
                hit["x"] = random.randint(150, WIDTH - 150)
                hit["size"] = random.choice([15, 25, 35])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gun_x > 100:
        gun_x -= 6
    if keys[pygame.K_RIGHT] and gun_x < WIDTH - 100:
        gun_x += 6

    screen.fill((30, 30, 60))
    pygame.draw.rect(screen, (50, 80, 50), (0, HEIGHT - 50, WIDTH, 50))
    for t in targets:
        draw_target(t)
    pygame.draw.rect(screen, (0, 100, 0), (CENTER_X - 30, HEIGHT - 90, 60, 40))
    aimed = get_aimed_target(gun_x)
    marker_color = (255, 255, 0) if aimed else (200, 0, 0)
    pygame.draw.line(screen, (80, 80, 80), (CENTER_X, HEIGHT - 90), (gun_x, HEIGHT - 200), 10)
    pygame.draw.circle(screen, marker_color, (gun_x, HEIGHT - 200), 8)
    draw_hud(score, time_left)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Aim at the smallest target and press SPACE, then a big one. Which gave you more points? What does the timer do?**

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

**Bug B** — Hitting a small target should give more points than a big one, but every target gives the same score.

```python
score = score + 5
```

**Hint:** the score should depend on the target's size.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Pressing SPACE on empty space should do nothing, but the program crashes when you miss.

```python
hit = get_aimed_target(gun_x)
score = score + (50 // hit["size"])
```

**Hint:** when nothing is aimed at, `hit` is `None`, and `None["size"]` is an error.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Add more targets

Change `range(3)` so more targets appear at once.

**Write the new number you chose and how the game feels with more targets:**

<div class="write-space"></div>

### 🎯 Change the game length

Change `GAME_DURATION` to make the round longer or shorter (it is in milliseconds, so 30000 is 30 seconds).

**Write the new duration you chose and what 1000 milliseconds equals in seconds:**

<div class="write-space"></div>

**Hint:** keep the targets inside `150` to `WIDTH - 150` so they never spawn off screen or under the HUD.

---

## 5 · Make It 📸

### 🎯 Build a scored shooting game

Build a program where:

1. several targets appear at once,
2. a HUD shows score and time,
3. smaller targets are worth more,
4. missing does not crash the game.

Send a **video** of 30 seconds of play, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I stored my targets as a list of …
>
> My HUD shows … in the corner.
>
> Small targets give more points because …
>
> I stopped misses from crashing by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of a full 30-second round. Talk through it like you are teaching someone. Try to use these words: **HUD**, **score**, **timer**, **dictionary**, **render**.

> 1. Show the HUD with score and time changing.
> 2. Hit a small target and a big one, and say the point difference.
> 3. Read the line that renders the score out loud.
> 4. Show what happens when you miss.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your 30-second play video to teacher on KakaoTalk.
