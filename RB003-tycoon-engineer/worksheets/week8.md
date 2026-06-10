# 🏭 RB003 Week 8 — English Worksheet

**Topic:** Ship It — Publish & Present · **Course:** Tycoon Engineer · **Time:** about 45 minutes

This week you **publish** your tycoon so anyone can play it, check that saving works in the real published game, and present your work. Light code week — you read **your own** scripts.

---

## 1 · Predict 🔮

This week you read your **own** scripts. Open each one in Roblox Studio, find the line, then answer.

```lua
-- Open YOUR dropper script.
-- Find this line and write your number:
task.wait( ? )
```

**How often does your dropper drop? With your payout, how much cash can a player earn from one dropper in one minute?**

<div class="write-space"></div>

```lua
-- Open YOUR buy button script.
-- Find this line and write your number:
if cash.Value >= ? then
```

**What does your cheapest upgrade cost? How many drops does a player need before they can buy it?**

<div class="write-space"></div>

```lua
-- Open YOUR DataStore script.
-- Find these two lines:
store:SetAsync(player.UserId, cash.Value)
local saved = store:GetAsync(player.UserId)
```

**Which line saves and which line loads? What does your script do for a brand-new player who has no save yet?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

These are **launch bugs** — the code is fine, but a setting or a step is wrong. Read what is **supposed** to happen, write the fix, then explain why it went wrong.

**Bug A** — You test saving in Studio. The code is perfect, but you see a red DataStore error in the Output window.

```
Game Settings → Security
[ ] Enable Studio Access to API Services   ← OFF
```

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — You send the game link to a friend. They see **"This experience is unavailable."** They should be able to join and play.

```
Game Settings → Permissions
Playability: Private
```

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Your friend plays your game, but they see **yesterday's version** — no gold dropper, old prices. They should see today's version.

```
Yesterday:  File → Publish to Roblox   ✅
Today:      changed prices, added GoldDropper
Today:      closed Studio without publishing   ← !
```

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now publish your tycoon: give it a **name**, a **description**, and an **icon**, and set it to **Public**. Then play your published game and check the DataStore — earn cash, leave, rejoin. Is your cash still there?

Send a photo or video of your game's page and your cash after rejoining, then write your **presentation plan**. Use these sentence starters — write 4 to 6 sentences total.

> My game is called … and you can play it by …
>
> My money loop works like this: …
>
> The hardest bug I fixed was …
>
> My favorite script is … because …
>
> I chose my prices so that …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) — this is your **presentation**. Talk through your published game like you are showing it to a new player. Try to use these words: **publish**, **public**, **DataStore**, **money loop**, **upgrade**.

> 1. Show your game's page — its name, icon, and that it is Public.
> 2. Play your published game: earn cash and buy an upgrade.
> 3. Leave and rejoin — show your cash is still there.
> 4. Tell the hardest bug you fixed and your favorite script.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
