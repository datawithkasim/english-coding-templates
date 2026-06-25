# 💥 RS004 Week 14 — English Worksheet

**Topic:** Vertical Patrol + Death Effect (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week is about thinking through **smarter enemies** and explaining how they work. A `patrol_type` lets one enemy walk left–right, another go up–down, and a third **chase** the player. When the player dies, a little **explosion** of particles bursts out. You will read this code closely and explain the code you wrote in your live lesson.

> 🧠 Words to know: **patrol_type**, **vertical**, **chase**, **particle**, **explosion**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it does.

```python
if self.patrol_type == "vertical":
    self.rect.y += self.direction * self.speed
    if self.rect.y > self.start_y + self.range_size:
        self.direction = -1
    if self.rect.y < self.start_y:
        self.direction = 1
```

**Which way does this enemy move? When does it turn around?**

<div class="write-space"></div>

```python
elif self.patrol_type == "chase" and player_rect is not None:
    if self.rect.x < player_rect.x:
        self.rect.x += 1
    elif self.rect.x > player_rect.x:
        self.rect.x -= 1
```

**The player is to the *right* of this enemy. Which way does it move?**

<div class="write-space"></div>

```python
for p in self.particles:
    p["x"] += p["vx"]
    p["y"] += p["vy"]
    p["vy"] += 0.3
    p["life"] -= 1
```

**Each particle has its own speed. Why does `vy` keep growing (`+= 0.3`)?**

<div class="write-space"></div>

---

## 2 · Pick the Patrol 🧭

Match each `patrol_type` to its behaviour.

```
1. "horizontal"   2. "vertical"   3. "chase"
```

```
A. moves up and down between two heights
B. follows the player when nearby
C. walks left and right between two x positions
```

**1 → ___  2 → ___  3 → ___**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — A vertical enemy should bounce between two heights. Right now it floats up forever and leaves the screen.

```python
if self.patrol_type == "vertical":
    self.rect.y += self.direction * self.speed
```

**Hint:** there is no turn-around check on the y edges.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A chasing enemy needs the player's position. Right now it crashes with a `NoneType` error.

```python
def update(self):
    if self.patrol_type == "chase":
        if self.rect.x < player_rect.x:
            self.rect.x += 1
```

**Hint:** `player_rect` must be passed in, with a safe default, and used only when it exists.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Dead particles should be removed so the explosion fades. Right now they pile up and slow the game down.

```python
for exp in explosions:
    exp.update()
    exp.draw(screen)
```

**Hint:** when an explosion `is_done()`, take it out of the list. Loop over a copy while removing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Here is a working enemy update that handles all three patrol types and takes the player's position safely.

```python
def update(self, player_rect=None):
    if self.patrol_type == "horizontal":
        self.rect.x += self.direction * self.speed
        if self.rect.x > self.start_x + self.range_size:
            self.direction = -1
        if self.rect.x < self.start_x:
            self.direction = 1

    elif self.patrol_type == "vertical":
        self.rect.y += self.direction * self.speed
        if self.rect.y > self.start_y + self.range_size:
            self.direction = -1
        if self.rect.y < self.start_y:
            self.direction = 1

    elif self.patrol_type == "chase" and player_rect is not None:
        if self.rect.x < player_rect.x:
            self.rect.x += 1
        elif self.rect.x > player_rect.x:
            self.rect.x -= 1
```

**What does `self.direction = -1` do, and when does it happen?**

<div class="write-space"></div>

**Why does the `vertical` block change `self.rect.y` instead of `self.rect.x`?**

<div class="write-space"></div>

**Why does the `chase` block check `player_rect is not None` before using it?**

<div class="write-space"></div>

**What would break if you deleted the `start_x` and `start_y` checks?**

<div class="write-space"></div>

**Tell the story of one chase frame: the player is to the left, so what happens line by line?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

In your live lesson today you wrote enemy and explosion code. Make a short phone video that explains **the code you wrote**. You may show it running. Try to use these words: **patrol_type**, **vertical**, **chase**, **particle**, **explosion**.

> 1. Point to where `patrol_type` decides how each enemy moves.
> 2. Read your chase code out loud and explain how it picks a direction.
> 3. Show the death **explosion** and explain how the **particle** loop works.
> 4. Say one part that was tricky and how you understood it.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
