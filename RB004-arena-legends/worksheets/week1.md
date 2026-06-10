# ⚔️ RB004 Week 1 — English Worksheet

**Topic:** Server vs Client — Who Owns the World? · **Course:** Arena Legends · **Time:** about 45 minutes

This week you learn the most important rule of multiplayer games: the **server** owns the world. Game scripts go in **ServerScriptService**, and each player's own computer is called a **client**. You test multiplayer with the **Test tab → 2 Players**.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Studio, write what you think will happen.

```lua
-- Script in ServerScriptService
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined the arena!")
end)
```

**You press Test → 2 Players. Player1 joins, then Player2 joins. What does the server print? How many lines?**

<div class="write-space"></div>

```lua
-- Script in ServerScriptService
local gate = workspace.ArenaGate
gate.BrickColor = BrickColor.new("Bright red")
```

**The server changes the gate's color. You test with 2 Players. Does Player1 see a red gate? Does Player2? Why?**

<div class="write-space"></div>

```lua
-- LocalScript in StarterPlayerScripts
local player = game:GetService("Players").LocalPlayer

print("Hello, " .. player.Name .. "!")
```

**A LocalScript runs on each player's own computer. With 2 Players, what does Player1's screen print? What does Player2's screen print?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The server is supposed to print a welcome message **every time** a player joins the arena.

```lua
-- Script in ServerScriptService
local Players = game:GetService("Players")

print(Players.LocalPlayer.Name .. " joined the arena!")
```

**Hint:** the server is not a player — it has no `LocalPlayer`. The server needs to **listen** for players joining.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This welcome script should see **every** player who joins. But it was put in the wrong place.

```lua
-- LocalScript in StarterPlayerScripts
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined the arena!")
end)
```

**Hint:** the code is fine — the **place** is wrong. A server script in the wrong place never sees everyone.

**Write the fixed code (including where it goes):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The server should print the player's name plus the words " joined the arena!" as one message.

```lua
-- Script in ServerScriptService
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name + " joined the arena!")
end)
```

**Hint:** in Luau, `+` is only for numbers. Strings join with a different symbol.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your own arena game in Roblox Studio. Add a server script in **ServerScriptService** that prints a welcome message when a player joins, then test it with **Test tab → 2 Players**. When you finish, come back here.

Send a photo or video of the Output window showing both players' messages, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I put my script in **ServerScriptService** because …
>
> When I tested with 2 Players, I saw …
>
> The server is different from a client because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you test your game with 2 Players. Talk through it like you are teaching someone who has never seen Roblox Studio. Try to use these words: **server**, **client**, **ServerScriptService**, **PlayerAdded**, **join**.

> 1. Show your script inside ServerScriptService, then press Test → 2 Players.
> 2. Point at the Output window and read what the server printed.
> 3. Say which things the **server** owns and which things belong to **one player only**.
> 4. Say in your own words why game scripts go on the server.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
