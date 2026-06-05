# 🌈 RS004 Week 2 — English Worksheet

**Topic:** Gradient Background (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week your flat sky becomes a **gradient** — a smooth blend from one colour at the top to another at the bottom. You will gather all your colours into one **palette** and draw the sky one line at a time.

> Keep these words handy: **gradient**, **palette**, **blend (interpolate)**, **`draw.line`**, **frame**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

```python
for y in range(HEIGHT):
    pygame.draw.line(screen, (100, 180, 255), (0, y), (WIDTH, y))
```

**How many lines get drawn? What do they cover together?**

<div class="write-space"></div>

```python
t = y / HEIGHT
r = int(SKY_TOP[0] * (1 - t) + SKY_BOTTOM[0] * t)
```

**At the very top (`y = 0`), what is `t`? Which colour wins — top or bottom?**

<div class="write-space"></div>

```python
SKY_TOP = (100, 180, 255)
SKY_BOTTOM = (200, 230, 255)
```

**These sit at the top of the file with the other colours. Why keep all colours in one place?**

<div class="write-space"></div>

---

## 2 · Blend Math 🧮

The blend formula is `int(A * (1 - t) + B * t)`. Fill in the table. `A = 100`, `B = 200`.

```
t = 0.0  → result = ___
t = 0.5  → result = ___
t = 1.0  → result = ___
```

<div class="write-space"></div>

**In your own words: when `t` goes from 0 to 1, the colour moves from ______ to ______.**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — The sky should blend from top to bottom, but the whole screen comes out one flat colour.

```python
for y in range(HEIGHT):
    t = 0
    r = int(SKY_TOP[0] * (1 - t) + SKY_BOTTOM[0] * t)
    g = int(SKY_TOP[1] * (1 - t) + SKY_BOTTOM[1] * t)
    b = int(SKY_TOP[2] * (1 - t) + SKY_BOTTOM[2] * t)
    pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))
```

**Hint:** `t` should *change* as `y` goes down. It is stuck at one value.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The gradient should fill the screen, but only the very top line is coloured.

```python
y = 0
t = y / HEIGHT
r = int(SKY_TOP[0] * (1 - t) + SKY_BOTTOM[0] * t)
pygame.draw.line(screen, (r, SKY_TOP[1], SKY_TOP[2]), (0, y), (WIDTH, y))
```

**Hint:** one line is drawn. How do we draw *every* row?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify the Sky 🛠️

Start from your working `draw_gradient_background()` function. Make small changes and write down what each does.

1. Swap `SKY_TOP` and `SKY_BOTTOM`. What happens to the direction of the blend?

<div class="write-space"></div>

2. Pick two brand-new colours (a sunrise: warm at the bottom, dark at the top). Write the RGB values you chose.

<div class="write-space"></div>

3. **Stretch:** make a *three*-colour gradient (top → middle → bottom). 

> Hint: split the screen in half. Blend top→middle for the upper rows, then middle→bottom for the lower rows.

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Build **your own** gradient background and run it on top of last week's window.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I chose my top and bottom colours: …
>
> The `for y in range(HEIGHT)` loop draws the sky by …
>
> The `t` value controls …
>
> I kept my colours in a palette so that …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video while your gradient sky runs. Teach it to someone new. Try to use these words: **gradient**, **palette**, **blend**, **line**, **loop**.

> 1. Show your gradient sky.
> 2. Point at your two palette colours and say which is top, which is bottom.
> 3. Read the blend line out loud and explain what `t` does.
> 4. Show one colour you changed and the before/after.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
