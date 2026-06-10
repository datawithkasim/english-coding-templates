# 📜 RB002 Week 3 — English Worksheet (Beginner)

**Topic:** Press E to Talk — ProximityPrompt · **Course:** Story Quest · **Level:** Beginner · **Time:** about 30 minutes

This week your NPCs come alive. A **ProximityPrompt** shows "Press E" when a player walks close, and **Triggered** runs your code when they press it.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it, circle or write your answer.

```lua
local prompt = Instance.new("ProximityPrompt")
prompt.ActionText = "Talk"
prompt.Parent = script.Parent
```

**You walk close to the part. Do you see the word `Talk` on the screen? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local prompt = script.Parent.ProximityPrompt

prompt.Triggered:Connect(function(player)
	print("Hello!")
end)
```

**You stand near the NPC but do NOT press E. Does `Hello!` print? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The NPC should say hello when the player **presses E**.

```lua
-- clean
local prompt = script.Parent.ProximityPrompt

prompt.Triggered:Connect(function(player)
	print("Hello!")
end)
```

```lua
-- buggy
local prompt = script.Parent.ProximityPrompt

prompt.Touched:Connect(function(player)
	print("Hello!")
end)
```

**What is wrong? Which event works with a prompt?**

<div class="write-space short"></div>

**Pair B** — The prompt should show on the wizard part.

```lua
-- clean
local prompt = Instance.new("ProximityPrompt")
prompt.ActionText = "Talk"
prompt.Parent = script.Parent
```

```lua
-- buggy
local prompt = Instance.new("ProximityPrompt")
prompt.ActionText = "Talk"
```

**What is wrong? Which line is missing?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The code should run when the player presses E. One word is missing. Fill it in using the word bank.

```lua
prompt.________:Connect(function(player)
	print("Hello!")
end)
```

**Word bank:** `Triggered` · `Touched` · `Color`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your own quest world. Add an NPC with a ProximityPrompt that prints a message when you press E. When you finish, come back here.

Send a photo or video of you talking to your NPC, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My NPC is a …
>
> When I press E, my code …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you talk to your NPC. Talk like you are teaching a friend. Try to use these words: **ProximityPrompt**, **Triggered**, **press E**.

> 1. Walk close to your NPC and show the prompt on the screen.
> 2. Press E and show what happens in the Output window.
> 3. Say in your own words what **Triggered** means.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
