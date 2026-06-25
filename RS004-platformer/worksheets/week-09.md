# 🗺️ RS004 Week 9 — English Worksheet

**Topic:** Level Design (Data, Respawn, Finish) · **Course:** Platformer Game · **Time:** about 45 minutes

This week you think about how **level data** is kept apart from the game code. A `build_level()` function turns a list of numbers into platforms, the player **respawns** at the start if it falls off, and a **finish** marker says "you cleared it!". You will read this code closely and then explain the code you wrote in today's live lesson.

> Keep these words handy: **level data**, **`build_level()`**, **respawn / start position**, **finish**, **cleared**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it does.

```python
LEVEL_1 = [
    (0, 550, 800, 50),
    (150, 450, 120, 20),
]
def build_level(level_data):
    return [pygame.Rect(*p) for p in level_data]
```

**What does `build_level(LEVEL_1)` give back? What does `*p` do?**

<div class="write-space"></div>

```python
if player.y > HEIGHT:
    player.x = start_x
    player.y = start_y
    velocity_y = 0
```

**The player falls below the bottom of the screen. What happens to it?**

<div class="write-space"></div>

```python
if player.colliderect(finish):
    cleared = True
```

**Once `cleared` is `True`, what should change about the game?**

<div class="write-space"></div>

---

## 2 · Why Separate the Data? 🤔

We keep the level as a list of numbers (`LEVEL_1`) instead of writing each `pygame.Rect(...)` by hand in the loop.

**Give one reason this makes it easier to build *many* levels later.**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it on paper so it works, then explain why the original was wrong.

**Bug A** — `build_level` should return real platforms, but the game crashes saying it got tuples, not Rects.

```python
def build_level(level_data):
    return level_data
```

**Hint:** each tuple of numbers must be turned into a `pygame.Rect`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A player who falls off should respawn at the start. Right now it keeps falling forever and never comes back.

```python
if player.y > HEIGHT:
    velocity_y = 0
```

**Hint:** resetting velocity isn't enough — move the player back to its start spot.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Touching the finish should clear the level once. Right now the "Level Clear!" text never shows.

```python
finish = pygame.Rect(710, 180, 50, 40)
if player.colliderect(player):
    cleared = True
```

**Hint:** the player is being compared with *itself*, not the finish.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working level loader closely. It keeps the level as data, builds the platforms, respawns the player, and clears the level at the finish.

```python
LEVEL_1 = [
    (0, 550, 800, 50),
    (150, 450, 120, 20),
    (400, 350, 120, 20),
]
start_x, start_y = 50, 500

def build_level(level_data):
    return [pygame.Rect(*p) for p in level_data]

platforms = build_level(LEVEL_1)
finish = pygame.Rect(710, 180, 50, 40)
cleared = False

# inside the game loop:
if player.y > HEIGHT:
    player.x = start_x
    player.y = start_y
    velocity_y = 0

if player.colliderect(finish):
    cleared = True
```

**What is stored inside `LEVEL_1`, and what does each group of four numbers describe?**

<div class="write-space"></div>

**What does `build_level(LEVEL_1)` return, and what is now inside `platforms`?**

<div class="write-space"></div>

**When does the `if player.y > HEIGHT:` block run, and what does it do to the player?**

<div class="write-space"></div>

**What has to be true for `cleared` to become `True`?**

<div class="write-space"></div>

**Why is `cleared` set to `False` at the start instead of `True`?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the code **you wrote in today's lesson**. Record a short video on your phone. You may show your level running. Try to use these words: **level data**, **build_level**, **respawn**, **finish**, **cleared**.

> 1. Show your level and point out the start and the finish.
> 2. Point to your level data and your `build_level()` and say what they do.
> 3. Fall off on purpose and show the respawn, then explain those lines.
> 4. Reach the finish and show the level clear.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
