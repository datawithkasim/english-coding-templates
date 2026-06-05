# 💬 RS001 Week 1 — English Worksheet

**Topic:** Talking to the Computer — Variables · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you start your adventure game. The computer **asks** the player a question with `game.ask()`, **remembers** the answer inside a **variable**, and **shows** it back with `game.say()`. A variable is just a labelled box that holds a value.

```python
name = game.ask("What is your name?")
game.say(f"Welcome, {name}! Your adventure begins.")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think the screen will show.

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

## 3 · 🎯 Build Your Opening

Open your game project. Write a short program that:

- asks the player for their **name**,
- uses a default name if they type nothing,
- prints a **welcome message** that uses their name,
- uses `\n` at least once so the intro is easy to read.

Make it your own — the forest, a castle, a spaceship, anything you like.

When it works, send a **photo or video** of your screen, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I asked the player for …
>
> I stored the answer in a variable called …
>
> If the player typed nothing, I …
>
> I used `\n` to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your program runs. Talk through it like you are teaching someone who has never seen code. Try to use these words: **variable**, **ask**, **say**, **f-string**, **new line**.

> 1. Run your program and answer your own question.
> 2. Point to the line that stores the answer in a variable.
> 3. Read your `f"..."` line out loud and say how the variable gets swapped in.
> 4. Show what happens when you type nothing.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
