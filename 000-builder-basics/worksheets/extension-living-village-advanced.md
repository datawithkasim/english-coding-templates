# 🏰 Builder Basics — The Living Village (Extension · Advanced)

**Topic:** Bring It All Together · **Course:** Builder Basics · **Level:** Advanced · **Time:** about 90 minutes

> 🧩 Bonus challenge, after **Complete Your Village**. Here you use **loops**, **variables** for sizes, and **one function you call more than once**.

---

## 1 · The Build 🎯

Two houses already stand: the **farm house** 🟨 and a tall house 🟪. Add a **watchtower** on the tall house, then build the other six parts with code.

Every part must meet its spec:

| Part | Spec |
|------|------|
| 🗼 Watchtower | on the tall house, **≥ 4 blocks taller** than it |
| 🌾 Farm | **2 crop types**, planted in **rows by a loop** |
| 🧱 Fence | **fully encloses** the farm or the animals — no gaps |
| 💧 Pond | a dug dip filled with water — measure its width **W** |
| 🐟 Fish | **≥ 3 fish** in the pond |
| 🌉 Bridge | spans the pond: **length = W** |
| 🪣 Well | square rim, water inside |
| 🐄 Animals | **≥ 4**, inside the fence |

> ⚠️ **Rules:** loops for anything repeated · **variables** for sizes · **one function** you call for **2 or more** parts · only animals are spawned, everything else is code.

---

## 2 · Plan the Map 🗺️

This is your village from above. 🟨 = farm house, 🟪 = tall house. **x** goes across, **z** goes forward.

<div style="page-break-inside:avoid;margin:14px 0"><table style="border-collapse:collapse"><tr><th style="font-size:11px;color:#999;text-align:center;height:18px;width:44px"></th><th style="font-size:11px;color:#999;text-align:center;height:18px;width:44px">1</th><th style="font-size:11px;color:#999;text-align:center;height:18px;width:44px">2</th><th style="font-size:11px;color:#999;text-align:center;height:18px;width:44px">3</th><th style="font-size:11px;color:#999;text-align:center;height:18px;width:44px">4</th><th style="font-size:11px;color:#999;text-align:center;height:18px;width:44px">5</th><th style="font-size:11px;color:#999;text-align:center;height:18px;width:44px">6</th></tr><tr><th style="font-size:11px;color:#999;text-align:center;width:44px">6</th><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td></tr><tr><th style="font-size:11px;color:#999;text-align:center;width:44px">5</th><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc;text-align:center;font-size:22px">🟪</td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td></tr><tr><th style="font-size:11px;color:#999;text-align:center;width:44px">4</th><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td></tr><tr><th style="font-size:11px;color:#999;text-align:center;width:44px">3</th><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc;text-align:center;font-size:22px">🟨</td><td style="width:44px;height:44px;border:1px solid #ccc"></td></tr><tr><th style="font-size:11px;color:#999;text-align:center;width:44px">2</th><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td></tr><tr><th style="font-size:11px;color:#999;text-align:center;width:44px">1</th><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td><td style="width:44px;height:44px;border:1px solid #ccc"></td></tr></table></div>

**Draw the other six parts on the map. Write the (x, z) corner where each one starts.**

<div class="write-space"></div>

**Bridge length = pond width W. What is your W, and how did you measure it?**

<div class="write-space short"></div>

---

## 3 · Loops, Variables, Functions 🔁

**The one function you call twice or more — what does it build, and what does it take in?**

<div class="write-space short"></div>

**Which sizes are variables? Name two and why.**

<div class="write-space short"></div>

---

## 4 · Show Your Work 📸🎥

Build all eight parts to spec, then move the agent between them so nothing overlaps.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Fill the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
