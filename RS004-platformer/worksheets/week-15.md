# 🏰 RS004 Week 15 — English Worksheet

**Topic:** Multi-Level Structure · **Course:** Platformer Game · **Time:** about 45 minutes

This week your game holds **many levels**. Every level is a dictionary of platforms, coins, enemies, and a finish. A `load_level()` function sets up the current one, and reaching the finish loads the **next** — until the last one, which means **victory**.

> Keep these words handy: **levels list**, **`load_level()`**, **next level**, **victory**, **game_state**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

```python
LEVELS = [
    { "platforms": [...], "coins": [...], "enemies": [...], "finish": (...) },
    { "platforms": [...], "coins": [...], "enemies": [...], "finish": (...) },
]
```

**How many levels are in this list? How would you read the first level's coins?**

<div class="write-space"></div>

```python
def load_level(idx):
    data = LEVELS[idx]
    platforms = [pygame.Rect(*p) for p in data["platforms"]]
    ...
    return platforms, coins, enemies, finish
```

**What does `load_level(1)` set up? Why return four things at once?**

<div class="write-space"></div>

```python
if player.colliderect(finish):
    current_level += 1
    if current_level < len(LEVELS):
        platforms, coins, enemies, finish = load_level(current_level)
    else:
        game_state = "victory"
```

**The player clears the last level. Which branch runs — load or victory?**

<div class="write-space"></div>

---

## 2 · Trace the Level Flow 🔢

There are 3 levels. The player keeps reaching the finish. Fill in `current_level` and what happens.

```
start:           current_level = 0
clear level:     current_level = ___   →  loads level ___
clear again:     current_level = ___   →  loads level ___
clear again:     current_level = ___   →  game_state = ___
```

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — Reaching the finish should load the next level. Right now the player just keeps playing the same level forever.

```python
if player.colliderect(finish):
    platforms, coins, enemies, finish = load_level(current_level)
```

**Hint:** `current_level` never advances. Increase it first.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — After the last level the game should show victory. Right now it crashes with an index error when it tries to load a level that doesn't exist.

```python
if player.colliderect(finish):
    current_level += 1
    platforms, coins, enemies, finish = load_level(current_level)
```

**Hint:** check whether `current_level` is still inside the list before loading.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `load_level` should turn the data into real game objects. Right now the enemies don't move because they were never made into `Enemy` objects.

```python
def load_level(idx):
    data = LEVELS[idx]
    platforms = [pygame.Rect(*p) for p in data["platforms"]]
    coins = [pygame.Rect(c[0], c[1], 20, 20) for c in data["coins"]]
    enemies = data["enemies"]
    finish = pygame.Rect(*data["finish"])
    return platforms, coins, enemies, finish
```

**Hint:** the enemy tuples need to become `Enemy(...)` objects, like the platforms became `Rect`s.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Author Your Levels 🛠️

Start from your working multi-level loader.

1. Write the data for your **first** level (platforms, coins, enemies, finish). Reuse a level you already designed.

<div class="write-space tall" style="min-height: 180px"></div>

2. Make your **second** level a little harder than the first. What did you change to raise the difficulty?

<div class="write-space"></div>

3. **Stretch:** make level three the hardest, with a tricky final jump. Describe it.

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Build **your own** three levels that play one after another, ending in a victory screen.

When it works, send a **photo or video** clearing all three levels, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I store every level as data in `LEVELS` so that …
>
> `load_level()` sets up the current level by …
>
> When the player clears a level, the game …
>
> After the last level, the game shows …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video clearing all three levels. Teach it to someone new. Try to use these words: **levels list**, **load_level**, **next level**, **victory**, **game_state**.

> 1. Show level 1 and clear it.
> 2. Show the game loading level 2, then 3.
> 3. Read the "next level or victory" check out loud and explain it.
> 4. Reach the victory screen.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
