# 🏃 RB001 Week 3 — English Worksheet (Beginner)

**Topic:** Functions & Events — the Lava Floor · **Course:** Obby Architect · **Level:** Beginner · **Time:** about 30 minutes

This week you learned **functions** and the **Touched event**. `lava.Touched:Connect(onTouch)` tells Roblox: "when something touches the lava, run this function."

---

## 1 · Predict 🔮

Read the script. Before you run anything, circle or write your answer.

```lua
local lava = script.Parent

local function onTouch(otherPart)
	print("Something touched the lava!")
end

lava.Touched:Connect(onTouch)
```

**The game starts but nothing has touched the lava yet. Does the message print? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

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

**A player steps on the lava. Does their health go to 0? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The lava should print a message when touched. One line is missing in the buggy version.

```lua
-- clean
local lava = script.Parent

local function onTouch(otherPart)
	print("Hot!")
end

lava.Touched:Connect(onTouch)
```

```lua
-- buggy
local lava = script.Parent

local function onTouch(otherPart)
	print("Hot!")
end
```

**What is wrong? Why does the buggy function never run?**

<div class="write-space short"></div>

**Pair B** — The lava should kill players only. The buggy version forgets the safety check.

```lua
-- clean
local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		humanoid.Health = 0
	end
end
```

```lua
-- buggy
local function onTouch(otherPart)
	local humanoid = otherPart.Parent:FindFirstChildWhichIsA("Humanoid")
	humanoid.Health = 0
end
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The script should run the function when the lava is touched. One word is missing. Fill it in using the word bank.

```lua
lava.Touched:____(onTouch)
```

**Word bank:** `Connect` · `print` · `local`

**Write the missing word:**

<div class="write-space short"></div>

The function needs its closing word. One word is missing.

```lua
local function onTouch(otherPart)
	print("Hot!")
____
```

**Word bank:** `end` · `local` · `true`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your own obby in Roblox Studio. Build a lava floor section with a kill brick — touch the lava and your character's health drops to 0. When you finish, come back here.

Send a photo or video of your lava section, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My function runs when …
>
> The lava kills the player by …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while a player runs your lava section. Talk like you are teaching a friend. Try to use these words: **function**, **event**, **Touched**, **Connect**.

> 1. Run the game and step on the lava.
> 2. Read your `lava.Touched:Connect(onTouch)` line out loud.
> 3. Say in your own words what an **event** is.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
