# 🏆 RS001 Week 16 — English Worksheet

**Topic:** Everything Together — The Finished Game · **Course:** Text Adventure (Python) · **Time:** about 60 minutes

This is the final week. You bring together **every** idea from weeks 1–15 into one game: variables, lists, cleaned and validated input, branching, battle functions, randomness, an inventory, and a score-based ending. Then you present it.

```python
if score == 3 and "golden key" in backpack and "gem" in backpack:
    ending = "King ending — every secret and treasure is yours!"
elif score == 3 and ("golden key" in backpack or "map" in backpack):
    ending = "Sage ending — you solved the riddles and found the way."
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

```python
backpack = ["sword", "map"]
if "map" in backpack:
    game.say("You unfold the map.")
else:
    game.say("You are lost.")
```

**Which message appears?**

<div class="write-space"></div>

```python
score = 3
backpack = ["golden key"]
if score == 3 and "golden key" in backpack:
    game.say("Best ending!")
else:
    game.say("Another ending.")
```

**`and` needs both sides true. Which message appears?**

<div class="write-space"></div>

```python
score = 3
backpack = ["map"]
if score == 3 and ("golden key" in backpack or "map" in backpack):
    game.say("Sage ending")
```

**`or` needs only one side true. Does the sage ending print? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — A reward won in battle should be added to the inventory. Right now the reward is named but never goes into the backpack.

```python
backpack = ["sword"]
reward = "golden key"
game.say(f"You won a {reward}!")
game.say(f"Bag: {backpack}")
```

**Hint:** use `backpack.append(reward)` to add it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The best ending should need **both** a perfect score **and** the golden key. Right now it uses `or`, so it fires too easily.

```python
score = 1
backpack = ["golden key"]
if score == 3 or "golden key" in backpack:
    game.say("King ending — perfect run!")
else:
    game.say("A smaller ending.")
```

**Hint:** swap `or` for `and` so both conditions must be true.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The endings should be checked from **best to worst**, so the rarest one is found first. Right now a low-bar ending is checked first and steals every player.

```python
if score >= 1:
    ending = "Adventurer ending"
elif score == 3 and "golden key" in backpack:
    ending = "King ending"
game.say(ending)
```

**Hint:** put the strictest condition (the King ending) at the top.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · 🎯 Finish Your Game

Open your game. Make sure all the pieces are connected into one flow, start to finish:

- a hero built from variables,
- a cleaned, validated path choice,
- at least one battle using your `fight()` function,
- some randomness (enemy, reward, or encounter),
- an inventory the player fills,
- a score from riddles,
- a final ending chosen with `and` / `or` from the score and the inventory.

Then play it all the way through at least once. When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made sure my game flowed from the opening to …
>
> The piece I am proudest of is …
>
> My endings split based on …
>
> The hardest bug to fix was …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 380px"></div>

---

## 4 · Record Your Presentation 🎥

Record a full play-through on your phone (or a parent's phone) and present your game. Teach it like the viewer has never coded. Try to use these words: **variable**, **function**, **random**, **inventory**, **ending**.

> 1. Play your game from start to finish.
> 2. Show one or two pieces of code you are most proud of and say what they do.
> 3. Tell us the hardest bug you hit and how you solved it.
> 4. Say one thing you would change if you built it again.

**Write what you will say in your presentation.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 380px"></div>

---

### Submit ✅

Send this worksheet + your full play-through video (and your code) to teacher on KakaoTalk.
