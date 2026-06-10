# 📜 RB002 Week 3 — English Worksheet

**Topic:** Press E to Talk — ProximityPrompt · **Course:** Story Quest · **Time:** about 45 minutes

This week your NPCs come alive. A **ProximityPrompt** shows "Press E" when a player walks close, and the **Triggered** event runs your code when they press it.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local prompt = Instance.new("ProximityPrompt")
prompt.ActionText = "Talk"
prompt.ObjectText = "Old Wizard"
prompt.Parent = script.Parent
```

**You walk close to the part. What words show on your screen?**

<div class="write-space"></div>

```lua
local prompt = script.Parent.ProximityPrompt

prompt.Triggered:Connect(function(player)
	print("Hello, " .. player.Name)
end)
```

**When does the print happen — when you walk near, or when you press E?**

<div class="write-space"></div>

```lua
local prompt = script.Parent.ProximityPrompt
local talkCount = 0

prompt.Triggered:Connect(function(player)
	talkCount = talkCount + 1
	print("You talked " .. talkCount .. " times")
end)
```

**You press E three times. What does the Output window say after the last press?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The wizard should say hello when the player **presses E**. Right now Studio shows an error, because a ProximityPrompt has no `Touched` event.

```lua
local prompt = script.Parent.ProximityPrompt

prompt.Touched:Connect(function(player)
	print("Hello, " .. player.Name)
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The prompt should show on the wizard part. Right now no "Press E" ever appears in the game.

```lua
local prompt = Instance.new("ProximityPrompt")
prompt.ActionText = "Talk"
prompt.ObjectText = "Old Wizard"
```

**Hint:** the prompt was made, but it was never put anywhere.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The screen should show the name **Old Wizard** on top and the action **Talk** next to the E. Right now the two words are in the wrong places.

```lua
local prompt = script.Parent.ProximityPrompt
prompt.ActionText = "Old Wizard"
prompt.ObjectText = "Talk"
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your own quest world. Add an NPC with a ProximityPrompt. Give it an `ActionText` and an `ObjectText`, and make `Triggered` print a message. When you finish, come back here.

Send a photo or video of you talking to your NPC, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My NPC is a …
>
> When I walk close, the screen shows …
>
> When I press E, my code …
>
> I used `Triggered` because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you talk to your NPC. Talk through it like you are teaching someone who has never seen it. Try to use these words: **ProximityPrompt**, **Triggered**, **ActionText**, **NPC**, **press E**.

> 1. Walk close to your NPC and show the prompt on the screen.
> 2. Press E and show what happens in the Output window.
> 3. Show your script and read the `Triggered:Connect` line out loud.
> 4. Say in your own words the difference between **walking near** and **pressing E**.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
