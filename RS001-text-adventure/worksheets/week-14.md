# 🌀 RS001 Week 14 — English Worksheet

**Topic:** Random Encounters + a Bigger Reward Pool · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week is about thinking through randomness and explaining it in your own words. Each path draws a random enemy from its own pool, rewards come from a big pool, and a surprise encounter fires only **some** of the time using a weighted `True`/`False` pick. You will read code, fix a broken version on paper, then explain the game you wrote in your live lesson.

> 🧠 Words to know: **random**, **pool**, **encounter**, **odds**, **different**

```python
import random
left_enemies = ["goblin", "bat", "spider"]
enemy = random.choice(left_enemies)

if random.choice([True, False, False]):   # about 1 in 3
    game.say("A bandit jumps out!")
```

---

## 1 · Predict 🔮

Read each piece of code. Run it in your head and write what you think happens.

```python
import random
left_enemies = ["goblin", "bat", "spider"]
enemy = random.choice(left_enemies)
game.say(f"You meet a {enemy}.")
```

**Can you say for sure which enemy appears? Why or why not?**

<div class="write-space"></div>

```python
import random
if random.choice([True, False, False]):
    game.say("ambush!")
else:
    game.say("quiet path")
```

**Out of the three items, how many are `True`? About how often does "ambush!" show?**

<div class="write-space"></div>

```python
import random
if random.choice([True, True, True, False]):
    game.say("rare event")
```

**How does changing the mix of True/False change how often the event happens?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

**Bug A** — Each path should draw from its **own** enemy pool. Right now both paths draw from the same list, so left and right feel identical.

```python
import random
left_enemies = ["goblin", "bat"]
right_enemies = ["orc", "troll"]
path = "right"
if path == "left":
    enemy = random.choice(left_enemies)
else:
    enemy = random.choice(left_enemies)
game.say(enemy)
```

**Hint:** the right path should pull from `right_enemies`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A rare event should fire only about 1 in 3 times. Right now the mix makes it fire almost every time.

```python
import random
if random.choice([True, True, False]):
    game.say("A rare treasure glows nearby!")
```

**Hint:** to make `True` rarer, change how many `True` vs `False` are in the list.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The reward pool should hold several rewards so the pick feels varied. Right now the list has only one item, so it is the "same random" every time.

```python
import random
rewards = ["gold"]
reward = random.choice(rewards)
game.say(f"You found {reward}")
```

**Hint:** a one-item pool always returns that one item — give it more choices.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working example. It picks a random enemy from the path's own pool, draws a reward from a bigger pool, and fires a surprise encounter only some of the time.

```python
import random

left_enemies = ["goblin", "bat", "spider"]
right_enemies = ["orc", "troll", "wolf"]
rewards = ["gold", "potion", "map", "gem", "key"]

path = "left"
if path == "left":
    enemy = random.choice(left_enemies)
else:
    enemy = random.choice(right_enemies)
game.say(f"A {enemy} blocks the path!")

reward = random.choice(rewards)
game.say(f"You won a {reward}.")

if random.choice([True, False, False]):   # about 1 in 3
    game.say("A bandit jumps out!")
```

**Which list does the enemy come from when `path` is `"left"`?**

<div class="write-space"></div>

**Why does the `reward` line give a different result on different playthroughs?**

<div class="write-space"></div>

**Look at `[True, False, False]`. About how often does the bandit appear?**

<div class="write-space"></div>

**If you wanted the bandit to appear more often, how would you change that list?**

<div class="write-space"></div>

**In your own words, why does this code make every playthrough feel different?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Take a short video on your phone (or a parent's phone) and explain the game **you** wrote in today's live lesson. You can show it running. Teach it like the viewer has never coded. Try to use these words: **random**, **pool**, **encounter**, **odds**, **different**.

> 1. Point to your enemy pools and say what is in each path's pool.
> 2. Show your reward pool and play once so a random reward appears.
> 3. Point to your weighted `True/False` line and explain the odds of the surprise encounter.
> 4. Say why every playthrough now feels different.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
