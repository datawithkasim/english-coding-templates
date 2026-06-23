# 🏆 RS003 Week 16 — English Worksheet

**Topic:** Polish — Missiles, Sprites, High Score, and Show & Tell · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This is the final week. You add the **polish** that makes a game feel finished: a second weapon (**missiles** with the M key) that hits harder, a **high score** that remembers your best, a restart key, and best of all you swap your drawn shapes for real **PNG sprites** loaded from image files. Then you present your finished game.

> 🧠 Words to know: **missile**, **sprite**, **image.load**, **high score**, **restart**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
ship_img = pygame.image.load("ship.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()
screen.blit(ship_img, (ship_x - ship_img.get_width() // 2, ship_y))
```

**These lines load picture files and put them on screen. What replaces your drawn rectangles and triangles?**

<div class="write-space"></div>

```python
if event.key == pygame.K_m:
    missiles.append([ship_x, ship_y - 20])
```

**Pressing M fires a missile instead of a bullet. Why might a game want a second, stronger weapon?**

<div class="write-space"></div>

```python
high_score = 0
if event.key == pygame.K_r and game_over:
    if score > high_score:
        high_score = score
    score = 0
    game_over = False
```

**Pressing R restarts the game. When does the high score update?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and fire both weapons

> 💡 For the sprite version below you need two small picture files saved next to your code: `ship.png` and `enemy.png`. If you finished the **AI Art** extension, use those. No images yet? Use the drawn shapes from week 15 and add `ship.png`/`enemy.png` once you have them.

```python
import pygame, random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 72)
clock = pygame.time.Clock()

SPACE = (10, 12, 40); WHITE = (255, 255, 255)
RED = (230, 60, 60); YELLOW = (255, 210, 40); GREY = (120, 120, 140)

ship_img = pygame.image.load("ship.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()

ship_x, ship_y = WIDTH // 2, HEIGHT - 100
SPEED = 5
bullets = []          # each: [x, y]
missiles = []         # each: [x, y]
enemies = []          # each: {"x","y","type","points"}
effects = []          # each: [x, y, timer]
score = 0
high_score = 0
spawn_timer = 0
game_over = False
start_time = pygame.time.get_ticks()
GAME_TIME = 30000

running = True
while running:
    elapsed = pygame.time.get_ticks() - start_time
    time_left = max(0, (GAME_TIME - elapsed) // 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullets.append([ship_x, ship_y - 20])
            if event.key == pygame.K_m and not game_over:
                missiles.append([ship_x, ship_y - 20])
            if event.key == pygame.K_r and game_over:
                if score > high_score:
                    high_score = score
                score = 0
                enemies.clear()
                start_time = pygame.time.get_ticks()
                game_over = False

    if time_left == 0:
        game_over = True

    if not game_over:
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
        for mi in missiles: mi[1] -= 4

        for e in enemies[:]:
            for b in bullets[:]:
                if abs(b[0] - e["x"]) < 22 and abs(b[1] - e["y"]) < 22:
                    score += e["points"]
                    effects.append([e["x"], e["y"], 8])
                    if e in enemies: enemies.remove(e)
                    if b in bullets: bullets.remove(b)
            for mi in missiles[:]:
                if abs(mi[0] - e["x"]) < 30 and abs(mi[1] - e["y"]) < 30:
                    score += e["points"] * 2
                    effects.append([e["x"], e["y"], 12])
                    if e in enemies: enemies.remove(e)
                    if mi in missiles: missiles.remove(mi)

        bullets = [b for b in bullets if b[1] > -10]
        missiles = [m for m in missiles if m[1] > -10]
        enemies = [e for e in enemies if e["y"] < HEIGHT + 20]

    screen.fill(SPACE)
    for b in bullets:   pygame.draw.rect(screen, YELLOW, (b[0] - 2, b[1] - 8, 4, 12))
    for mi in missiles: pygame.draw.rect(screen, WHITE, (mi[0] - 4, mi[1] - 12, 8, 18))
    for e in enemies:   screen.blit(enemy_img, (e["x"] - enemy_img.get_width() // 2, e["y"] - enemy_img.get_height() // 2))
    for fx in effects:  pygame.draw.circle(screen, YELLOW, (fx[0], fx[1]), fx[2])
    effects = [[x, y, t - 1] for x, y, t in effects if t > 1]
    screen.blit(ship_img, (ship_x - ship_img.get_width() // 2, ship_y))
    screen.blit(font.render(f"Score: {score}   Time: {time_left}   Best: {high_score}", True, WHITE), (10, 10))

    if game_over:
        screen.blit(big_font.render("GAME OVER", True, RED), (WIDTH // 2 - 160, HEIGHT // 2 - 60))
        screen.blit(font.render(f"Final: {score}    Press R to restart", True, WHITE), (WIDTH // 2 - 200, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Play one round. What is different about firing M instead of SPACE, what do the sprites look like, and what does R do?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The sprite is supposed to show your `ship.png` picture, but the program crashes saying it cannot find the file.

```python
ship_img = pygame.image.load("ship.png")
```

**Hint:** the picture file must be saved in the **same folder** as your code, with the exact name. Also use `.convert_alpha()` so the see-through background stays see-through.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The high score should remember your best across rounds, but it resets to 0 every restart.

```python
if event.key == pygame.K_r and game_over:
    high_score = 0
    score = 0
    game_over = False
```

**Hint:** before resetting, compare the score to the best so far.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — After the timer hits 0, the player should not be able to keep flying or firing, but the game keeps playing.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    ship_x -= SPEED
```

**Hint:** movement should only run while the game is not over.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

---

## 4 · Modify It 🔧

### 🎯 Tune your two weapons

A missile is worth `e["points"] * 2` and travels slower. Change those numbers — make missiles faster, slower, or worth even more.

**Write what you changed about the bullet and the missile:**

<div class="write-space"></div>

### 🎯 Add a difficulty or a title screen

Pick one polish idea: a start screen before the game, or Easy/Hard modes that change the spawn speed or the timer.

**Describe what you added and how it changes the game:**

<div class="write-space"></div>

**Hint:** a title screen is just another `game_state` — show text and wait for a key before starting the timer.

---

## 5 · Make It 🎤

### 🎯 Finish your game and prepare your show & tell

Finish your polished game with two weapons, PNG sprites, a high score, and restart. Then get ready to present it.

Use these sentence starters for your presentation notes — write 4 to 6 sentences total.

> My game is called …
>
> The function I am most proud of is … because …
>
> My favourite polish feature is …
>
> The hardest bug I solved was …
>
> I fixed it by …
>
> The next thing I would add is …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Final Video 🎥

Take a video of your finished game from start to game over to restart. Talk through it like you are presenting to the class. Try to use these words: **missile**, **sprite**, **image.load**, **high score**, **restart**.

> 1. Play a full round, firing both bullets and missiles, and let the timer run out.
> 2. Show the game-over screen and the high score.
> 3. Press R and show it restart.
> 4. Explain how you loaded your PNG sprites and one bug you fixed.

**Write what you will say in your video.** Plan it here before you record — this is your show & tell.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your full-play video + your show & tell notes to teacher on KakaoTalk.
