# 🏃 RB001 Week 5 — English Worksheet (Beginner)

**Topic:** Loops — Platforms that Vanish · **Course:** Obby Architect · **Level:** Beginner · **Time:** about 30 minutes

This week your scripts **repeat** using loops. A `for` loop repeats a set number of times. A `while true do` loop repeats forever.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

```lua
local platform = script.Parent

for i = 1, 10 do
	platform.Transparency = i / 10
	task.wait(0.1)
end
```

**Transparency = 1 means invisible. After the loop ends, is the platform invisible? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local platform = script.Parent

while true do
	platform.Transparency = 1
	task.wait(2)
	platform.Transparency = 0
	task.wait(2)
end
```

**`while true do` never stops. Does the platform keep blinking forever? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows a clean script first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The platform should blink: invisible, wait, visible, wait, forever.

```lua
-- clean
while true do
	platform.Transparency = 1
	task.wait(2)
	platform.Transparency = 0
	task.wait(2)
end
```

```lua
-- buggy
while true do
	platform.Transparency = 1
	platform.Transparency = 0
end
```

**What is wrong? What happens to Studio with no `task.wait`?**

<div class="write-space short"></div>

**Pair B** — The loop should count up from 1 to 10 to fade the platform.

```lua
-- clean
for i = 1, 10 do
	platform.Transparency = i / 10
	task.wait(0.1)
end
```

```lua
-- buggy
for i = 10, 1 do
	platform.Transparency = i / 10
	task.wait(0.1)
end
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The platform should vanish, wait 2 seconds, then come back. One word is missing. Fill it in using the word bank.

```lua
while true do
	platform.Transparency = 1
	task.____(2)
	platform.Transparency = 0
	task.wait(2)
end
```

**Word bank:** `wait` · `stop` · `loop`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your obby in Roblox Studio. Build one **blinking platform** using a `while true do` loop. Cross it in Play mode. When you finish, come back here.

Send a photo or video of your platform blinking, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I used a **loop** to …
>
> The platform vanishes when …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you cross your blinking platform in Play mode. Talk like you are teaching a friend. Try to use these words: **loop**, **repeat**, **forever**, **wait**.

> 1. Show your platform, then press Play.
> 2. Read your `while true do` line out loud.
> 3. Say in your own words what a **loop** does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
