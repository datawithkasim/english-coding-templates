# 📜 RB002 Week 7 — English Worksheet

**Topic:** Build Week — Your Full Quest · **Course:** Story Quest · **Time:** about 45 minutes

No new syntax this week. You connect everything you know — ProximityPrompt, `if/elseif/else` quest states, item counters, and reward functions — into **one full quest** that a player can start and finish.

---

## 1 · Predict 🔮

Read this complete NPC quest script. It is used for all three questions below.

```lua
local prompt = script.Parent.ProximityPrompt
local questDone = false

local function giveReward(player, amount)
	player.leaderstats.Coins.Value += amount
end

prompt.Triggered:Connect(function(player)
	local crystals = player.leaderstats.Crystals
	if questDone then
		print("Elder: Thank you again, " .. player.Name .. "!")
	elseif crystals.Value >= 5 then
		questDone = true
		giveReward(player, 100)
		print("Elder: All 5 crystals! Take 100 coins.")
	else
		print("Elder: Please find 5 crystals. You have " .. crystals.Value .. ".")
	end
end)
```

**A player with 2 crystals talks to the Elder. Which branch runs? What exactly does the Elder say?**

<div class="write-space"></div>

```lua
	elseif crystals.Value >= 5 then
		questDone = true
		giveReward(player, 100)
```

**The same player comes back with 5 crystals and talks again. What three things happen, in order?**

<div class="write-space"></div>

```lua
	if questDone then
		print("Elder: Thank you again, " .. player.Name .. "!")
```

**The player talks one more time AFTER finishing the quest. Does the Elder give 100 coins again? What does the Elder say? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The reward should happen **once**. Right now the Elder gives 100 coins every single talk, because the quest state never changes.

```lua
prompt.Triggered:Connect(function(player)
	local crystals = player.leaderstats.Crystals
	if questDone then
		print("Elder: Thank you again!")
	elseif crystals.Value >= 5 then
		giveReward(player, 100)
		print("Elder: All 5 crystals! Take 100 coins.")
	else
		print("Elder: Please find 5 crystals.")
	end
end)
```

**Hint:** which line should set `questDone` to `true`?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Same goal: reward only once. Here `questDone = true` exists, but the **branch order** is wrong, so the reward still repeats.

```lua
prompt.Triggered:Connect(function(player)
	local crystals = player.leaderstats.Crystals
	if crystals.Value >= 5 then
		questDone = true
		giveReward(player, 100)
	elseif questDone then
		print("Elder: Thank you again!")
	else
		print("Elder: Please find 5 crystals.")
	end
end)
```

**Hint:** the crystals stay at 5 after the quest, so the first check always wins. Which check must come **first**?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The quest should finish with 5 **or more** crystals. A player who collected 6 crystals can never finish.

```lua
	elseif crystals.Value == 5 then
		questDone = true
		giveReward(player, 100)
```

**Hint:** `==` means "exactly equal".

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your Story Quest game in Roblox Studio and build your **full quest world**. Plan it first: 3 NPCs, what each one says, where the items are, what the reward is, and how the quest ends. Then build it. When you finish, come back here.

Send a photo or video of your quest world, then explain your plan. Use these sentence starters — write 4 to 6 sentences total.

> My quest story is …
>
> My three NPCs are …
>
> NPC 1 says … and the player must …
>
> The items are hidden at …
>
> The reward is …
>
> The quest ends when …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you **playtest** your full quest from start to finish. Talk through it like you are teaching someone who has never seen it. Try to use these words: **quest**, **state**, **elseif**, **reward**, **function**.

> 1. Press Play and talk to each of your 3 NPCs. Read their lines out loud.
> 2. Collect all the quest items on camera.
> 3. Show the reward moment — the coins going up.
> 4. Talk to the quest NPC **again** and show that the line changed.
> 5. Say what would go wrong if `questDone` never turned `true`.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
