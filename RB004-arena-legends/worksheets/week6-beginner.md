# ⚔️ RB004 Week 6 — English Worksheet (Beginner)

**Topic:** Scoring & ModuleScripts — Team Points · **Course:** Arena Legends · **Level:** Beginner · **Time:** about 30 minutes

This week your arena learned to **count points** for Red and Blue, and you put your game settings in a **ModuleScript** — one shared box of values.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Roblox Studio, circle or write your answer.

```lua
local points = {Red = 0, Blue = 0}

points["Red"] += 1
print(points.Red)
```

**Does it print 1? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local Settings = {}
Settings.WinScore = 5
return Settings
```

```lua
local Settings = require(game.ServerScriptService.Settings)
print(Settings.WinScore)
```

**Does it print 5? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — A ModuleScript must **give back** its table at the end.

```lua
-- clean
local Settings = {}
Settings.WinScore = 5
return Settings
```

```lua
-- buggy
local Settings = {}
Settings.WinScore = 5
```

**What is wrong? What line is missing?**

<div class="write-space short"></div>

**Pair B** — Dictionary keys care about capital letters.

```lua
-- clean
points["Red"] += 1
```

```lua
-- buggy
points["red"] += 1
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The script should check if Red has **reached** the win score. One symbol is missing. Fill it in using the word bank.

```lua
if points.Red ____ Settings.WinScore then
	print("Red team wins!")
end
```

**Word bank:** `>=` · `=` · `+=`

**Write the missing symbol:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your arena in Roblox Studio. Add points for Red and Blue and a winner check. When you finish, come back here.

Send a photo or video of a team scoring and winning, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> A team gets a point when …
>
> I put **WinScore** in a ModuleScript because …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you playtest your scoring in Roblox Studio. Talk like you are teaching a friend. Try to use these words: **points**, **ModuleScript**, **WinScore**.

> 1. Show your Settings ModuleScript and read the values out loud.
> 2. Press Play and score a point.
> 3. Say in your own words when a team wins.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
