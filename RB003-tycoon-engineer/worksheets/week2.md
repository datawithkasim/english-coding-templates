# 🏭 RB003 Week 2 — English Worksheet

**Topic:** Conveyor & Collector — Touch, Pay, Destroy · **Course:** Tycoon Engineer · **Time:** about 45 minutes

This week ore rides a **conveyor** into a **collector pad**. The pad uses `Touched` to check the part's name, pay cash, and destroy the ore.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local conveyor = script.Parent
conveyor.Anchored = true
conveyor.AssemblyLinearVelocity = Vector3.new(8, 0, 0)
```

**The conveyor is anchored, so it stays still. What happens to an ore that lands on top of it?**

<div class="write-space"></div>

```lua
local collector = script.Parent

collector.Touched:Connect(function(otherPart)
	if otherPart.Name == "Ore" then
		print("Ore collected!")
	end
end)
```

**A part named `Ore` touches the pad. What prints? A player's foot touches the pad — what prints then?**

<div class="write-space"></div>

```lua
local collector = script.Parent
local cash = workspace.Cash -- an IntValue named "Cash"

collector.Touched:Connect(function(otherPart)
	if otherPart.Name == "Ore" then
		cash.Value += 5
		otherPart:Destroy()
	end
end)
```

**Three ores ride the conveyor onto the pad, one by one. How much cash do you earn in total? What happens to each ore?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The pad should pay 5 cash for every part named `Ore`. Ores touch the pad but the cash **never goes up** — and there is no red error.

```lua
collector.Touched:Connect(function(otherPart)
	if otherPart.Name == "ore" then
		cash.Value += 5
		otherPart:Destroy()
	end
end)
```

**Hint:** the ores in workspace are named `Ore` with a capital O.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Each ore should pay **once** and then disappear. Instead, the ores pile up on the pad and keep paying **over and over** every time they touch it.

```lua
collector.Touched:Connect(function(otherPart)
	if otherPart.Name == "Ore" then
		cash.Value += 5
	end
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The conveyor should stay in place and push the ore along the top. Instead, the **conveyor itself slides away** when the game starts.

```lua
local conveyor = script.Parent
conveyor.Anchored = false
conveyor.AssemblyLinearVelocity = Vector3.new(8, 0, 0)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to Roblox Studio and open your tycoon. Build a conveyor that pushes ore into a collector pad. The pad should pay cash with `+=` and destroy the ore. When you finish, come back here.

Send a photo or video of an ore riding the conveyor and your cash going up, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My conveyor pushes the ore because …
>
> When an ore touches the pad, …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your tycoon runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **Touched**, **conveyor**, **velocity**, **Destroy**, **cash**.

> 1. Press Play and show an ore landing on your conveyor.
> 2. Show the ore riding into the collector pad and your cash going up.
> 3. Read your `Touched` function out loud and say when the `if` runs.
> 4. Say in your own words why we call `otherPart:Destroy()`.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
