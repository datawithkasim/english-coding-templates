# ⚔️ RB004 Week 3 — English Worksheet

**Topic:** Round Timer — Countdown to Battle · **Course:** Arena Legends · **Time:** about 45 minutes

This week your arena gets a **round timer**. The server counts down with a `for` loop and stores the number in an IntValue called **TimeLeft**. A StringValue called **RoundStatus** says `"Intermission"` or `"Battle!"`, and a GUI TextLabel listens with `.Changed` so every player can watch the clock.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Studio, write what you think will happen.

```lua
-- Script in ServerScriptService
local timeLeft = game.ReplicatedStorage.TimeLeft -- IntValue

for t = 30, 0, -1 do
	timeLeft.Value = t
	task.wait(1)
end

print("Round over!")
```

**What is timeLeft.Value right after the loop starts? What is it at the end? About how many seconds does the loop take?**

<div class="write-space"></div>

```lua
-- LocalScript inside the TextLabel
local timeLeft = game.ReplicatedStorage.TimeLeft
local label = script.Parent

timeLeft.Changed:Connect(function(newTime)
	label.Text = "Time: " .. newTime
end)
```

**The server changes timeLeft.Value from 30 down to 0. What does the label show while the timer runs? When does the function run?**

<div class="write-space"></div>

```lua
-- Script in ServerScriptService
local roundStatus = game.ReplicatedStorage.RoundStatus -- StringValue

roundStatus.Value = "Intermission"
task.wait(10)
roundStatus.Value = "Battle!"
```

**What is roundStatus.Value during the first 10 seconds? What is it after? When would players see "Battle!" on screen?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The timer should count **down** from 30 to 0. Instead, the loop never runs at all and "Round over!" prints right away.

```lua
-- Script in ServerScriptService
local timeLeft = game.ReplicatedStorage.TimeLeft

for t = 30, 0 do
	timeLeft.Value = t
	task.wait(1)
end

print("Round over!")
```

**Hint:** without a step, a `for` loop counts **up** by 1 — and it cannot count up from 30 to 0.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The timer should tick once per second. Instead, it jumps from 30 to 0 instantly, then waits.

```lua
-- Script in ServerScriptService
local timeLeft = game.ReplicatedStorage.TimeLeft

for t = 30, 0, -1 do
	timeLeft.Value = t
end
task.wait(1)

print("Round over!")
```

**Hint:** the wait must happen **inside** the loop, once per tick.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The label should update every time the timer changes. Instead, it shows "Time: 30" forever.

```lua
-- LocalScript inside the TextLabel
local timeLeft = game.ReplicatedStorage.TimeLeft
local label = script.Parent

label.Text = "Time: " .. timeLeft.Value
```

**Hint:** setting the text **once** is a photo, not a video. The label needs to **listen** for changes.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your own arena game. Build a round timer: an IntValue **TimeLeft** in ReplicatedStorage, a server countdown loop, and a TextLabel that updates with `.Changed`. When you finish, come back here.

Send a photo or video of the timer counting down on screen, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My `for` loop counts down because …
>
> I put `task.wait(1)` inside the loop so that …
>
> The label updates when …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your timer counts down. Talk through it like you are teaching someone who has never seen it. Try to use these words: **countdown**, **loop**, **IntValue**, **Changed**, **update**.

> 1. Show your server script and read the `for` line out loud — say what 30, 0, and -1 mean.
> 2. Run the game and show the label ticking down once per second.
> 3. Point at the `.Changed` connection and say when it runs.
> 4. Say in your own words why the timer lives on the **server**, not on one player's screen.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
