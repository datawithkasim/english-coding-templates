# 🏭 RB003 Week 1 — English Worksheet (Beginner)

**Topic:** The Dropper — Making Parts with Code · **Course:** Tycoon Engineer · **Level:** Beginner · **Time:** about 30 minutes

This week your script **creates parts from code** using `Instance.new`. A dropper spawns ore again and again with a `while` loop and `task.wait`.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Roblox Studio, circle or write your answer.

```lua
local ore = Instance.new("Part")
ore.Position = Vector3.new(0, 10, 0)
ore.Parent = workspace
```

**The ore has a Parent. Does an ore appear in the game? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local ore = Instance.new("Part")
ore.Position = Vector3.new(0, 10, 0)
```

**This time the `ore.Parent` line is missing. Does an ore appear? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The ore should **appear in the game**.

```lua
-- clean
local ore = Instance.new("Part")
ore.Position = Vector3.new(0, 10, 0)
ore.Parent = workspace
```

```lua
-- buggy
local ore = Instance.new("Part")
ore.Position = Vector3.new(0, 10, 0)
```

**What is wrong? Why does the buggy ore never appear?**

<div class="write-space short"></div>

**Pair B** — The dropper should spawn one ore **every 2 seconds**, not freeze the game.

```lua
-- clean
while true do
	local ore = Instance.new("Part")
	ore.Parent = workspace
	task.wait(2)
end
```

```lua
-- buggy
while true do
	local ore = Instance.new("Part")
	ore.Parent = workspace
end
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The ore should appear in the game. One word is missing. Fill it in using the word bank.

```lua
local ore = Instance.new("Part")
ore.____ = workspace
```

**Word bank:** `Parent` · `Size` · `Position`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to Roblox Studio and open your tycoon. Build a dropper that spawns an ore every 2 seconds. When you finish, come back here.

Send a photo or video of your dropper spawning ore, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I used `Instance.new` to …
>
> My loop spawns a new ore every …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your dropper runs. Talk like you are teaching a friend. Try to use these words: **Instance.new**, **Parent**, **loop**, **task.wait**.

> 1. Show your dropper in Roblox Studio, then press Play.
> 2. Read your `while` loop out loud.
> 3. Say in your own words what `task.wait(2)` does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
