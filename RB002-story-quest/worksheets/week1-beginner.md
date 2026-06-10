# 📜 RB002 Week 1 — English Worksheet (Beginner)

**Topic:** Build Your World — Terrain & Anchored Models · **Course:** Story Quest · **Level:** Beginner · **Time:** about 30 minutes

This week you build the land for your quest world with the **Terrain Editor** and review **Anchored**. The code below is review from RB001.

---

## 1 · Predict 🔮

Read the script. Before you imagine running it, circle or write your answer.

```lua
print("Hello, hero!")
print("Goodbye, hero!")
```

**Does `Hello, hero!` print first? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
local rock = script.Parent
rock.Anchored = true
```

**The rock is floating in the sky. Does it fall down when the game starts? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The sign should turn green.

```lua
-- clean
local sign = script.Parent
sign.Color = Color3.fromRGB(0, 255, 0)
```

```lua
-- buggy
local sign = script.Parent
Sign.Color = Color3.fromRGB(0, 255, 0)
```

**What is wrong? Look at the small letters and big letters.**

<div class="write-space short"></div>

**Pair B** — The rock should stay in the sky.

```lua
-- clean
local rock = script.Parent
rock.Anchored = true
```

```lua
-- buggy
local rock = script.Parent
rock.Anchored = false
```

**What is wrong? What does the buggy rock do?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The rock should stay still in the sky. One word is missing. Fill it in using the word bank.

```lua
local rock = script.Parent
rock.________ = true
```

**Word bank:** `Anchored` · `Color` · `Transparency`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your own quest world in Roblox Studio. Build your terrain and a spawn area. When you finish, come back here.

Send a photo or video of your quest world, then explain what you built. Use these sentence starters — write 2 or 3 sentences.

> My quest world is a …
>
> I anchored … so that …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you walk through your quest world. Talk like you are giving a tour to a friend. Try to use these words: **terrain**, **anchored**, **spawn**.

> 1. Show your whole world, then walk through the spawn area.
> 2. Point at one anchored part and say why it does not fall.
> 3. Say which part of your world you like the most.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
