# 🏆 RS003 Week 16 — English Worksheet

**Topic:** Polish — Missiles, Sprites, High Score, and Show & Tell · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This is the final week. In this worksheet you think about and explain the **polish** that makes a game feel finished: a second weapon (**missiles** with the M key) that hits harder, a **high score** that remembers your best, a restart key, and real **PNG sprites** loaded from image files. Then you present and explain the finished game you built across the whole course.

> 🧠 Words to know: **missile**, **sprite**, **image.load**, **high score**, **restart**

---

## 1 · Predict 🔮

Read each piece of code. Write what you think it does. You do not need to run anything — just read and think.

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

```python
for mi in missiles[:]:
    if abs(mi[0] - e["x"]) < 30 and abs(mi[1] - e["y"]) < 30:
        score += e["points"] * 2
```

**A missile gives `e["points"] * 2`. How many points does a 3-point meteor give when a missile hits it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Write the fixed code, then explain why the original was wrong.

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

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read the central loop from this week's finished game. The full program is long, so this is the key part — the part that fires both weapons, loads the sprites, and handles restart. Read it carefully and answer the questions below. You do not need to run it.

```python
ship_img = pygame.image.load("ship.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()

for event in pygame.event.get():
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

for b in bullets: b[1] -= 8
for mi in missiles: mi[1] -= 4

for e in enemies[:]:
    for b in bullets[:]:
        if abs(b[0] - e["x"]) < 22 and abs(b[1] - e["y"]) < 22:
            score += e["points"]
            if e in enemies: enemies.remove(e)
            if b in bullets: bullets.remove(b)
    for mi in missiles[:]:
        if abs(mi[0] - e["x"]) < 30 and abs(mi[1] - e["y"]) < 30:
            score += e["points"] * 2
            if e in enemies: enemies.remove(e)
            if mi in missiles: missiles.remove(mi)

screen.blit(enemy_img, (e["x"] - enemy_img.get_width() // 2, e["y"] - enemy_img.get_height() // 2))
screen.blit(ship_img, (ship_x - ship_img.get_width() // 2, ship_y))
```

**Which line loads the ship picture, and what does `.convert_alpha()` do for it?**

<div class="write-space"></div>

**The bullet moves with `b[1] -= 8` and the missile with `mi[1] -= 4`. Which one moves faster up the screen, and how do you know?**

<div class="write-space"></div>

**A bullet hit gives `score += e["points"]` but a missile hit gives `score += e["points"] * 2`. Why is the missile worth more?**

<div class="write-space"></div>

**The R key only works `if ... game_over`. Why should restart only work when the game is over?**

<div class="write-space"></div>

**`screen.blit(ship_img, ...)` puts a picture on screen. How is `blit` different from `pygame.draw.rect`?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

This is your **show & tell**. Present the finished game **you** built across this whole course. Make a phone video: show the game running from start to game over to restart, and explain the key parts of your code out loud. Try to use these words: **missile**, **sprite**, **image.load**, **high score**, **restart**.

> 1. Play a full round, firing both bullets and missiles, and let the timer run out.
> 2. Show the game-over screen and your high score, then press R and show it restart.
> 3. Point to the line that uses `image.load` and explain how you loaded your PNG sprites.
> 4. Tell us the part of your code you are most proud of and one bug you fixed.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your finished-game presentation video to teacher on KakaoTalk.
