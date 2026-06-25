# 🌳 RS001 Week 10 — English Worksheet

**Topic:** Deeper Branches — Path → Enemy → Reward · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you think about how one choice ripples forward. The path you pick decides the enemy, the **reward**, and the **next place** — and the reward then changes what happens after. Choices stack into a chain. On this worksheet you read code, find bugs on paper, and explain the code you wrote in today's live lesson.

> 🧠 Words to know: **branch**, **reward**, **next**, **chain**, **depends on**

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

Read each piece of code. Run it in your head and write what you think happens.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Read this working example. One path choice sets three things, and then a second branch reads the **reward** to change the next scene — two layers of cause and effect.

```python
path = game.ask("Which way? left or right").strip().lower()

if path == "left":
    enemy = "goblin"
    reward = "gold coin"
    next_place = "deep cave"
else:
    enemy = "spider"
    reward = "silver ring"
    next_place = "dark forest"

game.say(f"A {enemy} blocks the way! You win a {reward}.")

if reward == "gold coin":
    game.say("A merchant shows you a secret passage.")
elif reward == "silver ring":
    game.say("The ring glows and lights up the path ahead.")

game.say(f"You move on to the {next_place}.")
```

**On the first line, what does `.strip().lower()` do to the player's answer?**

<div class="write-space"></div>

**If the player types "right", which three values get set, and why?**

<div class="write-space"></div>

**Why does the second `if` use `reward` instead of `path` to decide the next scene?**

<div class="write-space"></div>

**Trace the "left" path: list every line `game.say` prints, in order.**

<div class="write-space"></div>

**Where in this code is the **chain** — where does one choice cause the next thing to happen?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Take a short video on your phone (or a parent's phone) and explain the code **you wrote in today's lesson**. You may show your game running. Teach it like the viewer has never coded. Try to use these words: **branch**, **reward**, **next**, **chain**, **depends on**.

> 1. Show the path choice in your code and say what three things it sets.
> 2. Read one branch out loud and explain what **depends on** what.
> 3. Show how the reward changes the **next** scene — point to the chain.
> 4. Run a different path and explain why a different chain happens.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
