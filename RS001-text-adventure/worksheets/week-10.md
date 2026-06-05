# 🌳 RS001 Week 10 — English Worksheet

**Topic:** Deeper Branches — Path → Enemy → Reward · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week one choice ripples forward. The path you pick decides the enemy, the **reward**, and the **next place** — and the reward then changes what happens after. Choices stack into a chain.

```python
if path == "left":
    enemy = "goblin"
    reward = "gold coin"
    next_place = "deep cave"

if reward == "gold coin":
    game.say("A merchant shows you a secret passage.")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

```python
path = "left"
if path == "left":
    reward = "map"
else:
    reward = "ring"
game.say(f"You won a {reward}.")
```

**Which reward is printed?**

<div class="write-space"></div>

```python
reward = "ring"
if reward == "coin":
    game.say("The merchant helps you.")
elif reward == "ring":
    game.say("The ring glows and reveals a hidden path.")
```

**Which message appears?**

<div class="write-space"></div>

```python
path = "right"
if path == "left":
    reward = "map"
game.say(f"You won a {reward}.")
```

**The player went right, but there is no `else`. What goes wrong on the last line?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — Both paths should set `reward`, so the line after always has a value. Right now only the left path sets it, so the right path crashes.

```python
path = game.ask("way?").strip().lower()
if path == "left":
    reward = "map"
game.say(f"You found a {reward}.")
```

**Hint:** add an `else` (or second branch) that also sets `reward`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The reward should change the **next** scene. Right now the second `if` checks the wrong reward name, so the special scene never fires.

```python
reward = "golden key"
game.say(f"You picked up a {reward}.")
if reward == "gold key":
    game.say("The key opens a hidden door.")
```

**Hint:** the name you store and the name you check must match exactly.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This three-way path should give each route its own enemy, reward, and next place. Right now the middle path reuses the left path's reward.

```python
path = "middle"
if path == "left":
    reward = "map"
elif path == "middle":
    reward = "map"
elif path == "right":
    reward = "ring"
game.say(f"Reward: {reward}")
```

**Hint:** the middle path should have a reward of its own.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · 🎯 Chain Your Choices

Open your game. Make the path choice set **three** things — the enemy, the reward, and the next place. Then add a second branch that reads the **reward** and changes the next scene. That is two layers of cause and effect.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, the path choice decided …
>
> The reward from that path was …
>
> Later, the reward changed the story because …
>
> I made sure every branch set the variables so that …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your game runs. Teach it like the viewer has never coded. Try to use these words: **branch**, **reward**, **next**, **chain**, **depends on**.

> 1. Run your game down one path and show the reward.
> 2. Show how that reward changes the next scene.
> 3. Run a different path and show a different chain.
> 4. Read one branch out loud and explain what depends on what.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
