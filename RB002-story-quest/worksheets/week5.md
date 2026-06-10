# 📜 RB002 Week 5 — English Worksheet

**Topic:** Quest Items — Pick Up Crystals · **Course:** Story Quest · **Time:** about 45 minutes

This week your player picks up **quest items**. A crystal counts up when a player touches it, then disappears with `Destroy()`. A **debounce** stops double-counting, and a **TextLabel** on screen shows the count.

---

## 1 · Predict 🔮

Read each script. Before you imagine it running in Roblox Studio, write what you think will happen.

```lua
local crystal = script.Parent
local Players = game:GetService("Players")

crystal.Touched:Connect(function(hit)
	local player = Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Crystals.Value += 1
		crystal:Destroy()
	end
end)
```

**A player walks into the crystal. What happens to the Crystals counter? What happens to the crystal part?**

<div class="write-space"></div>

```lua
local count = 3
print("Crystals: " .. count)
```

**What exactly prints in the Output window? Write it letter by letter.**

<div class="write-space"></div>

```lua
local touched = false

crystal.Touched:Connect(function(hit)
	local player = Players:GetPlayerFromCharacter(hit.Parent)
	if player and not touched then
		touched = true
		print("Picked up!")
	end
end)
```

**The player's foot AND leg both touch the crystal at almost the same time. How many times does "Picked up!" print? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — Touching the crystal should add **exactly 1** to the counter. Right now it sometimes adds 2 or 3, because `Touched` fires many times before `Destroy()` finishes.

```lua
crystal.Touched:Connect(function(hit)
	local player = Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Crystals.Value += 1
		crystal:Destroy()
	end
end)
```

**Hint:** add a **debounce** variable that starts `false`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The label should show `Crystals: 4`. Right now the script turns red and shows an error.

```lua
label.Text = "Crystals: " + crystals.Value
```

**Hint:** in Luau, `+` is only for math. Joining text needs a different symbol.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Only **players** should collect the crystal. Right now the crystal destroys itself on ANY touch — even a rolling ball — and then the script errors because `player` is `nil`.

```lua
crystal.Touched:Connect(function(hit)
	crystal:Destroy()
	local player = Players:GetPlayerFromCharacter(hit.Parent)
	player.leaderstats.Crystals.Value += 1
end)
```

**Hint:** check `if player then` **before** you count or destroy anything.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your Story Quest game in Roblox Studio. Build at least 3 crystals that players can pick up, with a counter and a TextLabel that shows the count. When you finish, come back here.

Send a photo or video of your crystals and your label, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My crystal script uses **Touched** when …
>
> The counter went up when …
>
> My label shows …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you play your game in Studio. Talk through it like you are teaching someone who has never seen it. Try to use these words: **Touched**, **debounce**, **counter**, **Destroy**, **label**.

> 1. Show your crystals before you touch them, then press Play.
> 2. Pick up one crystal and show the counter going up by exactly 1.
> 3. Point at your label and read what it says out loud.
> 4. Open your script and read the debounce lines. Say why they stop double-counting.
> 5. Say in your own words what `Destroy()` does.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
