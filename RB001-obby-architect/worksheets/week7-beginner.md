# 🏃 RB001 Week 7 — English Worksheet (Beginner)

**Topic:** Build Week — Your Full Obby · **Course:** Obby Architect · **Level:** Beginner · **Time:** about 30 minutes

No new syntax this week. You put everything together: lava, doors, vanishing platforms, coins, and a win pad — one full obby.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

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

**A player jumps on the win pad. Does the pad flash colors? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local lava = script.Parent

lava.Touched:Connect(function(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		humanoid.Health = 0
	end
end)
```

**A loose block falls onto the lava. The block has no Humanoid. Does anything happen? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows a clean script first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The win pad should only celebrate for a **player**.

```lua
-- clean
winPad.Touched:Connect(function(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		print("You win!")
	end
end)
```

```lua
-- buggy
winPad.Touched:Connect(function(otherPart)
	print("You win!")
end)
```

**What is wrong? When does the buggy pad say "You win!" too early?**

<div class="write-space short"></div>

**Pair B** — The door should open: invisible **and** walk-through.

```lua
-- clean
if humanoid then
	door.Transparency = 1
	door.CanCollide = false
end
```

```lua
-- buggy
if humanoid then
	door.Transparency = 1
end
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The win pad needs to find the player's Humanoid. One word is missing. Fill it in using the word bank.

```lua
local humanoid = otherPart.Parent:FindFirstChildWhichIsA("________")
if humanoid then
	print("You win!")
end
```

**Word bank:** `Humanoid` · `Head` · `Part`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now build your full obby in Roblox Studio: a start, at least 2 sections, 1 checkpoint (SpawnLocation), and a win pad at the end. Beat it yourself in Play mode. When you finish, come back here.

Send a photo or video of your finished obby, then explain what you built. Use these sentence starters — write 2 or 3 sentences.

> My obby has … sections: …
>
> The hardest part is …
>
> My checkpoint is at …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you playtest your obby from start to finish. Talk like you are teaching a friend. Try to use these words: **section**, **checkpoint**, **win**.

> 1. Play through every section and show each one can be beaten.
> 2. Fall once on purpose and show the checkpoint works.
> 3. Touch the win pad and say what your win-pad script does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
