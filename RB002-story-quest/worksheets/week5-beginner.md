# 📜 RB002 Week 5 — English Worksheet (Beginner)

**Topic:** Quest Items — Pick Up Crystals · **Course:** Story Quest · **Level:** Beginner · **Time:** about 30 minutes

This week your player picks up **quest items**. A crystal counts up when a player touches it, then disappears with `Destroy()`.

---

## 1 · Predict 🔮

Read the script. Before you imagine it running in Roblox Studio, circle or write your answer.

```lua
crystal.Touched:Connect(function(hit)
	local player = Players:GetPlayerFromCharacter(hit.Parent)
	if player then
		crystals.Value += 1
		crystal:Destroy()
	end
end)
```

**A player touches the crystal. Does the counter go up? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
print("Crystals: " .. 3)
```

**Does this print `Crystals: 3`? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows a clean script first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The label should show the count, like `Crystals: 4`.

```lua
-- clean
label.Text = "Crystals: " .. crystals.Value
```

```lua
-- buggy
label.Text = "Crystals: " + crystals.Value
```

**What is wrong? Which symbol joins text in Luau?**

<div class="write-space short"></div>

**Pair B** — The crystal should **disappear** after the player picks it up.

```lua
-- clean
if player then
	crystals.Value += 1
	crystal:Destroy()
end
```

```lua
-- buggy
if player then
	crystals.Value += 1
end
```

**What is wrong? What happens to the crystal in the buggy version?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The label should show the count. One symbol is missing. Fill it in using the word bank.

```lua
label.Text = "Crystals: " ____ crystals.Value
```

**Word bank:** `..` · `+` · `==`

**Write the missing symbol:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now open your Story Quest game in Roblox Studio. Build 3 crystals that players can pick up, with a counter. When you finish, come back here.

Send a photo or video of your crystals, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My crystal script uses **Touched** when …
>
> The counter went up when …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you play your game in Studio. Talk like you are teaching a friend. Try to use these words: **Touched**, **counter**, **Destroy**.

> 1. Show your crystals, then press Play.
> 2. Pick up one crystal and show the counter going up.
> 3. Say in your own words what `Destroy()` does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
