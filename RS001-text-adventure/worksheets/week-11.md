# ⚔️ RS001 Week 11 — English Worksheet

**Topic:** Strategy — Fight or Think? · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you think about code that lets the player solve a problem in more than one way. A menu of actions — fight, think, run — leads to a different result for each choice. The **order** of your `if` / `elif` / `else` decides which result wins. Read the code, predict what it does, and get ready to explain it in your own words.

> 🧠 Words to know: **action**, **menu**, **elif**, **else**, **outcome**

```python
action = game.ask("Fight or think?").strip().lower()
if action == "fight":
    game.say("You swing your sword!")
elif action == "think":
    game.say("You spot the enemy's weakness!")
else:
    game.say("You hesitate and get hit!")
```

---

## 1 · Predict 🔮

Read each piece of code. Run it in your head and write what you think happens.

```python
action = "think"
if action == "fight":
    game.say("attack")
elif action == "think":
    game.say("clever")
else:
    game.say("oops")
```

**Which word is printed?**

<div class="write-space"></div>

```python
action = "dance"
if action == "fight":
    game.say("attack")
elif action == "think":
    game.say("clever")
else:
    game.say("You freeze in panic.")
```

**The player typed something not on the menu. What happens because of the `else`?**

<div class="write-space"></div>

```python
actions = ["fight", "think", "run"]
game.say(f"Choose: {actions[0]} / {actions[1]} / {actions[2]}")
```

**What menu line is printed?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

**Bug A** — Each action should give a **different** result. Right now "fight" and "think" print the same thing.

```python
action = game.ask("do?").strip().lower()
if action == "fight":
    game.say("You win the hard way!")
elif action == "think":
    game.say("You win the hard way!")
```

**Hint:** the "think" branch should describe a clever win, not a brute-force one.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — There should be a catch-all for answers not on the menu. Right now an off-menu answer prints nothing at all.

```python
action = game.ask("fight / think").strip().lower()
if action == "fight":
    game.say("You attack!")
elif action == "think":
    game.say("You outsmart it!")
```

**Hint:** add an `else` for everything else.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — A wrong answer should get one retry before the game continues. Right now there is no second chance.

```python
actions = ["fight", "think", "run"]
action = game.ask("do what?").strip().lower()
if action not in actions:
    game.say("Pick from the menu.")
game.say(f"You chose: {action}")
```

**Hint:** after the warning, ask again and store the new answer (reuse what you learned in week 7).

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Here is a working battle menu. Read it carefully and answer the questions below.

```python
actions = ["fight", "think", "run"]
game.say(f"An enemy appears! Choose: {actions[0]} / {actions[1]} / {actions[2]}")
action = game.ask("What do you do?").strip().lower()
if action == "fight":
    game.say("You swing your sword and win the hard way!")
elif action == "think":
    game.say("You spot the enemy's weakness and win cleverly!")
elif action == "run":
    game.say("You escape, but the enemy keeps your gold.")
else:
    game.say("You hesitate and get hit!")
```

**What is stored in the `actions` list, and how is it used to print the menu?**

<div class="write-space"></div>

**Why does this code use `elif` for "think" and "run" instead of three separate `if` statements?**

<div class="write-space"></div>

**Which line runs if the player types "dance"? Why?**

<div class="write-space"></div>

**The `.strip().lower()` runs on the player's answer. What does it do, and why does it help the comparisons work?**

<div class="write-space"></div>

**Each branch prints a different `outcome`. Name the outcome for "fight" and the outcome for "run".**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the battle menu code **you** wrote in today's live lesson. Record a short video on your phone (or a parent's phone). You may show it running. Teach it like the viewer has never coded, and try to use these words: **action**, **menu**, **elif**, **else**, **outcome**.

> 1. Show the menu your code prints and read out the actions on it.
> 2. Point to your `if` / `elif` / `else` and explain what each branch does.
> 3. Show what happens when the player types something off-menu, and explain why.
> 4. Explain why the order of your branches matters.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
