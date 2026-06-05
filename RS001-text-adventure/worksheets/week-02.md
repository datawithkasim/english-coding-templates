# 🦸 RS001 Week 2 — English Worksheet

**Topic:** Variables Go Deeper — A Rich Opening · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you keep last week's code and **add more variables**. Your hero gets a name, a weapon, and a hometown — and your opening scene grows. Every variable that could be empty gets a safe default.

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

Read each piece of code. Before you run it in your head, write what you think the screen will show.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

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

## 3 · 🎯 Grow Your Opening

Open your game from last week. **Do not delete it.** On top of it, add:

- a **weapon** variable and a **hometown** variable, each with a safe default,
- one variable of **your own** (favourite colour, animal, food …) that appears in the opening,
- a multi-line opening that uses all your variables.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I kept last week's code and added …
>
> My own extra variable was …
>
> I gave every variable a default so that …
>
> I made the opening easier to read by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your opening runs. Teach it like the viewer has never coded. Try to use these words: **variable**, **default**, **empty**, **f-string**, **opening**.

> 1. Run your opening and answer your own questions.
> 2. Point to each variable and say what it stores.
> 3. Show what happens when you leave one answer empty.
> 4. Read your final sentence and say which variables got swapped in.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
