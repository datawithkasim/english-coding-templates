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

# 🟩 Fill Loops — English Worksheet

**Topic:** One corner, six rectangles · **Course:** 3D Coordinates · **Level:** Extension · **Time:** about 40 minutes

<span class="timing">Type `del` before every `run`. Every time.</span>

Every `???` is one short thing for you to work out. There are no answers on this sheet.

---

## 1 · Read the loop 🔍

```python
x_start = 1
z_start = 1
x_end = 1
z_end = 1
for i in range(1, 7):
    blocks.fill(EMERALD_BLOCK,
        pos(x_start, 0, z_start),
        pos(x_end, 0, z_end), REPLACE)
    x_end = x_end + 2
    z_end = z_end + 3
```

**`range(1, 7)` gives you which numbers? Write them all.**

<div class="write-space short"></div>

**Two lines inside the loop change a variable. Write them.**

<div class="write-space short"></div>

**Four variables never change. Which?**

<div class="write-space short"></div>

<div class="check"><span class="lab">Got it right if</span> your list of numbers stops at 6, not 7.</div>

---

## 2 · Fill the table ✏️

Do it in your head first. Run the code after.

<table class="tr">
<tr><th>i</th><th>x_end</th><th>z_end</th><th>size</th><th>blocks</th></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1 x 1</td><td>1</td></tr>
<tr><td>2</td><td>3</td><td>4</td><td>3 x 4</td><td>12</td></tr>
<tr><td>3</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>4</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>5</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>6</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

**Add up the last column. How many blocks does the code write?**

<div class="write-space short"></div>

**Now walk on your build and count it. How many blocks are really there?**

<div class="write-space short"></div>

<div class="mini-q">The two numbers are different.</div>

**Why?**

<div class="write-space"></div>

---

## 3 · One fill instead of six 🎯

Only the last rectangle is still visible.

<div class="tpl">Template</div>

```python
blocks.fill(EMERALD_BLOCK,
    pos(1, 0, 1),
    pos(???, 0, ???), REPLACE)
```

<div class="steps"><span class="lab">Steps</span>
<ol>
<li>Type <code>del</code>.</li>
<li>Run your one-line version.</li>
<li>Type <code>del</code>. Run the loop version.</li>
<li>Look at both. Same shape?</li>
</ol>
</div>

<div class="check"><span class="lab">Works when</span> both builds look exactly the same.</div>

---

## 4 · Make it stand up 🧱

Right now `y_start` and `y_end` are both `0`, so your build is one block tall.

<div class="tpl">Template · inside the loop</div>

```python
    x_end = x_end + 2
    z_end = z_end + 3
    ??? = ??? + ???
```

<div class="warn"><span class="lab">Start small</span>
Use <b>1</b> first. Adding 3 six times makes it 15 tall and your <code>del</code> cannot reach the top.</div>

**Before you run it: how tall will it be after 6 turns if you add 1 each time?**

<div class="write-space short"></div>

<div class="check"><span class="lab">Works when</span> it is a solid block you can stand next to, not a floor.</div>

---

## 5 · Pull them apart ✂️

The near corner never moves, so the shapes sit on top of each other. Move it and they separate.

<div class="tpl">Template · inside the loop</div>

```python
    ??? = ??? + ???
```

**Tree of thought: tree 3 is 5 wide. How far must the corner move so shapes do not touch?**

<div class="write-space short"></div>

<div class="check"><span class="lab">Works when</span> you can walk between the shapes.</div>

<div class="stuck"><span class="lab">Still one lump?</span>
You changed <code>x_end</code> again instead of <code>x_start</code>. Read the variable name carefully.</div>

---

## 6 · Show Your Work 📸🎥

Record **one video**, one take, no stopping. A phone is fine. Show these in order:

> 1. Type `del`, then `run`. Walk around your build.
> 2. Show the two lines inside the loop and say what each one does.
> 3. Show your filled table and say why the two totals are different.
> 4. Show your one-line version next to the loop version.
> 5. Show your standing-up build and say which variable you changed.

Try to use these words: **loop**, **variable**, **corner**, **fill**, **cover**.

**Plan what you will say before you record.**

<div class="write-space tall" style="min-height: 240px"></div>

### Submit ✅

Send this worksheet and your video to teacher on KakaoTalk.
