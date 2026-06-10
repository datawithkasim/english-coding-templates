# 🏃 RB001 Week 7 — English Worksheet

**Topic:** Build Week — Your Full Obby · **Course:** Obby Architect · **Time:** about 45 minutes

No new syntax this week. You already know everything you need: parts, colors, lava, doors, loops, vanishing bridges, coins, and the leaderboard. This week you put it **all together** into one full obby with a start, checkpoints, and a win pad.

---

## 1 · Predict 🔮

Read each script. These mix ideas from past weeks. Write what you think will happen.

```lua
local winPad = script.Parent

winPad.Touched:Connect(function(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		print("You win!")
		for i = 1, 6 do
			winPad.Color = Color3.fromRGB(255, 215, 0)
			task.wait(0.2)
			winPad.Color = Color3.fromRGB(85, 255, 127)
			task.wait(0.2)
		end
	end
end)
```

**A player jumps onto the win pad. What prints in the Output? What does the pad look like, and for about how many seconds?**

<div class="write-space"></div>

```lua
local lava = script.Parent

lava.Touched:Connect(function(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		humanoid.Health = 0
	end
end)
```

**A player touches the lava — what happens? A loose part falls onto the lava — what happens then?**

<div class="write-space"></div>

```lua
local platform = script.Parent

while true do
	for i = 1, 10 do
		platform.Transparency = i / 10
		task.wait(0.1)
	end
	platform.CanCollide = false
	task.wait(2)
	platform.Transparency = 0
	platform.CanCollide = true
	task.wait(3)
end
```

**This is one platform of your bridge. In each cycle, for how many seconds is it solid and safe? When should a player run across?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the script is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The win pad should celebrate only when a **player** touches it. But a loose part rolled onto the pad and the game printed "You win!" with nobody there.

```lua
local winPad = script.Parent

winPad.Touched:Connect(function(otherPart)
	print("You win!")
	for i = 1, 6 do
		winPad.Color = Color3.fromRGB(255, 215, 0)
		task.wait(0.2)
		winPad.Color = Color3.fromRGB(85, 255, 127)
		task.wait(0.2)
	end
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The lava should only hurt players. But when a coin fell onto the lava, the Output showed a red error and the lava stopped working.

```lua
local lava = script.Parent

lava.Touched:Connect(function(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	humanoid.Health = 0
end)
```

**Hint:** a falling coin has no Humanoid, so `humanoid` is `nil`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The secret door should **open**: turn invisible and let the player walk through. It turns invisible — but the player still bumps into an invisible wall.

```lua
local door = script.Parent

door.Touched:Connect(function(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		door.Transparency = 1
	end
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Plan first, then build. List your obby sections in order, **easy → hard**. Write where the checkpoints (SpawnLocation parts) go, and where you will put lava, doors, vanishing bridges, and coins.

<div class="write-space"></div>

Now build your full obby in Roblox Studio: a start, at least 3 sections, at least 1 checkpoint, coins, and a win pad at the end. Beat it yourself in Play mode. When you finish, come back here.

Send a photo or video of your finished obby, then explain what you built. Use these sentence starters — write 4 to 6 sentences total.

> My obby has … sections, in this order: …
>
> The easiest section is … and the hardest is …
>
> I put a checkpoint at … because …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you **playtest** your full obby from start to finish. Talk through it like you are teaching someone who has never seen it. Try to use these words: **section**, **checkpoint**, **playtest**, **humanoid**, **win**.

> 1. Start at the spawn and play through every section — show that each one **can be beaten**.
> 2. Fall on purpose once and show that the checkpoint works — you respawn there, not at the start.
> 3. Collect a coin and show the leaderboard go up.
> 4. Touch the win pad and read your win-pad script out loud — say what the `if humanoid then` check stops.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
