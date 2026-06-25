# 🧼 RS001 Week 6 — English Worksheet

**Topic:** Clean Every Input Safely · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you think about how `.strip().lower()` cleans **every** `ask()` in your game, and how a game can accept several spellings of the same answer — Korean, English, short forms — so almost any sensible input works. You will read code closely and explain it in your own words.

> 🧠 Words to know: **clean**, **strip**, **lower**, **in**, **spelling**

---

## 1 · Predict 🔮

Read each piece of code. Run it in your head and write what you think happens.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Read this working example slowly. It cleans the player's answer and accepts several spellings of "left".

```python
direction = game.ask("Which way? (left/right)")
direction = direction.strip().lower()
if direction in ["left", "l", "왼쪽"]:
    direction = "left"
```

**What does `.strip()` remove from the player's answer?**

<div class="write-space"></div>

**What does `.lower()` do to a capital letter the player typed?**

<div class="write-space"></div>

**Why must the words in the list `["left", "l", "왼쪽"]` all be lowercase?**

<div class="write-space"></div>

**The player types `"  Left "`. After line 2, what is the value of `direction`? Does the `if` match?**

<div class="write-space"></div>

**Why is it helpful to turn `"l"` and `"왼쪽"` both into `"left"` before the rest of the game runs?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you cleaned the inputs in your own game. Now explain that code in a short video on your phone (or a parent's phone). You may show your game running. Teach it like the viewer has never coded. Try to use these words: **clean**, **strip**, **lower**, **in**, **spelling**.

> 1. Show one `ask()` line from your game and read your `.strip().lower()` out loud.
> 2. Explain what `.strip()` and `.lower()` each do to the player's answer.
> 3. Read your `if ... in [ ... ]` line and say which spellings you allowed.
> 4. Run it once with a "normal" answer and once with a different spelling, and show both reaching the same path.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
