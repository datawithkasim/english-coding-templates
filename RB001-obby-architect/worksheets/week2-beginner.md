# 🏃 RB001 Week 2 — English Worksheet (Beginner)

**Topic:** Variables — the Ghost Platform · **Course:** Obby Architect · **Level:** Beginner · **Time:** about 30 minutes

This week you learned **variables** — names that hold a value. With `local platform = script.Parent` you give the part a name, then use that name to change it.

---

## 1 · Predict 🔮

Read the script. Before you run anything, circle or write your answer.

```lua
local platform = script.Parent
platform.Transparency = 0.5
```

**Can you see through the platform when the game runs? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local platform = script.Parent
platform.CanCollide = false
```

**A player jumps onto this platform. Do they stand on it? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The platform should turn half see-through. Read the variable name very carefully.

```lua
-- clean
local platform = script.Parent
platform.Transparency = 0.5
```

```lua
-- buggy
local platform = script.Parent
platfrom.Transparency = 0.5
```

**What is wrong?**

<div class="write-space short"></div>

**Pair B** — The platform should be **half** see-through, not invisible. Transparency goes from `0` to `1`.

```lua
-- clean
local platform = script.Parent
platform.Transparency = 0.5
```

```lua
-- buggy
local platform = script.Parent
platform.Transparency = 50
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The script should make a variable for the platform. One word is missing. Fill it in using the word bank.

```lua
____ platform = script.Parent
platform.Transparency = 0.5
```

**Word bank:** `local` · `print` · `Parent`

**Write the missing word:**

<div class="write-space short"></div>

The ghost platform should let players fall through. One word is missing.

```lua
local platform = script.Parent
platform.CanCollide = ____
```

**Word bank:** `false` · `true` · `local`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your own obby in Roblox Studio. Build a ghost platform trick section — some platforms are real, and some are ghosts that players fall through. When you finish, come back here.

Send a photo or video of your trick section, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I made a variable called …
>
> The ghost platform …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while a player tries your trick section. Talk like you are teaching a friend. Try to use these words: **variable**, **local**, **Transparency**, **CanCollide**.

> 1. Run the game and fall through a ghost platform.
> 2. Read your `local platform = script.Parent` line out loud.
> 3. Say in your own words what a **variable** is.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
