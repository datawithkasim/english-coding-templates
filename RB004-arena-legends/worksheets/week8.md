# ⚔️ RB004 Week 8 — English Worksheet

**Topic:** Ship It — Publish & Playtest Party · **Course:** Arena Legends · **Time:** about 45 minutes

This is launch week. You **publish** your arena, make it **Public**, and join the class **playtest party** — everyone plays everyone's arena. Light code this week: you read **your own** round loop and get your game ready for real players.

---

## 1 · Predict 🔮

These are pieces of a round loop like yours. For each one, **find the matching part in YOUR script** and answer about your own game.

```lua
status.Value = "Intermission..."
task.wait(10)
```

**Find your intermission. How many seconds is YOUR intermission? What do players see on screen while they wait?**

<div class="write-space"></div>

```lua
if points.Red >= Settings.WinScore then
	status.Value = "Red team wins!"
end
```

**Open YOUR Settings ModuleScript. What is your `WinScore`? How many points does Blue need to win in your game?**

<div class="write-space"></div>

```lua
for i = Settings.RoundLength, 0, -1 do
	timeLeft.Value = i
	task.wait(1)
end
```

**What is YOUR `RoundLength`? About how long is one full round of your game, intermission included?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

These are not script bugs — they are **launch checklist** bugs. Each setting below would ruin the playtest party. Read what it is **supposed** to be, write the fixed setting, and explain why it matters.

**Bug A** — At the playtest party, your whole class should be able to join your arena **at the same time**.

```
File → Game Settings → Options
Maximum Player Count: 1
```

**Write the fixed setting:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This SpawnLocation is supposed to be for the **Red team only**. Right now players from both teams appear on it.

```
SpawnLocation → Properties
Neutral: ✅ true
TeamColor: Bright red
```

**Write the fixed setting:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Your classmates click your game link… and Roblox says they can't join.

```
File → Game Settings → Permissions
Playability: Private
```

**Hint:** after changing this, you still need to publish again so the change goes online.

**Write the fixed setting:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now publish your arena: **File → Publish to Roblox**, then Game Settings → Permissions → **Public**. Join the class playtest party and play your classmates' arenas too. When you finish, come back here.

Send a photo or video of your published game page or classmates playing in your arena, then write your **presentation plan** for class. Use these sentence starters — write 4 to 6 sentences total.

> My game mode is …
>
> The hardest multiplayer bug I fixed was …
>
> My favorite script in my game is … because …
>
> One balance decision I made was … (speed, win score, round length, power-up spots)
>
> When my classmates played my arena, …
>
> If I made Arena Legends 2, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) — this one is your **launch trailer + presentation**. Talk through it like you are showing your game to a new player. Try to use these words: **publish**, **Public**, **server**, **round**, **balance**.

> 1. Show your game page on Roblox and say its name. Show that it is Public.
> 2. Join your game and play part of a round: spawn, score, power-up, winner message.
> 3. Tell us the hardest multiplayer bug you fixed and how you fixed it.
> 4. Show your favorite script and read one line of it out loud.
> 5. Explain one balance decision — why those numbers?

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
