# 🏃 RB001 Week 6 — English Worksheet (Beginner)

**Topic:** Coins & the Leaderboard · **Course:** Obby Architect · **Level:** Beginner · **Time:** about 30 minutes

This week your obby gets **coins**. A `leaderstats` folder makes the leaderboard appear. Touching a coin makes Coins go up by 1.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

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

**You press Play and join. Does "Coins" show on the leaderboard? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
coin.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
		coin:Destroy()
	end
end)
```

**A loose block rolls into the coin. The block is not a player. Does Coins go up? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows a clean script first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The leaderboard only appears if the folder name is **exactly** `leaderstats`.

```lua
-- clean
local leaderstats = Instance.new("Folder")
leaderstats.Name = "leaderstats"
leaderstats.Parent = player
```

```lua
-- buggy
local leaderstats = Instance.new("Folder")
leaderstats.Name = "stats"
leaderstats.Parent = player
```

**What is wrong? What happens to the leaderboard?**

<div class="write-space short"></div>

**Pair B** — Only a **player** should get the point.

```lua
-- clean
local player = Players:GetPlayerFromCharacter(otherPart.Parent)
if player then
	player.leaderstats.Coins.Value += 1
	coin:Destroy()
end
```

```lua
-- buggy
local player = Players:GetPlayerFromCharacter(otherPart.Parent)
player.leaderstats.Coins.Value += 1
coin:Destroy()
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

After the point is added, the coin should disappear. One word is missing. Fill it in using the word bank.

```lua
if player then
	player.leaderstats.Coins.Value += 1
	coin:________()
end
```

**Word bank:** `Destroy` · `Delete` · `Hide`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your obby in Roblox Studio. Add the `leaderstats` script, then place at least 2 coins that give 1 point each. Collect them in Play mode. When you finish, come back here.

Send a photo or video of your leaderboard showing your Coins, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My coins give a point when …
>
> The leaderboard shows …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you collect your coins in Play mode. Talk like you are teaching a friend. Try to use these words: **leaderboard**, **coin**, **value**, **destroy**.

> 1. Press Play and point at the leaderboard.
> 2. Collect one coin and show Coins go up by 1.
> 3. Say in your own words what `coin:Destroy()` does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
