# 🌳 M003 Week 5 — English Worksheet

**Topic:** Layer Up — Terrain & Trees · **Course:** 3D Coordinates · **Time:** about 45 minutes

You already know the floor — **(x, z)**, across and forward. This week you go **up**. One **`fill`** makes a solid box between **two corners**. Raise the **middle number (y)** and the box gets **taller**; stack wider and narrower boxes and flat ground turns into **trees, hills, and towers**.

**Your mission this week: build this tree.** A fat brown **trunk** going up, then a green **cap** of boxes that get **smaller** as they rise.

<div style="display:flex; gap:14px; align-items:flex-start; margin:10px 0; page-break-inside:avoid; break-inside:avoid"><div style="flex:0 0 auto"><p style="margin:0 0 4px; font-weight:700">🌳 Build this</p><img src="../assets/week5-tree.png" alt="A Minecraft tree: a fat brown trunk with a green cap made of three stacked boxes, each box narrower than the one below" style="width:100%; max-width:200px; border-radius:8px; display:block"></div><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🧱 The idea</p><p style="margin:0 0 6px">• A <b>3 × 3</b> brown <b>trunk</b>, stacked up the <b>y</b> axis.</p><p style="margin:0 0 6px">• A green <b>cap</b> of 3 boxes: <b>widest</b> at the bottom, each one above is <b>narrower and higher</b>.</p><p style="margin:0">• Every box is one <code>fill</code> between two corners.</p></div></div>

### 🧭 Read every coordinate the same way: **(x, y, z)**

<div style="display:flex; gap:8px; flex-wrap:wrap; margin:6px 0 2px"><div style="flex:1; min-width:120px; background:#fff3ea; border:1px solid #ffd9c2; border-radius:8px; padding:8px 12px"><b style="color:#e0681c">1st number = X</b><br>across → (left ↔ right)</div><div style="flex:1; min-width:120px; background:#f0ecff; border:1px solid #d9cdff; border-radius:8px; padding:8px 12px"><b style="color:#6b4ee6">2nd number = Y</b><br>up ↑ (height)</div><div style="flex:1; min-width:120px; background:#e8f7ef; border:1px solid #c4ead6; border-radius:8px; padding:8px 12px"><b style="color:#1a8f5a">3rd number = Z</b><br>forward ⤴ (depth)</div></div>

<pre style="margin:8px 0; font-size:14px">pos( <span style="color:#ffb27a; font-weight:700">x</span> , <span style="color:#c3b1ff; font-weight:700">y</span> , <span style="color:#7ee6a8; font-weight:700">z</span> )   →   ( <span style="color:#ffb27a; font-weight:700">across</span> , <span style="color:#c3b1ff; font-weight:700">up</span> , <span style="color:#7ee6a8; font-weight:700">forward</span> )</pre>

> 🌱 **Big idea:** the **2nd number (y)** is height. Raise it and the box grows **up**. Stretch the **1st (x)** and **3rd (z)** to make a box **wider**.

---

## 1 · Predict 🔮

Read each set of steps. Look at each **column** — remember **1st = x, 2nd = y, 3rd = z**. Then write what you think you will see.

```
fill BROWN from (3, 0, 3) to (5, 6, 5)
```

**X goes 3 → 5 and Z goes 3 → 5, so how wide is the trunk across and deep? Y goes 0 → 6, so how tall is it?**

<div class="write-space"></div>

```
fill GREEN from (1, 7, 1) to (7, 8, 7)
fill GREEN from (2, 9, 2) to (6, 11, 6)
```

**Both are green boxes. Look at the x and z columns — which box is wider? Look at the y column — which box sits higher?**

<div class="write-space"></div>

```
fill GREEN from (3, 12, 3) to (5, 14, 5)
```

**This is the smallest cap box. Its y starts at 12 — is it near the top of the tree or the bottom?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should stack a **second cap box on top** of the first. Right now both boxes use the **same y**, so the second lands on the **same level** and nothing stacks up.

```
fill GREEN from (1, 7, 1) to (7, 8, 7)
fill GREEN from (2, 7, 2) to (6, 8, 6)
```

**Hint:** the **2nd number (y)** is height. Both boxes stop at y = 8. Which number must go higher?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should build the **trunk going up** at x = 3–5, z = 3–5. Right now it makes a **flat slab** on the ground with no height.

```
fill BROWN from (3, 0, 3) to (5, 0, 5)
```

**Hint:** check the **2nd column (y)** in both corners.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This green box should be a **wide cap** that sticks out past the trunk. Right now it is the **same width** as the trunk, so there is no cap.

```
fill GREEN from (3, 7, 3) to (5, 8, 5)
```

**Hint:** the trunk's x and z go 3 → 5. To overhang, the cap's **1st (x)** and **3rd (z)** must be wider.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build the Tree 📸

Now switch to your homework world and **build the tree from the top of this sheet**. Here is the exact recipe. Notice the colours: <b style="color:#e0681c">x</b> · <b style="color:#6b4ee6">y</b> · <b style="color:#1a8f5a">z</b> in every corner.

<div style="display:flex; gap:14px; align-items:flex-start; margin:10px 0; page-break-inside:avoid; break-inside:avoid"><div style="flex:0 0 auto; max-width:200px"><p style="margin:0 0 4px; font-weight:700">🧱 Blocks</p><img src="../assets/week5-tree-blocks.png" alt="MakeCode blocks: on chat command run — fill with brown from ~3 ~0 ~3 to ~5 ~6 ~5 replace, then three fill with green: 1,7,1 to 7,8,7; 2,9,2 to 6,11,6; 3,12,3 to 5,14,5; each replace" style="width:100%; max-width:200px; border-radius:8px; display:block; border:1px solid #e2e2e2"></div><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🐍 Python</p><pre style="margin:0; white-space:pre; font-size:11.5px">def on_run():
    blocks.fill(BROWN_CONCRETE,
        pos(<span style="color:#ffb27a">3</span>, <span style="color:#c3b1ff">0</span>, <span style="color:#7ee6a8">3</span>), pos(<span style="color:#ffb27a">5</span>, <span style="color:#c3b1ff">6</span>, <span style="color:#7ee6a8">5</span>),
        FillOperation.REPLACE)
    blocks.fill(GREEN_CONCRETE,
        pos(<span style="color:#ffb27a">1</span>, <span style="color:#c3b1ff">7</span>, <span style="color:#7ee6a8">1</span>), pos(<span style="color:#ffb27a">7</span>, <span style="color:#c3b1ff">8</span>, <span style="color:#7ee6a8">7</span>),
        FillOperation.REPLACE)
    # ...two more cap boxes: y = 9–11, then y = 12–14
player.on_chat("run", on_run)</pre></div></div>

When you finish, send a **photo or video** of your tree, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I built the trunk by …
>
> My trunk is … tall and … wide because the **x**, **y**, **z** numbers were …
>
> The number that grew for each new cap box was **y**, which means …
>
> My cap gets narrower because each box's **x** and **z** …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 300px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you show your tree in the world. Talk through it like you are teaching someone who has only seen flat pictures before. Try to use these words: **layer**, **fill**, **x**, **y**, **z**, **trunk**, **cap**.

> 1. Show your tree from the bottom of the trunk up to the top of the cap.
> 2. Point at one cap box and read its corner out loud — say which number is **x**, which is **y**, which is **z**.
> 3. Show two boxes and say which one is **wider** and why that makes a cap.
> 4. Say in your own words what each of **x**, **y**, and **z** does.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 320px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
