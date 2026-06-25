# 🏪 RS001 Week 4 — English Worksheet

**Topic:** Parallel Lists — A Shop Scene · **Course:** Text Adventure (Python) · **Time:** about 45 minutes

This week is about **parallel lists** — several lists that line up by index. Item `[1]`'s name, power, and price all sit at index `1` in three different lists. Together they build a shop. In this worksheet you will read code about parallel lists, think carefully, and then explain the shop code you wrote in today's live lesson.

```python
shop_weapons = ["wooden stick", "iron sword", "magic staff"]
shop_power   = [2, 8, 15]
shop_price   = [5, 30, 80]
game.say(f"{shop_weapons[1]} — power {shop_power[1]}, {shop_price[1]} gold")
```

> 🧠 Words to know: **parallel list**, **index**, **power**, **price**, **line up**

---

## 1 · Predict 🔮

Read each piece of code. Run it in your head and write what you think the screen will show.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, fix it on paper, then explain why the original was wrong.

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

## 3 · Explain the Code 📖

Here is a working shop menu built from three parallel lists. Read it slowly, then answer the questions below.

```python
names = ["stick", "sword", "staff"]
power = [2, 8, 15]
price = [5, 30, 80]
game.say(f"1. {names[0]} — power {power[0]}, {price[0]} gold")
game.say(f"2. {names[1]} — power {power[1]}, {price[1]} gold")
game.say(f"3. {names[2]} — power {power[2]}, {price[2]} gold")
```

**Why are there three separate lists instead of one?**

<div class="write-space"></div>

**Look at line 5. Which name, power, and price get printed together, and how do you know?**

<div class="write-space"></div>

**The index goes 0, then 1, then 2 down the menu. What is that index doing for the player?**

<div class="write-space"></div>

**If you changed `names[1]` to `names[2]` on line 5, what would go wrong on the screen?**

<div class="write-space"></div>

**What would break if the `price` list had only two numbers in it?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own shop scene with parallel lists. Take a short video on your phone (or a parent's phone) explaining the code **you** wrote. You may show it running. Teach it like the viewer has never coded, and try to use these words: **parallel list**, **index**, **power**, **price**, **line up**.

> 1. Show your three lists and say what each one holds.
> 2. Read one weapon out loud — its name, power, and price.
> 3. Point to where all three sit at the same index.
> 4. Explain what would break if one of your lists were shorter than the others.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
