# 🎮 RS003 Week 15 — English Worksheet

**Topic:** Put It All Together — Fire at Falling Enemies · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week everything you have learned comes together into one **playable mini game**: constants, for loops, functions, ship movement, falling enemies, bullets, and a score. In this worksheet you will think about that code and explain it — no typing in the app.

> 🧠 Words to know: **integrate**, **hit detection**, **bullet**, **score**, **hit effect**

---

## 1 · Predict 🔮

Read each piece of code. Write what you think it does. Do not run anything.

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

```python
spawn_timer += 1
if spawn_timer >= 40:
    spawn_timer = 0
    kind = random.choice(["alien", "meteor"])
    points = 1 if kind == "alien" else 3
    enemies.append({"x": random.randint(40, WIDTH - 40), "y": -20, "type": kind, "points": points})
```

**A new enemy appears every 40 frames. Why is a meteor worth more points than an alien?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Write the fixed code, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Here is the heart of the final mini game. Read it carefully, then answer the questions. Reading only — do not run it.

```python
ship_x, ship_y = WIDTH // 2, HEIGHT - 100
SPEED = 5
bullets = []          # each: [x, y]
enemies = []          # each: {"x","y","type","points"}
effects = []          # each: [x, y, timer]   hit flash
score = 0
spawn_timer = 0

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

    screen.fill(SPACE)
    for b in bullets:  pygame.draw.rect(screen, YELLOW, (b[0] - 2, b[1] - 8, 4, 12))
    for e in enemies:  draw_enemy(e)
    for fx in effects: pygame.draw.circle(screen, YELLOW, (fx[0], fx[1]), fx[2])
    effects = [[x, y, t - 1] for x, y, t in effects if t > 1]
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
```

**Why are `bullets`, `enemies`, and `effects` all lists instead of single variables?**

<div class="write-space"></div>

**The line `for e in enemies: e["y"] += 2` runs every frame. What does it make the enemies do?**

<div class="write-space"></div>

**Look at the two loops `for e in enemies[:]` and `for b in bullets[:]`. Why does the code check every bullet against every enemy?**

<div class="write-space"></div>

**What does `score += e["points"]` add to the score, and why is it `e["points"]` and not just `+ 1`?**

<div class="write-space"></div>

**The score is drawn with `font.render(f"Score: {score}", ...)`. What part of that line makes the number change on the screen?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the code **you** wrote in today's lesson. Record a short video on your phone (you can show the game running) and talk through it like you are teaching someone. Try to use these words: **integrate**, **hit detection**, **bullet**, **score**, **hit effect**.

> 1. Show where your code fires a **bullet** when you press SPACE.
> 2. Read your **hit detection** line out loud and explain how it knows a bullet touched an enemy.
> 3. Point at where the **score** goes up and where the **hit effect** flash is made.
> 4. Name two earlier-week ideas you had to **integrate** to make the full game.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
