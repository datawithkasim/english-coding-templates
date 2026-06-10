# ⚔️ RB004 Week 5 — English Worksheet (Beginner)

**Topic:** Power-Ups — Speed Pads with task.delay · **Course:** Arena Legends · **Level:** Beginner · **Time:** about 30 minutes

This week you built a **power-up**: a speed pad that makes a player faster for a few seconds. `task.delay` means "do this later, but don't stop the script."

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Roblox Studio, circle or write your answer.

```lua
pad.Touched:Connect(function(hit)
	local humanoid = hit.Parent:FindFirstChild("Humanoid")
	if humanoid then
		humanoid.WalkSpeed = 32
	end
end)
```

**A player steps on the pad. Does the player get faster? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
humanoid.WalkSpeed = 32
task.delay(5, function()
	humanoid.WalkSpeed = 16
end)
```

**Is the player still fast after 10 seconds? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The boost should go back to normal **after 5 seconds**.

```lua
-- clean
humanoid.WalkSpeed = 32
task.delay(5, function()
	humanoid.WalkSpeed = 16
end)
```

```lua
-- buggy
humanoid.WalkSpeed = 32
```

**What is wrong? How long does the buggy boost last?**

<div class="write-space short"></div>

**Pair B** — The pad should hide, then **come back after 10 seconds**.

```lua
-- clean
pad.Transparency = 1
pad.CanCollide = false
task.wait(10)
pad.Transparency = 0
pad.CanCollide = true
```

```lua
-- buggy
pad.Transparency = 1
pad.CanCollide = false
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The script should make the player faster. One word is missing. Fill it in using the word bank.

```lua
if humanoid then
	humanoid.____ = 32
end
```

**Word bank:** `WalkSpeed` · `Transparency` · `Touched`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your arena in Roblox Studio. Build a speed pad that boosts a player, then resets after 5 seconds. When you finish, come back here.

Send a photo or video of your power-up working, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> When a player touches the pad, …
>
> I used **task.delay** so that …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you playtest your power-up in Roblox Studio. Talk like you are teaching a friend. Try to use these words: **Touched**, **WalkSpeed**, **task.delay**.

> 1. Show your speed pad, then press Play.
> 2. Step on the pad and show how fast you run.
> 3. Say in your own words what **task.delay** does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
