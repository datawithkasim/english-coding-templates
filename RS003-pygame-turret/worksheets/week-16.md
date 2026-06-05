# 🏆 RS003 Week 16 — English Worksheet

**Topic:** Polish — Sound, High Score, and Show & Tell · **Course:** Pygame Turret · **Time:** about 45 minutes

This is the final week. You add the **polish** that makes a game feel finished: a sound when you shoot, a sound when you hit, a **game-over screen**, a **high score** that remembers your best, and a restart key. Then you present your finished game.

> 🧠 Words to know: **sound**, **game state**, **game over**, **high score**, **restart**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

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
if time_left == 0:
    game_over = True
if not game_over:
    keys = pygame.key.get_pressed()
    ...
```

**When `game_over` is True, the movement code is skipped. What does the player notice when the timer hits 0?**

<div class="write-space"></div>

```python
shoot_sound.play()
if abs(gun_x - target_x) < 25:
    hit_sound.play()
```

**Two different sounds can play. When do you hear each one?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and listen

```python
import pygame
import random
import array, math
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

def make_beep(frequency, duration_ms):
    sample_rate = 22050
    n = int(sample_rate * duration_ms / 1000)
    buf = array.array("h")
    amp = 16000
    for i in range(n):
        val = int(amp * math.sin(2 * math.pi * frequency * i / sample_rate))
        buf.append(val)
        buf.append(val)
    return pygame.mixer.Sound(buffer=buf.tobytes())

shoot_sound = make_beep(220, 50)
hit_sound = make_beep(880, 100)

gun_x = CENTER_X
target_x = random.randint(150, WIDTH - 150)
score = 0
high_score = 0
start_time = pygame.time.get_ticks()
GAME_TIME = 30000
game_over = False

running = True
while running:
    elapsed = pygame.time.get_ticks() - start_time
    time_left = max(0, (GAME_TIME - elapsed) // 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                shoot_sound.play()
                if abs(gun_x - target_x) < 25:
                    hit_sound.play()
                    score = score + 1
                    target_x = random.randint(150, WIDTH - 150)
            if event.key == pygame.K_r and game_over:
                if score > high_score:
                    high_score = score
                score = 0
                start_time = pygame.time.get_ticks()
                game_over = False

    if time_left == 0:
        game_over = True
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and gun_x > 100:
            gun_x -= 6
        if keys[pygame.K_RIGHT] and gun_x < WIDTH - 100:
            gun_x += 6

    screen.fill((135, 206, 235))
    pygame.draw.rect(screen, (0, 100, 0), (0, HEIGHT - 50, WIDTH, 50))
    pygame.draw.circle(screen, (200, 0, 0), (target_x, HEIGHT - 200), 25)
    pygame.draw.circle(screen, (255, 255, 0), (target_x, HEIGHT - 200), 10)
    pygame.draw.rect(screen, (0, 100, 0), (CENTER_X - 30, HEIGHT - 90, 60, 40))
    pygame.draw.line(screen, (80, 80, 80), (CENTER_X, HEIGHT - 90), (gun_x, HEIGHT - 200), 10)
    pygame.draw.circle(screen, (255, 0, 0), (gun_x, HEIGHT - 200), 8)
    screen.blit(font.render(f"Score: {score}   Time: {time_left}   Best: {high_score}", True, (0, 0, 0)), (10, 10))

    if game_over:
        screen.blit(big_font.render("GAME OVER", True, (255, 0, 0)), (WIDTH // 2 - 160, HEIGHT // 2 - 60))
        screen.blit(font.render(f"Final: {score}    Press R to restart", True, (255, 255, 255)), (WIDTH // 2 - 200, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Play one round. What sounds do you hear, what happens at 0 seconds, and what does R do?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The high score should remember your best across rounds, but it resets to 0 every restart.

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

**Bug B** — After the timer hits 0, the player should not be able to keep moving or scoring, but the game keeps playing.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and gun_x > 100:
    gun_x -= 6
```

**Hint:** movement should only run while the game is not over.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The shoot sound is supposed to play only when you actually fire, but it plays nonstop.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    shoot_sound.play()
```

**Hint:** `get_pressed` is true every frame the key is held. Use the `KEYDOWN` event for one play per press.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Make your own sounds

Change the frequency numbers in `make_beep(...)`. Lower numbers are deeper; higher numbers are sharper.

**Write the two frequencies you chose for shoot and hit:**

<div class="write-space"></div>

### 🎯 Add a difficulty or a title screen

Pick one polish idea: a start screen before the game, or Easy/Hard modes that change the target size or time.

**Describe what you added and how it changes the game:**

<div class="write-space"></div>

**Hint:** a title screen is just another `game_state` — show text and wait for a key before starting the timer.

---

## 5 · Make It 🎤

### 🎯 Finish your game and prepare your show & tell

Finish your polished game with sound, a game-over screen, a high score, and restart. Then get ready to present it.

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

Take a video of your finished game from start to game over to restart. Talk through it like you are presenting to the class. Try to use these words: **sound**, **game state**, **game over**, **high score**, **restart**.

> 1. Play a full round and let the timer run out.
> 2. Show the game-over screen and the high score.
> 3. Press R and show it restart.
> 4. Explain your favourite function and one bug you fixed.

**Write what you will say in your video.** Plan it here before you record — this is your show & tell.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your full-play video + your show & tell notes to teacher on KakaoTalk.
