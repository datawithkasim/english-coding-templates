# 📜 RB002 Week 4 — English Worksheet (Beginner)

**Topic:** Branching Dialogue — if / elseif / else · **Course:** Story Quest · **Level:** Beginner · **Time:** about 30 minutes

This week your NPC remembers the story. A **boolean** like `questAccepted` holds the quest state, and `if / else` picks **one** reply.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it, circle or write your answer.

```lua
local questAccepted = false

if questAccepted then
	print("Good luck, hero!")
else
	print("Will you help me?")
end
```

**Does it print `Good luck, hero!`? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local questAccepted = true

if questAccepted then
	print("Good luck, hero!")
else
	print("Will you help me?")
end
```

**Now the boolean is true. Does it print `Good luck, hero!`? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The NPC should say only **one** line each talk.

```lua
-- clean
if questAccepted then
	print("Good luck, hero!")
else
	print("Will you help me?")
end
```

```lua
-- buggy
if questAccepted then
	print("Good luck, hero!")
end
print("Will you help me?")
```

**What is wrong? When does the buggy question print?**

<div class="write-space short"></div>

**Pair B** — The second talk should be different from the first talk.

```lua
-- clean
if questAccepted then
	print("Did you find my cat yet?")
else
	print("Will you help me?")
	questAccepted = true
end
```

```lua
-- buggy
if questAccepted then
	print("Did you find my cat yet?")
else
	print("Will you help me?")
end
```

**What is wrong? Which line is missing?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The NPC should say one line when the quest is accepted, and a different line when it is not. One word is missing. Fill it in using the word bank.

```lua
if questAccepted then
	print("Good luck, hero!")
________
	print("Will you help me?")
end
```

**Word bank:** `else` · `end` · `print`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your own quest world. Give your NPC two replies with `if / else` so the reply changes after you accept the quest. When you finish, come back here.

Send a photo or video of the dialogue changing, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My NPC says … the first time I talk.
>
> After I accept the quest, my NPC says …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you talk to your NPC two times. Talk like you are teaching a friend. Try to use these words: **if**, **else**, **boolean**.

> 1. Press E the first time and show the NPC's first reply.
> 2. Press E again and show that the reply changed.
> 3. Say in your own words why only **one** line prints each time.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
