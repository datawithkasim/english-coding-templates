# 🏭 RB003 Week 7 — English Worksheet

**Topic:** Build Week — Your Full Tycoon · **Course:** Tycoon Engineer · **Time:** about 45 minutes

No new code this week. You connect everything you know: dropper → conveyor → collector → buy button → bigger dropper. You also design your **economy** — the prices and payouts that make your tycoon fun.

---

## 1 · Predict 🔮

All three scripts below come from **one tycoon**. Read each one. Before you imagine it running in Studio, write what you think will happen.

```lua
while true do
    task.wait(2)
    local ore = Instance.new("Part")
    ore.Name = "Ore"
    ore.Size = Vector3.new(1, 1, 1)
    ore.Position = dropper.Position - Vector3.new(0, 3, 0)
    ore.Parent = workspace
end
```

**How many ores drop in 10 seconds? What is each one named?**

<div class="write-space"></div>

```lua
local catalog = {
    {name = "Ore", payout = 5},
    {name = "Gold", payout = 20},
}

collector.Touched:Connect(function(hit)
    for _, item in ipairs(catalog) do
        if hit.Name == item.name then
            cash.Value += item.payout
            hit:Destroy()
        end
    end
end)
```

**A part named "Gold" touches the collector. How much cash does the player get? What happens to a part named "Rock"?**

<div class="write-space"></div>

```lua
local buying = false

pad.Touched:Connect(function(hit)
    if buying then return end
    buying = true

    if cash.Value >= 100 then
        cash.Value -= 100
        local model = ServerStorage.GoldDropper:Clone()
        model.Parent = workspace
    end

    task.wait(1)
    buying = false
end)
```

**Each Ore pays 5. How many ores must a player collect before they can buy this upgrade? After buying, how much cash is left?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The player just bought the GoldDropper. The collector should collect **Ore AND Gold**. Right now gold parts pile up on the conveyor and cash never goes up for them.

```lua
collector.Touched:Connect(function(hit)
    if hit.Name == "Ore" then
        cash.Value += 5
        hit:Destroy()
    end
end)
```

**Hint:** use the catalog with `ipairs`, like in Predict.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The pad's sign says **"Gold Dropper — 100"**. Buying should unlock the GoldDropper. Right now players pay 100 and get a second ore dropper instead.

```lua
if cash.Value >= 100 then
    cash.Value -= 100
    local model = ServerStorage.OreDropper:Clone()
    model.Parent = workspace
end
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The dropper and the collector should use **the same name**. Right now the collector never pays, because the names do not match.

```lua
-- dropper script
local ore = Instance.new("Part")
ore.Name = "ore"

-- collector script
if hit.Name == "Ore" then
    cash.Value += 5
    hit:Destroy()
end
```

**Hint:** names must match exactly — capital letters count.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your tycoon in Roblox Studio. First **design your economy**, then build the full chain: dropper, conveyor, collector, and buy buttons that unlock upgrades in order.

**Plan your upgrades before you build.** Fill in this table:

| Upgrade | Price | What it does |
| --- | --- | --- |
| 1. | | |
| 2. | | |
| 3. | | |

**Check your balance:** if your first drop pays 5 and your first upgrade costs 100, a player needs 20 drops. Do the same math for **your** numbers — how many drops until a player can buy your first upgrade? Is that fast enough to be fun?

<div class="write-space"></div>

When your tycoon works, send a photo or video of it running, then explain what you built. Use these sentence starters — write 4 to 6 sentences total.

> My money loop works like this: …
>
> My first upgrade costs … because …
>
> Players buy my upgrades in this order: …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you **playtest** your tycoon from the start. Talk through it like you are teaching someone who has never seen it. Try to use these words: **money loop**, **payout**, **price**, **upgrade**, **balance**.

> 1. Start with 0 cash. Collect drops and show the cash going up.
> 2. Buy your first upgrade and show what it unlocks.
> 3. Show that the new parts get collected too — nothing piles up.
> 4. Say one price or payout you changed to make the game more fun, and why.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
