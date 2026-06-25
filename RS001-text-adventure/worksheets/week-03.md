# 📋 RS001 Week 3 — English Worksheet

**Topic:** Lists and Choices · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you think about the **list** — one box that holds many values. You pull a value out by its **index**: the first item is `[0]`, the second is `[1]`, the third is `[2]`. On this sheet you read code, predict it, fix it on paper, and explain the code you wrote in today's lesson.

> 🧠 Words to know: **list**, **index**, **first**, **inventory**, **value**

```python
weapons = ["sword", "bow", "wand"]
game.say(f"You can choose: {weapons[0]}, {weapons[1]}, {weapons[2]}")
```

---

## 1 · Predict 🔮

Read each piece of code. Run it in your head — do not type it. Write what you think the screen will show.

```python
paths = ["left", "middle", "right"]
game.say(paths[1])
```

**Which word appears? (Careful — counting starts at 0.)**

<div class="write-space"></div>

```python
enemies = ["goblin", "orc", "dragon"]
enemy_hp = [10, 25, 100]
game.say(f"{enemies[2]} has {enemy_hp[2]} HP")
```

**The two lists share the same index. What sentence is printed?**

<div class="write-space"></div>

```python
items = ["map", "key", "torch"]
game.say(items[3])
```

**The list has 3 items but the code asks for `[3]`. What goes wrong?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

**Bug A** — This should print the **first** weapon in the list. Right now it prints the second one.

```python
weapons = ["sword", "bow", "wand"]
game.say(f"Your first weapon: {weapons[1]}")
```

**Hint:** the first item is not `[1]`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should show all three paths as a numbered menu. Right now every line shows the **same** path.

```python
paths = ["cave", "river", "field"]
game.say(f"1: {paths[0]}")
game.say(f"2: {paths[0]}")
game.say(f"3: {paths[0]}")
```

**Hint:** lines 2 and 3 should use a different index.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The enemy name and its HP should belong to the **same** enemy. Right now the name is the goblin but the HP is the dragon's.

```python
enemy_names = ["goblin", "orc", "dragon"]
enemy_hp = [10, 25, 100]
game.say(f"A {enemy_names[0]} appears! HP: {enemy_hp[2]}")
```

**Hint:** the same enemy lives at the same index in both lists.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Here is a working inventory. The hero starts with a **list** of items, and the code shows them on screen.

```python
inventory = ["map", "key", "torch"]
game.say(f"You carry: {inventory[0]}, {inventory[1]}, {inventory[2]}")
game.say(f"The first item in your inventory is the {inventory[0]}.")
```

**What is the name of the list, and what three values are inside it?**

<div class="write-space"></div>

**`inventory[0]` gives which item? Why that one and not the second?**

<div class="write-space"></div>

**Which index would you use to show the `torch`?**

<div class="write-space"></div>

**The last line says "the first item." What does the word *index* mean in your own words?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Today in your lesson you wrote your own inventory list. Make a short video on your phone (or a parent's phone) that explains the code **you** wrote. You may show it running. Teach it like the viewer has never coded. Try to use these words: **list**, **index**, **first**, **inventory**, **value**.

> 1. Point to the list you wrote and read the items out loud.
> 2. Pick one item and say its index.
> 3. Explain why the first item is index 0, not 1.
> 4. Say one thing that was tricky and how you worked it out.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
