# 🚀 RS003 Week 4 — English Worksheet

**Topic:** A Three-Part Ship — Body + Nose + Thrusters · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week your ship grows from one rectangle into a **three-part craft**: a body rectangle, a pointed **nose** triangle on top, and two **thruster** blocks at the bottom. You build each part from variables, and you learn that **draw order** decides what sits in front.

> 🧠 Words to know: **polygon**, **triangle**, **palette**, **draw order**, **thruster**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

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

**Name the three parts you can see and where each one is:**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Fix it, then explain why the original was wrong.

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

## 4 · Modify It 🔧

### 🎯 Recolour the whole ship with your own palette

At the top of the program, the colours are stored as constants. Change `SPACE`, `CYAN`, and the others to your own colours and run it.

**Write the colours you chose and what mood they give your ship:**

<div class="write-space"></div>

### 🎯 Add one extra detail to the ship

Add a small detail to your ship — for example a wing line on the side, or a light circle on the nose.

**Describe the detail you added and the shape you used to draw it:**

<div class="write-space"></div>

**Hint:** a wing is a `pygame.draw.line`; a light is a small `pygame.draw.circle`. Remember to draw it **after** the body so it shows on top.

---

## 5 · Make It 📸

### 🎯 Build your own three-part ship

Build a scene that has:

1. a body rectangle,
2. a nose triangle on top,
3. two thrusters at the bottom,
4. one extra detail of your own.

Send a **photo or video** of your ship, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I drew the body by …
>
> I built the nose as a triangle by …
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

Take a video of your three-part ship. Talk through it like you are teaching someone. Try to use these words: **polygon**, **triangle**, **palette**, **draw order**, **thruster**.

> 1. Show all three parts and name them.
> 2. Read the polygon line out loud and explain its three points.
> 3. Explain how draw order decides what sits in front.
> 4. Show the detail you added on top.

**Write what you will say in your video.** Plan it here before you record.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
