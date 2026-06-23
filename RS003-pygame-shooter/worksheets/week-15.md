# 🎮 RS003 Week 15 — English Worksheet

**Topic:** Put It All Together — Fire at Falling Enemies · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week everything you have learned comes together into one **playable mini game**. Constants, for loops, functions, ship movement, falling enemies, and a score — all in a single program. Enemies fall from the top; press SPACE to fire a bullet; a hit scores a point and makes a flash.

> 🧠 Words to know: **integrate**, **hit detection**, **bullet**, **score**, **hit effect**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    bullets.append([ship_x, ship_y - 20])
```

**Pressing SPACE adds a bullet to a list. What two numbers does each bullet remember?**

<div class="write-space"></div>

```python
for e in enemies[:]:
    for b in bullets[:]:
        if abs(b[0] - e["x"]) < 22 and abs(b[1] - e["y"]) < 22:
            score += e["points"]
            effects.append([e["x"], e["y"], 8])
            enemies.remove(e)
            bullets.remove(b)
```

**A bullet hits an enemy when it is close in both X and Y. What three things happen on a hit?**

<div class="write-space"></div>

```python
for fx in effects:
    pygame.draw.circle(screen, YELLOW, (fx[0], fx[1]), fx[2])
effects = [[x, y, t - 1] for x, y, t in effects if t > 1]
```

**Each effect is a yellow circle with a timer. What does the flash look like as the timer counts down?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and shoot an enemy

```python
import pygame, random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

SPACE = (10, 12, 40); WHITE = (255, 255, 255); CYAN = (80, 220, 255)
RED = (230, 60, 60); YELLOW = (255, 210, 40); GREY = (120, 120, 140)

def draw_ship(x, y):
    pygame.draw.rect(screen, CYAN, (x - 20, y, 40, 50))
    pygame.draw.polygon(screen, WHITE, [(x, y - 20), (x - 20, y), (x + 20, y)])

def draw_enemy(e):
    color = RED if e["type"] == "alien" else GREY
    pygame.draw.rect(screen, color, (e["x"] - 18, e["y"] - 18, 36, 36))

ship_x, ship_y = WIDTH // 2, HEIGHT - 100
SPEED = 5
bullets = []          # each: [x, y]
enemies = []          # each: {"x","y","type","points"}
effects = []          # each: [x, y, timer]   hit flash
score = 0
spawn_timer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([ship_x, ship_y - 20])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  ship_x -= SPEED
    if keys[pygame.K_RIGHT]: ship_x += SPEED
    if keys[pygame.K_UP]:    ship_y -= SPEED
    if keys[pygame.K_DOWN]:  ship_y += SPEED
    ship_x = max(20, min(WIDTH - 20, ship_x))
    ship_y = max(20, min(HEIGHT - 60, ship_y))

    spawn_timer += 1
    if spawn_timer >= 40:
        spawn_timer = 0
        kind = random.choice(["alien", "meteor"])
        points = 1 if kind == "alien" else 3
        enemies.append({"x": random.randint(40, WIDTH - 40), "y": -20, "type": kind, "points": points})

    for e in enemies: e["y"] += 2
    for b in bullets: b[1] -= 8

    for e in enemies[:]:
        for b in bullets[:]:
            if abs(b[0] - e["x"]) < 22 and abs(b[1] - e["y"]) < 22:
                score += e["points"]
                effects.append([e["x"], e["y"], 8])
                if e in enemies: enemies.remove(e)
                if b in bullets: bullets.remove(b)

    bullets = [b for b in bullets if b[1] > -10]
    enemies = [e for e in enemies if e["y"] < HEIGHT + 20]

    screen.fill(SPACE)
    for b in bullets:  pygame.draw.rect(screen, YELLOW, (b[0] - 2, b[1] - 8, 4, 12))
    for e in enemies:  draw_enemy(e)
    for fx in effects: pygame.draw.circle(screen, YELLOW, (fx[0], fx[1]), fx[2])
    effects = [[x, y, t - 1] for x, y, t in effects if t > 1]
    draw_ship(ship_x, ship_y)
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Fly under a falling enemy and press SPACE. What happens to the score and the enemy, and what flash do you see?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — Pressing SPACE should fire one bullet per press, but right now it fires a huge stream of bullets and the game slows down.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    bullets.append([ship_x, ship_y - 20])
```

**Hint:** `get_pressed` is true every frame the key is down. A `KEYDOWN` event fires once per press.

**Write the fixed code (use the event instead):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — When a bullet hits an enemy, the enemy should disappear and you score, but the enemy stays and you can score off it forever.

```python
if abs(b[0] - e["x"]) < 22 and abs(b[1] - e["y"]) < 22:
    score += e["points"]
```

**Hint:** the enemy and the bullet are never removed after a hit.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Bullets fly **up** the screen, but right now they move down instead.

```python
for b in bullets:
    b[1] += 8
```

**Hint:** up means the Y position should get smaller.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Make the game easier or harder

Change the `< 22` hit distance. A bigger number is more forgiving; a smaller number needs precise aim. You can also change how often enemies spawn (`>= 40`).

**Write the values you chose and whether it made the game easier or harder:**

<div class="write-space"></div>

### 🎯 Add one feature from an earlier week

Bring back something you built before — the falling starfield, the boost speed, the screen shake — into the final game.

**Write which feature you added and which week it came from:**

<div class="write-space"></div>

**Hint:** you already wrote that code. Copy the part you need and place it in the right spot in the game loop.

---

## 5 · Make It 📸

### 🎯 Build your full mini game

Build a program that:

1. uses constants, a list, and functions,
2. flies the ship and stays on screen,
3. spawns falling enemies and fires bullets,
4. scores a point and shows a flash on each hit.

Send a **photo or video** of you scoring, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I brought together my … from earlier weeks.
>
> A point is scored when …
>
> After a hit, the enemy …
>
> The feature I am most proud of is …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of you playing and scoring. Talk through it like you are teaching someone. Try to use these words: **integrate**, **hit detection**, **bullet**, **score**, **hit effect**.

> 1. Fire at a falling enemy and score a point.
> 2. Read the hit-detection line out loud and explain it.
> 3. Point at where the hit flash is made.
> 4. Name two earlier-week ideas you can see in this game.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your scoring video to teacher on KakaoTalk.
