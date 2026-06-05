# 🪟 RS004 Week 1 — English Worksheet

**Topic:** Game Window & Game Loop · **Course:** Platformer Game · **Time:** about 45 minutes

This week you open your very first **game window** and start the **game loop** — the heartbeat that runs every frame: read events → update → draw. Everything you build for the next 16 weeks lives inside this loop.

> Keep these words handy: **game loop**, **event**, **`pygame.QUIT`**, **`flip()`**, **FPS**, **RGB**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

## 3 · Spot the Bug 🐛

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

## 4 · Colour Lab 🎨

Each colour is `(Red, Green, Blue)`, where each number is 0–255. Write down what colour you expect, then check it in code.

```
(255, 0, 0)      → ___________
(0, 0, 0)        → ___________
(255, 255, 255)  → ___________
(135, 206, 235)  → ___________
```

<div class="write-space"></div>

**Now invent one.** Write an RGB value for a sunset orange sky, then test it in `screen.fill(...)`.

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Open your starter file. You have a working 800×600 sky-blue window at 60 FPS. Make it yours:

1. Change the background to a colour you like, and write down what its RGB numbers mean.
2. Change the window size to 1024×768.
3. Give the window your own caption (title).

When it works, send a **photo or video** of your window running, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I changed the background to …
>
> The three numbers in the colour mean …
>
> I made the window bigger by …
>
> The game loop keeps the window open because …
>
> One thing I was unsure about was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone while your window runs. Talk through it like you are teaching someone who has never seen Pygame. Try to use these words: **game loop**, **event**, **fill**, **flip**, **FPS**.

> 1. Show your window opening.
> 2. Point at the line that sets the background colour.
> 3. Explain what the game loop does every frame.
> 4. Click the X and show the window closing — say which line made that work.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
