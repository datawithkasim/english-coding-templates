# ⚙️ RS003 Week 2 — English Worksheet

**Topic:** FPS, Title, and a Colour-Cycling Nebula · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you make last week's window feel **alive**. You add a **clock** to control the frame rate (FPS), give the title bar a nicer name, and make the deep-space background slowly shift colour like a glowing nebula.

> 🧠 Words to know: **clock**, **FPS (frames per second)**, **frame**, **tick**, **modulo (`%`)**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)
```

**What does `clock.tick(60)` do to the speed of the game loop?**

<div class="write-space"></div>

```python
frame_count = 0
r = (frame_count * 1) % 256
frame_count = frame_count + 1
```

**`frame_count` goes up by 1 every loop. What does `% 256` do when it reaches 256?**

<div class="write-space"></div>

```python
r = (frame_count) % 256
g = 100
b = (200 - frame_count) % 256
screen.fill((r, g, b))
```

**Red is climbing and blue is falling, while green stays still. Describe how the nebula colour changes as time passes.**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and watch the colours move

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⚙️ Space Shooter v2 — 60 FPS")

clock = pygame.time.Clock()
FPS = 60
frame_count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    r = (frame_count) % 256
    g = 100
    b = (200 - frame_count) % 256

    screen.fill((r, g, b))
    pygame.display.flip()

    clock.tick(FPS)
    frame_count = frame_count + 1

pygame.quit()
```

**Watch for 10 seconds. What does the nebula background do?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — This game runs fine but your computer's fan gets loud and the CPU hits 100%.

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((100, 100, 200))
    pygame.display.flip()
```

**Hint:** without a clock, the loop runs as fast as it possibly can.

**Write the fixed code (show the loop):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The nebula should cycle colours, but the program crashes with an error about a colour value being too big.

```python
r = frame_count
screen.fill((r, 100, 50))
```

**Hint:** colour numbers must stay between 0 and 255. `frame_count` keeps growing past 255.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The colour is supposed to keep changing, but it is stuck on one colour forever.

```python
frame_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    r = frame_count % 256
    screen.fill((r, 100, 100))
    pygame.display.flip()
    clock.tick(60)
```

**Hint:** the frame counter never goes up.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Compare 30, 60, and 120 FPS

Change `FPS` to 30, run it, then to 60, then to 120. Watch how fast the colours move each time.

**Write what changed between 30, 60, and 120 FPS:**

<div class="write-space"></div>

### 🎯 Invent your own colour formula

Right now red rises and blue falls. Change the formulas so the colours change in your own way. For example, make the space slowly get darker, or make green move too.

**Write the formulas you used for r, g, and b:**

<div class="write-space"></div>

**Hint:** any formula works as long as you wrap the result in `% 256` so it stays a valid colour.

---

## 5 · Make It 📸

### 🎯 Tune your own living nebula

Make a window that:

1. runs at a steady frame rate using a clock,
2. has your own title in the bar,
3. slowly changes its background colour with your own formula.

When it works, send a **photo or video** of your moving nebula, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I added a clock so the loop …
>
> I set the FPS to … because …
>
> My colour formula makes the space …
>
> I used `% 256` to make sure …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while your nebula cycles. Talk through it like you are teaching someone. Try to use these words: **clock**, **FPS**, **frame**, **tick**, **modulo**.

> 1. Show the background slowly changing colour.
> 2. Read your colour formula out loud and say what makes it change.
> 3. Show what happens to the speed when you change FPS.
> 4. Say why `clock.tick` matters for your computer.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your FPS comparison video to teacher on KakaoTalk.
