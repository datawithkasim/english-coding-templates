# ⚔️ RB004 Week 7 — English Worksheet (Beginner)

**Topic:** Build Week — Your Full Arena Game · **Course:** Arena Legends · **Level:** Beginner · **Time:** about 30 minutes

No new syntax this week. You connect everything you know — teams, timer, power-ups, points — into **one full round loop**, and you design **your own** arena game.

---

## 1 · Predict 🔮

Read this part of a round loop. Before you imagine running it in Roblox Studio, circle or write your answer.

```lua
status.Value = "Intermission..."
task.wait(10)

status.Value = "FIGHT!"
points.Red = 0
points.Blue = 0
```

**Do both teams start the round with 0 points? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
if points.Red > points.Blue then
	status.Value = "Red team wins!"
end
```

**Red has 2 points and Blue has 5 points. Does "Red team wins!" appear? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — Every round should start fresh at 0–0.

```lua
-- clean
status.Value = "FIGHT!"
points.Red = 0
points.Blue = 0
```

```lua
-- buggy
status.Value = "FIGHT!"
```

**What is wrong? What happens in round 2?**

<div class="write-space short"></div>

**Pair B** — The countdown should take one second per number.

```lua
-- clean
for i = 60, 0, -1 do
	timeLeft.Value = i
	task.wait(1)
end
```

```lua
-- buggy
for i = 60, 0, -1 do
	timeLeft.Value = i
end
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The round should start with a 10-second intermission. One word is missing. Fill it in using the word bank.

```lua
status.Value = "Intermission..."
task.____(10)
status.Value = "FIGHT!"
```

**Word bank:** `wait` · `delay` · `spawn`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open Roblox Studio and build your full arena game: round loop, teams, timer, points. **You are the designer.** When you finish, come back here.

Send a photo or video of one full round, then explain your design. Use these sentence starters — write 2 or 3 sentences.

> My game mode is …
>
> A team scores a point when …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you playtest one full round. In Roblox Studio, use **Test → 2 Players** so both teams have a player. Talk like you are teaching a friend. Try to use these words: **intermission**, **countdown**, **winner**.

> 1. Start the 2-player test and show the intermission message.
> 2. Score a point and show the score changing.
> 3. Let the timer reach 0 and show the winner message.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
