# 🟩 RS003 Week 3 — English Worksheet

**Topic:** Build the Ship Body · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you think about the code that draws the first piece of your spaceship: a **body** that sits in the middle-bottom of the screen. You read code that draws shapes, stores important numbers as **constants**, and finds the centre of the screen with **integer division** (`//`). You will read it, fix it, and explain it.

> 🧠 Words to know: **constant**, **rectangle**, **circle**, **integer division (`//`)**, **centre**

---

## 1 · Predict 🔮

Read each piece of code. Just from reading it, write what you think it does. Do not run it.

```python
WIDTH = 800
CENTER_X = WIDTH // 2
```

**What number is `CENTER_X`? Why use `//` instead of `/` here?**

<div class="write-space"></div>

```python
pygame.draw.rect(screen, CYAN, (CENTER_X - 20, HEIGHT - 80, 40, 50))
```

**The four numbers are (left, top, width, height). Where on the screen does this rectangle appear, and how big is it?**

<div class="write-space"></div>

```python
pygame.draw.circle(screen, WHITE, (CENTER_X, HEIGHT - 90), 8)
```

**What shape, where, and how big? What does the last number 8 control?**

<div class="write-space"></div>

```python
screen.fill(SPACE)
pygame.draw.rect(screen, CYAN, (CENTER_X - 20, HEIGHT - 80, 40, 50))
pygame.display.flip()
```

**In what order do these three lines run? What would you see if `screen.fill(SPACE)` came AFTER the rectangle instead of before it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it on paper, then explain why the original was wrong.

**Bug A** — The ship body should sit in the **centre** across the screen. Right now it is glued to the left edge.

```python
pygame.draw.rect(screen, CYAN, (0, HEIGHT - 80, 40, 50))
```

**Hint:** use `CENTER_X` to place it in the middle.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — `CENTER_X` is supposed to be the middle of the screen, but it comes out as a number with a decimal point and the drawing looks off.

```python
CENTER_X = WIDTH / 2
```

**Hint:** screen positions must be whole numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The body is supposed to sit near the **bottom**, where the player ship belongs. Right now it is drawn near the top of the screen.

```python
pygame.draw.rect(screen, CYAN, (CENTER_X - 20, 80, 40, 50))
```

**Hint:** in Pygame, Y = 0 is the **top**. The bottom is near `HEIGHT`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working example line by line. Then answer the questions below by reading only — you do not need to run it.

```python
import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

SPACE = (10, 12, 40)
CYAN = (80, 220, 255)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SPACE)
    pygame.draw.rect(screen, CYAN, (CENTER_X - 20, HEIGHT - 80, 40, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**`WIDTH`, `HEIGHT`, `SPACE`, and `CYAN` are all constants. What is each one used for?**

<div class="write-space"></div>

**The rectangle's left value is `CENTER_X - 20`, not `CENTER_X`. Why subtract 20? What would happen if you used `CENTER_X` on its own?**

<div class="write-space"></div>

**What does the `while running:` loop do? What makes the loop stop?**

<div class="write-space"></div>

**Why is the cyan rectangle drawn in the middle across the screen? Point to the exact lines that make this happen.**

<div class="write-space"></div>

**Is the rectangle near the top or near the bottom of the window? How can you tell from the numbers?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote code with your teacher to draw your ship body. Now explain that code in a short phone video. You may show it running on the screen. Try to use these words: **constant**, **rectangle**, **circle**, **integer division**, **centre**.

> 1. Show your ship body sitting in the middle-bottom of the screen.
> 2. Read your `CENTER_X` line out loud and say what `//` does.
> 3. Point at your rectangle's four numbers and name each one (left, top, width, height).
> 4. Say why Y = 0 is the top, not the bottom.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
