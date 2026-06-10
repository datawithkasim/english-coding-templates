# 📜 RB002 Week 8 — English Worksheet

**Topic:** Ship It — Publish & Present · **Course:** Story Quest · **Time:** about 45 minutes

This week you **ship** your quest. Publish it to Roblox (File → Publish to Roblox), give it a clear name, description, and icon, set it to **Public** in Game Settings → Permissions, and present it like a real game developer.

---

## 1 · Predict 🔮

This week you read **your own scripts**. Open your Story Quest game in Roblox Studio, find each kind of line, and answer.

```lua
print("Elder: Welcome, " .. player.Name .. "!")
```

**Find a line in YOUR NPC script that uses `player.Name`. If your friend Mina plays your published game, what exactly will the NPC say to her?**

<div class="write-space"></div>

```lua
local questDone = false
```

**Find YOUR quest-state variable. What is its value when the game starts? Which line changes it, and at what moment in the quest?**

<div class="write-space"></div>

```lua
giveReward(player, 100)
```

**Find YOUR reward call. What are the two arguments? What would change for the player if you wrote `500` instead?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

These are **launch-checklist** problems. Each game below is about to ship, but something is broken. Read what is **supposed** to happen, write the fix, then explain why the original was wrong and why your fix works.

**Bug A** — Your friend should be able to join your game. Instead Roblox tells her she cannot play it.

```
Game Settings → Permissions → Private ✔
```

**Write the fix (what do you change, and where?):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Players should be able to **finish** the quest. The world only has 5 crystals, but the NPC script asks for more.

```lua
elseif crystals.Value >= 10 then
	questDone = true
	giveReward(player, 100)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When the quest finishes, the player should **see** that it is done. Right now the coins go up silently and players feel lost.

```lua
elseif crystals.Value >= 5 then
	questDone = true
	giveReward(player, 100)
end
```

**Hint:** add an ending message — a `print` or a label line like `"Quest complete!"`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now publish your game: File → Publish to Roblox, then in Game Settings add a name, a description, and an icon, and set Permissions to **Public**. Play it once from the Roblox app or website — not Studio. When you finish, come back here.

Send a photo or video of your game page on Roblox, then write your **presentation plan**. Use these sentence starters — write 4 to 6 sentences total.

> My game is called … and the quest story is …
>
> The hardest bug I had was …
>
> I fixed it by …
>
> My favorite script is … because …
>
> I set my game to Public so that …
>
> In my next update, I will …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) and **present your game** like a real developer. Talk through it like you are showing it at a game show. Try to use these words: **publish**, **public**, **description**, **quest**, **update**.

> 1. Show your game page on Roblox — say the name and read your description out loud.
> 2. Play your quest from start to finish: talk to the NPCs, collect the items, get the reward.
> 3. Tell the story of your quest in your own words.
> 4. Open your favorite script in Studio and read it out loud. Say why you like it.
> 5. Say one idea for your next update.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
