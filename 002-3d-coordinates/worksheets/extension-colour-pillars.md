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

# 🌈 Colour Pillars — English Worksheet

**Topic:** Six variables and `+ 4` · **Course:** 3D Coordinates · **Level:** Extension · **Time:** about 40 minutes

<span class="timing">World: variables intro · Type `del` before every `run`. Every time.</span>

Every `???` is one short thing for you to work out. There are no answers on this sheet.

Count on the screen. Do not count in your head.

---

## 1 · Six variables. That is all 🎯

You get these six. No new ones.

```python
x_start = 2
y_start = 0
z_start = 2
x_end = 2
y_end = 3
z_end = 2
```

**One `fill` from `y_start` to `y_end`. How many blocks tall is that? Count 0, 1, 2, 3.**

<div class="write-space short"></div>

**Why is `y_end` 3 and not 4?**

<div class="write-space short"></div>

<div class="mini-q">A pillar is three of these stacked up. Each part is a different block.</div>

**Last week you made a new variable for every part. Why is that slow?**

<div class="write-space"></div>

---

## 2 · Plus 4, minus 4 ➕➖

You do not need new variables. You do maths inside `pos()`.

```python
pos(x_start, y_start + 4, z_start)
```

**Fill the table. Part 1 is done for you.**

<table class="tr">
<tr><th>part</th><th>block</th><th>first y</th><th>last y</th><th>maths you write</th></tr>
<tr><td>1</td><td>bottom</td><td>0</td><td>3</td><td>y_start &nbsp; y_end</td></tr>
<tr><td>2</td><td>middle</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>3</td><td>top</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

**Why do you add 4 and not 3?**

<div class="write-space short"></div>

<div class="mini-q">Now start from the top instead.</div>

**If the top part uses `y_start`, what maths gives you the middle part and the bottom part?**

<div class="write-space"></div>

---

## 3 · One pillar, three colours 🌈

Pick three blocks you like. Write the block name straight inside `fill`.

<div class="tpl">Template</div>

```python
blocks.fill(REDSTONE_BLOCK,
    pos(x_start, y_start, z_start),
    pos(x_end, y_end, z_end), REPLACE)
blocks.fill(GOLD_BLOCK,
    pos(x_start, y_start + ???, z_start),
    pos(x_end, y_end + ???, z_end), REPLACE)
blocks.fill(DIAMOND_BLOCK,
    pos(x_start, y_start + ???, z_start),
    pos(x_end, y_end + ???, z_end), REPLACE)
```

<div class="where"><span class="lab">Careful</span>
Both corners of one part move by the same amount. Move only the end and the part gets longer instead of moving up.</div>

**Run it. How tall is your whole pillar? Count it on the screen.**

<div class="write-space short"></div>

<div class="check"><span class="lab">Works when</span> you see three colours, four blocks each, standing in one straight pillar.</div>

<div class="stuck"><span class="lab">Two colours touching in a strange place?</span>
Your maths is <code>+ 3</code> or <code>+ 5</code>. Count one part again: 0, 1, 2, 3.</div>

---

## 4 · A row of pillars 🔁

Now build four pillars in a row. Only `z` changes.

<div class="tpl">Template</div>

```python
def on_chat():
    x_start = 2
    y_start = 0
    z_start = 2
    x_end = 2
    y_end = 3
    z_end = 2
    for i in range(???):
        blocks.fill(REDSTONE_BLOCK,
            pos(x_start, y_start, z_start),
            pos(x_end, y_end, z_end), REPLACE)
        blocks.fill(GOLD_BLOCK,
            pos(x_start, y_start + ???, z_start),
            pos(x_end, y_end + ???, z_end), REPLACE)
        blocks.fill(DIAMOND_BLOCK,
            pos(x_start, y_start + ???, z_start),
            pos(x_end, y_end + ???, z_end), REPLACE)
        z_start = z_start + ???
        z_end = z_end + ???
player.on_chat("pillars", on_chat)
```

<div class="where"><span class="lab">Careful</span>
The two <code>z</code> lines go <b>inside</b> the loop, after all three fills. Count the spaces at the front.</div>

**Before you run: how many pillars, and where does the last one stand?**

<div class="write-space short"></div>

<div class="stuck"><span class="lab">All four pillars in one spot?</span>
Your <code>z</code> lines are outside the loop, so they run once at the end.</div>

<div class="stuck"><span class="lab">Pillars stuck together?</span>
<code>z</code> is going up by less than 4. Leave a gap and look again.</div>

**Your last pillar ends at z = ??? and y = ???. Write the `del` box that clears them all.**

```python
blocks.fill(AIR,
    pos(0, 0, 0), pos(???, ???, ???), REPLACE)
```

<div class="write-space short"></div>

---

## 5 · Show Your Work 📸🎥

Record **one video**, one take, no stopping. A phone is fine. Show these in order:

> 1. Type `del`, then `pillars`. Walk past all four pillars.
> 2. Point at your six variables and read them out.
> 3. Show one `+ 4` and say which part of the pillar it moves.
> 4. Show that the `z` lines are inside the loop.
> 5. Read row 3 of your table out loud.

Try to use these words: **variable**, **loop**, **start**, **end**, **plus four**.

**Plan what you will say before you record.**

<div class="write-space tall" style="min-height: 240px"></div>

### Submit ✅

Send this worksheet and your video to teacher on KakaoTalk.
