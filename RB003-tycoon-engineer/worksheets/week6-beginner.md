# 🏭 RB003 Week 6 — English Worksheet (Beginner)

**Topic:** Saving with DataStores — Keep Cash After Leaving · **Course:** Tycoon Engineer · **Level:** Beginner · **Time:** about 30 minutes

This week your tycoon remembers. A **DataStore** saves each player's cash when they leave and loads it when they join again. To test saving in Studio, turn on **Game Settings → Security → Enable Studio Access to API Services**.

---

## 1 · Predict 🔮

Read the script. Before you imagine it running in Studio, circle or write your answer.

```lua
Players.PlayerRemoving:Connect(function(player)
    pcall(function()
        store:SetAsync(player.UserId, cash.Value)
    end)
end)
```

**A player is still playing the game. Does this code save right now? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```lua
if saved ~= nil then
    cash.Value = saved
else
    cash.Value = 0
end
```

**A new player joins for the first time, so `saved` is `nil`. Does their cash become 0? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The save key must be something that **never changes**.

```lua
-- clean
store:SetAsync(player.UserId, cash.Value)
```

```lua
-- buggy
store:SetAsync(player.Name, cash.Value)
```

**What is wrong? What happens if the player changes their username?**

<div class="write-space short"></div>

**Pair B** — Saving should be **safe** — if saving fails, the game keeps running.

```lua
-- clean
pcall(function()
    store:SetAsync(player.UserId, cash.Value)
end)
```

```lua
-- buggy
store:SetAsync(player.UserId, cash.Value)
```

**What is wrong? What happens in the buggy version if saving fails?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

When a player joins, the game should **load** their saved cash. One word is missing. Fill it in using the word bank.

```lua
local saved = store:____(player.UserId)
```

**Word bank:** `GetAsync` · `SetAsync` · `Clone`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your tycoon in Roblox Studio. Add saving with a DataStore. When you finish, come back here.

Send a photo or video of your cash coming back after you rejoin, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My game saves cash when …
>
> When I joined again, …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you test saving. Talk like you are teaching a friend. Try to use these words: **save**, **load**, **DataStore**.

> 1. Earn some cash, then stop the test (this is "leaving").
> 2. Play again and show your cash is still there.
> 3. Say in your own words what a **DataStore** does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
