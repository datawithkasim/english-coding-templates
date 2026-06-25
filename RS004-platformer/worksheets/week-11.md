# 🪙 RS004 Week 11 — English Worksheet

**Topic:** Coins & Score · **Course:** Platformer Game · **Time:** about 45 minutes

This week is about **reading and explaining** the coin code you wrote in your live lesson. You keep coins in a list, check if the player touches one, **remove** it, and add to the **score**. Then you draw the score on screen with `pygame.font`. Here you think about how that code works and explain it in your own words.

> Keep these words handy: **coin**, **collect**, **`remove()`**, **score**, **HUD (on-screen text)**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it does.

```python
for coin in coins[:]:
    if player.colliderect(coin):
        coins.remove(coin)
        score = score + 1
```

**The player touches a coin. What two things happen?**

<div class="write-space"></div>

```python
score_text = font.render(f"점수: {score}", True, (0, 0, 0))
screen.blit(score_text, (10, 10))
```

**Where on the screen does the score appear? What does `render` make?**

<div class="write-space"></div>

```python
for coin in coins[:]:
```

**Why loop over `coins[:]` (a copy) instead of `coins` while removing items?**

<div class="write-space"></div>

---

## 2 · Trace the Score 🔢

The player collects coins one by one. Fill in the score after each step. Start with `score = 0` and 3 coins.

```
collect coin 1:  score = ___   coins left = ___
collect coin 2:  score = ___   coins left = ___
collect coin 3:  score = ___   coins left = ___
```

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — Touching a coin should remove it and add a point. Right now the score goes up but the coin stays, so it scores forever.

```python
for coin in coins[:]:
    if player.colliderect(coin):
        score = score + 1
```

**Hint:** the coin is never removed from the list.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Removing coins while looping over the original list skips some coins and may crash.

```python
for coin in coins:
    if player.colliderect(coin):
        coins.remove(coin)
        score += 1
```

**Hint:** loop over a *copy* of the list while you remove from the real one.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The score should show on screen, but nothing appears even though `score` is going up.

```python
score_text = font.render(f"점수: {score}", True, (0, 0, 0))
```

**Hint:** rendering the text isn't enough — you must `blit` it onto the screen.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working coins-and-score code, then answer the questions about it.

```python
coins = [pygame.Rect(200, 300, 16, 16), pygame.Rect(420, 180, 16, 16)]
score = 0
font = pygame.font.SysFont(None, 36)

for coin in coins[:]:
    if player.colliderect(coin):
        coins.remove(coin)
        score = score + 1

score_text = font.render(f"점수: {score}", True, (0, 0, 0))
screen.blit(score_text, (10, 10))
```

**What kind of data structure holds the coins, and what is each coin?**

<div class="write-space"></div>

**What does `player.colliderect(coin)` check, and when is it `True`?**

<div class="write-space"></div>

**What two things happen inside the `if` when a coin is touched?**

<div class="write-space"></div>

**Why does the loop use `coins[:]` instead of `coins`?**

<div class="write-space"></div>

**What is the difference between `font.render(...)` and `screen.blit(...)`?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the coins-and-score code **you wrote in today's lesson**. Record a short phone video. You may show it running. Try to use these words: **coin**, **collect**, **remove**, **score**, **render**.

> 1. Show your coins placed in the level.
> 2. Collect a few and show the score climbing.
> 3. Read your collect-and-remove lines out loud and explain them.
> 4. Explain how your score gets drawn on screen.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
