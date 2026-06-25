# 👾 RS004 Week 13 — English Worksheet

**Topic:** Enemies & Game Over · **Course:** Platformer Game · **Time:** about 45 minutes

This week is about **enemies**. You will read and think about an `Enemy` **class** that patrols left and right on its own, how touching an enemy triggers **Game Over**, and how pressing **R** restarts. A `game_state` variable decides what the game is doing. Then you will explain the code you wrote in today's live lesson.

> Keep these words handy: **class**, **patrol**, **game_state**, **Game Over**, **restart (R)**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it does.

```python
def update(self):
    self.rect.x = self.rect.x + self.direction * self.speed
    if self.rect.x > self.start_x + self.range_x:
        self.direction = -1
    if self.rect.x < self.start_x:
        self.direction = 1
```

**The enemy reaches the right end of its range. What happens to `direction`?**

<div class="write-space"></div>

```python
if player.colliderect(enemy.rect):
    game_state = "gameover"
```

**The player touches an enemy. What does the game switch to?**

<div class="write-space"></div>

```python
elif game_state == "gameover":
    if keys[pygame.K_r]:
        player.x = start_x
        player.y = start_y
        game_state = "playing"
```

**The game is over and R is pressed. What resets, and what does the game become?**

<div class="write-space"></div>

---

## 2 · Read the Class 🏷️

An `Enemy` is created with `Enemy(300, 530, 40, 40, 200)`. Match each value.

```
1. 300   2. 530   3. 40   4. 40   5. 200
```

```
A. patrol range (how far it walks)
B. start x
C. start y
D. width
E. height
```

**1 → ___  2 → ___  3 → ___  4 → ___  5 → ___**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — The enemy should walk back and forth. Right now it walks off the right side and never comes back.

```python
def update(self):
    self.rect.x = self.rect.x + self.speed
```

**Hint:** there is no `direction`, so it only ever moves one way. It needs to flip at the edges.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Movement should stop once the game is over. Right now the player keeps moving on the Game Over screen.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.x -= PLAYER_SPEED
if keys[pygame.K_RIGHT]:
    player.x += PLAYER_SPEED
for enemy in enemies:
    enemy.update()
    if player.colliderect(enemy.rect):
        game_state = "gameover"
```

**Hint:** wrap the play logic so it only runs when `game_state == "playing"`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — R should restart the game, but pressing it does nothing.

```python
if game_state == "gameover":
    player.x = start_x
    player.y = start_y
    game_state = "playing"
```

**Hint:** this restarts every frame with no key check. Only restart when R is pressed.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Here is a working enemy setup, just like the one from class. Read it carefully, then answer the questions.

```python
class Enemy:
    def __init__(self, start_x, start_y, width, height, range_x):
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.start_x = start_x
        self.range_x = range_x
        self.direction = 1
        self.speed = 2

    def update(self):
        self.rect.x = self.rect.x + self.direction * self.speed
        if self.rect.x > self.start_x + self.range_x:
            self.direction = -1
        if self.rect.x < self.start_x:
            self.direction = 1

enemies = [Enemy(300, 530, 40, 40, 200)]

if game_state == "playing":
    for enemy in enemies:
        enemy.update()
        if player.colliderect(enemy.rect):
            game_state = "gameover"
```

**Which line saves where the enemy started, and why does the patrol need it?**

<div class="write-space"></div>

**What does `self.direction = 1` mean, and what is happening when it becomes `-1`?**

<div class="write-space"></div>

**Why does every enemy go inside the `for enemy in enemies:` loop?**

<div class="write-space"></div>

**What turns the game into Game Over, and on which line does it happen?**

<div class="write-space"></div>

**Why is all of this wrapped inside `if game_state == "playing":`?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the code **you** wrote in today's lesson. Make a short phone video walking through your own game. You may show it running. Try to use these words: **class**, **patrol**, **game_state**, **Game Over**, **restart**.

> 1. Show your `Enemy` class and read the `update` out loud.
> 2. Explain how `direction` flips so the enemy patrols back and forth.
> 3. Touch an enemy and show `game_state` turn to Game Over.
> 4. Press R and explain how the restart resets the game.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
