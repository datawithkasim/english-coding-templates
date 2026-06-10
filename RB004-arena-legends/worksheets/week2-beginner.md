# ⚔️ RB004 Week 2 — English Worksheet (Beginner)

**Topic:** Teams — Red vs Blue · **Course:** Arena Legends · **Level:** Beginner · **Time:** about 30 minutes

This week your arena gets **teams**. Every team has a **TeamColor**, and a SpawnLocation with the same TeamColor (and `Neutral = false`) only spawns players from that team.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

```lua
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

**You test with 2 Players. Both teams are AutoAssignable. Do the two players end up on different teams? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local spawn = workspace.RedSpawn

spawn.TeamColor = BrickColor.new("Bright red")
spawn.Neutral = false
```

**RedSpawn is a SpawnLocation. Can a Blue player spawn at RedSpawn? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The Red team's color is "Bright red". The spawn's TeamColor must match it **exactly**.

```lua
-- clean
spawn.TeamColor = BrickColor.new("Bright red")
spawn.Neutral = false
```

```lua
-- buggy
spawn.TeamColor = BrickColor.new("Really red")
spawn.Neutral = false
```

**What is wrong? Why does nobody spawn at the buggy spawn?**

<div class="write-space short"></div>

**Pair B** — Players should join the team automatically.

```lua
-- clean
red.AutoAssignable = true
```

```lua
-- buggy
red.AutoAssignable = false
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

Players should join the Red team **automatically** when they enter the game. One word is missing. Fill it in using the word bank.

```lua
local red = Instance.new("Team")
red.Name = "Red"
red.TeamColor = BrickColor.new("Bright red")
red.____ = true
red.Parent = Teams
```

**Word bank:** `AutoAssignable` · `Neutral` · `Anchored`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your own arena game. Make a Red team and a Blue team, and give each team its own SpawnLocation with a matching TeamColor. Test with **Test tab → 2 Players**. When you finish, come back here.

Send a photo or video of the two players at their team spawns, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I gave each team a different **TeamColor** because …
>
> When I tested with 2 Players, I saw …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you test with 2 Players. Talk like you are teaching a friend. Try to use these words: **team**, **TeamColor**, **SpawnLocation**.

> 1. Show your two teams and read their names and colors out loud.
> 2. Press Test → 2 Players and show which team each player joined.
> 3. Say in your own words how a spawn knows which team it belongs to.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
