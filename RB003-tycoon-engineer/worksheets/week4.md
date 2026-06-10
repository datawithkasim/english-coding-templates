# 🏭 RB003 Week 4 — English Worksheet

**Topic:** Dictionaries — Items with Keys and Values · **Course:** Tycoon Engineer · **Time:** about 45 minutes

This week one item holds **many facts at once** using a **dictionary** — keys like `Name` and `Price` with values after the `=`. You read a fact with a **dot**: `item.Price`.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think prints in the Output window.

```lua
local item = {Name = "Gold Ore", Price = 50, Payout = 12}
print(item.Name)
print(item.Price)
```

**What two lines print?**

<div class="write-space"></div>

```lua
local item = {Name = "Gold Ore", Price = 50, Payout = 12}
print(item.price)
```

**Careful with capital letters! The key is `Price` but the script asks for `price`. What prints, and why?**

<div class="write-space"></div>

```lua
local catalog = {
	{Name = "Fast Dropper", Price = 100},
	{Name = "Gold Ore", Price = 250},
}

for i, item in ipairs(catalog) do
	print(i, item.Name, item.Price)
end
```

**How many lines print? What exactly is on the second line?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The script should print the price, `50`. Instead it prints `nil`.

```lua
local item = {Name = "Gold Ore", Price = 50}
print(item.price)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The script should make one item with a name and a price. Instead, Roblox Studio shows a **red error** before the game even runs.

```lua
local item = {Name "Gold Ore", Price = 50}
print(item.Name)
```

**Hint:** every key needs an `=` before its value.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The script should print the item's name, `Gold Ore`. The coder used `[1]` like an array, but a dictionary has **keys**, not numbered slots — so it prints `nil`.

```lua
local item = {Name = "Gold Ore", Price = 50}
print(item[1])
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to Roblox Studio and open your tycoon. Build a `catalog` — a list of at least 2 item dictionaries, each with a `Name` and a `Price` — and loop through it with `ipairs` to print every item's name and price. When you finish, come back here.

Send a photo or video of your script and the printed catalog, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My dictionary stores …
>
> I used a dot to …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you run your script. Talk through it like you are teaching someone who has never seen it. Try to use these words: **dictionary**, **key**, **value**, **dot**, **catalog**.

> 1. Show your `catalog` in the script.
> 2. Press Play and show every name and price printed in the Output window.
> 3. Read one dictionary out loud — say its keys and its values.
> 4. Say in your own words why `item.price` (small p) gives `nil`.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
