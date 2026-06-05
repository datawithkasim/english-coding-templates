# 🎲 RS001 Week 13 — English Worksheet

**Topic:** Chance and Randomness · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week your game stops being predictable. `random.choice()` picks one item from a list at random, so every play is different — random weapons, random battle results, random rewards. You must `import random` first.

```python
import random
rewards = ["gold", "potion", "magic ring", "old boots"]
prize = random.choice(rewards)
game.say(f"You found: {prize}")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

```python
import random
weapons = ["sword", "bow", "wand"]
chosen = random.choice(weapons)
game.say(chosen)
```

**Will the same word print every time you run it? Why or why not?**

<div class="write-space"></div>

```python
import random
outcomes = ["win", "lose"]
result = random.choice(outcomes)
if result == "win":
    game.say("Victory!")
else:
    game.say("Defeat...")
```

**Roughly how often would each message show if you ran this many times?**

<div class="write-space"></div>

```python
weapons = ["sword", "bow", "wand"]
chosen = random.choice(weapons)
game.say(chosen)
```

**This code forgot something at the top. What error appears when it runs?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — This should pick a random reward, but it forgot to bring in the random tool, so it crashes on the first line that uses it.

```python
rewards = ["gold", "potion", "ring"]
prize = random.choice(rewards)
game.say(f"You won {prize}")
```

**Hint:** one line is missing at the very top.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should pick **one** random reward from the list. Right now it prints the whole list instead of a single item.

```python
import random
rewards = ["gold", "potion", "ring"]
game.say(f"You won {rewards}")
```

**Hint:** you need `random.choice(...)` to pull one item out.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The battle result should be **random**, so it can go either way. Right now it always wins, because the result is fixed instead of chosen.

```python
import random
outcomes = ["win", "lose"]
result = "win"
if result == "win":
    game.say("You won!")
else:
    game.say("You lost...")
```

**Hint:** use `random.choice(outcomes)` to decide `result`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · 🎯 Add Some Luck

Open your game. Add randomness somewhere it makes the game more fun: a random reward after a battle, or a boss fight whose result is decided by chance. Run it a few times to see the difference.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I added `import random` and used it to …
>
> The list I picked from at random was …
>
> When I ran the game twice, I got …
>
> Randomness makes the game better because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone). Run your game **twice** so the random part comes out differently each time. Teach it like the viewer has never coded. Try to use these words: **random**, **import**, **choice**, **chance**, **different**.

> 1. Run your game once and show the random result.
> 2. Run it again and show a different random result.
> 3. Point to your `random.choice(...)` line.
> 4. Explain why the same code can give different answers.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
