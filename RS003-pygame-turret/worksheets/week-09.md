# 🚧 RS003 Week 9 — English Worksheet

**Topic:** Keep the Aim Inside the Screen · **Course:** Pygame Turret · **Time:** about 45 minutes

This week you stop the barrel from flying off the screen. You set a **minimum** and **maximum** X with constants, then use comparisons (`<`, `>`) to keep the aim inside. The trick of forcing a value back inside a range is called **clamping**.

> 🧠 Words to know: **minimum / maximum**, **compare (`<`, `>`)**, **clamp**, **boundary**, **limit**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
MIN_X = 50
MAX_X = WIDTH - 50
if keys[pygame.K_LEFT] and gun_tip_x > MIN_X:
    gun_tip_x -= SPEED
```

**The gun only moves left if two things are true. When does it stop moving left?**

<div class="write-space"></div>

```python
if gun_tip_x < MIN_X:
    gun_tip_x = MIN_X
if gun_tip_x > MAX_X:
    gun_tip_x = MAX_X
```

**This runs AFTER the gun moves. What does it do if the gun went too far left or too far right?**

<div class="write-space"></div>

```python
pygame.draw.line(screen, RED, (MIN_X, 0), (MIN_X, HEIGHT), 2)
pygame.draw.line(screen, RED, (MAX_X, 0), (MAX_X, HEIGHT), 2)
```

**Two vertical red lines are drawn. What do they show the player?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and hit the walls

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

MIN_X = 50
MAX_X = WIDTH - 50
gun_tip_x = CENTER_X
SPEED = 5
RED = (200, 0, 0)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gun_tip_x > MIN_X:
        gun_tip_x -= SPEED
    if keys[pygame.K_RIGHT] and gun_tip_x < MAX_X:
        gun_tip_x += SPEED

    screen.fill((135, 206, 235))
    pygame.draw.line(screen, RED, (MIN_X, 0), (MIN_X, HEIGHT), 2)
    pygame.draw.line(screen, RED, (MAX_X, 0), (MAX_X, HEIGHT), 2)
    pygame.draw.rect(screen, (0, 100, 0), (CENTER_X - 30, HEIGHT - 80, 60, 40))
    pygame.draw.line(screen, (80, 80, 80), (CENTER_X, HEIGHT - 80), (gun_tip_x, HEIGHT - 200), 10)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Aim all the way left, then all the way right. Where does the barrel stop? What stops it?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The gun should not move past the left wall, but it flies right off the left edge of the screen.

```python
if keys[pygame.K_LEFT]:
    gun_tip_x -= SPEED
```

**Hint:** there is no check that the gun is still past `MIN_X`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The clamp is supposed to pull the gun back if it goes too far, but the comparisons are backwards so it teleports to the wrong wall.

```python
if gun_tip_x > MIN_X:
    gun_tip_x = MIN_X
if gun_tip_x < MAX_X:
    gun_tip_x = MAX_X
```

**Hint:** if the gun is **smaller** than MIN_X it went too far left. Check the directions.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The right boundary line is supposed to sit a little inside the right edge, but it is drawn off the screen and you cannot see it.

```python
MAX_X = WIDTH + 50
```

**Hint:** the screen ends at `WIDTH`. To sit inside, the boundary must be a bit **less** than that.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Make the play area narrower

Change `MIN_X` and `MAX_X` so the gun has a smaller space to aim in.

**Write the new values you chose:**

<div class="write-space"></div>

### 🎯 Try the clamp method instead of the guard method

Right now the example checks `> MIN_X` before moving. Rewrite it so the gun moves freely, then a clamp pulls it back inside afterwards.

**Write your clamp lines:**

<div class="write-space"></div>

**Hint:** both methods keep the gun inside. The clamp lets it move first, then snaps it back if it went too far.

---

## 5 · Make It 📸

### 🎯 Build a turret that stays on screen

Build a program where:

1. the barrel aims left and right,
2. it can never leave the screen,
3. red boundary lines show where the limits are.

Send a **photo or video** showing the gun stopping at both walls, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I set MIN_X and MAX_X to …
>
> The gun stops on the left because …
>
> The gun stops on the right because …
>
> Clamping means …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while the gun hits both walls. Talk through it like you are teaching someone. Try to use these words: **minimum**, **maximum**, **compare**, **clamp**, **boundary**.

> 1. Aim into the left wall and show it stop.
> 2. Aim into the right wall and show it stop.
> 3. Read one boundary check out loud and explain it.
> 4. Say what would happen with no limits at all.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
