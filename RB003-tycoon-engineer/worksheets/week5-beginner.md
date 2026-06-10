# 🏭 RB003 Week 5 — English Worksheet (Beginner)

**Topic:** Buy Buttons — Spend Cash to Unlock Upgrades · **Course:** Tycoon Engineer · **Level:** Beginner · **Time:** about 30 minutes

This week your tycoon gets **buy buttons** — touch pads that take the player's cash and unlock a new upgrade by **cloning** a model.

---

## 1 · Predict 🔮

Read the script. Before you imagine it running in Studio, circle or write your answer.

```lua
local price = 50

if cash.Value >= price then
    print("Bought!")
end
```

**The player has exactly 50 cash. Does "Bought!" print? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local price = 50

if cash.Value >= price then
    print("Bought!")
end
```

**Now the player has only 30 cash. Does "Bought!" print? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The buy button should **take the player's cash** when they buy.

```lua
-- clean
if cash.Value >= price then
    cash.Value -= price
    model.Parent = workspace
end
```

```lua
-- buggy
if cash.Value >= price then
    model.Parent = workspace
end
```

**What is wrong? Why is the upgrade free in the buggy code?**

<div class="write-space short"></div>

**Pair B** — A player with **exactly** 50 cash should be able to buy.

```lua
-- clean
if cash.Value >= price then
    cash.Value -= price
end
```

```lua
-- buggy
if cash.Value > price then
    cash.Value -= price
end
```

**What is wrong? The player has exactly 50 cash — which version lets them buy?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The buy button should make a copy of the upgrade and put it in the world. One word is missing. Fill it in using the word bank.

```lua
local model = upgradeModel:____()
model.Parent = workspace
```

**Word bank:** `Clone` · `Touched` · `Destroy`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your tycoon in Roblox Studio. Build a buy button that takes cash and unlocks an upgrade. When you finish, come back here.

Send a photo or video of your buy button working, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My buy button costs …
>
> When I step on it, …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you test your buy button. Talk like you are teaching a friend. Try to use these words: **buy button**, **price**, **clone**.

> 1. Show your cash, then step on your buy button.
> 2. Show the new upgrade appearing.
> 3. Say in your own words what **Clone** does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
