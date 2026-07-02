# 🔀 Extra — If Statements: Intermediate

**Topic:** If / Elif / Else + and / or · **Course:** Extra Worksheet · **Time:** about 35 minutes

Conditions can check **more than one thing at once** with `and` and `or`. On paper you will read, predict, fix, and explain. Then you will write and run your own code in the IDE.

> Keep these words handy: **and**, **or**, **condition**, **elif**, **boolean**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will print.

```python
age = 13
has_ticket = True

if age >= 12 and has_ticket:
    print("Welcome in!")
else:
    print("Sorry, can't enter.")
```

**What prints? Which part of the condition is checked first — `age`, `has_ticket`, or both?**

<div class="write-space"></div>

```python
score = 4
lives = 0

if score > 10 or lives > 0:
    print("Still playing")
else:
    print("Game over")
```

**What prints? Why does `or` only need one side to be true?**

<div class="write-space"></div>

```python
name = "Kasim"
level = 5

if name == "Kasim" and level >= 3:
    print("VIP access")
elif level >= 3:
    print("Regular access")
else:
    print("No access")
```

**What prints? What would print if `name` was `"Dami"` instead?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should let a player in only if they are 12 or older **and** have a ticket. Right now it lets anyone in who is 12 or older, ticket or not.

```python
age = 14
has_ticket = False

if age >= 12 or has_ticket:
    print("Welcome in!")
```

**Hint:** think about what `or` needs versus what `and` needs.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should print "Pass" for a score of `60` or higher, and "Fail" below that. A score of exactly `60` prints "Fail" — that's wrong.

```python
score = 60

if score > 60:
    print("Pass")
else:
    print("Fail")
```

**Hint:** should `60` count as a pass?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

```python
temp = 22
is_raining = False

if temp >= 25 and not is_raining:
    print("Go to the beach")
elif temp >= 15 and not is_raining:
    print("Go for a walk")
else:
    print("Stay inside")
```

**What prints when `temp` is `22` and `is_raining` is `False`? Walk through each condition it checks.**

<div class="write-space"></div>

**What would print if `is_raining` was `True` instead? What changes?**

<div class="write-space"></div>

**What does `not is_raining` mean in plain English?**

<div class="write-space"></div>

---

## 4 · Code It 💻

Open the IDE at **app.english-coding.co.uk** and write your own program.

Write code that:
- stores a variable `score`
- stores a variable `is_bonus_round` (`True` or `False`)
- prints `"Big win!"` if `score >= 50` **and** `is_bonus_round` is `True`
- prints `"Nice score"` if `score >= 50` **and** `is_bonus_round` is `False`
- prints `"Try again"` otherwise

Test it with at least 2 different sets of values. Run it, then write what you tested and what printed.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + a screenshot of your working code to teacher on KakaoTalk.
