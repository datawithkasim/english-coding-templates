# 💬 RS001 Week 1 — English Worksheet

**Topic:** Talking to the Computer — Variables · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you think about how an adventure game talks to the player. The computer **asks** a question with `game.ask()`, **remembers** the answer inside a **variable**, and **shows** it back with `game.say()`. A variable is just a labelled box that holds a value. On this worksheet you read code, predict what it does, fix broken code on paper, and explain the code you wrote in your live lesson.

> 🧠 Words to know: **variable**, **ask**, **say**, **f-string**, **new line**

```python
name = game.ask("What is your name?")
game.say(f"Welcome, {name}! Your adventure begins.")
```

---

## 1 · Predict 🔮

Read each piece of code. In your head, work out what the screen will show, then write your prediction.

```python
hero = game.ask("Hero name?")
game.say(f"Hello {hero}")
```

**The player types `Mina`. What appears on screen?**

<div class="write-space"></div>

```python
hero = game.ask("Hero name?")
game.say("Hello {hero}")
```

**This one has no `f` before the quotes. How is the output different from the one above?**

<div class="write-space"></div>

```python
weapon = game.ask("Pick a weapon")
if weapon == "":
    weapon = "rusty sword"
game.say(f"You hold a {weapon}.")
```

**The player just presses enter without typing anything. What weapon do they end up with? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — The code should greet the player by the name they typed. Right now it always prints the word `name` instead of their answer.

```python
name = game.ask("What is your name?")
game.say(f"Welcome, name!")
```

**Hint:** the variable only gets swapped in when it is inside `{ }`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — If the player types nothing, the game should call them `brave traveller`. Right now an empty answer slips through and the greeting looks empty.

```python
name = game.ask("What is your name?")
game.say(f"Welcome, {name}!")
```

**Hint:** check for an empty answer with `if name == "":` *before* you say the greeting.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The intro should print on **three separate lines**. Right now it all runs together on one line.

```python
game.say("Welcome! You enter a dark forest. Two paths lie ahead.")
```

**Hint:** `\n` means "new line". Where would you put it to split the sentence?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working opening program carefully. It asks for a name, uses a default if the player types nothing, and prints a welcome message split across lines.

```python
name = game.ask("What is your name?")
if name == "":
    name = "brave traveller"
game.say(f"Welcome, {name}!\nYou enter a dark forest.\nTwo paths lie ahead.")
```

**Which line stores the player's answer, and what is the variable called?**

<div class="write-space"></div>

**What does the `if name == "":` line do, and when does it run?**

<div class="write-space"></div>

**In the last line, what gets swapped in where `{name}` is written?**

<div class="write-space"></div>

**There are two `\n` marks in the last line. What do they do to the output?**

<div class="write-space"></div>

**If the player just presses enter without typing, what name appears on screen?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In your live lesson you wrote your own opening for your adventure game. Now explain **the code you wrote** in a short video on your phone (or a parent's phone). You may show it running. Talk through it like you are teaching someone who has never seen code, and try to use these words: **variable**, **ask**, **say**, **f-string**, **new line**.

> 1. Read out the line where you used `ask` to get the player's answer.
> 2. Point to the **variable** that stores the answer and say its name.
> 3. Read your `f"..."` line and say how the variable gets swapped in.
> 4. Show or explain what happens when the player types nothing.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
