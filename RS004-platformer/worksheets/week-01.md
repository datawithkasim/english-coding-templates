# 🪟 RS004 Week 1 — English Worksheet

**Topic:** Game Window & Game Loop · **Course:** Platformer Game · **Time:** about 45 minutes

This week you think about your very first **game window** and the **game loop** — the heartbeat that runs every frame: read events → update → draw. On paper you will read this code, predict it, fix it, and explain it in your own words. Everything you build for the next 16 weeks lives inside this loop.

> Keep these words handy: **game loop**, **event**, **`pygame.QUIT`**, **`flip()`**, **FPS**, **RGB**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will do.

```python
screen.fill((135, 206, 235))
pygame.display.flip()
```

**What colour fills the screen, and what does `flip()` do?**

<div class="write-space"></div>

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

**A player clicks the X button. What happens to `running`, and then to the loop?**

<div class="write-space"></div>

```python
clock.tick(60)
```

**This line is at the end of the loop. What is it controlling?**

<div class="write-space"></div>

---

## 2 · Read & Match 🔗

Match each line to its job. Write the letter next to each number.

```
1. pygame.init()
2. pygame.display.set_mode((800, 600))
3. pygame.display.set_caption("나의 플랫포머")
4. screen.fill(SKY_BLUE)
5. pygame.display.flip()
```

```
A. paints the whole screen one colour
B. starts up pygame so we can use it
C. shows everything we drew this frame
D. makes the 800×600 window
E. writes the title on the window bar
```

**1 → ___  2 → ___  3 → ___  4 → ___  5 → ___**

<div class="write-space"></div>

---

## 3 · Read the Colours 🎨

Each colour is `(Red, Green, Blue)`, where each number is 0–255. Write down what colour you think each one makes.

```
(255, 0, 0)      → ___________
(0, 0, 0)        → ___________
(255, 255, 255)  → ___________
(135, 206, 235)  → ___________
```

<div class="write-space"></div>

**Now invent one.** Write an RGB value for a sunset orange sky, and say what each of the three numbers means.

<div class="write-space"></div>

---

## 4 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — The window should stay open until the player closes it. Right now it flashes open and shuts instantly.

```python
running = True
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
screen.fill((135, 206, 235))
pygame.display.flip()
```

**Hint:** the drawing and event-reading need to *repeat*. What kind of loop is missing?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The screen should turn sky-blue, but the window stays black even though `fill` runs.

```python
screen.fill((135, 206, 235))
clock.tick(60)
```

**Hint:** we filled the screen but never *showed* it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 5 · Explain the Code 📖

Here is a complete working game window — an 800×600 sky-blue screen running at 60 FPS. Read it carefully, then answer the questions.

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("나의 플랫포머")
clock = pygame.time.Clock()
SKY_BLUE = (135, 206, 235)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SKY_BLUE)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Which line creates the window, and how big is it?**

<div class="write-space"></div>

**What does the `while running:` loop do, and when does it stop?**

<div class="write-space"></div>

**Inside the loop, what is the job of `screen.fill(SKY_BLUE)`, and what is the job of `pygame.display.flip()`?**

<div class="write-space"></div>

**What would change on screen if `SKY_BLUE` was `(255, 0, 0)` instead?**

<div class="write-space"></div>

**Why is `clock.tick(60)` inside the loop, and what does the 60 mean?**

<div class="write-space"></div>

---

## 6 · Explain Your Lesson Code 🎥

Today in the live lesson you wrote your own game window. Take a short video on your phone and explain **the code you wrote** — you can show it running. Teach it like you are talking to someone who has never seen Pygame. Try to use these words: **game loop**, **event**, **fill**, **flip**, **FPS**.

> 1. Show your window opening.
> 2. Point at the line that sets the background colour and read it out.
> 3. Explain what your game loop does every frame.
> 4. Click the X and show the window closing — say which line made that work.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
