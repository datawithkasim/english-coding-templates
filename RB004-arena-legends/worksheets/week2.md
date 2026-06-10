# ⚔️ RB004 Week 2 — English Worksheet

**Topic:** Teams — Red vs Blue · **Course:** Arena Legends · **Time:** about 45 minutes

This week your arena gets **teams**. The Teams service holds a Team object for each side, every team has a **TeamColor**, and a SpawnLocation with a matching TeamColor (and `Neutral = false`) only spawns players from that team.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Studio, write what you think will happen.

```lua
-- Script in ServerScriptService
local Teams = game:GetService("Teams")

local red = Instance.new("Team")
red.Name = "Red"
red.TeamColor = BrickColor.new("Bright red")
red.AutoAssignable = true
red.Parent = Teams

local blue = Instance.new("Team")
blue.Name = "Blue"
blue.TeamColor = BrickColor.new("Bright blue")
blue.AutoAssignable = true
blue.Parent = Teams
```

**You test with 2 Players. Both teams are AutoAssignable. Which team does Player1 get? Which team does Player2 get?**

<div class="write-space"></div>

```lua
-- Script in ServerScriptService
local spawn = workspace.RedSpawn

spawn.TeamColor = BrickColor.new("Bright red")
spawn.Neutral = false
```

**RedSpawn is a SpawnLocation. After this script runs, which players are allowed to spawn at RedSpawn? What about a Blue player?**

<div class="write-space"></div>

```lua
-- Script in ServerScriptService
local Teams = game:GetService("Teams")

local red = Instance.new("Team")
red.Name = "Red"
red.TeamColor = BrickColor.new("Bright red")
red.AutoAssignable = true
red.Parent = Teams

local blue = Instance.new("Team")
blue.Name = "Blue"
blue.TeamColor = BrickColor.new("Bright blue")
blue.AutoAssignable = false
blue.Parent = Teams
```

**Blue is NOT AutoAssignable. You test with 2 Players. Which team do both players join? What happens to the Blue team?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The Red team uses `BrickColor.new("Bright red")`. This SpawnLocation should spawn **only Red players**, but nobody ever spawns there.

```lua
-- Script in ServerScriptService
local spawn = workspace.RedSpawn

spawn.TeamColor = BrickColor.new("Really red")
spawn.Neutral = false
```

**Hint:** the spawn's TeamColor must match a team's TeamColor **exactly** — "Really red" and "Bright red" are two different colors.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Players should be sorted onto Red and Blue automatically when they join. Instead, everyone joins as Neutral.

```lua
-- Script in ServerScriptService
local Teams = game:GetService("Teams")

local red = Instance.new("Team")
red.Name = "Red"
red.TeamColor = BrickColor.new("Bright red")
red.AutoAssignable = false
red.Parent = Teams

local blue = Instance.new("Team")
blue.Name = "Blue"
blue.TeamColor = BrickColor.new("Bright blue")
blue.AutoAssignable = false
blue.Parent = Teams
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Red and Blue should be two different teams. But in the game, the two teams get mixed up and the spawns don't work right.

```lua
-- Script in ServerScriptService
local Teams = game:GetService("Teams")

local red = Instance.new("Team")
red.Name = "Red"
red.TeamColor = BrickColor.new("Bright red")
red.AutoAssignable = true
red.Parent = Teams

local blue = Instance.new("Team")
blue.Name = "Blue"
blue.TeamColor = BrickColor.new("Bright red")
blue.AutoAssignable = true
blue.Parent = Teams
```

**Hint:** Roblox tells teams apart by **TeamColor**, not by Name. Two teams must never share one color.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your own arena game. Make a Red team and a Blue team, give each team its own SpawnLocation with a matching TeamColor and `Neutral = false`, then test with **Test tab → 2 Players**. When you finish, come back here.

Send a photo or video of the two players standing at their team spawns, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I gave each team a different **TeamColor** because …
>
> I set **Neutral = false** on the spawns so that …
>
> When I tested with 2 Players, I saw …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you test your teams with 2 Players. Talk through it like you are teaching someone who has never seen it. Try to use these words: **team**, **TeamColor**, **AutoAssignable**, **SpawnLocation**, **Neutral**.

> 1. Show your Teams folder and read the two team names and colors out loud.
> 2. Press Test → 2 Players and show which team each player joined.
> 3. Show that each player spawned at their own team's SpawnLocation.
> 4. Say in your own words how a SpawnLocation knows which team it belongs to.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
