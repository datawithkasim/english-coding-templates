# 🟩 RS003 Week 3 — English Worksheet

**Topic:** Build the Ship Body · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you draw the first piece of your spaceship: a **body** that sits in the middle-bottom of the screen. You learn to draw shapes, store important numbers as **constants**, and find the centre of the screen with **integer division** (`//`).

> 🧠 Words to know: **constant**, **rectangle**, **circle**, **integer division (`//`)**, **centre**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

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

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and find the ship body

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

**Where does the cyan rectangle sit? Is it really in the centre across? How can you tell?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

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

## 4 · Modify It 🔧

### 🎯 Add a cockpit circle on the body

A ship needs a cockpit. Add a small circle on top of the body where the pilot sits.

```python
pygame.draw.circle(screen, (255, 255, 255), (CENTER_X, HEIGHT - 70), 8)
```

**Add this line below the rectangle, run it, and write what you see:**

<div class="write-space"></div>

### 🎯 Resize the body using constants

Make the body wider, then narrower, by changing only the width number. Then try making the body its own constant so the size is easy to change in one place.

**Write the constant you made and the size it sets (for example `BODY_WIDTH = 40`):**

<div class="write-space"></div>

**Hint:** a constant is just a name in CAPITALS that holds a number you do not want to keep retyping.

---

## 5 · Make It 📸

### 🎯 Draw your own ship body in the centre

Build a window that:

1. uses constants for `WIDTH` and `HEIGHT`,
2. finds the centre with `//`,
3. draws a body rectangle in the middle-bottom,
4. adds a cockpit circle on top.

Send a **photo or video** of your ship body, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I set up my constants for …
>
> I found the centre by …
>
> I placed the body at the bottom by using …
>
> I added a cockpit circle so that …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your ship body. Talk through it like you are teaching someone. Try to use these words: **constant**, **rectangle**, **circle**, **integer division**, **centre**.

> 1. Show your body sitting in the middle-bottom.
> 2. Read your `CENTER_X` line out loud and say what `//` does.
> 3. Point at the rectangle's four numbers and name each one.
> 4. Say why Y = 0 is the top, not the bottom.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
