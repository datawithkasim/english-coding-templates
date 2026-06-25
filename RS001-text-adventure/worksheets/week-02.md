# 🦸 RS001 Week 2 — English Worksheet

**Topic:** Variables Go Deeper — A Rich Opening · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you think about how more variables make an opening richer. Your hero gets a name, a weapon, and a hometown, and every variable that could be empty gets a safe default. You will read the code, debug it on paper, and explain the code you wrote in your live lesson.

> 🧠 Words to know: **variable**, **default**, **empty**, **f-string**, **opening**

```python
hero = game.ask("Hero's name?")
if hero == "":
    hero = "brave traveller"

weapon = game.ask("Starting weapon?")
if weapon == "":
    weapon = "rusty sword"

game.say(f"{hero}, you grip your {weapon} and set out.")
```

---

## 1 · Predict 🔮

Read each piece of code. Run it in your head and write what you think the screen will show.

```python
hero = "Mina"
weapon = "bow"
game.say(f"{hero} draws a {weapon}.")
```

**What single line appears on screen?**

<div class="write-space"></div>

```python
hometown = game.ask("Hometown?")
if hometown == "":
    hometown = "a village with no name"
game.say(f"You came from {hometown}.")
```

**The player types nothing. What town name ends up in the sentence?**

<div class="write-space"></div>

```python
hero = game.ask("Hero?")
if hero == "":
    hero = "brave traveller"
game.say(f"=== The Adventure Begins ===\n{hero}, your story starts now.")
```

**There is a `\n` in the middle. Sketch how the two lines look on screen.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

**Bug A** — Three variables (`hero`, `weapon`, `hometown`) should all appear in the final sentence. Right now `weapon` is spelled differently in two places, so it crashes.

```python
weapon = game.ask("Weapon?")
game.say(f"You carry a {weopon}.")
```

**Hint:** the name you store with and the name you print with must match **exactly**.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Every variable should fall back to a default when the player types nothing. Right now only `hero` is protected; `weapon` is left unsafe.

```python
hero = game.ask("Hero?")
if hero == "":
    hero = "brave traveller"

weapon = game.ask("Weapon?")
game.say(f"{hero} holds a {weapon}.")
```

**Hint:** `weapon` needs its own `if ... == "":` check.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The empty-check should match a truly **empty** answer. Right now it checks for a single space, so an empty answer is not caught.

```python
name = game.ask("Name?")
if name == " ":
    name = "brave traveller"
game.say(f"Welcome, {name}.")
```

**Hint:** `""` means nothing typed; `" "` means one space. Which one do you want here?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working opening carefully. It asks for two variables, gives each a safe default, then prints one sentence.

```python
hero = game.ask("Hero's name?")
if hero == "":
    hero = "brave traveller"

weapon = game.ask("Starting weapon?")
if weapon == "":
    weapon = "rusty sword"

game.say(f"{hero}, you grip your {weapon} and set out.")
```

**What does the variable `hero` store after the player answers?**

<div class="write-space"></div>

**What happens when the player leaves the weapon answer empty?**

<div class="write-space"></div>

**Why does the last line use an `f` before the quotes?**

<div class="write-space"></div>

**Which two values get swapped into the final sentence?**

<div class="write-space"></div>

**Why is it useful to give each variable a default?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the code **you wrote in today's live lesson**. Take a short video on your phone (or a parent's phone) and walk through your own opening. You may show it running. Teach it like the viewer has never coded, and use these words: **variable**, **default**, **empty**, **f-string**, **opening**.

> 1. Point to each variable you made and say what it stores.
> 2. Show which variables have a default and explain why.
> 3. Show what happens when you leave one answer empty.
> 4. Read your final sentence and say which variables got swapped in.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
