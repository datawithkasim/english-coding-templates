# 🏃 RB001 Week 2 — English Worksheet

**Topic:** Variables — the Ghost Platform · **Course:** Obby Architect · **Time:** about 45 minutes

This week you learned **variables** — names that hold a value. With `local platform = script.Parent` you give the part a name, then use that name to change it. You used this to build a ghost platform trick.

---

## 1 · Predict 🔮

Read each script. Before you run anything, write what you think will happen.

```lua
local platform = script.Parent
platform.Transparency = 0.5
```

**What does the platform look like when the game runs?**

<div class="write-space"></div>

```lua
local name = "Ghost Step"
local jumps = 3
print(name)
print(jumps)
```

**What does the Output window show? Write the lines in order.**

<div class="write-space"></div>

```lua
local platform = script.Parent
platform.Transparency = 0.5
platform.CanCollide = false
```

**A player jumps onto this platform. What do they see? What happens to them?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The script should make the platform half see-through. It runs, but there is a red error in the Output window. Read the variable name very carefully.

```lua
local platform = script.Parent
platfrom.Transparency = 0.5
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The platform should be **half** see-through, so players can still spot it. Instead it disappears completely.

```lua
local platform = script.Parent
platform.Transparency = 50
```

**Hint:** Transparency goes from `0` to `1`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The script should make a variable for the platform, then turn off its collision. One Luau word is missing at the start.

```lua
platform = script.Parent
platform.CanCollide = false
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your own obby in Roblox Studio. Build a ghost platform trick section — some platforms are real, and some are ghosts that players fall through. Use variables, `Transparency`, and `CanCollide`. When you finish, come back here.

Send a photo or video of your trick section, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I made a variable called …
>
> The ghost platform uses `Transparency` of … because …
>
> `CanCollide = false` means …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while a player tries your trick section. Talk through it like you are teaching someone who has never seen it. Try to use these words: **variable**, **local**, **Transparency**, **CanCollide**, **ghost**.

> 1. Show your trick section in Roblox Studio, then run the game.
> 2. Walk onto a real platform, then fall through a ghost one.
> 3. Open your script and read the `local platform = script.Parent` line out loud.
> 4. Say in your own words what a **variable** is.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
