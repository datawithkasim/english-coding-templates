# 📜 RB002 Week 7 — English Worksheet (Beginner)

**Topic:** Build Week — Your Full Quest · **Course:** Story Quest · **Level:** Beginner · **Time:** about 30 minutes

No new syntax this week. You connect everything you know into **one full quest** that a player can start and finish.

---

## 1 · Predict 🔮

Read the NPC script. Before you imagine it running in Roblox Studio, circle or write your answer.

```lua
if questDone then
	print("Elder: Thank you again!")
elseif crystals.Value >= 5 then
	print("Elder: Here is your reward!")
else
	print("Elder: Please find 5 crystals.")
end
```

**The player has 0 crystals and `questDone` is `false`. Does the Elder say "Please find 5 crystals."? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
if questDone then
	print("Elder: Thank you again!")
elseif crystals.Value >= 5 then
	print("Elder: Here is your reward!")
end
```

**Now `questDone` is `true`. Does the Elder say "Thank you again!"? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows a clean script first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The reward should happen **once**, so the script must remember the quest is done.

```lua
-- clean
elseif crystals.Value >= 5 then
	questDone = true
	giveReward(player, 100)
end
```

```lua
-- buggy
elseif crystals.Value >= 5 then
	giveReward(player, 100)
end
```

**What is wrong? What happens every time the player talks to the Elder?**

<div class="write-space short"></div>

**Pair B** — The world only has 5 crystals, so the quest must finish at 5.

```lua
-- clean
elseif crystals.Value >= 5 then
	questDone = true
end
```

```lua
-- buggy
elseif crystals.Value >= 50 then
	questDone = true
end
```

**What is wrong? Can the player ever finish the buggy quest?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

When the player brings 5 crystals, the script should remember the quest is done. One word is missing. Fill it in using the word bank.

```lua
elseif crystals.Value >= 5 then
	questDone = ____
	giveReward(player, 100)
end
```

**Word bank:** `true` · `false` · `nil`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your Story Quest game in Roblox Studio and build your **full quest**: 2 or 3 NPCs, items to collect, and a reward. When you finish, come back here.

Send a photo or video of your quest world, then explain your plan. Use these sentence starters — write 2 or 3 sentences.

> My quest story is …
>
> The player must collect …
>
> The reward is …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you play your quest from start to finish. Talk like you are teaching a friend. Try to use these words: **quest**, **reward**, **elseif**.

> 1. Press Play, talk to your NPC, and read the line out loud.
> 2. Collect the items and show the reward moment.
> 3. Talk to the NPC again and show that the line changed.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
