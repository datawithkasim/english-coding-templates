# 🧼 RS001 Week 6 — English Worksheet

**Topic:** Clean Every Input Safely · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you apply `.strip().lower()` to **every** `ask()` in your game, and you accept several spellings of the same answer — Korean, English, short forms — so almost any sensible input works.

```python
direction = game.ask("Which way? (left/right)")
direction = direction.strip().lower()
if direction in ["left", "l", "왼쪽"]:
    direction = "left"
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

```python
d = "  RIGHT "
d = d.strip().lower()
game.say(f"[{d}]")
```

**What is printed inside the brackets?**

<div class="write-space"></div>

```python
d = game.ask("way?")
d = d.strip().lower()
if d in ["left", "l", "왼쪽"]:
    d = "left"
game.say(d)
```

**The player types `L`. What single word is printed?**

<div class="write-space"></div>

```python
d = "Left"
d = d.lower().strip()
game.say(f"[{d}]")
```

**Here `.lower()` runs before `.strip()`. Does the result change? Why or why not?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — This should accept `"left"`, `"l"`, or `"왼쪽"` and turn them all into `"left"`. Right now it only matches the full word `"left"`.

```python
d = game.ask("way?").strip().lower()
if d == "left":
    d = "left"
game.say(d)
```

**Hint:** swap `==` for `in [ ... ]` and list the spellings you want to allow.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Two inputs (a direction and an action) should both be cleaned. Right now only the first one is, so the action still has spaces and capitals.

```python
direction = game.ask("way?").strip().lower()
action = game.ask("do what?")
game.say(f"{direction} / {action}")
```

**Hint:** the second input needs the same cleaning treatment.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The match list should be in **lowercase** so the cleaned input can find it. Right now the list has a capital letter, so a cleaned `"left"` never matches.

```python
d = game.ask("way?").strip().lower()
if d in ["Left", "l"]:
    d = "left"
game.say(d)
```

**Hint:** after `.lower()`, the input is lowercase — the list must be too.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · 🎯 Clean the Whole Game

Open your game. Go through **every** `ask()` you have written so far and add `.strip().lower()` to each one. Pick one important choice (a direction, for example) and make it accept several spellings.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I found every place I used `ask()`, and …
>
> The choice I made accept many spellings was …
>
> The spellings I allowed were …
>
> I tested it by typing different versions, and …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your game runs. Teach it like the viewer has never coded. Try to use these words: **clean**, **strip**, **lower**, **in**, **spelling**.

> 1. Run your game and type one answer the "normal" way.
> 2. Run it again and type a different spelling of the same answer.
> 3. Show both answers leading to the same path.
> 4. Read your `if ... in [ ... ]` line out loud and explain it.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
