# 🎮 RB005 Week 8 — English Worksheet

**Topic:** Launch & Showcase — Publish and Present · **Course:** Dream Game Studio · **Time:** about 45 minutes

This is it — **launch week**. You publish your game as **Public** and present it like a real game studio: what the game is, your hardest bug story, your favorite script read out loud, and what you would build next.

---

## 1 · Predict 🔮

Read each situation. Before it happens for real, write what you think will happen.

> You publish your game and set it to **Public**. Your classmate searches its title on Roblox from their own house.

**What can your classmate do now that they could not do yesterday? What can they NOT do (hint: they cannot open your scripts)?**

<div class="write-space"></div>

> Your game is Public, but you only ever tested it **alone in Studio**. A stranger joins and clicks Play.

**Predict one thing that might go wrong for the stranger that never went wrong for you. How would you find out about it?**

<div class="write-space"></div>

```lua
local door = script.Parent

door.Touched:Connect(function(hit)
	local player = game.Players:GetPlayerFromCharacter(hit.Parent)
	if player and player.leaderstats.Coins.Value >= 5 then
		door.CanCollide = false
		door.Transparency = 0.7
	end
end)
```

**In your showcase you read a script like this out loud. Practice now: what does this script do, in one or two sentences a non-coder could understand?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Launch-day bugs! Read what each one is **supposed** to be, write your fix, then explain why the original was wrong and why your fix works.

**Bug A** — Everyone should be able to find and play the game. You told the whole class it is live, but nobody can join.

> In Game Settings → Permissions, the game is still set to **Private**.

**Write the fix (what setting do you change, and to what):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Players should start with **0 coins** and earn them by playing. But this test script from week 6 is still in `ServerScriptService`, so everyone wins instantly.

```lua
-- TEST: remove before launch!
game.Players.PlayerAdded:Connect(function(player)
	local leaderstats = player:WaitForChild("leaderstats")
	leaderstats.Coins.Value = 999
end)
```

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — A showcase presentation should be interesting for the audience. This is a classmate's whole plan:

> *"Hi. This is my game. I show the game now. … OK that's all. The end."*

**Write a fixed plan (list at least 4 things the presentation should include — think: what the game is, the hardest bug story, a script read aloud, what comes next):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Publish your game as **Public**, then plan your showcase here. Send a photo or video of your live game page, and write your presentation plan. Use these sentence starters — write 4 to 6 sentences total.

> My game is called … and it is a game where …
>
> The hardest bug I ever had was … and I fixed it by …
>
> My favorite script is the one that … because …
>
> In Roblox 1 week 1, I could not … but this week I …
>
> The next thing I would build is …
>
> The best moment of these 5 courses was …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

This week your video **IS** the presentation. Take a video on your phone (or a parent's phone) and present your game from start to finish, like you are on stage at a game studio. Try to use these words: **publish**, **public**, **bug**, **script**, **update**.

> 1. Say your game's name and what kind of game it is. Show the title screen.
> 2. Play your game on camera and show the core mechanic.
> 3. Tell your hardest bug story — what happened, and how you fixed it.
> 4. Open your favorite script and read it out loud. Explain it in simple words.
> 5. Finish with what you would build next if the studio kept going.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
