# 📋 RS001 Week 3 — English Worksheet

**Topic:** Lists and Choices · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you learn the **list** — one box that holds many values. You pull a value out by its **index**: the first item is `[0]`, the second is `[1]`, the third is `[2]`.

```python
weapons = ["sword", "bow", "wand"]
game.say(f"You can choose: {weapons[0]}, {weapons[1]}, {weapons[2]}")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think the screen will show.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

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

## 3 · 🎯 Add an Inventory

Open your game. After your opening, add a **list** for the hero's starting items (an inventory) and show them on screen. Then add a second list — a menu of **paths** the player can read.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made a list called …
>
> The items inside it were …
>
> To show the second item, I used index …
>
> I learned that the first item is …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your inventory prints. Teach it like the viewer has never coded. Try to use these words: **list**, **index**, **first**, **inventory**, **value**.

> 1. Run your game and show the inventory on screen.
> 2. Point to the list in your code and read the items.
> 3. Pick one item and say its index out loud.
> 4. Explain why the first item is index 0, not 1.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
