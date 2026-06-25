# ⚙️ RS003 Week 2 — English Worksheet

**Topic:** FPS, Title, and a Colour-Cycling Nebula · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you think about the code that makes last week's window feel **alive** — a **clock** that controls the frame rate (FPS), a nicer title bar, and a deep-space background that slowly shifts colour like a glowing nebula. You will read it, predict it, fix it, and explain it in your own words.

> 🧠 Words to know: **clock**, **FPS (frames per second)**, **frame**, **tick**, **modulo (`%`)**

---

## 1 · Predict 🔮

Read each piece of code. Just from reading it, write what you think will happen. Do not run it.

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

```python
pygame.display.set_caption("⚙️ Space Shooter v2 — 60 FPS")
```

**What part of the window will this line change?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Read it carefully and fix it on paper, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Read this working program line by line. Do not run it. Answer the questions using only what you can see.

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

**Which line decides how many frames happen each second, and what number is it set to?**

<div class="write-space"></div>

**The green value `g` is always 100. The red and blue values change. Explain why green stays the same colour but red and blue do not.**

<div class="write-space"></div>

**What does `frame_count = frame_count + 1` do, and why does the nebula need it?**

<div class="write-space"></div>

**What makes the loop stop and the window close?**

<div class="write-space"></div>

**`clock.tick(FPS)` is near the bottom of the loop. In your own words, what would happen to the speed of the colours if you removed it?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Now explain the code **you** wrote during today's lesson. Record a short phone video where you talk through your own nebula code. You can show it running too. Try to use these words: **clock**, **FPS**, **frame**, **tick**, **modulo**.

> 1. Show your background slowly changing colour.
> 2. Read your colour formula out loud and say what makes it change.
> 3. Say what FPS you used and what `clock.tick` does for your computer.
> 4. Point to the line that makes the colour keep moving.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
