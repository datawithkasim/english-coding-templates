# 🏭 RB003 Week 1 — English Worksheet

**Topic:** The Dropper — Making Parts with Code · **Course:** Tycoon Engineer · **Time:** about 45 minutes

This week your script **creates parts from code** using `Instance.new`. A dropper spawns ore again and again with a `while` loop and `task.wait`.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local ore = Instance.new("Part")
ore.Size = Vector3.new(1, 1, 1)
ore.Position = Vector3.new(0, 10, 0)
ore.Parent = workspace
```

**A new ore appears 10 studs up in the air. It is NOT anchored. What does it do right after it appears?**

<div class="write-space"></div>

```lua
local ore = Instance.new("Part")
ore.Size = Vector3.new(1, 1, 1)
ore.Position = Vector3.new(0, 10, 0)
ore.Anchored = true
ore.Parent = workspace
```

**This ore IS anchored. Does it fall or float in the air? Why?**

<div class="write-space"></div>

```lua
while true do
	local ore = Instance.new("Part")
	ore.Size = Vector3.new(1, 1, 1)
	ore.Position = Vector3.new(0, 10, 0)
	ore.Parent = workspace
	task.wait(2)
end
```

**About how many ores exist after 6 seconds? What does `task.wait(2)` control?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The script is supposed to make one ore appear in the game. When you press Play, **nothing appears** — but there is no red error.

```lua
local ore = Instance.new("Part")
ore.Size = Vector3.new(1, 1, 1)
ore.Position = Vector3.new(0, 10, 0)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The dropper should spawn one ore **every 2 seconds**. Instead, Roblox Studio spawns thousands of ores instantly and **freezes**.

```lua
while true do
	local ore = Instance.new("Part")
	ore.Position = Vector3.new(0, 10, 0)
	ore.Parent = workspace
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The dropper part itself should **float in the air** above the conveyor. Right now it falls to the ground as soon as the game starts.

```lua
local dropper = Instance.new("Part")
dropper.Size = Vector3.new(2, 2, 2)
dropper.Position = Vector3.new(0, 10, 0)
dropper.Anchored = false
dropper.Parent = workspace
```

**Hint:** look at the `Anchored` line.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to Roblox Studio and open your tycoon. Build a dropper that spawns an ore every 2 seconds using `Instance.new` and a `while` loop. When you finish, come back here.

Send a photo or video of your dropper spawning ore, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I used `Instance.new` to …
>
> My loop spawns a new ore every …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your dropper runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **Instance.new**, **Parent**, **loop**, **task.wait**, **spawn**.

> 1. Show your dropper in Roblox Studio, then press Play.
> 2. Read your `while` loop out loud and say what each line does.
> 3. Point at the falling ores and say how often a new one spawns.
> 4. Say in your own words why `ore.Parent = workspace` is needed.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
