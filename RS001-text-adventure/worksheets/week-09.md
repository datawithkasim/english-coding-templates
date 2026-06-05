# 🔀 RS001 Week 9 — English Worksheet

**Topic:** Cause and Effect — Enemies Appear · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week one choice changes what happens next. `if` / `else` lets you run different code depending on the player's path — so the **left** road meets a goblin and the **right** road meets an orc.

```python
path = game.ask("Which way? (left/right)").strip().lower()
if path == "left":
    enemy = "goblin"
else:
    enemy = "orc"
game.say(f"A {enemy} appears!")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

```python
path = "left"
if path == "left":
    game.say("cave")
else:
    game.say("field")
```

**Which word is printed?**

<div class="write-space"></div>

```python
paths = ["left", "right"]
enemies = ["goblin", "orc"]
path = "right"
if path == paths[0]:
    game.say(enemies[0])
elif path == paths[1]:
    game.say(enemies[1])
```

**Which enemy is printed, and which branch ran?**

<div class="write-space"></div>

```python
path = "up"
if path == "left":
    game.say("goblin")
elif path == "right":
    game.say("orc")
```

**The player typed `"up"`. What appears on screen?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — Left should give a goblin and right should give an orc. Right now **both** paths give a goblin.

```python
path = game.ask("way?").strip().lower()
if path == "left":
    enemy = "goblin"
if path == "right":
    enemy = "goblin"
game.say(f"A {enemy} appears!")
```

**Hint:** the second branch has the wrong enemy.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The second branch should be an `elif`, not a fresh `if`, so the two choices are linked as one decision.

```python
path = game.ask("way?").strip().lower()
if path == "left":
    game.say("A goblin blocks the cave.")
else path == "right":
    game.say("An orc roams the field.")
```

**Hint:** the word after the first branch should be `elif`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The enemy's name and HP should come from the **same** index. Here the name is from the left path but the HP is from the right.

```python
paths = ["left", "right"]
enemies = ["goblin", "orc"]
enemy_hp = [10, 25]
path = "left"
if path == paths[0]:
    game.say(f"{enemies[0]} (HP {enemy_hp[1]})")
```

**Hint:** match the index across all three lists.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · 🎯 Branch Your Story

Open your game. After your validated path choice, make the path **matter**: each direction should meet a different enemy. Use `if` / `else` (or `elif`) and describe each encounter so it feels different.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I asked the player to choose a path, and …
>
> If they went left, the game …
>
> If they went right, the game …
>
> The cause was the choice and the effect was …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your game runs. Teach it like the viewer has never coded. Try to use these words: **if**, **else**, **branch**, **cause**, **effect**.

> 1. Run your game and take the left path.
> 2. Run it again and take the right path.
> 3. Show that each choice leads to a different enemy.
> 4. Read your `if` / `else` out loud and explain which branch runs when.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
