# 📜 RB002 Week 1 — English Worksheet

**Topic:** Build Your World — Terrain & Anchored Models · **Course:** Story Quest · **Time:** about 45 minutes

This week you build the land for your quest world with the **Terrain Editor**, group parts into **models**, and review **Anchored**. The code below is review from RB001 — you already know all of it.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
print("Welcome to Story Quest!")
print("Chapter 1: The Village")
print("Your adventure begins.")
```

**Three print lines. What shows in the Output window, and in what order?**

<div class="write-space"></div>

```lua
local signText = "The Old Village"
print(signText)
signText = "The Dark Forest"
print(signText)
```

**The variable changes in the middle. What two lines print?**

<div class="write-space"></div>

```lua
local sign = script.Parent
sign.Color = Color3.fromRGB(0, 170, 255)
sign.Color = Color3.fromRGB(255, 200, 0)
print("Sign is ready!")
```

**The script sets the color two times. What color is the sign at the end? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The welcome sign should print a message, then turn green.

```lua
local sign = script.Parent
print("Welcome, hero!")
Sign.Color = Color3.fromRGB(0, 255, 0)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The gate countdown should print one number per second: 3 … 2 … 1 … then open. Right now all the numbers print at the same time.

```lua
print("3")
print("2")
print("1")
task.wait(3)
print("The gate is open!")
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The floating rock should stay in the sky above the spawn area. Right now it falls to the ground when the game starts.

```lua
local rock = script.Parent
rock.Anchored = false
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your own quest world in Roblox Studio. Build your terrain and a spawn area. Group your builds into models. When you finish, come back here.

Send a photo or video of your quest world, then explain what you built. Use these sentence starters — write 4 to 6 sentences total.

> My quest world is a …
>
> First, I made the terrain by …
>
> I grouped … into a model called …
>
> I anchored … so that …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk through your quest world. Talk through it like you are giving a tour. Try to use these words: **terrain**, **model**, **group**, **anchored**, **spawn**.

> 1. Show your whole world, then walk through the spawn area.
> 2. Point at one model and say what parts are grouped inside it.
> 3. Show one anchored part and say what would happen if it was not anchored.
> 4. Say which part of your world you are most proud of.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
