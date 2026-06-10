# 🎮 RB005 Week 4 — English Worksheet

**Topic:** Game Feel — Juice with Tweens and Sound · **Course:** Dream Game Studio · **Time:** about 45 minutes

**Juice** is the little touches that make a game feel alive: smooth movement and sound. This week you add juice to your game with `TweenService` and `Sound`.

---

## 1 · Predict 🔮

Read each script. Before you run it in Studio, write what you think will happen.

```lua
local TweenService = game:GetService("TweenService")
local door = workspace.Door

local info = TweenInfo.new(0.5)
local tween = TweenService:Create(door, info, {Position = door.Position + Vector3.new(0, 6, 0)})
tween:Play()
```

**What does the door do? How far does it go, and how long does it take?**

<div class="write-space"></div>

```lua
local TweenService = game:GetService("TweenService")
local star = workspace.WinStar

local info = TweenInfo.new(2)
local tween = TweenService:Create(star, info, {Transparency = 1})
tween:Play()
```

**What does the player see happen to the star over 2 seconds?**

<div class="write-space"></div>

```lua
local pad = script.Parent
local sound = pad.PopSound

pad.Touched:Connect(function(hit)
	sound:Play()
end)
```

**`PopSound` is a Sound inside the pad with its SoundId already set. When does the sound play? A player stands on the pad and wiggles — does it play once or many times?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The door should slide up smoothly. The script runs with no errors — but the door never moves.

```lua
local TweenService = game:GetService("TweenService")
local door = workspace.Door

local info = TweenInfo.new(0.5)
local tween = TweenService:Create(door, info, {Position = door.Position + Vector3.new(0, 6, 0)})
```

**Hint:** the tween was created … but was it ever started?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The secret wall should fade away in **half a second**. Instead it fades so slowly nobody ever notices.

```lua
local TweenService = game:GetService("TweenService")
local wall = workspace.SecretWall

local info = TweenInfo.new(500)
local tween = TweenService:Create(wall, info, {Transparency = 1})
tween:Play()
```

**Hint:** `TweenInfo.new` takes **seconds**. How long is 500 seconds?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The script should make a sound and play it. It runs with no errors — but you hear nothing.

```lua
local sound = Instance.new("Sound")
sound.Parent = script.Parent
sound:Play()
sound.SoundId = "rbxassetid://9118823106"
```

**Hint:** look at the **order** of the lines. What was the SoundId when `Play()` ran?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your game and add juice: at least **one tween** and **one sound** on a moment that matters (winning, picking up, opening a door). When it feels good, come back here.

Send a photo or video of the juicy moment, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> I added a tween to …
>
> My TweenInfo time is … seconds because …
>
> My sound plays when …
>
> Before the juice, that moment felt … Now it feels …
>
> One tricky moment was when …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your game runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **TweenService**, **TweenInfo**, **tween**, **sound**, **juice**.

> 1. Show the moment BEFORE the juice triggers, then trigger it.
> 2. Open your script, show the tween, and read your `TweenInfo` time out loud.
> 3. Trigger your sound and say which event plays it.
> 4. Say in your own words what **juice** adds to a game.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
