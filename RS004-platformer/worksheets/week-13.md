# 👾 RS004 Week 13 — English Worksheet

**Topic:** Enemies & Game Over · **Course:** Platformer Game · **Time:** about 45 minutes

This week your game gets **enemies**. You build an `Enemy` **class** that patrols left and right on its own. Touching an enemy triggers **Game Over**, and pressing **R** restarts. A `game_state` variable decides what the game is doing.

> Keep these words handy: **class**, **patrol**, **game_state**, **Game Over**, **restart (R)**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

## 4 · Populate & Polish 🛠️

Start from your working enemies.

1. Add a second enemy with a *different* patrol range. Write its `Enemy(...)` line.

<div class="write-space"></div>

2. Change an enemy's speed. Does a faster enemy make the level harder or just annoying?

<div class="write-space"></div>

3. **Stretch:** show the final score on the Game Over screen. Where do you draw it?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Add patrolling enemies to your own level. Place at least three, and make sure the level is still clearable.

When it works, send a **photo or video** showing you dodging enemies *and* a Game Over, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, my `Enemy` class patrols by …
>
> The `direction` flips when …
>
> Touching an enemy sets `game_state` to …
>
> I restart with R by …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video showing dodging, dying, and restarting. Teach it to someone new. Try to use these words: **class**, **patrol**, **game_state**, **Game Over**, **restart**.

> 1. Show an enemy patrolling back and forth.
> 2. Dodge one, then touch one and trigger Game Over.
> 3. Read the patrol `update` out loud and explain the direction flip.
> 4. Press R and show the restart.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
