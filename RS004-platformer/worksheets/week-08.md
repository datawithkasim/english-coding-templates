# 🧗 RS004 Week 8 — English Worksheet

**Topic:** Side Collision + Varied Platforms (Read & Explain) · **Course:** Platformer Game · **Time:** about 45 minutes

Until now the player only landed from above. This week walls **block from the side**, and bumping your **head** on a platform stops you and drops you back down. The trick: handle the **horizontal** move and the **vertical** move *separately*. This worksheet is about reading that code closely and explaining it in your own words — including the code you wrote in today's live lesson.

> Keep these words handy: **side collision**, **horizontal / vertical**, **`player.right` / `player.left`**, **head bump**, **wall**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it does.

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

## 4 · Explain the Code 📖

Here is the full side-and-vertical collision code. Read it carefully, then answer the questions.

```python
# horizontal move, then resolve horizontal collisions
player.x = player.x + vx
for plat in platforms:
    if player.colliderect(plat):
        if vx > 0:
            player.right = plat.left
        elif vx < 0:
            player.left = plat.right

# vertical move, then resolve vertical collisions
player.y = player.y + vy
for plat in platforms:
    if player.colliderect(plat):
        if vy > 0:
            player.bottom = plat.top
            vy = 0
        elif vy < 0:
            player.top = plat.bottom
            vy = 0
```

**Why is the horizontal move done first, in its own loop, before the vertical move?**

<div class="write-space"></div>

**When `vx > 0` and the player hits a wall, why do we set `player.right = plat.left` instead of `player.left`?**

<div class="write-space"></div>

**In the vertical loop, what is the difference between the `vy > 0` case and the `vy < 0` case?**

<div class="write-space"></div>

**Both vertical cases set `vy = 0`, but the horizontal cases do not change `vx`. Why is that?**

<div class="write-space"></div>

**What would go wrong if the player never called `player.colliderect(plat)` before snapping the edges?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the collision code **you wrote in today's lesson**. Record a short video on your phone. You may show your game running. Try to use these words: **side collision**, **wall**, **head bump**, **horizontal**, **vertical**.

> 1. Show your code and point to where you split the move into horizontal and vertical.
> 2. Run your game: walk into a wall from the side and show it blocks you.
> 3. Jump up under a platform and show the head bump.
> 4. Read one collision line out loud and explain which edge it lines up.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
