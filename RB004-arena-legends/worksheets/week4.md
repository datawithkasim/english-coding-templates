# ⚔️ RB004 Week 4 — English Worksheet

**Topic:** RemoteEvents — Arena Announcements · **Course:** Arena Legends · **Time:** about 45 minutes

This week the server learns to talk to players. A **RemoteEvent** in ReplicatedStorage is like a megaphone: the server **shouts** with `FireAllClients`, and every player's screen **listens** with `OnClientEvent` in a LocalScript.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Studio, write what you think will happen.

```lua
-- Script in ServerScriptService
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local announceEvent = ReplicatedStorage.AnnounceEvent

announceEvent:FireAllClients("Round started!")
```

**You test with 2 Players. The server fires the event. How many players receive the message "Round started!"?**

<div class="write-space"></div>

```lua
-- LocalScript inside the TextLabel
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local announceEvent = ReplicatedStorage.AnnounceEvent
local label = script.Parent

announceEvent.OnClientEvent:Connect(function(message)
	label.Text = message
end)
```

**The server fires `FireAllClients("Round started!")`. What does this label show? What does it show on the OTHER player's screen?**

<div class="write-space"></div>

```lua
-- Script in ServerScriptService
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")
local announceEvent = ReplicatedStorage.AnnounceEvent

local winner = Players.Player1
announceEvent:FireClient(winner, "You win!")
```

**`FireClient` sends to ONE player. You test with 2 Players. What does Player1's screen show? What does Player2's screen show?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — Every player's screen should show the server's announcement. But this listener never runs, because LocalScripts cannot run in ServerScriptService.

```lua
-- LocalScript in ServerScriptService
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local announceEvent = ReplicatedStorage.AnnounceEvent
local label = game.StarterGui.ArenaGui.AnnounceLabel

announceEvent.OnClientEvent:Connect(function(message)
	label.Text = message
end)
```

**Hint:** the listener belongs on the **player's side** — for example, a LocalScript inside the TextLabel in StarterGui.

**Write the fixed code (including where it goes):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The server should announce "Round started!" to **every** player. Instead, the script errors and nobody sees anything.

```lua
-- Script in ServerScriptService
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local announceEvent = ReplicatedStorage.AnnounceEvent

announceEvent:FireClient("Round started!")
```

**Hint:** `FireClient` needs a **player** first — but here we want to shout to everyone, so a different function fits better.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The player's screen should listen for the server's message. But the listener uses the wrong ear and never runs.

```lua
-- LocalScript inside the TextLabel
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local announceEvent = ReplicatedStorage.AnnounceEvent
local label = script.Parent

announceEvent.OnServerEvent:Connect(function(message)
	label.Text = message
end)
```

**Hint:** the **client** listens with `OnClientEvent`. `OnServerEvent` is for the server's ear, not the player's.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your own arena game. Add a RemoteEvent named **AnnounceEvent** in ReplicatedStorage, make the server fire "Round started!" when the round begins, and make a TextLabel show the message on every player's screen. Test with **Test tab → 2 Players**. When you finish, come back here.

Send a photo or video of the announcement appearing on both players' screens, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I put the RemoteEvent in **ReplicatedStorage** because …
>
> The server shouts with **FireAllClients** when …
>
> The player's screen listens with **OnClientEvent** and then …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you test your announcements with 2 Players. Talk through it like you are teaching someone who has never seen it. Try to use these words: **RemoteEvent**, **server**, **client**, **FireAllClients**, **OnClientEvent**.

> 1. Show the RemoteEvent in ReplicatedStorage and your two scripts — say which one is the server and which one is the client.
> 2. Press Test → 2 Players and show the announcement appearing on both screens.
> 3. Read the `FireAllClients` line and the `OnClientEvent` line out loud, and say which one shouts and which one listens.
> 4. Say in your own words why the server cannot change a player's screen directly.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
