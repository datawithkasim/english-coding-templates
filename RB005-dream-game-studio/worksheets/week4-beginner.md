# 🎮 RB005 Week 4 — English Worksheet (Beginner)

**Topic:** Game Feel — Juice with Tweens and Sound · **Course:** Dream Game Studio · **Level:** Beginner · **Time:** about 30 minutes

**Juice** is the little touches that make a game feel alive: smooth movement and sound. This week you add a **tween** and a **sound** to your game.

---

## 1 · Predict 🔮

Read the code. Before you run it in Studio, circle or write your answer.

```lua
local TweenService = game:GetService("TweenService")
local door = workspace.Door

local info = TweenInfo.new(0.5)
local tween = TweenService:Create(door, info, {Position = door.Position + Vector3.new(0, 6, 0)})
tween:Play()
```

**Does the door move? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local TweenService = game:GetService("TweenService")
local door = workspace.Door

local info = TweenInfo.new(0.5)
local tween = TweenService:Create(door, info, {Position = door.Position + Vector3.new(0, 6, 0)})
```

**This script never calls `tween:Play()`. Does the door move? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The door should slide up smoothly.

```lua
-- clean
local tween = TweenService:Create(door, info, {Position = door.Position + Vector3.new(0, 6, 0)})
tween:Play()
```

```lua
-- buggy
local tween = TweenService:Create(door, info, {Position = door.Position + Vector3.new(0, 6, 0)})
```

**What is missing? What does the buggy door do?**

<div class="write-space short"></div>

**Pair B** — The fade should take **half a second**.

```lua
-- clean
local info = TweenInfo.new(0.5)
```

```lua
-- buggy
local info = TweenInfo.new(500)
```

**What is wrong? How long does the buggy fade take?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The tween is created but it still needs to start. One word is missing. Fill it in using the word bank.

```lua
local tween = TweenService:Create(door, info, {Transparency = 1})
tween:____()
```

**Word bank:** `Play` · `Go` · `Start`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your game and add **one tween** and **one sound** to a moment that matters (winning, picking up, opening a door). When it works, come back here.

Send a photo or video of the juicy moment, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I added a tween to …
>
> My sound plays when …
>
> Before the juice, that moment felt … Now it feels …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your game runs. Talk like you are teaching a friend. Try to use these words: **tween**, **sound**, **juice**.

> 1. Trigger your juicy moment and show the tween.
> 2. Read your `TweenInfo` time out loud.
> 3. Say in your own words what **juice** adds to a game.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
