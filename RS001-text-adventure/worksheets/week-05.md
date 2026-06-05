# 🧹 RS001 Week 5 — English Worksheet

**Topic:** Handling the Player's Choice — Cleaning Input · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you make your game forgiving. Players type messy answers — extra spaces, capital letters. `.strip()` removes spaces from the ends, and `.lower()` makes everything lowercase, so `" Left "`, `"LEFT"`, and `"left"` all match.

```python
choice = game.ask("Pick a path (left/right)")
choice = choice.strip().lower()
if choice == "left":
    game.say("You enter the dark cave...")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

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

## 3 · 🎯 Clean the Player's Choice

Open your game. At your shop or your first path choice, take the player's answer and clean it with `.strip().lower()` before you compare it. Then react differently depending on what they chose.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I asked the player to …
>
> Before comparing, I cleaned the answer by …
>
> I tested it by typing the answer with extra spaces, and …
>
> Cleaning input matters because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your game runs. Teach it like the viewer has never coded. Try to use these words: **strip**, **lower**, **clean**, **spaces**, **lowercase**.

> 1. Run your game and answer cleanly first.
> 2. Run it again and answer messily (CAPS and extra spaces).
> 3. Show that both answers lead to the same result.
> 4. Read the cleaning line out loud and explain what each part does.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
