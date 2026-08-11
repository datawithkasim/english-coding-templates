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

# 🌳 Growing Trees — English Worksheet

**Topic:** Two counters in one loop · **Course:** 3D Coordinates · **Level:** Extension · **Time:** about 40 minutes

<span class="timing">Type `del` before every `run`. Every time.</span>

Every `???` is one short thing for you to work out. There are no answers on this sheet.

---

## 1 · One tree, two fills 🌲

A tree is a thin pole and a fat box.

```python
blocks.fill(OAK_LOG,
    pos(x, 0, z),
    pos(x, trunk_h, z), REPLACE)
```

**In the trunk fill, which of x, y, z is different between the two corners?**

<div class="write-space short"></div>

**So what shape do you get when only one of the three changes?**

<div class="write-space short"></div>

```python
blocks.fill(OAK_LEAVES,
    pos(x - leaf, trunk_h + 1, z - leaf),
    pos(x + leaf, trunk_h + 3, z + leaf), REPLACE)
```

**One corner uses minus. The other uses plus. Why?**

<div class="write-space"></div>

**If `leaf` is 2, how wide is the leaf box? Count the middle block too.**

<div class="write-space short"></div>

---

## 2 · Two counters ✏️

```python
    trunk_h = trunk_h + 2
    leaf = leaf + 1
    x = x + 8
```

Start values: `x = 4`, `trunk_h = 4`, `leaf = 2`.

**Fill the table.**

<table class="tr">
<tr><th>i</th><th>x</th><th>trunk_h</th><th>leaf</th><th>leaf width</th></tr>
<tr><td>1</td><td>4</td><td>4</td><td>2</td><td>5</td></tr>
<tr><td>2</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>3</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>4</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

<div class="mini-q">Look down the columns.</div>

**`trunk_h` goes up by 2. `leaf` goes up by 1. Which tree is tallest, and which has the widest leaves?**

<div class="write-space short"></div>

---

## 3 · Build it 🌳

<div class="tpl">Template</div>

```python
def on_chat():
    x = 4
    z = 8
    trunk_h = 4
    leaf = 2
    for i in range(1, ???):
        blocks.fill(OAK_LOG,
            pos(x, 0, z), pos(x, ???, z), REPLACE)
        blocks.fill(OAK_LEAVES,
            pos(x - ???, trunk_h + 1, z - ???),
            pos(x + ???, trunk_h + 3, z + ???), REPLACE)
        trunk_h = trunk_h + ???
        leaf = leaf + ???
        x = x + ???
player.on_chat("trees", on_chat)
```

<div class="where"><span class="lab">Careful</span>
The three counter lines go at the <b>end</b> of the loop, after both fills. Put them first and your first tree comes out wrong.</div>

**Before you run: how many trees will you get?**

<div class="write-space short"></div>

<div class="check"><span class="lab">Works when</span> three trees stand in a row, each taller and wider than the one before.</div>

<div class="stuck"><span class="lab">All the trees are the same?</span>
Your counter lines are outside the loop. Check the spaces at the front.</div>

<div class="stuck"><span class="lab">Only one tree?</span>
`x` is not changing, so every tree is built in the same place.</div>

---

## 4 · The gap 📏

Tree 3 has `leaf = 4`, so its leaves are 9 wide.

**Trees are 8 apart. Is 8 enough space for a 9 wide tree? Try it and look.**

<div class="write-space short"></div>

**Change the 8 to a smaller number. Run it. What happens to the leaves?**

<div class="write-space"></div>

<div class="check"><span class="lab">You understand it when</span> you can say the smallest gap that keeps every tree separate.</div>

---

## 5 · Clean up 🧹

Your trees reach x = 24 and y = 11.

<div class="tpl">Template</div>

```python
blocks.fill(AIR,
    pos(0, 0, 0), pos(???, ???, ???), REPLACE)
```

**Your old `del` used 15. Why is that not big enough now?**

<div class="write-space short"></div>

---

## 6 · Show Your Work 📸🎥

Record **one video**, one take, no stopping. A phone is fine. Show these in order:

> 1. Type `del`, then `trees`. Walk past all three trees.
> 2. Show the trunk fill and say why it makes a pole.
> 3. Show the leaf fill and point at the minus and the plus.
> 4. Show your three counter lines and say what each one grows.
> 5. Show your filled table and read row 3 out loud.

Try to use these words: **loop**, **counter**, **trunk**, **leaves**, **gap**.

**Plan what you will say before you record.**

<div class="write-space tall" style="min-height: 240px"></div>

### Submit ✅

Send this worksheet and your video to teacher on KakaoTalk.
