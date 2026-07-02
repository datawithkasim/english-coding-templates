# 🔀 Extra — If Statements: Only Sometimes

**Topic:** If / Elif / Else · **Course:** Extra Worksheet · **Time:** about 30 minutes

Some code runs **every time**. Some code runs **only if** something is true. On paper you will read `if` code, predict it, fix it, and explain it in your own words.

> Keep these words handy: **condition**, **`==`**, **`else`**, **`elif`**, **indent**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will print.

```python
score = 7
if score > 5:
    print("You win!")
```

**Does "You win!" print? Why?**

<div class="write-space"></div>

```python
age = 10
if age == 12:
    print("You are 12.")
else:
    print("You are not 12.")
```

**What prints?**

<div class="write-space"></div>

```python
weather = "rain"
if weather == "sun":
    print("Wear sunglasses")
elif weather == "rain":
    print("Bring umbrella")
else:
    print("Just go outside")
```

**What prints? Why did it skip the first line?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should check if `score` equals `10`. Instead it always prints "Perfect!", even when `score` is `3`.

```python
score = 3
if score = 10:
    print("Perfect!")
```

**Hint:** checking equal uses two of something.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should print "Too cold" only when `temp` is below `0`. Right now it prints "Too cold" no matter what `temp` is.

```python
temp = 15
if temp < 0:
print("Too cold")
```

**Hint:** the line inside the `if` needs to be pushed in.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Here is a complete program that checks a player's score and prints a message.

```python
score = 8

if score >= 9:
    print("A+ player!")
elif score >= 5:
    print("Good job!")
else:
    print("Keep practicing!")
```

**What prints when `score` is `8`? Walk through why it picks that branch.**

<div class="write-space"></div>

**What would print if `score` was `9`? What about `2`?**

<div class="write-space"></div>

**Why does the program stop checking once it finds a true condition?**

<div class="write-space"></div>

---

### Submit ✅

Send this worksheet to teacher on KakaoTalk.
