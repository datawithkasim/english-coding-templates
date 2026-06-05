# 💥 RS004 Week 14 — English Worksheet

**Topic:** Vertical Patrol + Death Effect (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week enemies get **smarter**. A `patrol_type` lets one enemy walk left–right, another go up–down, and a third **chase** the player. When the player dies, a little **explosion** of particles bursts out.

> Keep these words handy: **patrol_type**, **vertical**, **chase**, **particle**, **explosion**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

## 4 · Mix the Enemies 🛠️

Start from your working enemy types.

1. Place one of each kind in your level: horizontal, vertical, chase. Write the three `Enemy(...)` lines.

<div class="write-space tall" style="min-height: 160px"></div>

2. Give each kind a different colour or shape so the player can tell them apart. What did you choose?

<div class="write-space"></div>

3. **Stretch:** position an enemy so it guards a coin. Which coin, and which enemy?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Add all three enemy kinds to your own level, each at least once, plus the death explosion.

When it works, send a **photo or video** showing all three enemies and a death burst, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, the `patrol_type` decides …
>
> My chasing enemy follows the player by …
>
> I gave it a safe default so that …
>
> The death explosion works by …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video showing all three enemy kinds and a death. Teach it to someone new. Try to use these words: **patrol_type**, **vertical**, **chase**, **particle**, **explosion**.

> 1. Show the horizontal, vertical, and chasing enemies.
> 2. Walk near the chaser and show it follow you.
> 3. Die on purpose and show the explosion.
> 4. Read the chase code out loud and explain how it picks a direction.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
