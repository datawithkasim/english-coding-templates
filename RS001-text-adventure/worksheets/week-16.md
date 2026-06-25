# 🏆 RS001 Week 16 — English Worksheet

**Topic:** Everything Together — The Finished Game · **Course:** Text Adventure (Python) · **Time:** about 60 minutes

This is the final week. In your live lesson you built one whole game out of **every** idea from weeks 1–15: variables, lists, cleaned and validated input, branching, battle functions, randomness, an inventory, and a score-based ending. This worksheet is for **thinking about** and **explaining** that code — reading it, predicting it, and finding bugs on paper. At the end you will present the finished game you built.

> 🧠 Words to know: **variable**, **function**, **random**, **inventory**, **ending**

```python
if score == 3 and "golden key" in backpack and "gem" in backpack:
    ending = "King ending — every secret and treasure is yours!"
elif score == 3 and ("golden key" in backpack or "map" in backpack):
    ending = "Sage ending — you solved the riddles and found the way."
```

---

## 1 · Predict 🔮

Read each piece of code. In your head, work out what happens, then write your answer.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

This is how a finished game decides its ending. Read it carefully, then answer the questions.

```python
backpack = ["golden key", "map"]
score = 3

if score == 3 and "golden key" in backpack and "gem" in backpack:
    ending = "King ending — every secret and treasure is yours!"
elif score == 3 and ("golden key" in backpack or "map" in backpack):
    ending = "Sage ending — you solved the riddles and found the way."
elif score >= 1:
    ending = "Adventurer ending — you made it out alive."
else:
    ending = "Lost ending — the dungeon keeps you."

game.say(ending)
```

**What two things does the `backpack` list hold at the start, and what number is in `score`?**

<div class="write-space"></div>

**The King ending needs three things to all be true. Why does this run NOT give the King ending?**

<div class="write-space"></div>

**Which ending does this code actually choose? Explain how Python reached it.**

<div class="write-space"></div>

**Why is the King ending checked before the Sage ending and not after?**

<div class="write-space"></div>

**What would the last line `game.say(ending)` print to the player?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Present the finished game you built across this course. Record a video on your phone (or a parent's phone): show the game **running**, then explain the key parts of the code in your own words. Teach it like the viewer has never coded. Try to use these words: **variable**, **function**, **random**, **inventory**, **ending**.

> 1. Play your finished game from start to finish so we can see it run.
> 2. Point to one or two pieces of code you are most proud of and say what they do.
> 3. Explain how your endings are chosen from the score and the inventory.
> 4. Tell us the hardest bug you hit and how you solved it.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your finished-game presentation video to teacher on KakaoTalk.
