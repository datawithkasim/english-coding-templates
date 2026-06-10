# 🏃 RB001 Week 4 — English Worksheet

**Topic:** Conditionals — the Magic Door · **Course:** Obby Architect · **Time:** about 45 minutes

This week you learned **if / else**. The code asks a question — if the answer is true, one branch runs; if not, the `else` branch runs. You used this to build a magic door that opens only for players.

---

## 1 · Predict 🔮

Read each script. Before you run anything, write what you think will happen.

```lua
local door = script.Parent

local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		door.Transparency = 0.8
		door.CanCollide = false
	end
end

door.Touched:Connect(onTouch)
```

**A player touches the door — what happens? A rolling ball touches the door — what happens?**

<div class="write-space"></div>

```lua
local door = script.Parent

local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		print("Welcome, player!")
	else
		print("You are not a player.")
	end
end

door.Touched:Connect(onTouch)
```

**A loose ball rolls into the door. Which message prints? Why?**

<div class="write-space"></div>

```lua
local password = "magic"

if password == "magic" then
	print("The door opens")
else
	print("The door stays shut")
end
```

**Which line prints? What prints if you change the first line to `local password = "abc"`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The script should print `The door opens` when the password is `"magic"`. Instead there is a red error. Count the equals signs.

```lua
local password = "magic"

if password = "magic" then
	print("The door opens")
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The door should open when a player touches it. There is a red error as soon as the game starts. One word is missing.

```lua
local door = script.Parent

local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		door.Transparency = 0.8
		door.CanCollide = false
end

door.Touched:Connect(onTouch)
```

**Hint:** every `if … then` and every `function` needs its own `end`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The door should **open** for players (see-through, walk through) and stay solid for everything else. Right now it does the opposite. The two branches are swapped.

```lua
local door = script.Parent

local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		door.Transparency = 0
		door.CanCollide = true
	else
		door.Transparency = 0.8
		door.CanCollide = false
	end
end

door.Touched:Connect(onTouch)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your own obby in Roblox Studio. Build a magic door — when a player touches it, it turns see-through (`Transparency = 0.8`) and lets them walk through (`CanCollide = false`). When you finish, come back here.

Send a photo or video of your magic door, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My `if` checks whether …
>
> When the condition is true, the door …
>
> The `else` branch runs when …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while a player walks through your magic door. Talk through it like you are teaching someone who has never seen it. Try to use these words: **if**, **else**, **condition**, **true**, **Humanoid**.

> 1. Show your magic door in Roblox Studio, then run the game.
> 2. Walk into the door and show it opening for you.
> 3. Open your script and read the `if humanoid then` line out loud.
> 4. Say in your own words what **if / else** means.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
