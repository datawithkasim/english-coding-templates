# ⚔️ RB004 Week 3 — English Worksheet (Beginner)

**Topic:** Round Timer — Countdown to Battle · **Course:** Arena Legends · **Level:** Beginner · **Time:** about 30 minutes

This week your arena gets a **round timer**. The server counts down with a `for` loop, and a TextLabel listens with `.Changed` so every player can watch the clock.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

```lua
local timeLeft = game.ReplicatedStorage.TimeLeft -- IntValue

for t = 30, 0, -1 do
	timeLeft.Value = t
	task.wait(1)
end
```

**Does the timer go down by 1 every second? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
timeLeft.Changed:Connect(function(newTime)
	label.Text = "Time: " .. newTime
end)
```

**The server changes timeLeft.Value to 29. Does the label now show "Time: 29"? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The timer should count **down** from 30 to 0. It needs the `-1` step.

```lua
-- clean
for t = 30, 0, -1 do
	timeLeft.Value = t
	task.wait(1)
end
```

```lua
-- buggy
for t = 30, 0 do
	timeLeft.Value = t
	task.wait(1)
end
```

**What is wrong? Why does the buggy loop never run?**

<div class="write-space short"></div>

**Pair B** — The wait must be **inside** the loop so the timer ticks once per second.

```lua
-- clean
for t = 30, 0, -1 do
	timeLeft.Value = t
	task.wait(1)
end
```

```lua
-- buggy
for t = 30, 0, -1 do
	timeLeft.Value = t
end
task.wait(1)
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The timer should count **down** from 30 to 0, one number at a time. One thing is missing. Fill it in using the word bank.

```lua
for t = 30, 0, ____ do
	timeLeft.Value = t
	task.wait(1)
end
```

**Word bank:** `-1` · `1` · `0`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your own arena game. Build a countdown timer with a `for` loop and show it on a TextLabel. When you finish, come back here.

Send a photo or video of the timer counting down on screen, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My `for` loop counts down because …
>
> The label updates when …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your timer counts down. Talk like you are teaching a friend. Try to use these words: **countdown**, **loop**, **update**.

> 1. Show your script and read the `for` line out loud.
> 2. Run the game and show the label ticking down.
> 3. Say in your own words what `-1` does in the loop.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
