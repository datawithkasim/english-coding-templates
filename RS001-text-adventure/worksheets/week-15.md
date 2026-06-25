# 🧠 RS001 Week 15 — English Worksheet

**Topic:** Logic, Knowledge, and Multiple Endings · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week the ending depends on what the player **knows**, not on luck. In your live lesson you built code that stores riddles and answers in parallel lists, keeps a **score**, and uses the score to pick one of several endings. This worksheet is about reading and explaining that code in your own words.

> 🧠 Words to know: **score**, **riddle**, **answer**, **ending**, **logic**

```python
questions = ["I have four legs but cannot walk. What am I?"]
answers   = ["table"]
guess = game.ask(questions[0]).strip()
if guess == answers[0]:
    score = score + 1
```

---

## 1 · Predict 🔮

Read each piece of code. Work it out in your head and write what you think happens. Do not run it.

```python
score = 0
score = score + 1
score = score + 1
game.say(score)
```

**What number is printed?**

<div class="write-space"></div>

```python
questions = ["cold and melts fast?", "rains and it opens?"]
answers   = ["ice", "umbrella"]
guess = "ice"
if guess == answers[0]:
    game.say("correct")
else:
    game.say("wrong")
```

**Which message appears?**

<div class="write-space"></div>

```python
score = 2
if score == 3:
    game.say("perfect")
elif score == 2:
    game.say("great")
else:
    game.say("keep trying")
```

**Which ending prints, and why does the first branch get skipped?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

**Bug A** — A correct answer should add **one** to the score. Right now the score never goes up, because the result of the addition is thrown away.

```python
score = 0
guess = "table"
answer = "table"
if guess == answer:
    score + 1
game.say(score)
```

**Hint:** store the new total back into `score` with `score = score + 1`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The riddle and its answer should share the **same** index. Here question 0 is checked against answer 1, so a correct guess is marked wrong.

```python
questions = ["four legs, cannot walk?", "cold, melts fast?"]
answers   = ["table", "ice"]
guess = game.ask(questions[0]).strip()
if guess == answers[1]:
    game.say("correct")
else:
    game.say("wrong")
```

**Hint:** match the answer index to the question index.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The endings should split by score: 3 = wise, 2 = hero, else = beginner. Right now every score over 0 gives the same ending, because separate `if`s overwrite each other.

```python
score = 3
if score >= 1:
    ending = "beginner"
if score >= 2:
    ending = "hero"
if score == 3:
    ending = "wise"
game.say(ending)
```

**Hint:** use `if` / `elif` / `else` and check the **highest** score first.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

This is a working version of the score-based ending code, like the one from your lesson. Read it carefully, then answer the questions below.

```python
questions = ["four legs, cannot walk?", "cold, melts fast?", "opens when it rains?"]
answers   = ["table", "ice", "umbrella"]
score = 0

for i in range(len(questions)):
    guess = game.ask(questions[i]).strip()
    if guess == answers[i]:
        score = score + 1

if score == 3:
    ending = "wise"
elif score == 2:
    ending = "hero"
else:
    ending = "beginner"

game.say("Your ending: " + ending)
```

**Why do `questions` and `answers` need to be the same length?**

<div class="write-space"></div>

**What does `answers[i]` give you on the second loop, when `i` is 1?**

<div class="write-space"></div>

**What is the largest number `score` can reach with this code, and why?**

<div class="write-space"></div>

**A player gets 2 riddles right. Which ending do they see, and which branch is checked first?**

<div class="write-space"></div>

**Why does this game give a fair ending based on knowledge, not luck?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Take a short video on your phone (or a parent's phone) explaining the score-based ending code **you** wrote in today's lesson. You may show it running. Teach it like the viewer has never coded. Try to use these words: **score**, **riddle**, **answer**, **ending**, **logic**.

> 1. Show your riddle and answer lists, and explain how they line up.
> 2. Point to the line where the score goes up, and say when it happens.
> 3. Show the different endings and explain what decides which one appears.
> 4. Explain why the ending depends on knowledge, not luck.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
