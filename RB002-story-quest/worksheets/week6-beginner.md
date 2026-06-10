# 📜 RB002 Week 6 — English Worksheet (Beginner)

**Topic:** Functions with Parameters & Returns · **Course:** Story Quest · **Level:** Beginner · **Time:** about 30 minutes

This week you write functions that take **parameters** and give back **return** values. A parameter is a slot in the function. You fill the slot when you **call** the function.

---

## 1 · Predict 🔮

Read the script. Before you imagine it running in Roblox Studio, circle or write your answer.

```lua
local function giveReward(player, amount)
	player.leaderstats.Coins.Value += amount
end

giveReward(player, 50)
```

**Does the player get 50 coins? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local function questComplete(count)
	return count >= 5
end

print(questComplete(2))
```

**Does this print `true`? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows a clean script first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The call should fill **both** slots: the player and the amount.

```lua
-- clean
giveReward(player, 50)
```

```lua
-- buggy
giveReward(player)
```

**What is wrong? What is missing in the buggy call?**

<div class="write-space short"></div>

**Pair B** — The function should **return** the answer.

```lua
-- clean
local function questComplete(count)
	return count >= 5
end
```

```lua
-- buggy
local function questComplete(count)
	count >= 5
end
```

**What is wrong? Which word is missing?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The function should give back `true` when the count is 5 or more. One word is missing. Fill it in using the word bank.

```lua
local function questComplete(count)
	______ count >= 5
end
```

**Word bank:** `return` · `print` · `local`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your Story Quest game in Roblox Studio. Write a `giveReward` function and call it with two arguments. When you finish, come back here.

Send a photo or video of your function working, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My function `giveReward` takes …
>
> I called it with …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you play your game in Studio. Talk like you are teaching a friend. Try to use these words: **function**, **parameter**, **call**.

> 1. Open your script and read your `giveReward` function out loud.
> 2. Press Play and show the reward happening in the game.
> 3. Say in your own words what a **parameter** is.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
