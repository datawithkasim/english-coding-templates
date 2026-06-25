# 🧹 RS001 Week 5 — English Worksheet

**Topic:** Handling the Player's Choice — Cleaning Input · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week is about thinking through how a game becomes forgiving. Players type messy answers — extra spaces, capital letters. `.strip()` removes spaces from the ends, and `.lower()` makes everything lowercase, so `" Left "`, `"LEFT"`, and `"left"` all match. You will read code, fix code on paper, and explain the code you wrote in your live lesson.

> 🧠 Words to know: **strip**, **lower**, **clean**, **spaces**, **lowercase**

```python
choice = game.ask("Pick a path (left/right)")
choice = choice.strip().lower()
if choice == "left":
    game.say("You enter the dark cave...")
```

---

## 1 · Predict 🔮

Read each piece of code. In your head, work out what happens, then write your answer.

```python
choice = "  left  "
choice = choice.strip()
game.say(f"[{choice}]")
```

**The square brackets show exactly what is stored. What is printed inside them?**

<div class="write-space"></div>

```python
choice = "LEFT"
choice = choice.lower()
game.say(choice)
```

**What word appears on screen?**

<div class="write-space"></div>

```python
choice = game.ask("left or right?")
if choice == "left":
    game.say("cave")
else:
    game.say("field")
```

**The player types ` left ` with spaces around it. Which message shows — and is that what they wanted?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

**Bug A** — A player who types `"Left"` should be sent to the cave. Right now only an exact lowercase `"left"` works.

```python
choice = game.ask("left or right?")
if choice == "left":
    game.say("You enter the cave.")
else:
    game.say("You walk into the field.")
```

**Hint:** clean the answer with `.lower()` before you compare it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The cleaned answer should be **saved**. Right now `.strip()` runs but the spaces come back, because the result was thrown away.

```python
choice = game.ask("left or right?")
choice.strip()
if choice == "left":
    game.say("Cave!")
```

**Hint:** `.strip()` makes a clean copy — you have to store it back into the variable.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should accept `"Right"`, `"RIGHT"`, and `" right "` all the same. Right now it cleans the spaces but not the capitals.

```python
choice = game.ask("left or right?")
choice = choice.strip()
if choice == "right":
    game.say("Field!")
```

**Hint:** add one more cleaning step after `.strip()`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working example. It asks the player for a path, cleans the answer, then reacts differently depending on what they chose.

```python
choice = game.ask("Pick a path (left/right)")
choice = choice.strip().lower()
if choice == "left":
    game.say("You enter the dark cave...")
else:
    game.say("You walk into the open field.")
```

**What does `game.ask(...)` give back, and where is it stored?**

<div class="write-space"></div>

**The line `choice = choice.strip().lower()` does two cleaning jobs. What does each part do?**

<div class="write-space"></div>

**Why does the cleaning line come before the `if`, and not after?**

<div class="write-space"></div>

**The player types ` LEFT ` with capitals and spaces. After cleaning, what is stored in `choice`?**

<div class="write-space"></div>

**Which message shows for that player, and why?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In your live lesson you wrote code that cleans the player's choice. Now explain *your own* code in a short video on your phone (or a parent's phone). You may show it running. Teach it like the viewer has never coded, and use these key words: **strip**, **lower**, **clean**, **spaces**, **lowercase**.

> 1. Show the line where you ask the player for their choice.
> 2. Point to the cleaning step and explain what `.strip()` and `.lower()` each do.
> 3. Run it once with a clean answer, then once with CAPS and extra spaces, and show both give the same result.
> 4. Explain in your own words why cleaning the input matters.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
