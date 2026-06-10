# 📜 RB002 Week 2 — English Worksheet

**Topic:** Strings — Talking Code · **Course:** Story Quest · **Time:** about 45 minutes

This week your code starts **talking**. You join strings together with `..` to build messages, and you greet every player by name when they join your world.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local name = "Mina"
print("Welcome, " .. name .. "!")
```

**What exactly prints in the Output window? Where does the name go?**

<div class="write-space"></div>

```lua
local first = "Story"
local second = "Quest"
print(first .. second)
```

**Is there a space between the two words? What exactly prints?**

<div class="write-space"></div>

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print("Welcome, " .. player.Name .. "!")
end)
```

**When does this print — right away, or when something happens? If a player named Jiho joins, what prints?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The script should print `Hello, Mina!`. Right now Studio shows a red error and nothing prints.

```lua
local name = "Mina"
print("Hello, " name "!")
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The script should print `Welcome to the Dark Forest`. Right now two words stick together: `Welcome tothe Dark Forest`.

```lua
local placeName = "the Dark Forest"
print("Welcome to" .. placeName)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The script should greet every player by name when they join. Right now Studio shows an error instead.

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print("Welcome, " + player.Name + "!")
end)
```

**Hint:** in Luau, `+` is only for numbers.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your own quest world. Add a script that greets every player by name when they join, and at least one more message built with `..`. When you finish, come back here.

Send a photo or video of your messages in the Output window, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My world says … when a player joins.
>
> I used `..` to join …
>
> `player.Name` gives me …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you test your world. Talk through it like you are teaching someone who has never seen it. Try to use these words: **string**, **join**, **variable**, **player**, **message**.

> 1. Show your script, then press Play and show the welcome message in the Output window.
> 2. Read your `print` line out loud and point at each `..`.
> 3. Say what `player.Name` is and where your name appears in the message.
> 4. Say in your own words what `..` does to two strings.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
