# 🌀 RS001 Week 14 — English Worksheet

**Topic:** Random Encounters + a Bigger Reward Pool · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week randomness spreads through your whole game. Each path draws a random enemy from its own pool, rewards come from a big pool, and a surprise encounter fires only **some** of the time using a weighted `True`/`False` pick.

```python
import random
left_enemies = ["goblin", "bat", "spider"]
enemy = random.choice(left_enemies)

if random.choice([True, False, False]):   # about 1 in 3
    game.say("A bandit jumps out!")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

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

## 3 · 🎯 Make Every Playthrough Different

Open your game. Add at least three kinds of randomness: a random enemy per path, a reward drawn from a bigger pool, and a surprise encounter that fires only some of the time. Tune the odds so the surprise is not too common or too rare.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I gave each path its own enemy pool, which were …
>
> My reward pool had these items …
>
> My surprise encounter fired about … of the time.
>
> I tuned the odds by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone). Play your game at least **twice** so the differences show. Teach it like the viewer has never coded. Try to use these words: **random**, **pool**, **encounter**, **odds**, **different**.

> 1. Play once and narrate the enemy, reward, and any surprise.
> 2. Play again and show what came out differently.
> 3. Point to your weighted `True/False` line and explain the odds.
> 4. Say why every playthrough now feels fresh.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
