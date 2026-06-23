# ✨ RS003 Week 12 — English Worksheet

**Topic:** A Falling Starfield and Dropping Meteors · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week your background **moves**. Stars fall down the screen to make it feel like the ship is rushing forward, wrapping back to the top when they leave the bottom, and meteors drift down at different speeds. You store each star and meteor as a small **dictionary** of facts and loop over a **list** of them every frame.

> 🧠 Words to know: **list**, **dictionary**, **fall**, **wrap-around**, **speed**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
stars = []
for i in range(80):
    stars.append({"x": random.randint(0, WIDTH), "y": random.randint(0, HEIGHT), "speed": random.randint(1, 4)})
```

**This builds a list of 80 stars. What three facts does each star remember?**

<div class="write-space"></div>

```python
star["y"] = star["y"] + star["speed"]
if star["y"] > HEIGHT:
    star["y"] = 0
```

**Each star moves down a little every frame. What happens when a star goes off the bottom edge?**

<div class="write-space"></div>

```python
meteor["y"] = meteor["y"] + meteor["speed"]
pygame.draw.circle(screen, (120, 120, 140), (meteor["x"], int(meteor["y"])), meteor["size"])
```

**Each meteor falls down at its own speed and each has a different `size`. What do the meteors look like together?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and watch it fall

```python
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

stars = []
for i in range(80):
    stars.append({"x": random.randint(0, WIDTH), "y": random.randint(0, HEIGHT), "speed": random.randint(1, 4)})

meteors = []
for i in range(5):
    meteors.append({"x": random.randint(0, WIDTH), "y": random.randint(-200, 0), "speed": random.uniform(1.0, 3.0), "size": random.randint(15, 30)})

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 12, 40))

    for star in stars:
        star["y"] = star["y"] + star["speed"]
        if star["y"] > HEIGHT:
            star["y"] = 0
            star["x"] = random.randint(0, WIDTH)
        pygame.draw.circle(screen, (255, 255, 255), (star["x"], star["y"]), 2)

    for meteor in meteors:
        meteor["y"] = meteor["y"] + meteor["speed"]
        if meteor["y"] > HEIGHT + meteor["size"]:
            meteor["y"] = -meteor["size"]
            meteor["x"] = random.randint(0, WIDTH)
        pygame.draw.circle(screen, (120, 120, 140), (meteor["x"], int(meteor["y"])), meteor["size"])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Watch for 10 seconds. Describe what the stars do and what the meteors do:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — All the stars are supposed to fall at different speeds, but instead they all fall together in a solid wall.

```python
stars.append({"x": random.randint(0, WIDTH), "y": random.randint(0, HEIGHT), "speed": 2})
```

**Hint:** every star has the same `speed`, so they all move the same.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Stars should keep falling forever, but once they reach the bottom they never come back and the screen goes empty.

```python
star["y"] = star["y"] + star["speed"]
pygame.draw.circle(screen, (255, 255, 255), (star["x"], star["y"]), 2)
```

**Hint:** there is no wrap-around to send the star back to the top.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The program crashes when drawing a meteor because a position has a decimal point.

```python
meteor["y"] = meteor["y"] + meteor["speed"]
pygame.draw.circle(screen, (120, 120, 140), (meteor["x"], meteor["y"]), meteor["size"])
```

**Hint:** `speed` is a decimal, so `meteor["y"]` becomes a decimal. Positions must be whole numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Add more meteors at different speeds

Change `range(5)` to make more meteors. The speeds and sizes are already random, so they will all differ.

**Write the new meteor count you chose and how the screen looks now:**

<div class="write-space"></div>

### 🎯 Give stars a few different colours

Most stars are white, but make some of them slightly yellow or blue.

**Describe how you decided which stars get which colour:**

<div class="write-space"></div>

**Hint:** you can store a `"color"` fact in each star's dictionary, picked with `random.choice([...])` when you build the list.

---

## 5 · Make It 📸

### 🎯 Build a living background behind your ship

Build a scene with a moving background — a falling starfield, dropping meteors, or your own idea — placed behind your ship from earlier weeks.

Send a **photo or video** of your living scene, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I stored each star as a dictionary with …
>
> I looped over the list every frame to …
>
> The meteors fall because I …
>
> They wrap back to the top by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your living background. Talk through it like you are teaching someone. Try to use these words: **list**, **dictionary**, **fall**, **wrap-around**, **speed**.

> 1. Show the stars falling and meteors dropping.
> 2. Read the line that builds one star out loud and name its facts.
> 3. Point at the wrap-around code and explain it.
> 4. Change the meteor count live and show the difference.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
