# 💎 RS004 Week 12 — English Worksheet

**Topic:** Coin Types + Spin Animation (Apply) · **Course:** Platformer Game · **Time:** about 45 minutes

This week coins come in **kinds** — gold (1 point), gem (5), secret (10). You store each coin as a **dictionary** with its rect, kind, and value, and you make them **spin** with a `sin` wave that wobbles their width.

> Keep these words handy: **dictionary**, **kind / value**, **`math.sin`**, **wobble (animate)**, **frame**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

```python
coins = [
    {"rect": pygame.Rect(180, 480, 20, 20), "kind": "gold", "value": 1},
    {"rect": pygame.Rect(580, 480, 20, 20), "kind": "gem",  "value": 5},
]
```

**Each coin is now a dictionary. How do you read the second coin's value?**

<div class="write-space"></div>

```python
wave = math.sin(frame * 0.1) * 8
w = max(2, int(20 + wave))
```

**`math.sin(...)` swings between -1 and +1. What is the smallest the width `w` can get, and why the `max(2, ...)`?**

<div class="write-space"></div>

```python
if player.colliderect(coin["rect"]):
    score = score + coin["value"]
```

**The player grabs a gem. How much does the score go up?**

<div class="write-space"></div>

---

## 2 · Read the Dictionary 🗂️

A coin is `{"rect": pygame.Rect(450, 250, 20, 20), "kind": "secret", "value": 10}`. Fill in the blanks.

```
coin["kind"]   = ___
coin["value"]  = ___
coin["rect"].x = ___
```

<div class="write-space"></div>

**Why is a dictionary better than three separate lists (one for rects, one for kinds, one for values)?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — Every coin should add its own value, but all coins add 1 point no matter the kind.

```python
for coin in coins[:]:
    if player.colliderect(coin["rect"]):
        score = score + 1
        coins.remove(coin)
```

**Hint:** use `coin["value"]`, not a fixed `1`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The collision check should compare the player with the coin's rectangle, but it crashes saying a dict can't collide.

```python
for coin in coins[:]:
    if player.colliderect(coin):
        score += coin["value"]
```

**Hint:** the rect lives inside the dictionary under a key.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The coins should keep wobbling, but they spin once and then freeze.

```python
def draw_coin(coin, frame):
    wave = math.sin(frame * 0.1) * 8
    w = max(2, int(20 + wave))
    ...
# in the game loop:
frame = 0
draw_coin(coin, frame)
```

**Hint:** `frame` never increases, so `sin` never changes. Where should `frame` grow?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Add a Kind 🛠️

Start from your working coin types.

1. Add a fourth coin kind (for example a time bonus). Write its dictionary entry.

<div class="write-space"></div>

2. Reposition the secret coin so it fits *your* level. Where did you place it?

<div class="write-space"></div>

3. **Stretch:** make the spin faster for gems than for gold. Which number controls the speed?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Put three kinds of spinning coins into your own level — gold, gem, and a secret coin reachable only by a tricky jump.

When it works, send a **photo or video** collecting each kind, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I stored each coin as a dictionary so that …
>
> The different kinds add different points because …
>
> The spin works with `math.sin` by …
>
> The `max(2, ...)` stops the coin from …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video collecting all three kinds. Teach it to someone new. Try to use these words: **dictionary**, **kind**, **value**, **sin**, **spin**.

> 1. Show your gold, gem, and secret coins.
> 2. Collect each one and show the score jump by different amounts.
> 3. Read your `math.sin` line out loud and explain the wobble.
> 4. Show the secret coin and the jump to reach it.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
