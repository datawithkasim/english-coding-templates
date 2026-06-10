# 🏭 RB003 Week 6 — English Worksheet

**Topic:** Saving with DataStores — Keep Cash After Leaving · **Course:** Tycoon Engineer · **Time:** about 45 minutes

This week your tycoon remembers. A **DataStore** saves each player's cash when they leave and loads it when they join again. `pcall` means **"try safely — if saving fails, the game keeps running."** To test saving in Studio, turn on **Game Settings → Security → Enable Studio Access to API Services**.

---

## 1 · Predict 🔮

Read each script. Before you imagine it running in Studio, write what you think will happen.

```lua
local DataStoreService = game:GetService("DataStoreService")
local store = DataStoreService:GetDataStore("CashStore")
local Players = game:GetService("Players")

Players.PlayerRemoving:Connect(function(player)
    local cash = player.leaderstats.Cash
    pcall(function()
        store:SetAsync(player.UserId, cash.Value)
    end)
end)
```

**When does the save happen — every second, or when a player leaves? What number gets saved?**

<div class="write-space"></div>

```lua
local saved = store:GetAsync(player.UserId)

if saved ~= nil then
    cash.Value = saved
else
    cash.Value = 0
end
```

**A brand-new player joins for the first time. What does `GetAsync` return for them? What does their cash become?**

<div class="write-space"></div>

```lua
local ok = pcall(function()
    store:SetAsync(player.UserId, cash.Value)
end)

if ok then
    print("Saved!")
else
    print("Save failed — but the game keeps running.")
end
```

**The internet has a problem and `SetAsync` fails. Does the script crash? What prints?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each script below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The save should still work even if the player **changes their username** next month. The key must be something that never changes.

```lua
Players.PlayerRemoving:Connect(function(player)
    local cash = player.leaderstats.Cash
    pcall(function()
        store:SetAsync(player.Name, cash.Value)
    end)
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Loading should work for **everyone** — old players get their saved cash, and brand-new players start at 0. Right now the script breaks for new players, because they have no save yet.

```lua
local saved = store:GetAsync(player.UserId)
cash.Value = saved
```

**Hint:** check for `nil` before using `saved`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Saving should be **safe**. If the network fails for one player, the script should keep running for everyone else. Right now one failed save makes the whole script error.

```lua
Players.PlayerRemoving:Connect(function(player)
    local cash = player.leaderstats.Cash
    store:SetAsync(player.UserId, cash.Value)
end)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your tycoon in Roblox Studio. Add saving with a DataStore: save cash when a player leaves, load it when they join. When you finish, come back here.

Send a photo or video of your cash coming back after you rejoin, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My game saves cash when …
>
> I used **pcall** because …
>
> I tested saving by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you test saving. Talk through it like you are teaching someone who has never seen it. Try to use these words: **DataStore**, **save**, **load**, **pcall**, **UserId**.

> 1. Earn some cash, then stop the test (this is "leaving").
> 2. Play again and show your cash is still there.
> 3. Read your `SetAsync` line out loud and say when it runs.
> 4. Say in your own words what **pcall** does.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
