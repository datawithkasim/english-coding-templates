# 🏭 RB003 Week 3 — English Worksheet

**Topic:** Arrays — A List of Upgrades · **Course:** Tycoon Engineer · **Time:** about 45 minutes

This week your tycoon gets an **array** — one variable that holds a whole list of upgrades. You grab items with an **index** like `upgrades[1]` and loop through the list with `ipairs`.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think prints in the Output window.

```lua
local upgrades = {"Fast Dropper", "Gold Ore", "Mega Conveyor"}
print(upgrades[1])
print(upgrades[3])
```

**What two lines print? Remember: Luau lists start at 1, not 0.**

<div class="write-space"></div>

```lua
local upgrades = {"Fast Dropper", "Gold Ore", "Mega Conveyor"}
print(#upgrades)
print(upgrades[4])
```

**What number does `#upgrades` give you? There is no item 4 — what prints for `upgrades[4]`?**

<div class="write-space"></div>

```lua
local upgrades = {"Fast Dropper", "Gold Ore", "Mega Conveyor"}

for i, name in ipairs(upgrades) do
	print(i, name)
end
```

**How many lines print? What exactly is on the second line?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The script should print the **first** upgrade, `Fast Dropper`. Instead it prints `nil`.

```lua
local upgrades = {"Fast Dropper", "Gold Ore", "Mega Conveyor"}
print(upgrades[0])
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The script should make a list of three upgrades. Instead, Roblox Studio shows a **red error** before the game even runs.

```lua
local upgrades = {"Fast Dropper" "Gold Ore" "Mega Conveyor"}
print(upgrades[2])
```

**Hint:** what goes **between** items in a list?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The shop should print **every** upgrade in the list. Instead it prints `Fast Dropper` three times.

```lua
local upgrades = {"Fast Dropper", "Gold Ore", "Mega Conveyor"}

for i = 1, #upgrades do
	print(upgrades[1])
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to Roblox Studio and open your tycoon. Make an `upgrades` array with at least 3 upgrades and use an `ipairs` loop to print the full shop list to the Output window. When you finish, come back here.

Send a photo or video of your script and the printed list, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My array holds …
>
> I used **ipairs** to …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you run your script. Talk through it like you are teaching someone who has never seen it. Try to use these words: **array**, **index**, **ipairs**, **length**, **nil**.

> 1. Show your `upgrades` array in the script.
> 2. Press Play and show the printed list in the Output window.
> 3. Read your `ipairs` loop out loud and say what `i` and `name` are.
> 4. Say in your own words why `upgrades[4]` gives `nil`.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
