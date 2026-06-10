# 🏭 RB003 Week 4 — English Worksheet (Beginner)

**Topic:** Dictionaries — Items with Keys and Values · **Course:** Tycoon Engineer · **Level:** Beginner · **Time:** about 30 minutes

This week one item holds **many facts at once** using a **dictionary** — keys like `Name` and `Price` with values after the `=`. You read a fact with a **dot**: `item.Price`.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Roblox Studio, circle or write your answer.

```lua
local item = {Name = "Gold Ore", Price = 50}
print(item.Name)
```

**Does it print `Gold Ore`? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local item = {Name = "Gold Ore", Price = 50}
print(item.price)
```

**The key is `Price` but the script asks for `price` with a small p. Does it print `50`? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The key is `Price` with a **capital P**. The script should print `50`.

```lua
-- clean
local item = {Name = "Gold Ore", Price = 50}
print(item.Price)
```

```lua
-- buggy
local item = {Name = "Gold Ore", Price = 50}
print(item.price)
```

**What is wrong? What does the buggy script print?**

<div class="write-space short"></div>

**Pair B** — Every key needs an `=` before its value.

```lua
-- clean
local item = {Name = "Gold Ore", Price = 50}
```

```lua
-- buggy
local item = {Name "Gold Ore", Price = 50}
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The script should print the price, `50`. One key is missing. Fill it in using the word bank.

```lua
local item = {Name = "Gold Ore", Price = 50}
print(item.____)
```

**Word bank:** `Price` · `price` · `Name`

**Write the missing key:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to Roblox Studio and open your tycoon. Make an `item` dictionary with a `Name` and a `Price`, and print both to the Output window. When you finish, come back here.

Send a photo or video of your script and the printed facts, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My dictionary stores …
>
> I used a dot to …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you run your script. Talk like you are teaching a friend. Try to use these words: **dictionary**, **key**, **value**, **dot**.

> 1. Show your `item` dictionary in the script.
> 2. Press Play and show the name and price printed in the Output window.
> 3. Say in your own words what a **key** and a **value** are.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
