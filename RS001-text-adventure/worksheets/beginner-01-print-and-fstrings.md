# 🖨️ Beginner 1 — print() and f-strings

**Topic:** Showing words on the screen · **Course:** Text Adventure (Python) · **Time:** about 40 minutes

This is your first worksheet. You do not need a computer for most of it. You read code, guess what the screen shows, and fix small mistakes on paper.

> 🧠 Words to know: **print**, **variable**, **f-string**, **quotes**, **output**

```python
print("Hello!")                 # screen shows:  Hello!

name = "Amy"
print(f"Hi {name}")             # screen shows:  Hi Amy

print("Hi {name}")              # screen shows:  Hi {name}
```

The little **f** is what swaps the box for its value.

---

## 1 · Warm Up ⭕

**Which line puts words on the screen? Circle one:** `name = "Amy"` · `print("Amy")`

**Which line makes a variable? Circle one:** `print("hp")` · `hp = 100`

**Which line needs an `f`? Circle one:** `print("Hello!")` · `print("Hello {name}")`

---

## 2 · Predict 🔮

Read the code. Write exactly what the screen shows.

```python
name = "Warrior"
health = 100
print(f"{name} has {health} health")
```

**What appears on screen?**

<div class="write-space"></div>

```python
first = "Dark"
second = "Knight"
print(first + second)
```

**What appears on screen? Look carefully at the spaces.**

<div class="write-space"></div>

```python
damage = 20
bonus = 5
print(f"Total damage: {damage + bonus}")
```

**What number appears?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each one is broken. Write the fixed line.

**Bug A** — This should show `Hello, Amy!` but it shows `Hello, {name}!`

```python
name = "Amy"
print("Hello, {name}!")
```

**Write the fixed line:**

<div class="write-space"></div>

**Bug B** — This should show the word `Sword` but Python gives an error.

```python
print(Sword)
```

**Write the fixed line:**

<div class="write-space"></div>

**Bug C** — This should show `Level 5` but Python gives an error.

```python
level = 5
print(f"Level {level}"
```

**Write the fixed line:**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this small program.

```python
hero = "Mina"
potions = 3
print(f"{hero} the brave")
print(f"You carry {potions} potions.")
```

**Which two lines make a variable? Write their names.**

<div class="write-space"></div>

**What does `{hero}` turn into on the screen?**

<div class="write-space"></div>

**How many lines appear on the screen when you run this?**

<div class="write-space"></div>

**Change `potions` to `7`. What is different on the screen?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Record a short video on your phone (or a parent's phone). Show the code you wrote in your lesson and talk about it. Try to use these words: **print**, **variable**, **f-string**.

> 1. Read out one `print` line from your code.
> 2. Point to a **variable** and say its name.
> 3. Read an `f"..."` line and say what gets swapped in.

---

### Submit ✅

Send a photo of this worksheet and your video to teacher on KakaoTalk.
