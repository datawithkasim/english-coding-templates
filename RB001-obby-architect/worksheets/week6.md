# 🏃 RB001 Week 6 — English Worksheet

**Topic:** Coins & the Leaderboard · **Course:** Obby Architect · **Time:** about 45 minutes

This week your obby gets **coins**. When a player joins, your script builds a `leaderstats` folder with a `Coins` value. When a player touches a coin, Coins goes up by 1 and the coin disappears.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Studio, write what you think will happen.

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"
	leaderstats.Parent = player

	local coins = Instance.new("IntValue")
	coins.Name = "Coins"
	coins.Parent = leaderstats
end)
```

**You press Play and join the game. What shows on the leaderboard in the top-right corner? What number does Coins start at?**

<div class="write-space"></div>

```lua
local Players = game:GetService("Players")
local coin = script.Parent

coin.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if player then
		print("a player touched the coin")
	else
		print("not a player")
	end
end)
```

**A loose part rolls into the coin. Which message prints? Then you walk into the coin yourself. Which message prints now?**

<div class="write-space"></div>

```lua
local Players = game:GetService("Players")
local coin = script.Parent
local collected = false

coin.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if player and not collected then
		collected = true
		player.leaderstats.Coins.Value += 1
		coin:Destroy()
	end
end)
```

**You step on this coin. What happens to your Coins number? What happens to the coin itself?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the script is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — When a player joins, Coins should appear on the **leaderboard**. The script runs with no errors, but the leaderboard never shows up.

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "MyStats"
	leaderstats.Parent = player

	local coins = Instance.new("IntValue")
	coins.Name = "Coins"
	coins.Parent = leaderstats
end)
```

**Hint:** Roblox only shows the folder if its name is **exactly** right.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — One coin should give **exactly 1** point. But when you run through the coin, you sometimes get 2 or 3 points from one coin.

```lua
local Players = game:GetService("Players")
local coin = script.Parent

coin.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
		coin:Destroy()
	end
end)
```

**Hint:** `Touched` fires once for each body part. You need a `local collected = false` guard.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The coin should give a point only to a **player**. But when a loose part bumps the coin, the Output window shows a red error and the coin breaks.

```lua
local Players = game:GetService("Players")
local coin = script.Parent
local collected = false

coin.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	collected = true
	player.leaderstats.Coins.Value += 1
	coin:Destroy()
end)
```

**Hint:** when the toucher is not a player, `player` is `nil`. Check before you use it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your obby in Roblox Studio. Add a `leaderstats` script with Coins, then place at least 3 coins in your obby that each give 1 point and disappear. Collect them all in Play mode. When you finish, come back here.

Send a photo or video of your leaderboard showing your Coins, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> The leaderboard works because the folder is named …
>
> I used `GetPlayerFromCharacter` to …
>
> My debounce `collected` stops …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you collect your coins in Play mode. Talk through it like you are teaching someone who has never seen it. Try to use these words: **leaderboard**, **player**, **value**, **debounce**, **destroy**.

> 1. Press Play and point at the leaderboard with Coins on it.
> 2. Collect one coin and show the number go up by exactly 1.
> 3. Read your coin script out loud and say what `if player and not collected` checks.
> 4. Say in your own words why the coin is destroyed at the end.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
