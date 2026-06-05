# 🏰 RS003 Week 4 — English Worksheet

**Topic:** A Three-Part Base — Ground + Base + Pivot · **Course:** Pygame Turret · **Time:** about 45 minutes

This week your base grows from one rectangle into a **three-part scene**: a long ground bar across the bottom, the base body on top of it, and a small pivot circle where the gun will spin. You also learn that **draw order** decides what sits in front.

> 🧠 Words to know: **ground**, **palette**, **outline (border)**, **draw order**, **pivot**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```python
pygame.draw.rect(screen, EARTH, (0, HEIGHT - 50, WIDTH, 50))
```

**This rectangle starts at the far left and is as wide as the whole screen. What does it look like?**

<div class="write-space"></div>

```python
pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 35, HEIGHT - 90, 70, 45))
pygame.draw.rect(screen, BLACK, (CENTER_X - 35, HEIGHT - 90, 70, 45), 2)
```

**The same rectangle is drawn twice. The second one has an extra `2` at the end. What does that `2` add?**

<div class="write-space"></div>

```python
screen.fill(SKY)
pygame.draw.rect(screen, EARTH, ...)   # ground
pygame.draw.circle(screen, SILVER, ...) # pivot
```

**Things are drawn from first to last. Which one ends up on top — the sky, the ground, or the pivot?**

<div class="write-space"></div>

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and name the three parts

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SKY = (135, 206, 235)
EARTH = (95, 60, 30)
DARK_GREEN = (0, 100, 0)
LIGHT_GREEN = (50, 150, 50)
BLACK = (0, 0, 0)
SILVER = (180, 180, 180)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    pygame.draw.rect(screen, EARTH, (0, HEIGHT - 50, WIDTH, 50))
    pygame.draw.rect(screen, LIGHT_GREEN, (0, HEIGHT - 55, WIDTH, 8))
    pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 35, HEIGHT - 90, 70, 45))
    pygame.draw.rect(screen, BLACK, (CENTER_X - 35, HEIGHT - 90, 70, 45), 2)
    pygame.draw.circle(screen, SILVER, (CENTER_X, HEIGHT - 90), 12)
    pygame.draw.circle(screen, BLACK, (CENTER_X, HEIGHT - 90), 12, 2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Name the three parts you can see and where each one is:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

**Bug A** — The ground should appear **behind** the base. Right now the ground is drawn last and covers the base.

```python
pygame.draw.rect(screen, DARK_GREEN, (CENTER_X - 35, HEIGHT - 90, 70, 45))
pygame.draw.rect(screen, EARTH, (0, HEIGHT - 50, WIDTH, 50))
```

**Hint:** whatever is drawn last sits on top.

**Write the fixed code (show both lines in the right order):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The base is supposed to have a thin **black outline**, but right now the whole base turns solid black.

```python
pygame.draw.rect(screen, BLACK, (CENTER_X - 35, HEIGHT - 90, 70, 45))
```

**Hint:** a missing last number means "fill completely". Add the border thickness.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The ground should stretch **all the way across** the screen. Right now it only covers part of the width.

```python
pygame.draw.rect(screen, EARTH, (0, HEIGHT - 50, 200, 50))
```

**Hint:** the third number is the width of the rectangle.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It 🔧

### 🎯 Recolour the whole scene with your own palette

At the top of the program, the colours are stored as constants. Change `SKY`, `EARTH`, and the greens to your own colours and run it.

**Write the colours you chose and what mood they give your scene:**

<div class="write-space"></div>

### 🎯 Add one extra detail to the base

Add a small detail to your base — for example an antenna line going up, or a flag rectangle on the side.

**Describe the detail you added and the shape you used to draw it:**

<div class="write-space"></div>

**Hint:** an antenna is a `pygame.draw.line`; a flag is a small `pygame.draw.rect`. Remember to draw it **after** the base so it shows on top.

---

## 5 · Make It 📸

### 🎯 Build your own three-part base

Build a scene that has:

1. a ground bar across the bottom,
2. a base body with an outline,
3. a pivot circle on top,
4. one extra detail of your own.

Send a **photo or video** of your base, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I drew the ground by …
>
> I gave the base an outline by adding …
>
> The draw order matters because …
>
> My extra detail is … and I made it with …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of your three-part base. Talk through it like you are teaching someone. Try to use these words: **ground**, **palette**, **outline**, **draw order**, **pivot**.

> 1. Show all three parts and name them.
> 2. Read one rectangle line out loud and explain its four numbers.
> 3. Explain how draw order decides what sits in front.
> 4. Show the detail you added on top.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
