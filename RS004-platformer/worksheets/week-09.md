# 🗺️ RS004 Week 9 — English Worksheet

**Topic:** Level Design (Data, Respawn, Finish) · **Course:** Platformer Game · **Time:** about 45 minutes

This week you separate your **level data** from your game code. A `build_level()` function turns a list of numbers into platforms, the player **respawns** at the start if it falls off, and a **finish** marker says "you cleared it!".

> Keep these words handy: **level data**, **`build_level()`**, **respawn / start position**, **finish**, **cleared**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

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

## 4 · Shape a Level 🛠️

Start from your working level loader.

1. Move one platform 60 pixels higher. Can the player still reach it with a jump? Note the result.

<div class="write-space"></div>

2. Move the finish marker somewhere harder to reach. Where did you put it?

<div class="write-space"></div>

3. **Stretch:** show a "Level Clear!" message on screen when `cleared` is true. What font size did you use?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Design **your own** level data. It should have a clear start, a path of platforms, and a finish marker. Make sure the whole level is reachable.

When it works, send a **photo or video** of a full run from start to finish, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I kept my level as data so that …
>
> `build_level()` turns the numbers into …
>
> When the player falls off, it respawns by …
>
> My finish marker is at … and the player reaches it by …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of a full clear of your level. Teach it to someone new. Try to use these words: **level data**, **build_level**, **respawn**, **finish**, **cleared**.

> 1. Show your level and point out the start and finish.
> 2. Fall off on purpose and show the respawn.
> 3. Read the respawn lines out loud and explain them.
> 4. Reach the finish and show the clear.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
