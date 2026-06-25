# 🚀 RS003 Week 4 — English Worksheet

**Topic:** A Three-Part Ship — Body + Nose + Thrusters · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week is all about **thinking about** and **explaining** the three-part ship — a body rectangle, a pointed **nose** triangle, and two **thruster** blocks — and how **draw order** decides what sits in front.

> 🧠 Words to know: **polygon**, **triangle**, **palette**, **draw order**, **thruster**

---

## 1 · Predict 🔮

Read each piece of code and write what you think it does. Just read — no running.

```python
pygame.draw.rect(screen, CYAN, (CENTER_X - 20, HEIGHT - 80, 40, 50))
```

**This is the ship body. Where does it sit on the screen and how big is it?**

<div class="write-space"></div>

```python
pygame.draw.polygon(screen, WHITE, [(CENTER_X, HEIGHT - 100), (CENTER_X - 20, HEIGHT - 80), (CENTER_X + 20, HEIGHT - 80)])
```

**A polygon connects three points. One point is higher than the other two. What shape does it make, and where does it sit on the ship?**

<div class="write-space"></div>

```python
screen.fill(SPACE)
pygame.draw.rect(screen, CYAN, ...)     # body
pygame.draw.polygon(screen, WHITE, ...) # nose
pygame.draw.rect(screen, RED, ...)      # thruster
```

**Things are drawn from first to last. Which one ends up on top — the space, the body, or the nose?**

<div class="write-space"></div>

```python
pygame.draw.rect(screen, RED, (CENTER_X - 16, y + 50, 8, 10))   # thruster L
pygame.draw.rect(screen, RED, (CENTER_X + 8, y + 50, 8, 10))    # thruster R
```

**These two lines draw the thrusters. What is different between them, and why does that put one on each side?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Write the fixed code, then explain why the original was wrong.

**Bug A** — The body should appear **behind** the nose. Right now the body is drawn last and covers the nose.

```python
pygame.draw.polygon(screen, WHITE, [(CENTER_X, y - 20), (CENTER_X - 20, y), (CENTER_X + 20, y)])
pygame.draw.rect(screen, CYAN, (CENTER_X - 20, y, 40, 50))
```

**Hint:** whatever is drawn last sits on top.

**Write the fixed code (show both lines in the right order):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The nose is supposed to be a **triangle** pointing up, but the point is at the bottom and it looks upside down.

```python
pygame.draw.polygon(screen, WHITE, [(CENTER_X, y + 20), (CENTER_X - 20, y), (CENTER_X + 20, y)])
```

**Hint:** to point up, the tip point needs a **smaller** Y than the two base points.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The ship should have **two** thrusters, one on each side. Right now both thrusters land on top of each other in the same spot.

```python
pygame.draw.rect(screen, RED, (CENTER_X - 16, y + 50, 8, 10))
pygame.draw.rect(screen, RED, (CENTER_X - 16, y + 50, 8, 10))
```

**Hint:** the second thruster needs a different X so it sits on the other side.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this full program. It draws the three-part ship. Answer the questions below by reading — you do not need to run it.

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SPACE = (10, 12, 40)
CYAN = (80, 220, 255)
WHITE = (255, 255, 255)
RED = (230, 60, 60)

y = HEIGHT - 80

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SPACE)
    pygame.draw.rect(screen, CYAN, (CENTER_X - 20, y, 40, 50))                            # body
    pygame.draw.polygon(screen, WHITE, [(CENTER_X, y - 20), (CENTER_X - 20, y), (CENTER_X + 20, y)])  # nose
    pygame.draw.rect(screen, RED, (CENTER_X - 16, y + 50, 8, 10))                         # thruster L
    pygame.draw.rect(screen, RED, (CENTER_X + 8, y + 50, 8, 10))                          # thruster R
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**What do `SPACE`, `CYAN`, `WHITE`, and `RED` store, and why are they written at the top with capital letters?**

<div class="write-space"></div>

**The line `screen.fill(SPACE)` runs first inside the loop. What does it do before any shapes are drawn?**

<div class="write-space"></div>

**Look at the three points in the `polygon` line. Which point is the tip of the nose, and how can you tell?**

<div class="write-space"></div>

**The two thruster lines both use `RED`. What makes one go to the left and the other to the right?**

<div class="write-space"></div>

**If you moved the body line to be the *last* draw line, what would happen to the nose and thrusters?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own three-part ship code. Now record a short phone video explaining **the code you wrote**. You can show it running. Try to use these words: **polygon**, **triangle**, **palette**, **draw order**, **thruster**.

> 1. Show your code and name the three parts — body, nose, thrusters.
> 2. Read your polygon line out loud and explain its three points.
> 3. Explain how draw order decides what sits in front in your ship.
> 4. Point to your palette colours and say what mood they give.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
