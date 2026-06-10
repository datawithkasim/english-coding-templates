# 🎮 RB005 Week 5 — English Worksheet

**Topic:** Menus & UI — Title Screens and Buttons · **Course:** Dream Game Studio · **Time:** about 45 minutes

This week your game gets a **title screen**. A `ScreenGui` holds a `Frame`, and the `Frame` holds a `TextButton` that says Play. When the player clicks the button, `MouseButton1Click` fires and your menu disappears.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Studio, write what you think will happen.

```lua
local button = script.Parent
local menuGui = button.Parent.Parent -- the ScreenGui

button.MouseButton1Click:Connect(function()
	menuGui.Enabled = false
end)
```

**The player clicks the Play button. What happens to the menu? What happens if the player only moves the mouse over the button without clicking?**

<div class="write-space"></div>

```lua
local label = script.Parent -- a TextLabel inside the menu Frame

label.Text = "Collect 10 coins to open the door!"
label.TextScaled = true
```

**A new player opens your game and reads the menu. What do they learn before they even press Play?**

<div class="write-space"></div>

```lua
local button = script.Parent
local menuGui = button.Parent.Parent

button.MouseButton1Click:Connect(function()
	button.Text = "Loading..."
	task.wait(1)
	menuGui.Enabled = false
end)
```

**The player clicks Play. Write what they see, in order, from the click until the game starts.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — When the player **clicks** the Play button, the menu should close. Right now nothing ever happens.

```lua
local button = script.Parent
local menuGui = button.Parent.Parent

button.Touched:Connect(function()
	menuGui.Enabled = false
end)
```

**Hint:** `Touched` is for parts in the world. Buttons have their own click event.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This code is correct, but it lives in a normal **Script** inside `ServerScriptService`. The menu never closes for the player.

```lua
local button = script.Parent
local menuGui = button.Parent.Parent

button.MouseButton1Click:Connect(function()
	menuGui.Enabled = false
end)
```

**Hint:** GUI code runs on the player's screen, so it must be a **LocalScript** placed inside the GUI (inside the button works well). Think about *where* this script should live, not just what it says.

**Write the fix (what kind of script, and where you put it):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Clicking Play should close the **whole menu**. Right now the Frame disappears, but the title TextLabel (which sits in the ScreenGui, next to the Frame) stays stuck on the screen.

```lua
local button = script.Parent
local frame = button.Parent -- the Frame
local menuGui = frame.Parent -- the ScreenGui

button.MouseButton1Click:Connect(function()
	frame.Visible = false
end)
```

**Hint:** hiding one Frame is not the same as turning off the whole ScreenGui.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now open your own game in Studio. Build a title screen: a `ScreenGui` with a `Frame`, a title, a `TextLabel` with short instructions, and a Play `TextButton` that closes the menu. When you finish, come back here.

Send a photo or video of your title screen, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My title screen shows …
>
> When the player clicks Play, …
>
> I used a **LocalScript** because …
>
> My instructions label tells the player …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you test your menu in Studio. Talk through it like you are teaching someone who has never seen it. Try to use these words: **ScreenGui**, **Frame**, **TextButton**, **MouseButton1Click**, **Enabled**.

> 1. Show your title screen before you click anything. Read your instructions label out loud.
> 2. Click Play and show the menu disappearing.
> 3. Open your LocalScript and read the `MouseButton1Click` line out loud. Say what it does.
> 4. Say in your own words why the menu code is a **LocalScript** and not a normal Script.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
