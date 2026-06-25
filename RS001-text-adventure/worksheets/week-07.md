# 🛡️ RS001 Week 7 — English Worksheet

**Topic:** Stopping Mistakes — Validating Input · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you think about how to check whether an answer is **allowed** before you act on it. `in` and `not in` test if a value is inside a list of valid choices. If the answer is wrong, you give a second chance — and if it is still wrong, you fall back to a safe default. In this worksheet you read code, fix code on paper, and explain the code you wrote in your live lesson.

> 🧠 Words to know: **valid**, **in**, **not in**, **retry**, **default**

---

## 1 · Predict 🔮

Read each piece of code. Picture what happens in your head, then write your answer.

```python
valid = ["left", "right"]
choice = "up"
game.say(choice in valid)
```

**`in` answers True or False. Which one is printed?**

<div class="write-space"></div>

```python
valid = ["left", "right"]
choice = "left"
if choice not in valid:
    game.say("not allowed")
else:
    game.say("allowed")
```

**Which message appears?**

<div class="write-space"></div>

```python
valid = ["left", "right"]
choice = game.ask("Where?").strip().lower()
if choice not in valid:
    choice = "left"
game.say(choice)
```

**The player types `"up"`. What value ends up in `choice`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

**Bug A** — This should warn the player when their choice is **not** valid. Right now the warning shows for valid answers instead.

```python
valid = ["left", "right"]
choice = game.ask("Where?").strip().lower()
if choice in valid:
    game.say("That is not a real direction.")
```

**Hint:** the warning belongs with `not in`, not `in`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — On a wrong answer, the player should get **one more try**. Right now a wrong answer just gives up with no second chance.

```python
valid = ["left", "right", "back"]
choice = game.ask("Where to?").strip().lower()
if choice not in valid:
    game.say("Not a valid way.")
game.say(f"Final: {choice}")
```

**Hint:** after the warning, ask again and store the new answer.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — If the answer is still wrong after the retry, the game should pick a safe **default** so it never breaks. Right now a wrong answer is used as-is.

```python
valid = ["left", "right"]
choice = game.ask("Where to?").strip().lower()
if choice not in valid:
    choice = game.ask("left or right?").strip().lower()
game.say(f"You move {choice}.")
```

**Hint:** add one more check that swaps in a default like `"left"` if it is still invalid.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working example. It validates a choice, gives one retry, then falls back to a safe default.

```python
valid = ["left", "right", "back"]
choice = game.ask("Where to?").strip().lower()
if choice not in valid:
    game.say("That is not a real direction.")
    choice = game.ask("Try again — left, right, or back?").strip().lower()
if choice not in valid:
    choice = "left"
game.say(f"You go {choice}.")
```

**What does the list `valid` hold, and why does the code need it?**

<div class="write-space"></div>

**What does `not in` check on the first `if` line?**

<div class="write-space"></div>

**Why is the player asked a second time inside the first `if`?**

<div class="write-space"></div>

**The second `if` runs after the retry. What does it do if the answer is still wrong?**

<div class="write-space"></div>

**If the player typed `"jump"` both times, what value reaches the last `game.say` line?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the validation code **you** wrote in today's live lesson. Record a short video on your phone (or a parent's phone). You may show your game running while you talk. Teach it like the viewer has never coded. Try to use these words: **valid**, **in**, **not in**, **retry**, **default**.

> First, I list my valid choices, which are …
>
> I use `in` (or `not in`) to check whether …
>
> When the player types something wrong, my game gives a retry by …
>
> If it is still wrong, my safe default is …

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
