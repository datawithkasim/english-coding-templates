# 🎮 RB005 Week 6 — English Worksheet (Beginner)

**Topic:** Playtest & Iterate — Find Bugs, Fix Bugs · **Course:** Dream Game Studio · **Level:** Beginner · **Time:** about 30 minutes

This week you are a **bug hunter**. Real game studios test, find bugs, fix them, and test again: **see it → write it → fix it → retest**.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

```lua
local coin = script.Parent

coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
		coin:Destroy()
	end
end)
```

**The player touches the coin one time. The coin is destroyed. Can they touch it again to get more points? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local coin = script.Parent

coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
	end
end)
```

**This coin is never destroyed. The player stands on it and touches it many times. Could they get many points from one coin? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — One coin should give **only 1 point**.

```lua
-- clean
coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
		coin:Destroy()
	end
end)
```

```lua
-- buggy
coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
	end
end)
```

**What is wrong? Why can the buggy coin give too many points?**

<div class="write-space short"></div>

**Pair B** — The door should open at **5 coins or more**.

```lua
-- clean
if player.leaderstats.Coins.Value >= 5 then
	door.CanCollide = false
end
```

```lua
-- buggy
if player.leaderstats.Coins.Value > 5 then
	door.CanCollide = false
end
```

**What is wrong? With the buggy code, what happens when the player has exactly 5 coins?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The door should open when the player has **5 coins or more**. One symbol is missing. Fill it in using the word bank.

```lua
if player.leaderstats.Coins.Value ____ 5 then
	door.CanCollide = false
end
```

**Word bank:** `>=` · `+` · `=`

**Write the missing symbol:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now playtest your own game. Find **one bug** (code bug or a confusing place) and fix it. When you finish, come back here.

Send a photo or video of your game after the fix, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The bug I found was …
>
> I fixed it by …
>
> When I tested again, …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) showing your bug **before and after** the fix. Talk like you are teaching a friend. Try to use these words: **bug**, **fix**, **test**, **again**.

> 1. Show the bug happening.
> 2. Show the line you changed and read it out loud.
> 3. Test again on camera and show the bug is gone.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
