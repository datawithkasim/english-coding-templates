# 🎮 RB005 Week 3 — English Worksheet

**Topic:** Core Mechanic — Pick Your Pattern · **Course:** Dream Game Studio · **Time:** about 45 minutes

You finished RB001–004, so you own a toolbox of script **patterns**. This week you pick the right pattern from the toolbox and script your game's **core mechanic** — the thing the player does again and again.

---

## 1 · Predict 🔮

Read each pattern. Before you run it in Studio, write what you think will happen.

**Pattern A — the pickup**

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

**A player touches the coin. What happens to their leaderstats? Why does the coin only count once?**

<div class="write-space"></div>

**Pattern B — the countdown**

```lua
local timeLeft = 30

while timeLeft > 0 do
	print(timeLeft .. " seconds left!")
	task.wait(1)
	timeLeft -= 1
end

print("Time is up!")
```

**What prints in the Output, and how long does the whole loop take?**

<div class="write-space"></div>

**Pattern C — the if-gate**

```lua
local door = workspace.GoldDoor

door.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player and player.leaderstats.Coins.Value >= 10 then
		door.CanCollide = false
		door.Transparency = 0.5
	end
end)
```

**A player with 4 coins touches the door. What happens? What about a player with 12 coins?**

<div class="write-space"></div>

**Match the pattern to the game idea. Write A, B, or C next to each, then say which pattern is closest to YOUR game's core mechanic and why.**

> A collecting game where players grab gems for points → ___
>
> A survival game where each round lasts 30 seconds → ___
>
> An adventure game with a boss door that needs 10 keys → ___

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — One touch should give the player **1** coin, then the coin disappears. Right now one touch gives 5, 10, sometimes 20 coins.

```lua
local coin = script.Parent

coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
	end
end)
```

**Hint:** `Touched` fires many times for one touch. What did we use in RB003 to stop that?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Lava should set the toucher's health to 0. It works for players, but the Output shows a red error when a loose part falls onto the lava.

```lua
local lava = script.Parent

lava.Touched:Connect(function(hit)
	local humanoid = hit.Parent:FindFirstChild("Humanoid")
	humanoid.Health = 0
end)
```

**Hint:** a falling part has no Humanoid — so what is `humanoid` then?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The countdown should tick once per second. Right now all 30 numbers print instantly in one frame.

```lua
local timeLeft = 30

while timeLeft > 0 do
	print(timeLeft .. " seconds left!")
	timeLeft -= 1
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your game and script YOUR core mechanic, using the pattern you matched in section 1 (or a mix). When it works, come back here.

Send a photo or video of your mechanic working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My core mechanic is …
>
> I used the … pattern because …
>
> The event my script listens for is …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your core mechanic runs. Talk through it like you are teaching someone who has never seen your game. Try to use these words: **pattern**, **event**, **debounce**, **leaderstats**, **task.wait**.

> 1. Play your game and show the core mechanic working.
> 2. Name the pattern you used from the toolbox.
> 3. Open your script and read the most important line out loud.
> 4. Explain one check in your code (like `if player` or `not debounce`) and why it is there.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
