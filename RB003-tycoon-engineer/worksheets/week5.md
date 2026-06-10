# 🏭 RB003 Week 5 — English Worksheet

**Topic:** Buy Buttons — Spend Cash to Unlock Upgrades · **Course:** Tycoon Engineer · **Time:** about 45 minutes

This week your tycoon gets **buy buttons** — touch pads that take the player's cash and unlock a new upgrade by **cloning** a model. A **debounce** makes sure one step on the pad means one buy.

---

## 1 · Predict 🔮

Read each script. Before you imagine it running in Studio, write what you think will happen.

```lua
local price = 50

if cash.Value >= price then
    cash.Value -= price
    print("Bought!")
end
```

**The player has exactly 50 cash. Does "Bought!" print? How much cash is left after?**

<div class="write-space"></div>

```lua
local ServerStorage = game:GetService("ServerStorage")
local upgradeModel = ServerStorage.SuperDropper

local model = upgradeModel:Clone()
model.Parent = workspace
```

**What appears in the game world? Does the original SuperDropper leave ServerStorage?**

<div class="write-space"></div>

```lua
local buying = false

pad.Touched:Connect(function(hit)
    if buying then return end
    buying = true

    print("One buy!")

    task.wait(1)
    buying = false
end)
```

**A player stands on the pad, and `Touched` fires 10 times in one second. How many times does "One buy!" print? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The buy button should work when the player has **exactly** the price. A player with exactly 100 cash should be able to buy.

```lua
local price = 100

if cash.Value > price then
    cash.Value -= price
    local model = upgradeModel:Clone()
    model.Parent = workspace
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The buy button should **take the player's cash** when they buy. Right now the upgrade is free — players can buy forever and never lose cash.

```lua
local price = 100

if cash.Value >= price then
    local model = upgradeModel:Clone()
    model.Parent = workspace
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — One step on the pad should mean **one** buy. Right now one step can buy two or three upgrades and take the cash every time.

```lua
pad.Touched:Connect(function(hit)
    if cash.Value >= price then
        cash.Value -= price
        local model = upgradeModel:Clone()
        model.Parent = workspace
    end
end)
```

**Hint:** add a **debounce** — a `buying` variable that blocks the pad while a buy is happening.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your tycoon in Roblox Studio. Build a buy button that takes cash and unlocks an upgrade by cloning it. When you finish, come back here.

Send a photo or video of your buy button working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My buy button costs … and unlocks …
>
> I used **Clone** when …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you test your buy button. Talk through it like you are teaching someone who has never seen it. Try to use these words: **buy button**, **price**, **clone**, **debounce**, **subtract**.

> 1. Show your cash, then step on the buy button.
> 2. Show the cash going down and the new upgrade appearing.
> 3. Read your `if cash.Value >= price` line out loud and say what it checks.
> 4. Say in your own words what a **debounce** does.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
