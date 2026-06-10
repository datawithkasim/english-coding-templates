# 📜 RB002 Week 6 — English Worksheet

**Topic:** Functions with Parameters & Returns · **Course:** Story Quest · **Time:** about 45 minutes

This week you write functions that take **parameters** and give back **return** values. A parameter is a slot in the function. An argument is the value you put in the slot when you **call** the function.

---

## 1 · Predict 🔮

Read each script. Before you imagine it running in Roblox Studio, write what you think will happen.

```lua
local function giveReward(player, amount)
	player.leaderstats.Coins.Value += amount
end

giveReward(player, 50)
```

**How many coins does the player get? What value does `amount` hold inside the function?**

<div class="write-space"></div>

```lua
local function questComplete(count)
	return count >= 5
end

print(questComplete(3))
print(questComplete(7))
```

**Two lines print. What are they? Why are they different?**

<div class="write-space"></div>

```lua
local function double(n)
	return n * 2
end

local reward = double(10) + 5
print(reward)
```

**What number prints? Follow the return value step by step.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The player should get **50 coins**. Right now the script errors, because `amount` is `nil`.

```lua
local function giveReward(player, amount)
	player.leaderstats.Coins.Value += amount
end

giveReward(player)
```

**Hint:** the function has two parameters, so the call needs two **arguments**.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — After giving the reward, the script should print the amount. Right now the last line errors, because `amount` does not exist there.

```lua
local function giveReward(player, amount)
	player.leaderstats.Coins.Value += amount
end

giveReward(player, 50)
print("Reward was: " .. amount)
```

**Hint:** a parameter only lives **inside** its function. Move the print.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `questComplete` should answer `true` or `false`. Right now "Quest finished!" never prints, even with 6 crystals.

```lua
local function questComplete(count)
	if count >= 5 then
		print("done")
	end
end

if questComplete(6) then
	print("Quest finished!")
end
```

**Hint:** the function checks the count but never **returns** anything, so the answer is `nil`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your Story Quest game in Roblox Studio. Write a `giveReward` function with parameters and a `questComplete` function that returns `true` or `false`. Use both in your quest. When you finish, come back here.

Send a photo or video of your functions working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My function `giveReward` takes … as parameters.
>
> I called it with the arguments …
>
> My function `questComplete` returns …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you play your game in Studio. Talk through it like you are teaching someone who has never seen it. Try to use these words: **function**, **parameter**, **argument**, **return**, **call**.

> 1. Open your script and read your `giveReward` function out loud.
> 2. Point at the parameters, then point at the arguments in the call.
> 3. Press Play and show the reward happening in the game.
> 4. Read your `questComplete` function and say what it returns when the count is 2, and when it is 5.
> 5. Say in your own words what **return** means.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
