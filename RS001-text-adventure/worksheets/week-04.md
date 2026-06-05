# 🏪 RS001 Week 4 — English Worksheet

**Topic:** Parallel Lists — A Shop Scene · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week you use **parallel lists** — several lists that line up by index. Item `[1]`'s name, power, and price all sit at index `1` in three different lists. Together they build a shop.

```python
shop_weapons = ["wooden stick", "iron sword", "magic staff"]
shop_power   = [2, 8, 15]
shop_price   = [5, 30, 80]
game.say(f"{shop_weapons[1]} — power {shop_power[1]}, {shop_price[1]} gold")
```

---

## 1 · Predict 🔮

Read each piece of code. Before you run it in your head, write what you think the screen will show.

```python
names = ["dagger", "axe", "spear"]
price = [10, 40, 25]
game.say(f"{names[1]} costs {price[1]} gold")
```

**Which item and which price get printed together?**

<div class="write-space"></div>

```python
names = ["dagger", "axe", "spear"]
power = [3, 9, 6]
game.say(f"{names[0]} — power {power[2]}")
```

**The indexes do not match. What strange sentence comes out?**

<div class="write-space"></div>

```python
names = ["dagger", "axe"]
price = [10, 40]
game.say(f"{names[2]} costs {price[2]} gold")
```

**Each list only has 2 items. What happens when the code asks for `[2]`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it, then explain why the original was wrong.

**Bug A** — This shop line should show the **axe** with **its own** price. Right now it shows the axe's name but the dagger's price.

```python
names = ["dagger", "axe", "spear"]
price = [10, 40, 25]
game.say(f"{names[1]} costs {price[0]} gold")
```

**Hint:** the name and the price should share the same index.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A new weapon `"hammer"` was added to the names list, but the other lists were not updated. Now line 4 crashes when it reaches the hammer.

```python
names = ["stick", "sword", "staff", "hammer"]
power = [2, 8, 15]
price = [5, 30, 80]
game.say(f"{names[3]} — power {power[3]}, {price[3]} gold")
```

**Hint:** if one list grows, the parallel lists must grow too.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should print a full 3-line shop menu. Right now line 2 forgot to change its index, so the same weapon shows up twice.

```python
names = ["stick", "sword", "staff"]
price = [5, 30, 80]
game.say(f"1. {names[0]} — {price[0]} gold")
game.say(f"2. {names[0]} — {price[1]} gold")
game.say(f"3. {names[2]} — {price[2]} gold")
```

**Hint:** look closely at the name index on line 2.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · 🎯 Build Your Shop

Open your game. After your opening and inventory, add a **shop scene** built from parallel lists: weapon names, their power, and their price. Print a clear numbered menu the player could buy from. Put it in your hometown if you like.

When it works, send a **photo or video**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made three lists for …
>
> They line up by index so that …
>
> The item at index 2 was …
>
> When I added a new weapon, I remembered to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your shop prints. Teach it like the viewer has never coded. Try to use these words: **parallel list**, **index**, **power**, **price**, **line up**.

> 1. Run your game and show the shop menu.
> 2. Pick one weapon and read its name, power, and price.
> 3. Point to where all three sit at the same index.
> 4. Explain what would break if one list were shorter than the others.

**Write what you will say in your video.** Plan it here first.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
