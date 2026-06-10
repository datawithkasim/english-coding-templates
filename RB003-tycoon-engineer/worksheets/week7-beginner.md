# 🏭 RB003 Week 7 — English Worksheet (Beginner)

**Topic:** Build Week — Your Full Tycoon · **Course:** Tycoon Engineer · **Level:** Beginner · **Time:** about 30 minutes

No new code this week. You connect everything you know: dropper → conveyor → collector → buy button.

---

## 1 · Predict 🔮

Read the script. Before you imagine it running in Studio, circle or write your answer.

```lua
collector.Touched:Connect(function(hit)
    if hit.Name == "Gold" then
        cash.Value += 20
        hit:Destroy()
    end
end)
```

**A part named "Gold" touches the collector. Does cash go up? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
collector.Touched:Connect(function(hit)
    if hit.Name == "Gold" then
        cash.Value += 20
        hit:Destroy()
    end
end)
```

**Now a part named "Rock" touches the collector. Does cash go up? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The dropper and the collector should use **the same name**. Capital letters count.

```lua
-- clean
ore.Name = "Ore"

if hit.Name == "Ore" then
    cash.Value += 5
end
```

```lua
-- buggy
ore.Name = "ore"

if hit.Name == "Ore" then
    cash.Value += 5
end
```

**What is wrong? Why does cash never go up in the buggy version?**

<div class="write-space short"></div>

**Pair B** — The pad's sign says **"Gold Dropper — 100"**. Buying should unlock the GoldDropper.

```lua
-- clean
local model = ServerStorage.GoldDropper:Clone()
model.Parent = workspace
```

```lua
-- buggy
local model = ServerStorage.OreDropper:Clone()
model.Parent = workspace
```

**What is wrong? What do players get for their 100 cash in the buggy version?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The collector should pay the player the right amount from the catalog. One word is missing. Fill it in using the word bank.

```lua
local catalog = {
    {name = "Ore", payout = 5},
    {name = "Gold", payout = 20},
}

for _, item in ipairs(catalog) do
    if hit.Name == item.name then
        cash.Value += item.____
    end
end
```

**Word bank:** `payout` · `name` · `price`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your tycoon in Roblox Studio. Connect your dropper, conveyor, collector, and one buy button. When you finish, come back here.

Send a photo or video of your tycoon running, then explain what you built. Use these sentence starters — write 2 or 3 sentences.

> My money loop works like this: …
>
> My first upgrade costs …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you play your tycoon from the start. Talk like you are teaching a friend. Try to use these words: **money loop**, **price**, **upgrade**.

> 1. Collect drops and show the cash going up.
> 2. Buy one upgrade and show what it unlocks.
> 3. Say which part of your tycoon is your favorite.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
