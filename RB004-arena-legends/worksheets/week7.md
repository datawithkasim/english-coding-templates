# ⚔️ RB004 Week 7 — English Worksheet

**Topic:** Build Week — Your Full Arena Game · **Course:** Arena Legends · **Time:** about 45 minutes

No new syntax this week. You already know everything: Teams, the countdown timer, RemoteEvents, power-ups, points, and your Settings ModuleScript. This week you connect it all into **one full round loop** — and you design **your own** arena game.

---

## 1 · Predict 🔮

This is a full round loop, like the one in your game. Read each part. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local Settings = require(game.ServerScriptService.Settings)
local status = game.ReplicatedStorage.Status
local timeLeft = game.ReplicatedStorage.TimeLeft
local points = {Red = 0, Blue = 0}

while true do
	status.Value = "Intermission..."
	task.wait(10)

	status.Value = "FIGHT!"
	points.Red = 0
	points.Blue = 0
```

**What do players see on screen first, and for how long? Why do we set both points back to 0 here?**

<div class="write-space"></div>

```lua
	for i = Settings.RoundLength, 0, -1 do
		timeLeft.Value = i
		task.wait(1)
	end
```

**`RoundLength` is 60. What does `timeLeft.Value` count — up or down? About how many seconds does this part take?**

<div class="write-space"></div>

```lua
	if points.Red > points.Blue then
		status.Value = "Red team wins!"
	elseif points.Blue > points.Red then
		status.Value = "Blue team wins!"
	else
		status.Value = "It's a tie!"
	end
	task.wait(5)
end
```

**Red has 3 points and Blue has 3 points when the timer ends. What does the status say? What happens after the 5-second wait — does the game stop?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each round loop below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — Every round should start fresh at 0–0. But in this game, round 2 starts with last round's points, so one team wins instantly.

```lua
while true do
	status.Value = "Intermission..."
	task.wait(10)

	status.Value = "FIGHT!"

	for i = Settings.RoundLength, 0, -1 do
		timeLeft.Value = i
		task.wait(1)
	end
```

**Write the fixed code (just the part you change or add):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The winner should be announced **after** the timer ends. In this game, "Red team wins!" appears the moment the round starts, before anyone even scores.

```lua
	status.Value = "FIGHT!"
	points.Red = 0
	points.Blue = 0

	if points.Red >= points.Blue then
		status.Value = "Red team wins!"
	end

	for i = Settings.RoundLength, 0, -1 do
		timeLeft.Value = i
		task.wait(1)
	end
```

**Write the fixed code (just the part you change or move):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The countdown should take one second per number. In this game, the timer jumps from 60 to 0 instantly and the round ends right away.

```lua
	for i = Settings.RoundLength, 0, -1 do
		timeLeft.Value = i
	end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open Roblox Studio and build your full arena game: round loop, teams, timer, power-ups, points, winner check. **You are the designer** — you choose the game mode. When you finish, come back here.

Send a photo or video of one full round, then explain your design. Use these sentence starters — write 4 to 6 sentences total.

> My game mode is …
>
> A team scores a point when …
>
> I put my power-ups … because …
>
> My round length is … seconds because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you playtest one full round. In Roblox Studio, use **Test → 2 Players** so both teams have a player. Talk through it like you are teaching someone who has never seen it. Try to use these words: **round loop**, **intermission**, **countdown**, **points**, **winner**.

> 1. Start the 2-player test and show the intermission message.
> 2. When the round starts, score a point and show the score changing for both test players.
> 3. Grab a power-up and show what it does.
> 4. Let the timer reach 0 and show the winner message. Check out loud: did the points reset for the next round?

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
