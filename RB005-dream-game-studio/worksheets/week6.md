# 🎮 RB005 Week 6 — English Worksheet

**Topic:** Playtest & Iterate — Find Bugs, Fix Bugs · **Course:** Dream Game Studio · **Time:** about 45 minutes

This week you are a **bug hunter**. Real game studios playtest, write down every bug, fix it, and test again. Your loop is: **see it → write the steps → fix it → retest**.

---

## 1 · Predict 🔮

A classmate playtested your game and left these complaints. Before you open any script, predict **which script** most likely has the bug, and what is wrong inside it.

> Playtester says: *"I touched a coin but my points did not go up."*

**Which script would you open first — the coin's Touched script, the menu LocalScript, or the leaderstats script? What would you look for inside it?**

<div class="write-space"></div>

> Playtester says: *"I touched one coin and got 3 points from it!"*

**Which script has the bug? What is the script missing? (Hint: it is something you add so a Touched event cannot fire many times.)**

<div class="write-space"></div>

> Playtester says: *"The sign says I need 5 coins, but the door opened when I only had 4."*

**Which script has the bug? Which exact line would you read carefully, and what number or symbol might be wrong?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Two of these are real code bugs, one is a **design bug** — a bug with no broken code at all. Read what each one is **supposed** to do, then write your fix and explain why it works.

**Bug A** — Touching a coin should give **exactly 1 point**, then the coin should be gone. Right now one touch can give many points.

```lua
local coin = script.Parent

coin.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		player.leaderstats.Coins.Value += 1
	end
end)
```

**Hint:** a debounce variable stops the event from firing again, or you can `coin:Destroy()` after the first point.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The door should open when the player has **5 coins or more**. Playtesters say it only opens at 6.

```lua
local door = script.Parent

door.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player and player.leaderstats.Coins.Value > 5 then
		door.CanCollide = false
		door.Transparency = 0.7
	end
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — *Design bug, no broken code.* Every playtester spawns, looks around, and walks the **wrong way**. They say: *"I don't know where to go."* All your scripts work perfectly.

**Write your fix idea (think: signs, arrows, a TextLabel instruction, a glowing path, a camera view of the goal):**

<div class="write-space"></div>

**Why is this still a bug, even though no script is broken?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now playtest your own game (and swap with a classmate online if you can — watch them play, do not help them!). Hunt for at least 3 bugs and log them in the table. A "bug" can be a code bug OR a design bug.

| # | What happened? | Steps to make it happen | My fix idea | Fixed? ✅ |
|---|----------------|--------------------------|-------------|-----------|
| 1 |                |                          |             |           |
| 2 |                |                          |             |           |
| 3 |                |                          |             |           |

Send a photo or video of your game after the fixes, then explain your bug hunt. Use these sentence starters — write 4 to 6 sentences total.

> The worst bug I found was …
>
> To make it happen again, I had to …
>
> I fixed it by …
>
> When I retested, …
>
> My playtester was confused when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) showing **one bug before and after the fix**. Talk through it like you are teaching someone who has never seen it. Try to use these words: **bug**, **reproduce**, **debounce**, **fix**, **retest**.

> 1. Show the bug happening. Say the steps to reproduce it out loud.
> 2. Open the script and point at the broken line (or show the confusing place in your map for a design bug).
> 3. Show your fix and read the changed line out loud.
> 4. Retest on camera and show that the bug is gone.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
