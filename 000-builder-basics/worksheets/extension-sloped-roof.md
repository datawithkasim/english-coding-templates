# 🏠 Builder Basics — The Sloped Roof (Extension)

**Topic:** Variables · **Course:** Builder Basics · **Type:** Extension Activity · **Time:** about 45 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable building shapes and you are ready to think about how one number can do a lot of work.

---

## 1 · Predict 🔮

In the **Sloped Roof** world, typing `slope` in the chat runs a program that builds a stepped roof. It does not build the roof block by block. Instead it stacks four square **rings** of stairs, one on top of the next. The bottom ring is the widest. Each ring above it is a little smaller, so the roof climbs inward and upward until it reaches a point at the top — like a small pyramid made of steps.

The size of each ring is held in a variable called `roof_len`. This is the length of one side of the ring. It **starts at 7**, and every time a new ring is built it **loses 2**. So the side gets shorter each layer until the roof reaches its peak.

**Write the four values of `roof_len`, from the bottom ring to the top ring.**

<div class="write-space"></div>

**Each ring has four sides. To estimate the stairs in a ring, think of about four times the side length. Add up the four sides — 7, then 5, then 3, then 1 — and write the rough total number of stairs in the whole roof. Show your adding.**

<div class="write-space"></div>

**What is the LAST value of `roof_len`, the one at the very top? What kind of shape does a ring that small make?**

<div class="write-space"></div>

Now meet a second variable. Imagine there is a variable called `step` that decides **how much the ring shrinks** each layer. Right now `step` is 2, so the side drops 7, 5, 3, 1.

**If `step` were 1 instead of 2, would the roof be steeper (rises fast) or gentler (rises slowly)? Would it need MORE rings or FEWER rings to reach the peak? Explain why in a sentence or two.**

<div class="write-space tall"></div>

---

## 2 · Trace Two Things 🔢

Each layer changes two things at once. The ring **side** gets smaller, and the **height** goes up by 1 (each ring sits one block higher than the last). Fill in the table. Start `roof_len` at 7 and a height of 1, take 2 off the side each row, and add 1 to the height each row.

| Layer | `roof_len` (ring side) | Height |
|:-----:|:----------------------:|:------:|
| 1     | 7                      | 1      |
| 2     |                        |        |
| 3     |                        |        |
| 4     |                        |        |

**Which change makes the ring smaller each layer?**

<div class="write-space"></div>

**Which change makes the roof taller each layer?**

<div class="write-space"></div>

**Which ring becomes the peak — the top point of the roof — and why is it the peak?**

<div class="write-space"></div>

---

## 3 · Reason About Bugs 🧠

No code to rewrite here — just read what goes wrong and explain it in writing.

**Bug A — The shrink happens too early.** Imagine the program takes 2 off `roof_len` **before** it builds the ring, instead of after. So the first ring is built using the already-shrunk number, not 7.

**What goes wrong with the roof? (Think about the bottom ring.) How would you fix the order of the steps?**

<div class="write-space tall"></div>

**Bug B — The variable never changes.** Imagine `roof_len` stays at 7 for every layer and never loses its 2.

**What shape would you get instead of a roof? Why does the roof need the variable to update each time?**

<div class="write-space tall"></div>

---

## 4 · Design Your Own Roof 🏗️

Plan a roof of your own — in numbers and words, not in a code box.

**Pick a starting `roof_len` (the widest ring) and a `step` (how much it shrinks each layer):**

<div class="write-space short"></div>

**List the ring sizes your numbers produce, layer by layer, until you reach the peak. Just write the numbers, in order.**

<div class="write-space"></div>

**How many rings does it take to reach the peak?**

<div class="write-space short"></div>

**Now the big idea. The whole roof is built from one variable plus one shrink rule, instead of four rings written out by hand. In writing, explain WHY that is better. To help you think: if you wanted a much bigger roof, what is the smallest thing you would change?**

<div class="write-space tall"></div>

---

## 5 · Build It 📸

Open the **Sloped Roof** world and type `slope` in the chat to run the program and watch the roof build. Then build your **own** version by changing the numbers — try a different starting `roof_len` or a different `step` and see how the roof changes shape.

Send a photo or video of your roof, then explain what you did. Use these starters — write 4 to 6 sentences total.

> First, I ran `slope` and saw …
>
> The **variable** I changed was …
>
> I gave it a new **value** of …
>
> Each layer the program **updates** the side by …
>
> My **slope** turned out steeper / gentler because …
>
> The **peak** was reached after … rings.

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and teach someone how the sloped roof works. You are narrating and explaining — not presenting to a class. Try to use these words: **variable**, **value**, **update**, **slope**, **peak**, **ring**.

> 1. Point to the bottom **ring** and the **peak**, and say which is wider.
> 2. Explain the **variable** `roof_len` and its starting **value**.
> 3. Show how the program **updates** that value — taking 2 off each layer.
> 4. Explain how the shrinking makes the **slope**, and why the rings stop at the **peak**.
> 5. Say one thing you would change to make a bigger or steeper roof.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
