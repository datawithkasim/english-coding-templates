# 🧗 RS004 Week 8 — English Worksheet

**Topic:** Side Collision + Varied Platforms (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

Until now the player only landed from above. This week walls **block from the side**, and bumping your **head** on a platform stops you and drops you back down. The trick: handle the **horizontal** move and the **vertical** move *separately*.

> Keep these words handy: **side collision**, **horizontal / vertical**, **`player.right` / `player.left`**, **head bump**, **wall**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

```python
player.x = player.x + vx
for plat in platforms:
    if player.colliderect(plat):
        if vx > 0:
            player.right = plat.left
```

**The player moves right into a wall. What does `player.right = plat.left` do?**

<div class="write-space"></div>

```python
elif vy < 0:
    player.top = plat.bottom
    vy = 0
```

**`vy < 0` means moving up. The player's head hits a platform. What happens next?**

<div class="write-space"></div>

```python
# 1. move horizontally, check horizontal collisions
# 2. move vertically, check vertical collisions
```

**Why do we handle horizontal and vertical movement in two separate steps?**

<div class="write-space"></div>

---

## 2 · Edge Words 📐

Match the line to what it lines up. A player runs into a platform.

```
1. player.right = plat.left
2. player.left  = plat.right
3. player.bottom = plat.top
4. player.top   = plat.bottom
```

```
A. player landing on top of the platform
B. player's head bumping the platform's underside
C. player stopped at the platform's left wall (moving right)
D. player stopped at the platform's right wall (moving left)
```

**1 → ___  2 → ___  3 → ___  4 → ___**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — Moving right into a wall should stop the player at the wall. Right now the player slides straight through.

```python
player.x = player.x + vx
for plat in platforms:
    if player.colliderect(plat):
        vx = 0
```

**Hint:** setting `vx = 0` after moving doesn't undo the overlap. Snap the player's edge to the wall.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Head bumps and landings should both work. Right now a head bump is treated like a landing, so the player sticks to the ceiling.

```python
player.y = player.y + vy
for plat in platforms:
    if player.colliderect(plat):
        player.bottom = plat.top
        vy = 0
```

**Hint:** check the *direction* of `vy`. Down (`> 0`) is landing, up (`< 0`) is a head bump.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Horizontal and vertical checks should be separate. Right now they happen in one move, and the player jitters and gets stuck in corners.

```python
player.x += vx
player.y += vy
for plat in platforms:
    if player.colliderect(plat):
        player.right = plat.left
        player.bottom = plat.top
```

**Hint:** move on X and resolve X first, *then* move on Y and resolve Y.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Design with Walls 🛠️

Start from your working full collision.

1. Add one tall thin platform to act as a **wall**. Walk into it from both sides and confirm it blocks you. Write its `Rect`.

<div class="write-space"></div>

2. Add a low platform you can bump your **head** on. Where did you place it?

<div class="write-space"></div>

3. **Stretch:** build a narrow corridor the player must walk through. Sketch the idea in words.

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Design **your own** level using platforms of different sizes — include at least one wall the player bumps into from the side.

When it works, send a **photo or video** showing top, side, and head collisions, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I split movement into horizontal and vertical because …
>
> When the player hits a wall on the right, I set …
>
> A head bump is when `vy < 0`, and I handle it by …
>
> My level has a wall / corridor at …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video showing all three collision types. Teach it to someone new. Try to use these words: **side collision**, **wall**, **head bump**, **horizontal**, **vertical**.

> 1. Walk into a wall from the side and show it blocks you.
> 2. Jump up under a platform and bump your head.
> 3. Land on a platform from above.
> 4. Read one collision line out loud and explain which edge it lines up.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
