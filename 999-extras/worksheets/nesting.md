<style>
.dg { margin: 16px 0; font-family: "JetBrains Mono","Consolas",monospace; font-size: 14.5px; line-height: 1.5; }
.dg .ln { padding: 3px 10px; }
.dg .key { color: #6b4ee6; font-weight: 700; }
.dg .box { border: 2px dashed #ff7849; border-radius: 8px; background: #fff6ef; margin: 4px 0 8px 26px; padding: 26px 10px 10px; position: relative; }
.dg .box.purple { border-color: #6b4ee6; background: #f3f0ff; }
.dg .tag { position: absolute; top: -11px; left: 12px; background: #ff7849; color: #fff; font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 10px; }
.dg .box.purple .tag { background: #6b4ee6; }
.dg .note { font-family: "Inter", sans-serif; font-size: 12.5px; color: #888; }
.dg .always { color: #2e9e5b; font-weight: 700; }
.dg .danger { color: #d63b3b; font-weight: 700; }
</style>

# 🪆 Extra — Nesting: Code Inside Code

**Topic:** Nesting & Indenting · **Course:** Extra Worksheet · **Time:** about 30 minutes

---

## 1 · Code Lives in Boxes 📦

In block code, a loop has an arm. The arm holds the blocks inside.

Real code has no arm. So we **indent**. We push the inside lines to the right with spaces.

> Indenting shows what is **inside**.

The box is the inside:

<div class="dg">
  <div class="ln key">while true:</div>
  <div class="box"><span class="tag">INSIDE the loop</span>
    <div class="ln">place block</div>
  </div>
</div>

---

## 2 · Inside Means "Only If" 🛡️

The hero raises a shield only **if** a monster is near.

<div class="dg">
  <div class="ln key">if a monster is near:</div>
  <div class="box"><span class="tag">INSIDE the if — runs ONLY if a monster is near</span>
    <div class="ln">raise shield</div>
  </div>
  <div class="ln"><span class="always">say "phew, I am safe"</span> &nbsp;<span class="note">← OUTSIDE — runs EVERY time</span></div>
</div>

Inside the box → runs only when a monster is near.

Outside the box → always runs.

**No monster is near. Which line runs? Which is skipped?**

<div class="write-space"></div>

---

## 3 · Why It MUST Be Inside ⚠️

The indent tells the computer where the `if` stops.

Now we push the last line **inside** too:

<div class="dg">
  <div class="ln key">if a monster is near:</div>
  <div class="box"><span class="tag">Now EVERYTHING is inside the if</span>
    <div class="ln">raise shield</div>
    <div class="ln danger">say "phew, I am safe"</div>
  </div>
</div>

Now the hero feels safe only when a monster is near. Wrong! 🙈

> Inside the box → runs only if true.
> Outside the box → always runs.
> Move a line in or out → the code changes.

**Where should `say "phew, I am safe"` go? Why?**

<div class="write-space"></div>

---

## 4 · Predict 🔮

Read this code. The agent runs it over and over.

```
function go:
    while true:
        move forward
        if there is a flower:
            pick the flower
```

`move forward` is inside the `while`, so it happens every time.

`pick the flower` is inside the `if`, so it happens only sometimes.

**What does the agent do every time? When does it pick a flower?**

<div class="write-space"></div>

---

## 5 · Debug 🐛

This code should pick a flower **only** when there is one. But the agent picks all the time. The indent is wrong.

```
function go:
    while true:
        if there is a flower:
        pick the flower
```

`pick the flower` is not pushed in under the `if`. So it is **outside** the `if`, and runs every time.

**Write the code again with the right indent. Then say why your fix works.**

<div class="write-space tall" style="min-height: 200px"></div>

---

## 6 · Write 🖊️

Now you write one piece of code. Make the agent do this:

- a **function** called `patrol`
- inside it, a **while true**
- inside the while, an **if a monster is near**
- inside the if, **swing the sword**

Push each box in one more step than the box above it.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet to teacher on KakaoTalk.
