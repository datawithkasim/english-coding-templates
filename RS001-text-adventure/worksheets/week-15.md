# 🧠 RS001 Week 15 — English Worksheet

**Topic:** Logic, Knowledge, and Multiple Endings · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week the ending depends on what the player **knows**, not on luck. You store riddles and answers in parallel lists, keep a **score**, and use the score to pick one of several endings.

```python
questions = ["I have four legs but cannot walk. What am I?"]
answers   = ["table"]
guess = game.ask(questions[0]).strip()
if guess == answers[0]:
    score = score + 1
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

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

## 3 · 🎯 Score-Based Endings

Open your game. Before the final scene, ask the player a few riddles using parallel question/answer lists. Count correct answers into a `score`, then use the score to print one of several different endings.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I stored my riddles and answers in …
>
> Each correct answer added to the score by …
>
> The endings I built were …
>
> A knowledge-based ending is different from a random one because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone). Teach it like the viewer has never coded. Try to use these words: **score**, **riddle**, **answer**, **ending**, **logic**.

> 1. Play once answering well and show the high-score ending.
> 2. Play again answering poorly and show a different ending.
> 3. Point to where the score goes up.
> 4. Explain why the ending depends on knowledge, not luck.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
