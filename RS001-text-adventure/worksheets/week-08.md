# 🧰 RS001 Week 8 — English Worksheet

**Topic:** Validation Across the Whole Game · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you wrap the "clean → validate → retry → default" pattern into **one reusable function** called `safe_choice()`. Then you use it everywhere — directions, weapons, actions — so no input can ever break your game.

```python
def safe_choice(prompt, valid_list, default):
    answer = game.ask(prompt).strip().lower()
    if answer not in valid_list:
        answer = game.ask("Try again: " + prompt).strip().lower()
    if answer not in valid_list:
        answer = default
    return answer
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think happens.

```python
def greet(name):
    return f"Hi {name}!"

game.say(greet("Mina"))
```

**A function with `return`. What is printed?**

<div class="write-space"></div>

```python
def safe_choice(prompt, valid_list, default):
    answer = game.ask(prompt).strip().lower()
    if answer not in valid_list:
        answer = default
    return answer

result = safe_choice("way?", ["left", "right"], "left")
game.say(result)
```

**The player types `"up"`. What does `result` become?**

<div class="write-space"></div>

```python
direction = safe_choice("way?", ["left", "right"], "left")
action = safe_choice("do?", ["fight", "run"], "run")
game.say(f"{direction}, {action}")
```

**The same function is reused twice with different lists. Why is reusing it better than copying the code?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — `safe_choice` should hand the answer back to whoever called it. Right now it cleans the answer but forgets to `return` it, so the caller gets nothing.

```python
def safe_choice(prompt, valid_list, default):
    answer = game.ask(prompt).strip().lower()
    if answer not in valid_list:
        answer = default

result = safe_choice("way?", ["left", "right"], "left")
game.say(result)
```

**Hint:** a function needs `return` to give a value back.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The default must itself be a **valid** answer, or the game ends up holding something not in the list. Here the default `"up"` is not in the valid list.

```python
def safe_choice(prompt, valid_list, default):
    answer = game.ask(prompt).strip().lower()
    if answer not in valid_list:
        answer = default
    return answer

move = safe_choice("way?", ["left", "right"], "up")
game.say(f"You go {move}.")
```

**Hint:** pick a default that lives inside the valid list.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The valid list should be lowercase so the cleaned answer can match it. Here `"Fight"` has a capital, so a cleaned `"fight"` is never accepted.

```python
action = safe_choice("do what?", ["Fight", "run"], "run")
game.say(f"You chose {action}.")
```

**Hint:** the input gets `.lower()`-ed, so the list items must be lowercase too.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · 🎯 Protect the Whole Game

Open your game. Add a `safe_choice()` function and use it for **every** choice the player makes — direction, weapon, action. Then try to break your own game on purpose: type empty answers, nonsense, and CAPS. It should never crash.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I wrote a function called `safe_choice` that …
>
> I used it for these choices in my game …
>
> To test it, I deliberately typed …
>
> Reusing one function was better than copying because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you try to break your game. Teach it like the viewer has never coded. Try to use these words: **function**, **return**, **reuse**, **default**, **valid**.

> 1. Run your game and answer normally first.
> 2. Run it again and type nonsense at every prompt.
> 3. Show the default keeping the game alive.
> 4. Read your `safe_choice` function out loud and explain `return`.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
