# ⚔️ RB004 Week 4 — English Worksheet (Beginner)

**Topic:** RemoteEvents — Arena Announcements · **Course:** Arena Legends · **Level:** Beginner · **Time:** about 30 minutes

This week the server learns to talk to players. A **RemoteEvent** is like a megaphone: the server **shouts** with `FireAllClients`, and every player's screen **listens** with `OnClientEvent`.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

```lua
-- Script in ServerScriptService
local announceEvent = game.ReplicatedStorage.AnnounceEvent

announceEvent:FireAllClients("Round started!")
```

**You test with 2 Players. Do BOTH players receive the message "Round started!"? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
-- LocalScript inside the TextLabel
announceEvent.OnClientEvent:Connect(function(message)
	label.Text = message
end)
```

**The server fires "Round started!". Does the label now show "Round started!"? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The player's screen listens with `OnClientEvent`, not `OnServerEvent`.

```lua
-- clean: LocalScript inside the TextLabel
announceEvent.OnClientEvent:Connect(function(message)
	label.Text = message
end)
```

```lua
-- buggy: LocalScript inside the TextLabel
announceEvent.OnServerEvent:Connect(function(message)
	label.Text = message
end)
```

**What is wrong? Whose ear is `OnServerEvent`?**

<div class="write-space short"></div>

**Pair B** — To shout to **everyone**, the server uses `FireAllClients`.

```lua
-- clean
announceEvent:FireAllClients("Round started!")
```

```lua
-- buggy
announceEvent:FireClient("Round started!")
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The player's screen should **listen** for the server's message. One word is missing. Fill it in using the word bank.

```lua
announceEvent.____:Connect(function(message)
	label.Text = message
end)
```

**Word bank:** `OnClientEvent` · `OnServerEvent` · `Changed`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your own arena game. Add a RemoteEvent named **AnnounceEvent** in ReplicatedStorage, make the server shout "Round started!", and show it on a TextLabel. Test with **Test tab → 2 Players**. When you finish, come back here.

Send a photo or video of the announcement on both players' screens, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The server shouts with **FireAllClients** when …
>
> When I tested with 2 Players, I saw …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you test with 2 Players. Talk like you are teaching a friend. Try to use these words: **RemoteEvent**, **shout**, **listen**.

> 1. Show the RemoteEvent in ReplicatedStorage, then press Test → 2 Players.
> 2. Show the announcement appearing on both screens.
> 3. Say in your own words who shouts and who listens.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
