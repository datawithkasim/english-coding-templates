# ⚔️ RB004 Week 5 — English Worksheet

**Topic:** Power-Ups — Speed Pads with task.delay · **Course:** Arena Legends · **Time:** about 45 minutes

This week you built a **power-up**: a speed pad that makes a player faster for a few seconds, then disappears and **respawns** later. The magic words are `task.delay` (do something later, don't wait) and `task.wait` (stop and wait here).

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local pad = script.Parent

pad.Touched:Connect(function(hit)
	local humanoid = hit.Parent:FindFirstChild("Humanoid")
	if humanoid then
		humanoid.WalkSpeed = 32
	end
end)
```

**A player steps on the pad. What happens to their speed? Now a loose brick falls on the pad — does anything happen? Why?**

<div class="write-space"></div>

```lua
humanoid.WalkSpeed = 32
print("Boost on!")
task.delay(5, function()
	humanoid.WalkSpeed = 16
end)
print("This line runs!")
```

**In what order do the two prints appear? Does the script stop and wait 5 seconds between them? When does the speed go back to 16?**

<div class="write-space"></div>

```lua
pad.Transparency = 1
pad.CanCollide = false
task.wait(10)
pad.Transparency = 0
pad.CanCollide = true
```

**What does the player see right after this code starts? What happens after 10 seconds? Why do we change `CanCollide` too, not just `Transparency`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The speed boost should last **5 seconds**, then the player goes back to normal speed (16). Right now the boost is **forever**.

```lua
pad.Touched:Connect(function(hit)
	local humanoid = hit.Parent:FindFirstChild("Humanoid")
	if humanoid then
		humanoid.WalkSpeed = 32
	end
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Same goal: boost to 32, then back to 16 **after 5 seconds**. But this boost lasts **0 seconds** — the player never feels faster.

```lua
if humanoid then
	humanoid.WalkSpeed = 32
	humanoid.WalkSpeed = 16
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — After a player grabs the pickup, it should hide, then **come back after 10 seconds**. Right now it disappears and **never comes back**.

```lua
pad.Transparency = 1
pad.CanCollide = false
```

**Hint:** the script needs to **wait**, then turn the pad back on.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your arena in Roblox Studio. Build a speed pad power-up: it boosts `WalkSpeed`, resets after 5 seconds, hides when touched, and respawns after 10 seconds. When you finish, come back here.

Send a photo or video of your power-up working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> When a player touches the pad, …
>
> I used **task.delay** so that …
>
> The pad respawns when …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you playtest your power-up in Roblox Studio. Talk through it like you are teaching someone who has never seen it. Try to use these words: **Touched**, **Humanoid**, **WalkSpeed**, **task.delay**, **respawn**.

> 1. Show your speed pad in the arena, then press Play.
> 2. Step on the pad and show how fast you run. Say what number `WalkSpeed` became.
> 3. Wait and show the speed going back to normal. Explain why the script did not freeze while waiting.
> 4. Show the pad disappearing and coming back. Say in your own words what **task.delay** does.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
