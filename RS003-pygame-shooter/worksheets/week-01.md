# 🪟 RS003 Week 1 — English Worksheet

**Topic:** Open a Pygame Window · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

This week you open your very first **Pygame window** — a blank screen your game will live in. You learn that the screen is a space measured in **width** and **height**, fill it with a deep-space colour, and keep it open with a **game loop**.

> 🧠 Words to know: **import**, **window**, **screen**, **fill**, **flip**, **game loop**

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

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

---

## 2 · Run It 🏃

### 🎯 Type the example, run it, and report what you see

Type this into your code editor exactly as it is, then run it.

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

**What colour is the window? What words are in the title bar at the top?**

<div class="write-space"></div>

**Try clicking the X button. What happens? Which line of code made that work?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below was meant to do something but is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

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

## 4 · Modify It 🎨

### 🎯 Change the colour and the title to make the window yours

Go back to your working window from Part 2. Make these small changes and run after each one:

- Change `SPACE` to a colour you choose. Remember each number is `(red, green, blue)` from 0 to 255.
- Change the title text in `set_caption(...)` to your own game name.

**Write down the three numbers you used and the colour they made:**

<div class="write-space"></div>

### 🎯 Find the centre of the screen

The window is 800 across and 600 down. The exact middle is halfway across and halfway down.

**Work out the centre point with maths, then write the (X, Y) for the centre:**

<div class="write-space"></div>

**Hint:** halfway across 800 is one number, halfway down 600 is another. The centre is `(across ÷ 2, down ÷ 2)`.

---

## 5 · Make It 📸

### 🎯 Build your own game window and show it off

Build a window that:

1. opens at 800 × 600,
2. is filled with your own deep-space colour,
3. has your own game name in the title bar,
4. closes when you click the X button.

When it works, send a **photo or video** of your window, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I set the window size to …
>
> I chose the colour … because …
>
> The line that makes the colour appear is …
>
> The game loop keeps the window open by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your window opens and closes. Talk through it like you are teaching someone who has never seen Pygame. Try to use these words: **window**, **screen**, **fill**, **flip**, **game loop**.

> 1. Show your window opening with its colour and title.
> 2. Read the `set_mode` line out loud and say what the two numbers mean.
> 3. Point at the line that makes the colour appear.
> 4. Click the X and say which code let the window close.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your photo or video to teacher on KakaoTalk.
