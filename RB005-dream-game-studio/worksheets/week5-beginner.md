# 🎮 RB005 Week 5 — English Worksheet (Beginner)

**Topic:** Menus & UI — Title Screens and Buttons · **Course:** Dream Game Studio · **Level:** Beginner · **Time:** about 30 minutes

This week your game gets a **title screen**. A `TextButton` says Play. When the player **clicks** it, `MouseButton1Click` fires and the menu disappears.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Studio, circle or write your answer.

```lua
local button = script.Parent
local menuGui = button.Parent.Parent

button.MouseButton1Click:Connect(function()
	menuGui.Enabled = false
end)
```

**The player clicks the Play button. Does the menu disappear? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local button = script.Parent
local menuGui = button.Parent.Parent

button.MouseButton1Click:Connect(function()
	menuGui.Enabled = false
end)
```

**Now the player only looks at the button and does NOT click. Does the menu disappear? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The menu should close when the player **clicks** the button.

```lua
-- clean
button.MouseButton1Click:Connect(function()
	menuGui.Enabled = false
end)
```

```lua
-- buggy
button.Touched:Connect(function()
	menuGui.Enabled = false
end)
```

**What is wrong? Why does the buggy button do nothing?**

<div class="write-space short"></div>

**Pair B** — Clicking Play should make the menu **disappear**.

```lua
-- clean
button.MouseButton1Click:Connect(function()
	menuGui.Enabled = false
end)
```

```lua
-- buggy
button.MouseButton1Click:Connect(function()
	menuGui.Enabled = true
end)
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The menu should close when the player clicks the button. One word is missing. Fill it in using the word bank.

```lua
button.____:Connect(function()
	menuGui.Enabled = false
end)
```

**Word bank:** `MouseButton1Click` · `Touched` · `Text`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your own game in Studio. Build a title screen with a Play `TextButton` that closes the menu. When you finish, come back here.

Send a photo or video of your title screen, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My title screen shows …
>
> When the player clicks Play, …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you test your menu in Studio. Talk like you are teaching a friend. Try to use these words: **button**, **click**, **menu**, **Enabled**.

> 1. Show your title screen, then click Play.
> 2. Read your `MouseButton1Click` line out loud.
> 3. Say in your own words what happens when the button is clicked.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
