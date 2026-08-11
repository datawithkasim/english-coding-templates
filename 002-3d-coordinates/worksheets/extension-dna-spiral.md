<style>
.steps { border-left: 4px solid #6b4ee6; background: #f7f5ff; border-radius: 0 8px 8px 0; padding: 10px 14px; margin: 12px 0; }
.steps .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #6b4ee6; text-transform: uppercase; }
.steps ol { margin: 6px 0 0; padding-left: 20px; }
.steps li { margin: 3px 0; font-size: 14.5px; }
.stuck { border: 2px dashed #ffc75c; background: #fffdf3; border-radius: 8px; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.stuck .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #c07a00; text-transform: uppercase; display: block; margin-bottom: 3px; }
.check { border-left: 4px solid #2e9e5b; background: #f2fbf5; border-radius: 0 8px 8px 0; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.check .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #2e9e5b; text-transform: uppercase; display: block; margin-bottom: 3px; }
.where { border-left: 4px solid #1f7f9c; background: #f1fafd; border-radius: 0 8px 8px 0; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.where .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #1f7f9c; text-transform: uppercase; display: block; margin-bottom: 3px; }
.warn { border-left: 4px solid #d94f4f; background: #fdf3f3; border-radius: 0 8px 8px 0; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.warn .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #b93131; text-transform: uppercase; display: block; margin-bottom: 3px; }
.mini-q { font-size: 14px; font-weight: 700; margin: 10px 0 2px; }
.timing { font-family: "Inter", sans-serif; font-size: 12px; color: #8a8aa0; letter-spacing: .04em; text-transform: uppercase; font-weight: 700; }
.tpl { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #6b4ee6; text-transform: uppercase; margin: 12px 0 -6px; }
table.tr { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 14px; }
table.tr th, table.tr td { border: 1px solid #ddd; padding: 5px 9px; text-align: center; }
table.tr th { background: #f7f5ff; color: #6b4ee6; font-size: 12px; text-transform: uppercase; letter-spacing: .05em; }

/* nothing gets cut in half by a page break */
.steps, .stuck, .check, .where, .warn, .mini-q, .tpl,
table, tr, blockquote, pre, ul, ol,
.write-space, .answer-lines, .qa { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3, h4, .mini-q, .timing, .tpl { page-break-after: avoid; break-after: avoid; }
p { orphans: 3; widows: 3; }
</style>

# 🧬 DNA Spiral — English Worksheet

**Topic:** Lists and `%` make a spiral · **Course:** 3D Coordinates · **Level:** Extension · **Time:** about 40 minutes

<span class="timing">Type `del` before every `run`. This build is 30 tall.</span>

Every `???` is one short thing for you to work out. There are no answers on this sheet.

---

## 1 · Eight spots 📍

Two lists hold eight places around a circle.

```python
XS = [ 6, 4, 0, -4, -6, -4,  0,  4]
ZS = [ 0, 4, 6,  4,  0, -4, -6, -4]
```

**Spot 0 is `XS[0]`, `ZS[0]`. Write it.**

<div class="write-space short"></div>

**Write spot 2 and spot 5.**

<div class="write-space short"></div>

**The centre is (8, 8). Spot 0 lands at x = 8 + 6 = 14. Where does spot 4 land?**

<div class="write-space short"></div>

<div class="check"><span class="lab">Got it right if</span> spot 0 and spot 4 are on opposite sides of the centre.</div>

---

## 2 · The `%` sign 🔁

`%` gives the **remainder** after dividing.

**Fill this in.**

<table class="tr">
<tr><th>i</th><th>0</th><th>1</th><th>7</th><th>8</th><th>9</th><th>15</th><th>16</th></tr>
<tr><th>i % 8</th><td>0</td><td>1</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

**What is the biggest number `i % 8` can ever be?**

<div class="write-space short"></div>

<div class="mini-q">Why this matters.</div>

**Your lists only have 8 spots. `i` counts to 23. Explain what `%` is doing for you.**

<div class="write-space"></div>

---

## 3 · The other strand ↔️

```python
k = i % 8
j = (k + 4) % 8
```

**Fill this in.**

<table class="tr">
<tr><th>k</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
<tr><th>j</th><td>4</td><td>5</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

**Why is there a second `% 8` on the `j` line? What goes wrong without it?**

<div class="write-space"></div>

<div class="check"><span class="lab">Got it right if</span> every j is between 0 and 7.</div>

---

## 4 · Build it 🧬

<div class="tpl">Template</div>

```python
XS = [6, 4, 0, -4, -6, -4, 0, 4]
ZS = [0, 4, 6, 4, 0, -4, -6, -4]

def on_chat():
    for i in range(0, 24):
        k = i % 8
        j = (??? + ???) % ???
        ax = 8 + XS[k]
        az = 8 + ZS[k]
        bx = 8 + XS[???]
        bz = 8 + ZS[???]
        blocks.fill(GOLD_BLOCK,
            pos(ax, ???, az), pos(ax + 1, ???, az + 1), REPLACE)
        blocks.fill(EMERALD_BLOCK,
            pos(bx, ???, bz), pos(bx + 1, ???, bz + 1), REPLACE)
player.on_chat("dna", on_chat)
```

<div class="mini-q">The `y` blanks are all the same thing.</div>

**Which variable makes it climb?**

<div class="write-space short"></div>

<div class="check"><span class="lab">Works when</span> two coloured strands wind around each other, and they are never on the same side.</div>

<div class="stuck"><span class="lab">It is a straight tower?</span>
Your `y` is a fixed number instead of a variable. It must change every turn.</div>

<div class="stuck"><span class="lab">Both strands in the same place?</span>
Check the `j` line. `(k + 4)` not `(k + 8)`.</div>

---

## 5 · Add the bars 🪜

Real DNA has rungs joining the two strands.

<div class="tpl">Template · inside the loop</div>

```python
        if i % ??? == 0:
            blocks.fill(QUARTZ_BLOCK,
                pos(ax, i, az), pos(bx, i, bz), REPLACE)
```

**24 steps. You want 6 bars. What number goes in the blank?**

<div class="write-space short"></div>

<div class="check"><span class="lab">Works when</span> you can count your bars and get the number you planned.</div>

---

## 6 · Show Your Work 📸🎥

Record **one video**, one take, no stopping. A phone is fine. Show these in order:

> 1. Type `del`, then `dna`. Walk all the way round it.
> 2. Show your two lists and say what one spot means.
> 3. Show the `k` line and explain `%` in your own words.
> 4. Show the `j` line and say why it is always the opposite side.
> 5. Show your bars and say how you chose the number.

Try to use these words: **list**, **remainder**, **opposite**, **loop**, **climb**.

**Plan what you will say before you record.**

<div class="write-space tall" style="min-height: 240px"></div>

### Submit ✅

Send this worksheet and your video to teacher on KakaoTalk.
