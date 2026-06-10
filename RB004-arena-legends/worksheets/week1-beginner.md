# ⚔️ RB004 Week 1 — English Worksheet (Beginner)

**Topic:** Server vs Client — Who Owns the World? · **Course:** Arena Legends · **Level:** Beginner · **Time:** about 30 minutes

This week you learn the big rule of multiplayer games: the **server** owns the world. Game scripts go in **ServerScriptService**. You test with the **Test tab → 2 Players**.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

```lua
-- Script in ServerScriptService
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined the arena!")
end)
```

**You test with 2 Players. Both players join. Does the server print a message for both of them? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
-- LocalScript in StarterPlayerScripts
local player = game:GetService("Players").LocalPlayer

print("Hello, " .. player.Name .. "!")
```

**This runs on each player's own computer. Does Player1's screen say "Hello, Player2!"? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The welcome script should see **every** player who joins, so it must run on the server.

```lua
-- clean: Script in ServerScriptService
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined the arena!")
end)
```

```lua
-- buggy: LocalScript in StarterPlayerScripts
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined the arena!")
end)
```

**What is wrong? Why is the place important?**

<div class="write-space short"></div>

**Pair B** — In Luau, strings join with `..`, not `+`.

```lua
-- clean
print(player.Name .. " joined the arena!")
```

```lua
-- buggy
print(player.Name + " joined the arena!")
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The server should run the function **every time** a player joins. One word is missing. Fill it in using the word bank.

```lua
local Players = game:GetService("Players")

Players.____:Connect(function(player)
	print(player.Name .. " joined the arena!")
end)
```

**Word bank:** `PlayerAdded` · `PlayerRemoving` · `Changed`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your own arena game in Roblox Studio. Add a server script in **ServerScriptService** that prints a welcome message when a player joins. Test it with **Test tab → 2 Players**. When you finish, come back here.

Send a photo or video of the Output window showing the messages, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I put my script in **ServerScriptService** because …
>
> When I tested with 2 Players, I saw …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you test with 2 Players. Talk like you are teaching a friend. Try to use these words: **server**, **client**, **join**.

> 1. Show your script inside ServerScriptService, then press Test → 2 Players.
> 2. Point at the Output window and read what the server printed.
> 3. Say in your own words what the **server** does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
