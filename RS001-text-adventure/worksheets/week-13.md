# 🎲 RS001 Week 13 — English Worksheet

**Topic:** Chance and Randomness · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week is about thinking through and explaining code that makes a game unpredictable. `random.choice()` picks one item from a list at random, so every play is different — random weapons, random battle results, random rewards. You must `import random` first. Read the code closely and explain in your own words how it works.

> 🧠 Words to know: **random**, **import**, **choice**, **chance**, **different**

```python
import random
rewards = ["gold", "potion", "magic ring", "old boots"]
prize = random.choice(rewards)
game.say(f"You found: {prize}")
```

---

## 1 · Predict 🔮

Read each piece of code. In your head, work out what it does, then write what you think happens.

```python
import random
weapons = ["sword", "bow", "wand"]
chosen = random.choice(weapons)
game.say(chosen)
```

**Will the same word print every time? Why or why not?**

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

**Roughly how often would each message show if this ran many times?**

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Read this working example carefully, then answer the questions below in your own words.

```python
import random
rewards = ["gold", "potion", "magic ring", "old boots"]
prize = random.choice(rewards)
game.say(f"You found: {prize}")
```

**What does the first line, `import random`, do for the rest of the code?**

<div class="write-space"></div>

**What is stored inside `rewards`, and how many items could be picked?**

<div class="write-space"></div>

**In your own words, what does `random.choice(rewards)` give back?**

<div class="write-space"></div>

**Why does `prize` hold a different word each time the code runs?**

<div class="write-space"></div>

**What would the player see if `random.choice` picked `"potion"`?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Take a short video on your phone (or a parent's phone) explaining the code **you wrote in today's live lesson**. You can show it running. Teach it like the viewer has never coded. Try to use these words: **random**, **import**, **choice**, **chance**, **different**.

> 1. Show the code you wrote in the lesson and read out your `random.choice(...)` line.
> 2. Explain what list it picks from at random.
> 3. Show it running, or describe two different results it can give.
> 4. Explain why the same code can give a different answer by chance.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
