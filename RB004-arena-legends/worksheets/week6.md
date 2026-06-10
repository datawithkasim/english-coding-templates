# ⚔️ RB004 Week 6 — English Worksheet

**Topic:** Scoring & ModuleScripts — Team Points · **Course:** Arena Legends · **Time:** about 45 minutes

This week your arena learned to **count points** with a dictionary, and you put your game settings in a **ModuleScript** — one shared box of values that other scripts can `require`.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local points = {Red = 0, Blue = 0}

points["Red"] += 1
points["Red"] += 1
points["Blue"] += 1

print(points.Red, points.Blue)
```

**What two numbers print? Which team is winning?**

<div class="write-space"></div>

```lua
-- ModuleScript named "Settings" in ServerScriptService
local Settings = {}
Settings.RoundLength = 60
Settings.WinScore = 5
return Settings
```

```lua
-- Script in ServerScriptService
local Settings = require(game.ServerScriptService.Settings)
print(Settings.WinScore)
```

**What prints? If you change `WinScore` to 10 in the ModuleScript, do you need to change the second script too? Why or why not?**

<div class="write-space"></div>

```lua
if points.Red >= Settings.WinScore then
	print("Red team wins!")
end
```

**`WinScore` is 5. Red has exactly 5 points — does Red win? What if Red has 4 points? What does `>=` mean?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This ModuleScript should share `RoundLength` and `WinScore` with other scripts. But every script that uses `require` on it gets an error.

```lua
-- ModuleScript named "Settings"
local Settings = {}
Settings.RoundLength = 60
Settings.WinScore = 5
```

**Hint:** a ModuleScript must **give back** its table at the end.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — When the Red team scores, Red should get one point. Instead the script crashes with an error about `nil`.

```lua
local points = {Red = 0, Blue = 0}

points["red"] += 1
```

**Hint:** dictionary keys care about capital letters.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should check **if** Red has reached the win score. Instead Roblox Studio shows a red error line and the script will not run.

```lua
if points.Red = Settings.WinScore then
	print("Red team wins!")
end
```

**Hint:** one `=` puts a value in. Comparing needs something else — and "reached" means equal **or more**.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your arena in Roblox Studio. Add a points dictionary for Red and Blue, a winner check using `Settings.WinScore`, and a Settings ModuleScript that other scripts `require`. When you finish, come back here.

Send a photo or video of a team scoring and winning, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> A team gets a point when …
>
> I put **RoundLength** and **WinScore** in a ModuleScript because …
>
> My winner check uses **>=** so that …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you playtest your scoring in Roblox Studio. Talk through it like you are teaching someone who has never seen it. Try to use these words: **dictionary**, **points**, **ModuleScript**, **require**, **WinScore**.

> 1. Show your Settings ModuleScript and read the values out loud.
> 2. Press Play and score a point. Show the points changing in the Output window or on screen.
> 3. Show the winner check line and explain when "wins!" appears.
> 4. Say in your own words why a ModuleScript is better than typing 5 in every script.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
