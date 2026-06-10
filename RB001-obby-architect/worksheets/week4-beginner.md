# 🏃 RB001 Week 4 — English Worksheet (Beginner)

**Topic:** Conditionals — the Magic Door · **Course:** Obby Architect · **Level:** Beginner · **Time:** about 30 minutes

This week you learned **if / else**. The code asks a question — if the answer is true, one branch runs; if not, the `else` branch runs. You used this to build a magic door.

---

## 1 · Predict 🔮

Read the script. Before you run anything, circle or write your answer.

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

**A player touches the door. Does the door open? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local password = "magic"

if password == "magic" then
	print("The door opens")
else
	print("The door stays shut")
end
```

**Does `The door opens` print? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The script should check the password. Count the equals signs.

```lua
-- clean
if password == "magic" then
	print("The door opens")
end
```

```lua
-- buggy
if password = "magic" then
	print("The door opens")
end
```

**What is wrong?**

<div class="write-space short"></div>

**Pair B** — Every `if … then` needs its own `end`. One is missing in the buggy version.

```lua
-- clean
if humanoid then
	door.CanCollide = false
end
```

```lua
-- buggy
if humanoid then
	door.CanCollide = false
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The door should open when a Humanoid is found. One word is missing. Fill it in using the word bank.

```lua
if humanoid ____
	door.CanCollide = false
end
```

**Word bank:** `then` · `else` · `end`

**Write the missing word:**

<div class="write-space short"></div>

The `if` block needs its closing word. One word is missing.

```lua
if humanoid then
	print("Welcome, player!")
____
```

**Word bank:** `end` · `then` · `local`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your own obby in Roblox Studio. Build a magic door — when a player touches it, it turns see-through and lets them walk through. When you finish, come back here.

Send a photo or video of your magic door, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My `if` checks whether …
>
> When the condition is true, the door …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while a player walks through your magic door. Talk like you are teaching a friend. Try to use these words: **if**, **else**, **condition**, **true**.

> 1. Run the game and walk into your magic door.
> 2. Read your `if humanoid then` line out loud.
> 3. Say in your own words what **if / else** means.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
