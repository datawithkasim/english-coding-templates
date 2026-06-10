# 🏃 RB001 Week 5 — English Worksheet

**Topic:** Loops — Platforms that Vanish · **Course:** Obby Architect · **Time:** about 45 minutes

This week your scripts **repeat** using loops. A `for` loop repeats a set number of times. A `while true do` loop repeats forever. With loops, one platform can fade out, vanish, and come back — again and again.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Studio, write what you think will happen.

```lua
local platform = script.Parent

for i = 1, 10 do
	platform.Transparency = i / 10
	task.wait(0.1)
end
```

**The loop runs 10 times. What does the platform look like when the loop ends? About how many seconds does the fade take?**

<div class="write-space"></div>

```lua
local platform = script.Parent

while true do
	task.wait(3)
	platform.Transparency = 1
	platform.CanCollide = false
	task.wait(2)
	platform.Transparency = 0
	platform.CanCollide = true
end
```

**This loop never stops. What does the platform do, over and over? For how many seconds is it safe to stand on?**

<div class="write-space"></div>

```lua
local platform = script.Parent

while true do
	for i = 1, 10 do
		platform.Transparency = i / 10
		task.wait(0.1)
	end
	platform.CanCollide = false
	task.wait(2)
	platform.Transparency = 0
	platform.CanCollide = true
	task.wait(3)
end
```

**You are standing on this platform when the fade finishes. What happens to you? When is it safe to step on again?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the script is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The platform should blink: vanish, wait 2 seconds, come back, wait 2 seconds, forever. But when you press Play, Studio **freezes**.

```lua
local platform = script.Parent

while true do
	platform.Transparency = 1
	platform.CanCollide = false
	platform.Transparency = 0
	platform.CanCollide = true
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The platform is invisible. This loop should fade it **back in**, from invisible to solid. But nothing happens at all.

```lua
local platform = script.Parent

for i = 10, 1 do
	platform.Transparency = i / 10
	task.wait(0.1)
end
```

**Hint:** counting **down** needs one extra number in the `for` line.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The platform should fade out, vanish for 2 seconds, then come back good as new. But after the first cycle, players fall through a platform they **cannot even see** — and it never looks solid again.

```lua
local platform = script.Parent

while true do
	for i = 1, 10 do
		platform.Transparency = i / 10
		task.wait(0.1)
	end
	platform.CanCollide = false
	task.wait(2)
	platform.CanCollide = true
	task.wait(3)
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your obby in Roblox Studio. Build a **vanishing bridge**: at least 3 platforms that fade out and come back using a loop. Cross it yourself in Play mode. When you finish, come back here.

Send a photo or video of your bridge while it is fading, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> I used a **loop** to …
>
> The platform fades because `Transparency = i / 10` means …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you cross your vanishing bridge in Play mode. Talk through it like you are teaching someone who has never seen it. Try to use these words: **loop**, **repeat**, **forever**, **fade**, **wait**.

> 1. Show your bridge, then press Play.
> 2. Read your `while true do` loop out loud and say what repeats.
> 3. Point at `task.wait` and say what would happen without it.
> 4. Cross the bridge and say when it is safe and when it is not.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
