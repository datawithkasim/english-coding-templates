# ✨ RS003 Week 12 — English Worksheet

**Topic:** Twinkling Stars and Drifting Clouds · **Course:** Pygame Turret · **Time:** about 45 minutes

This week your background **moves**. Stars twinkle at different brightnesses and clouds drift slowly across the screen, wrapping back around when they leave. You store each star and cloud as a small **dictionary** of facts and loop over a **list** of them every frame.

> 🧠 Words to know: **list**, **dictionary**, **drift**, **wrap-around**, **brightness**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
stars = []
for i in range(80):
    stars.append({"x": random.randint(0, WIDTH), "y": random.randint(0, HEIGHT - 100), "phase": random.randint(0, 60)})
```

**This builds a list of 80 stars. What three facts does each star remember?**

<div class="write-space"></div>

```python
cloud["x"] = cloud["x"] - cloud["speed"]
if cloud["x"] < -cloud["size"]:
    cloud["x"] = WIDTH + cloud["size"]
```

**Each cloud moves left a little every frame. What happens when a cloud goes off the left edge?**

<div class="write-space"></div>

```python
brightness = 100 + ((frame + star["phase"]) * 4 % 156)
pygame.draw.circle(screen, (brightness, brightness, brightness), (star["x"], star["y"]), 2)
```

**The brightness changes every frame and each star has a different `phase`. What do the stars look like together?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and watch it breathe

```python
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

stars = []
for i in range(80):
    stars.append({"x": random.randint(0, WIDTH), "y": random.randint(0, HEIGHT - 100), "phase": random.randint(0, 60)})

clouds = []
for i in range(5):
    clouds.append({"x": random.randint(0, WIDTH), "y": random.randint(40, 200), "speed": random.uniform(0.3, 1.0), "size": random.randint(40, 80)})

frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 30, 80))

    for star in stars:
        brightness = 100 + ((frame + star["phase"]) * 4 % 156)
        pygame.draw.circle(screen, (brightness, brightness, brightness), (star["x"], star["y"]), 2)

    for cloud in clouds:
        cloud["x"] = cloud["x"] - cloud["speed"]
        if cloud["x"] < -cloud["size"]:
            cloud["x"] = WIDTH + cloud["size"]
            cloud["y"] = random.randint(40, 200)
        cx = int(cloud["x"])
        pygame.draw.circle(screen, (200, 200, 220), (cx, cloud["y"]), cloud["size"] // 2)
        pygame.draw.circle(screen, (200, 200, 220), (cx + 20, cloud["y"] - 10), cloud["size"] // 2)
        pygame.draw.circle(screen, (200, 200, 220), (cx - 20, cloud["y"] - 5), cloud["size"] // 2)

    pygame.display.flip()
    frame = frame + 1
    clock.tick(60)

pygame.quit()
```

**Watch for 10 seconds. Describe what the stars do and what the clouds do:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — All the stars are supposed to twinkle at different times, but instead they all flash on and off together.

```python
stars.append({"x": random.randint(0, WIDTH), "y": random.randint(0, HEIGHT - 100), "phase": 0})
```

**Hint:** every star has the same `phase`, so they share the same beat.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Clouds should keep flowing forever, but once they leave the left side they never come back and the sky goes empty.

```python
cloud["x"] = cloud["x"] - cloud["speed"]
pygame.draw.circle(screen, (200, 200, 220), (int(cloud["x"]), cloud["y"]), cloud["size"] // 2)
```

**Hint:** there is no wrap-around to send the cloud back to the right side.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The program crashes when drawing a cloud because a position has a decimal point.

```python
cloud["x"] = cloud["x"] - cloud["speed"]
pygame.draw.circle(screen, (200, 200, 220), (cloud["x"], cloud["y"]), cloud["size"] // 2)
```

**Hint:** `speed` is a decimal, so `cloud["x"]` becomes a decimal. Positions must be whole numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Add more clouds at different speeds

Change `range(5)` to make more clouds. The speeds and sizes are already random, so they will all differ.

**Write the new cloud count you chose and how the sky looks now:**

<div class="write-space"></div>

### 🎯 Give stars a few different colours

Most stars are white, but make some of them slightly yellow or blue.

**Describe how you decided which stars get which colour:**

<div class="write-space"></div>

**Hint:** you can store a `"color"` fact in each star's dictionary, picked with `random.choice([...])` when you build the list.

---

## 5 · Make It 📸

### 🎯 Build a living background behind your turret

Build a scene with a moving background — twinkling stars, drifting clouds, or your own idea like falling snow — placed behind your turret from earlier weeks.

Send a **photo or video** of your living scene, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I stored each star as a dictionary with …
>
> I looped over the list every frame to …
>
> The clouds drift because I …
>
> They wrap around the screen by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your living background. Talk through it like you are teaching someone. Try to use these words: **list**, **dictionary**, **drift**, **wrap-around**, **brightness**.

> 1. Show the stars twinkling and clouds drifting.
> 2. Read the line that builds one star out loud and name its facts.
> 3. Point at the wrap-around code and explain it.
> 4. Change the cloud count live and show the difference.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
