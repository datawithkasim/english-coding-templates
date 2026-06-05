# 🪙 RS004 Week 11 — English Worksheet

**Topic:** Coins & Score · **Course:** Platformer Game · **Time:** about 45 minutes

This week your level gets **coins** to collect. You keep them in a list, check if the player touches one, **remove** it, and add to the **score**. Then you draw the score on the screen with `pygame.font`.

> Keep these words handy: **coin**, **collect**, **`remove()`**, **score**, **HUD (on-screen text)**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

## 4 · Place & Extend 🛠️

Start from your working coins and score.

1. Move one coin so it sits above a platform, reachable only by a jump. Write its position.

<div class="write-space"></div>

2. Change the score text colour and position. What did you pick?

<div class="write-space"></div>

3. **Stretch:** show a message when *all* coins are collected. How do you know the list is empty?

<div class="write-space"></div>

---

## 5 · Build & Show 📸

Add coins to your own level. Place several around the platforms, and make at least one a jump-only coin.

When it works, send a **photo or video** of collecting coins with the score going up, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I kept my coins in a list so that …
>
> When the player touches a coin, I …
>
> I loop over `coins[:]` because …
>
> The score shows on screen using …
>
> One tricky moment was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video of collecting coins. Teach it to someone new. Try to use these words: **coin**, **collect**, **remove**, **score**, **render**.

> 1. Show your coins placed in the level.
> 2. Collect a few and show the score climbing.
> 3. Read the collect-and-remove lines out loud and explain them.
> 4. Reach and collect the jump-only coin.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
