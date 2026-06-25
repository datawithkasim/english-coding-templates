# 🔀 RS001 Week 9 — English Worksheet

**Topic:** Cause and Effect — Enemies Appear · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week is about thinking through how one choice changes what happens next. `if` / `else` lets different code run depending on the player's path — so the **left** road meets a goblin and the **right** road meets an orc. You will read branching code, fix broken code on paper, and explain in your own words how a choice causes an effect.

> 🧠 Words to know: **if**, **else**, **elif**, **branch**, **cause**, **effect**

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

Read each piece of code. In your head, work out what happens, then write your answer.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Read this working example. The player chooses a path, and the choice decides which enemy appears.

```python
path = game.ask("Which way? (left/right)").strip().lower()
if path == "left":
    enemy = "goblin"
    game.say("A goblin blocks the cave.")
elif path == "right":
    enemy = "orc"
    game.say("An orc roams the field.")
else:
    enemy = "shadow"
    game.say("A shadow waits on an unknown road.")
game.say(f"A {enemy} appears!")
```

**What does `.strip().lower()` do to the player's answer, and why is that helpful here?**

<div class="write-space"></div>

**Which branch runs if the player types `right`? Which line of `enemy =` runs?**

<div class="write-space"></div>

**When does the `else` branch run?**

<div class="write-space"></div>

**The choice is the cause. What is the effect of choosing `left`?**

<div class="write-space"></div>

**Why does the last `game.say(...)` line run no matter which path the player picks?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote branching code for your own game. Make a short video on your phone (or a parent's phone) explaining the code you wrote. You may show it running. Teach it like the viewer has never coded, and use these words: **if**, **else**, **branch**, **cause**, **effect**.

> 1. Show the `if` / `else` code you wrote and read it out loud.
> 2. Explain which branch runs when the player goes left, and which runs when they go right.
> 3. Point out the cause (the choice) and the effect (the enemy that appears).
> 4. Show it running once for each path so the effect is clear.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
