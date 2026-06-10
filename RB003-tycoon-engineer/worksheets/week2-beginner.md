# 🏭 RB003 Week 2 — English Worksheet (Beginner)

**Topic:** Conveyor & Collector — Touch, Pay, Destroy · **Course:** Tycoon Engineer · **Level:** Beginner · **Time:** about 30 minutes

This week ore rides a **conveyor** into a **collector pad**. The pad uses `Touched` to check the part's name, pay cash, and destroy the ore.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it in Roblox Studio, circle or write your answer.

```lua
collector.Touched:Connect(function(otherPart)
	if otherPart.Name == "Ore" then
		cash.Value += 5
	end
end)
```

**A part named `Ore` touches the pad. Does the cash go up? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
collector.Touched:Connect(function(otherPart)
	if otherPart.Name == "Ore" then
		cash.Value += 5
	end
end)
```

**Now a part named `Rock` touches the pad. Does the cash go up? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The ores are named `Ore` with a **capital O**. The pad should pay for them.

```lua
-- clean
if otherPart.Name == "Ore" then
	cash.Value += 5
	otherPart:Destroy()
end
```

```lua
-- buggy
if otherPart.Name == "ore" then
	cash.Value += 5
	otherPart:Destroy()
end
```

**What is wrong? Why does the buggy pad never pay?**

<div class="write-space short"></div>

**Pair B** — Each ore should pay **once** and then disappear.

```lua
-- clean
if otherPart.Name == "Ore" then
	cash.Value += 5
	otherPart:Destroy()
end
```

```lua
-- buggy
if otherPart.Name == "Ore" then
	cash.Value += 5
end
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The pad should add 5 cash when an ore touches it. One symbol is missing. Fill it in using the word bank.

```lua
if otherPart.Name == "Ore" then
	cash.Value ____ 5
	otherPart:Destroy()
end
```

**Word bank:** `+=` · `==` · `..`

**Write the missing symbol:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to Roblox Studio and open your tycoon. Build a conveyor that pushes ore into a collector pad that pays cash. When you finish, come back here.

Send a photo or video of an ore riding the conveyor and your cash going up, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> When an ore touches the pad, …
>
> My conveyor pushes the ore because …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your tycoon runs. Talk like you are teaching a friend. Try to use these words: **Touched**, **conveyor**, **Destroy**, **cash**.

> 1. Press Play and show an ore riding your conveyor.
> 2. Show your cash going up when the ore touches the pad.
> 3. Say in your own words what `otherPart:Destroy()` does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
