# 🏃 RB001 Week 3 — English Worksheet

**Topic:** Functions & Events — the Lava Floor · **Course:** Obby Architect · **Time:** about 45 minutes

This week you learned **functions** and the **Touched event**. A function is a block of code with a name. `lava.Touched:Connect(onTouch)` tells Roblox: "when something touches the lava, run this function." You used this to build a kill brick.

---

## 1 · Predict 🔮

Read each script. Before you run anything, write what you think will happen.

```lua
local lava = script.Parent

local function onTouch(otherPart)
	print("Something touched the lava!")
end

lava.Touched:Connect(onTouch)
```

**When does the message print? Does it print if nothing ever touches the lava?**

<div class="write-space"></div>

```lua
local lava = script.Parent

local function onTouch(otherPart)
	print("Lava is ready")
end

print("Game started")
lava.Touched:Connect(onTouch)
```

**Which message prints first when the game starts? When does the other one print?**

<div class="write-space"></div>

```lua
local lava = script.Parent

local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		humanoid.Health = 0
	end
end

lava.Touched:Connect(onTouch)
```

**A player steps on the lava — what happens to them? A loose ball rolls onto the lava — what happens to it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The lava should kill any player who touches it. The script runs with no error, but nothing ever happens when you step on it. One line is missing.

```lua
local lava = script.Parent

local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		humanoid.Health = 0
	end
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The lava should kill players only. It works for players, but when a loose ball rolls onto the lava, a red error appears in the Output window.

```lua
local lava = script.Parent

local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	humanoid.Health = 0
end

lava.Touched:Connect(onTouch)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The lava should print `Burned!` when touched. There is a red error as soon as the game starts. Look at the **order** of the lines.

```lua
local lava = script.Parent

lava.Touched:Connect(onTouch)

local function onTouch(otherPart)
	print("Burned!")
end
```

**Hint:** Luau reads a script from top to bottom.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your own obby in Roblox Studio. Build a lava floor section with kill bricks — touch the lava and your character's health drops to 0. When you finish, come back here.

Send a photo or video of your lava section, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My function is called … and it runs when …
>
> I used `:Connect` to …
>
> I checked for a Humanoid because …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while a player runs your lava section. Talk through it like you are teaching someone who has never seen it. Try to use these words: **function**, **event**, **Touched**, **Connect**, **Humanoid**.

> 1. Show your lava section in Roblox Studio, then run the game.
> 2. Step on the lava and show what happens to your character.
> 3. Open your script and read the `lava.Touched:Connect(onTouch)` line out loud.
> 4. Say in your own words what an **event** is.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
