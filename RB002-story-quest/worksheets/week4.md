# 📜 RB002 Week 4 — English Worksheet

**Topic:** Branching Dialogue — if / elseif / else · **Course:** Story Quest · **Time:** about 45 minutes

This week your NPC remembers the story. A **boolean** like `questAccepted` holds the quest state, and `if / elseif / else` picks **one** reply that fits the moment.

---

## 1 · Predict 🔮

Read each script. Before you imagine running it in Roblox Studio, write what you think will happen.

```lua
local questAccepted = false

if questAccepted then
	print("Good luck, hero!")
else
	print("Will you help me find my cat?")
end
```

**`questAccepted` is false. Which line prints?**

<div class="write-space"></div>

```lua
local questDone = true
local questAccepted = true

if questDone then
	print("You found my cat! Thank you!")
elseif questAccepted then
	print("Did you find my cat yet?")
else
	print("Will you help me find my cat?")
end
```

**Both booleans are true. Which ONE line prints? Why only one?**

<div class="write-space"></div>

```lua
local questAccepted = false
local prompt = script.Parent.ProximityPrompt

prompt.Triggered:Connect(function(player)
	if questAccepted then
		print("Did you find my cat yet?")
	else
		print("Will you help me find my cat?")
		questAccepted = true
	end
end)
```

**You press E two times. What prints the first time? What prints the second time?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The NPC should say only **one** line each talk. Right now, on the first talk, BOTH lines print.

```lua
local questAccepted = false

if questAccepted == false then
	print("Will you help me find my cat?")
	questAccepted = true
end
if questAccepted == true then
	print("Did you find my cat yet?")
end
```

**Hint:** two separate `if` blocks both run. You only need one `if … else … end`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The first talk should ask for help. The second talk should say `Did you find my cat yet?`. Right now the NPC asks for help forever.

```lua
local questAccepted = false
local prompt = script.Parent.ProximityPrompt

prompt.Triggered:Connect(function(player)
	if questAccepted then
		print("Did you find my cat yet?")
	else
		print("Will you help me find my cat?")
	end
end)
```

**Hint:** the boolean never changes.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When the quest is done, the NPC should say thank you. Right now the thank-you line never prints, even when `questDone` is true.

```lua
local questDone = true
local questAccepted = true

if questAccepted then
	print("Did you find my cat yet?")
elseif questDone then
	print("You found my cat! Thank you!")
else
	print("Will you help me find my cat?")
end
```

**Hint:** the order of the checks matters. The first true check wins.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your own quest world. Give your NPC branching dialogue: a boolean quest state and `if / elseif / else` so the reply changes as the quest moves forward. When you finish, come back here.

Send a photo or video of the dialogue changing, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My NPC says … the first time I talk.
>
> After I accept the quest, my NPC says …
>
> My boolean is called … and it starts as …
>
> I used `elseif` because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you talk to your NPC more than once. Talk through it like you are teaching someone who has never seen it. Try to use these words: **if**, **elseif**, **else**, **boolean**, **quest**.

> 1. Press E the first time and show the NPC's first reply.
> 2. Press E again and show that the reply changed.
> 3. Show your script and read the `if / elseif / else` block out loud.
> 4. Say in your own words why only **one** line prints each time.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
