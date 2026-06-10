# 🎮 RB005 Week 3 — English Worksheet (Beginner)

**Topic:** Core Mechanic — Pick Your Pattern · **Course:** Dream Game Studio · **Level:** Beginner · **Time:** about 30 minutes

This week you script your game's **core mechanic** — the thing the player does again and again — using a **pattern** from your toolbox.

---

## 1 · Predict 🔮

Read the code. Before you run it in Studio, circle or write your answer.

```lua
local coin = script.Parent
local debounce = false

coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player and not debounce then
		debounce = true
		player.leaderstats.Coins.Value += 1
		coin:Destroy()
	end
end)
```

**You touch the coin. Do your Coins go up? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local door = workspace.GoldDoor

door.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player and player.leaderstats.Coins.Value >= 10 then
		door.CanCollide = false
	end
end)
```

**You have 4 coins and touch the door. Does it open? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — One touch should give **1** coin, not many.

```lua
-- clean
local debounce = false

coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player and not debounce then
		debounce = true
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

**What is missing? How many coins can one touch give in the buggy code?**

<div class="write-space short"></div>

**Pair B** — The countdown should tick once per second.

```lua
-- clean
while timeLeft > 0 do
	print(timeLeft)
	task.wait(1)
	timeLeft -= 1
end
```

```lua
-- buggy
while timeLeft > 0 do
	print(timeLeft)
	timeLeft -= 1
end
```

**What is missing? What does the buggy countdown look like in the Output?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The countdown should pause for 1 second between numbers. One word is missing. Fill it in using the word bank.

```lua
local timeLeft = 30

while timeLeft > 0 do
	print(timeLeft .. " seconds left!")
	task.____(1)
	timeLeft -= 1
end
```

**Word bank:** `wait` · `stop` · `sleep`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your game and script your core mechanic using a pattern from the toolbox. When it works, come back here.

Send a photo or video of your mechanic working, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My core mechanic is …
>
> I used the … pattern …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your mechanic runs. Talk like you are teaching a friend. Try to use these words: **pattern**, **event**, **debounce**.

> 1. Play your game and show the core mechanic working.
> 2. Read your `Touched` line (or your loop) out loud.
> 3. Say which pattern you used from the toolbox.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
