# ⚔️ RS001 Week 11 — English Worksheet

**Topic:** Strategy — Fight or Think? · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week the player solves a problem in more than one way. You offer a menu of actions — fight, think, run — and each one leads to a different result. The **order** of your `if` / `elif` / `else` decides which result wins.

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

Read each piece of code. Before you run it in your head, write what you think happens.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

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

## 3 · 🎯 Add a Battle Menu

Open your game. When the player meets an enemy, give them a menu: fight, think, run (or your own). Each action should lead to a different outcome. Validate the answer so off-menu input is handled.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, the enemy appeared and I offered the actions …
>
> Fighting led to …
>
> Thinking led to …
>
> Running led to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your battle runs. Teach it like the viewer has never coded. Try to use these words: **action**, **menu**, **elif**, **else**, **outcome**.

> 1. Run your game and fight the enemy.
> 2. Run it again and think instead — show the different result.
> 3. Type something off-menu and show what happens.
> 4. Read your `if` / `elif` / `else` out loud and explain why order matters.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
