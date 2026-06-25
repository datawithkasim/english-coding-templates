# 🪟 RS003 Week 1 — English Worksheet

**Topic:** Open a Pygame Window · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you think about your very first **Pygame window** — a blank screen your game will live in. On this worksheet you read code, predict it, fix it, and explain it in your own words. The screen is a space measured in **width** and **height**, filled with a deep-space colour, and kept open with a **game loop**.

> 🧠 Words to know: **import**, **window**, **screen**, **fill**, **flip**, **game loop**

---

## 1 · Predict 🔮

Read each piece of code. Do **not** run it. Just from reading, write what you think will happen.

```python
screen = pygame.display.set_mode((800, 600))
```

**What does `(800, 600)` mean? Which number is across, which is down?**

<div class="write-space"></div>

```python
SPACE = (10, 12, 40)
screen.fill(SPACE)
```

**The screen gets filled with a colour. But will you actually SEE it yet? What is still missing?**

<div class="write-space"></div>

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

**What is this loop watching for? What makes the window finally close?**

<div class="write-space"></div>

```python
pygame.display.set_caption("Space Shooter")
```

**Where do you think these words will appear on the screen?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Read what it is **supposed** to do, then fix it on paper and explain why the original was wrong.

**Bug A** — This should open a window, but nothing appears. The screen is filled, but it never shows up.

```python
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((10, 12, 40))
```

**Hint:** filling the screen is not enough. One line makes it visible.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This is supposed to make an **800 wide, 600 tall** window. Right now it is tall and thin instead of wide.

```python
screen = pygame.display.set_mode((600, 800))
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The window opens but freezes and you cannot close it with the X button.

```python
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((10, 12, 40))
pygame.display.flip()

while True:
    pass
```

**Hint:** the loop never listens for the QUIT event.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working program carefully. Do **not** run it — answer every question just by reading it line by line.

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")

SPACE = (10, 12, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SPACE)
    pygame.display.flip()

pygame.quit()
```

**What does the line `import pygame` do, and why must it come first?**

<div class="write-space"></div>

**What does `set_mode((800, 600))` create, and what would change if you swapped the two numbers to `(600, 800)`?**

<div class="write-space"></div>

**Which line actually makes the new picture show up on the window?**

<div class="write-space"></div>

**Trace the variable `running`. What value does it start as, and which line changes it?**

<div class="write-space"></div>

**The `screen.fill(SPACE)` line is inside the loop, not above it. Why do you think it sits inside the loop?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own Pygame window code. Now explain **your own code** — the one you made in class. Record a short video on your phone (or a parent's phone) and talk through it like you are teaching someone who has never seen Pygame. You can show your window opening and closing if you like. Try to use these words: **window**, **screen**, **fill**, **flip**, **game loop**.

> 1. Read your `set_mode` line out loud and say what the two numbers mean.
> 2. Point at the line that fills your screen with colour, and say which colour you chose.
> 3. Show or say which line makes the colour actually appear (**flip**).
> 4. Say which line lets the window close when you click the X.

**Write what you will say in your video. Plan it here before you record — you can read from it while filming.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
