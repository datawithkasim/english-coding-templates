<style>
.steps { border-left: 4px solid #6b4ee6; background: #f7f5ff; border-radius: 0 8px 8px 0; padding: 10px 14px; margin: 12px 0; }
.steps .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #6b4ee6; text-transform: uppercase; }
.steps ol { margin: 6px 0 0; padding-left: 20px; }
.steps li { margin: 3px 0; font-size: 14.5px; }
.stuck { border: 2px dashed #ffc75c; background: #fffdf3; border-radius: 8px; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.stuck .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #c07a00; text-transform: uppercase; display: block; margin-bottom: 3px; }
.check { border-left: 4px solid #2e9e5b; background: #f2fbf5; border-radius: 0 8px 8px 0; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.check .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #2e9e5b; text-transform: uppercase; display: block; margin-bottom: 3px; }
.info { border-left: 4px solid #38a8c8; background: #f1fafd; border-radius: 0 8px 8px 0; padding: 10px 14px; margin: 12px 0; font-size: 14.5px; }
.info .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #1f7f9c; text-transform: uppercase; display: block; margin-bottom: 3px; }
.mini-q { font-size: 14px; font-weight: 700; margin: 10px 0 2px; }
</style>

# 🔫 Extra — Bullets, Lists, and the Frame Loop

**Topic:** Lists · Deleting Safely · Timers · Collisions · **Course:** Extra Worksheet · **Time:** about 60 minutes

> Keep these words handy: **frame**, **list**, **copy**, **index**, **cooldown**, **collide**, **remove**

Today you gave your ship bullets. A bullet is a small list `[x, y]` living inside a bigger list `bullets`. Everything hard about bullets is really about lists: adding to them, walking them, and deleting from them safely. This sheet is reading and tracing on paper first, then two builds in your own game.

<div class="steps"><span class="lab">How to use this sheet</span>
<ol>
<li>Read on paper first. Do not open the IDE until section 8.</li>
<li>Every question has small steps under it. Do them in order.</li>
<li>Stuck? Read the yellow box. It points at where to look — never the answer.</li>
<li>Write something in every box. A wrong answer you can talk about beats an empty box.</li>
</ol>
</div>

---

## 1 · The Map of the Window 🗺️

Before any code: every number in your game is a distance in **pixels**, measured from the top-left corner.

<div style="page-break-inside:avoid; break-inside:avoid; margin:10px 0 4px">
<div style="position:relative;height:330px;width:520px;max-width:100%;margin:0 auto;background:#eafce9;border:2px solid #444;border-radius:6px">
  <span style="position:absolute;left:6px;top:4px;font:700 11px 'JetBrains Mono',monospace;color:#222">(0, 0) start here</span>

  <div style="position:absolute;left:150px;top:26px;width:330px;border-top:2px solid #d63b3b"></div>
  <span style="position:absolute;left:150px;top:6px;font:700 12px 'JetBrains Mono',monospace;color:#d63b3b">◀ S_WIDTH = 400 pixels ▶</span>

  <div style="position:absolute;left:26px;top:60px;height:230px;border-left:2px solid #6b4ee6"></div>
  <span style="position:absolute;left:34px;top:296px;font:700 12px 'JetBrains Mono',monospace;color:#6b4ee6">▲ S_HEIGHT = 400 pixels ▼</span>

  <div style="position:absolute;left:0;top:150px;width:250px;border-top:1px dashed #444"></div>
  <span style="position:absolute;left:60px;top:128px;font:700 11px 'JetBrains Mono',monospace;color:#444">bullet_x = 197 → across from the LEFT</span>

  <div style="position:absolute;left:250px;top:0;height:150px;border-left:1px dashed #444"></div>
  <span style="position:absolute;left:258px;top:70px;font:700 11px 'JetBrains Mono',monospace;color:#444">bullet_y = 175 ↓ down from the TOP</span>

  <div style="position:absolute;left:250px;top:150px;width:10px;height:26px;background:#d00;border:1px solid #900"></div>
  <span style="position:absolute;left:268px;top:152px;font:700 10px 'JetBrains Mono',monospace;color:#900">the bullet (drawn bigger here)</span>

  <div style="position:absolute;left:225px;top:200px;width:60px;height:60px;background:#0ff;border:1px solid #066"></div>
  <span style="position:absolute;left:292px;top:222px;font:700 11px 'JetBrains Mono',monospace;color:#066">player 50 × 50</span>

</div>
<p style="font:700 12px 'JetBrains Mono',monospace;color:#444;margin:6px 0 0;text-align:center">x grows to the RIGHT · y grows DOWNWARDS · the bottom of the window is y = 400</p>
</div>

**In one sentence each: what is `S_WIDTH`, and what is `S_HEIGHT`?**

<div class="write-space short"></div>

**A bullet sits at `[197, 20]`. Describe where it is on the screen.**

<div class="write-space short"></div>

**Which is bigger for something near the top of the screen — a big `y` or a small `y`?**

<div class="write-space short"></div>

---

## 2 · The Size of One Bullet 📏

`bullet_x` and `bullet_y` say **where** the bullet is. `bullet_width` and `bullet_height` say **how big** it is. Four different jobs, four different numbers.

<div style="page-break-inside:avoid; break-inside:avoid; margin:10px 0 4px">
<div style="position:relative;height:240px;background:#f7f7fb;border:2px solid #ddd;border-radius:6px">
  <span style="position:absolute;left:10px;top:8px;font:700 12px 'JetBrains Mono',monospace;color:#666">zoomed in ×10</span>

  <div style="position:absolute;left:120px;top:50px;width:60px;height:160px;background:#d00;border:1px solid #900"></div>

  <div style="position:absolute;left:120px;top:34px;width:60px;border-top:2px solid #6b4ee6"></div>
  <span style="position:absolute;left:190px;top:26px;font:700 12px 'JetBrains Mono',monospace;color:#6b4ee6">bullet_width = 6 → how WIDE</span>

  <div style="position:absolute;left:100px;top:50px;height:160px;border-left:2px solid #d63b3b"></div>
  <span style="position:absolute;left:190px;top:120px;font:700 12px 'JetBrains Mono',monospace;color:#d63b3b">bullet_height = 16 → how TALL</span>

  <span style="position:absolute;left:120px;top:214px;font:700 11px 'JetBrains Mono',monospace;color:#444">the corner here is (bullet_x, bullet_y)</span>
</div>
</div>

<div class="info"><span class="lab">The line that uses all four</span>
<code>pygame.draw.rect(screen, bullet_colour, (bullet[0], bullet[1], bullet_width, bullet_height))</code><br>
Position first, size second. Always in that order.
</div>

**Your bullet is 6 wide and 16 tall. Draw the shape you expect — tall and thin, or short and fat?**

<div class="write-space blank short"></div>

**Which two of these four numbers change while the bullet flies up the screen?**

<div class="write-space short"></div>

**A player at `player_x = 380` is 50 wide, in a window 400 wide. What is wrong, and which line in your game stops it?**

<div class="write-space"></div>

---

## 3 · Predict 🔮

Read each block. Write what happens — just from reading.

```python
bullet = [197, 300]
bullet_speed = 12

bullet[1] = bullet[1] - bullet_speed
print(bullet)
```

<p class="mini-q">Step 1 — Which slot changed, and what does that slot mean?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — What prints? Did the bullet move up or down?</p>

<div class="write-space short"></div>

```python
bullets = []
bullets.append([197, 300])
bullets.append([197, 300])
bullets.append([197, 300])

print(len(bullets))
```

<p class="mini-q">What prints? Why are they allowed to look identical?</p>

<div class="write-space short"></div>

```python
bullet_cooldown = 300
bullet_lastshot = 0
now = 250

print(now - bullet_lastshot > bullet_cooldown)
```

<p class="mini-q">Step 1 — Work out the left side of the `>` first.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — True or False? So does a bullet get made?</p>

<div class="write-space short"></div>

```python
bullets = [[0, 10], [0, 20], [0, 30], [0, 40]]

for bullet in bullets:
    bullets.remove(bullet)

print(bullets)
```

<p class="mini-q">Careful — this is the trap from the lesson. What is left in the list?</p>

<div class="write-space"></div>

---

## 4 · Trace the Cooldown 📋

Your game runs 60 frames a second, so `now` jumps about 16 each frame. You are holding SPACE the whole time.

`bullet_cooldown = 300`

<div class="steps"><span class="lab">How to fill each row</span>
<ol>
<li>Work out <code>now - bullet_lastshot</code>.</li>
<li>Is that bigger than 300? Write yes or no.</li>
<li>If yes, a bullet is made and <code>bullet_lastshot</code> becomes <code>now</code>.</li>
<li>If no, <code>bullet_lastshot</code> does not change. Carry it down to the next row.</li>
</ol>
</div>

<div style="page-break-inside:avoid; break-inside:avoid; margin:14px 0">
<table style="width:100%">
<tr><th>now</th><th>bullet_lastshot</th><th>now − lastshot</th><th>bigger than 300?</th><th>bullet made?</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>no</td><td>no</td></tr>
<tr><td>160</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>320</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>480</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>640</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>800</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>
</div>

**Holding SPACE for 3 whole seconds — how many bullets with a cooldown of 300?**

<div class="write-space short"></div>

**And with no cooldown at all, at 60 frames a second?**

<div class="write-space short"></div>

<div class="stuck"><span class="lab">Stuck?</span> 3 seconds is 3000 milliseconds. How many 300s fit inside 3000?</div>

---

## 5 · Trace the Bullets List 🧾

One bullet is fired, then the game runs three more frames. `bullet_speed = 12`. Bullets are deleted when `y` goes below 0.

Fill in the list after each frame.

<div style="page-break-inside:avoid; break-inside:avoid; margin:14px 0">
<table style="width:100%">
<tr><th>frame</th><th>what happens</th><th>bullets list after the frame</th><th>len(bullets)</th></tr>
<tr><td>1</td><td>SPACE pressed, bullet made at y = 300</td><td>[[197, 300]]</td><td>1</td></tr>
<tr><td>2</td><td>move loop runs</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>3</td><td>move loop runs, SPACE pressed again (cooldown allows it)</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>4</td><td>move loop runs</td><td style="height:34px">&nbsp;</td><td>&nbsp;</td></tr>
</table>
</div>

**The new bullet in frame 3 starts at y = 300 again. Why not at 276 like the first one?**

<div class="write-space"></div>

---

## 6 · Spot the Bug 🐛

Every one of these is a real mistake from a real shooter game. Work the steps for each.

<div class="steps"><span class="lab">Bug method — use it every time</span>
<ol>
<li>Say what this code is <b>supposed</b> to do.</li>
<li>Read it one line at a time and say what it <b>actually</b> does.</li>
<li>Circle the exact line where those two stop matching.</li>
<li>Write the fixed code.</li>
<li>Say why your fix works.</li>
</ol>
</div>

**Bug A** — Bullets should disappear off the top. Instead about half of them stay in the list forever.

```python
for bullet in bullets:
    if bullet[1] < 0:
        bullets.remove(bullet)
```

**Hint:** four bullets go in. Count how many the loop actually looks at.

<p class="mini-q">Write the fixed code:</p>

<div class="write-space"></div>

<p class="mini-q">Why was it wrong? Why does your fix work?</p>

<div class="write-space"></div>

**Bug B** — Holding SPACE gives a solid wall of bullets. The cooldown seems to do nothing.

```python
if keys[pygame.K_SPACE] and now - bullet_lastshot > bullet_cooldown:
    bullet_x = player_x + (player_width // 2) - (bullet_width // 2)
    bullet_y = player_y
    bullets.append([bullet_x, bullet_y])
```

**Hint:** something must change after a shot, or the sum stays true forever.

<p class="mini-q">Write the fixed code:</p>

<div class="write-space short"></div>

<p class="mini-q">Why was it wrong? Why does your fix work?</p>

<div class="write-space"></div>

**Bug C** — Bullets come out of the ship and fall to the bottom of the screen.

```python
for bullet in bullets:
    bullet[1] = bullet[1] + bullet_speed
```

**Hint:** in pygame, y = 0 is the top.

<p class="mini-q">Write the fixed code:</p>

<div class="write-space short"></div>

<p class="mini-q">Why was it wrong? Why does your fix work?</p>

<div class="write-space"></div>

**Bug D** — No bullets are ever visible, even though `len(bullets)` keeps going up.

```python
for bullet in bullets:
    pygame.draw.rect(screen, bullet_colour, (bullet[0], bullet[1], bullet_width, bullet_height))

screen.fill((152, 251, 152))
pygame.draw.rect(screen, CYAN, (player_x, player_y, player_width, player_height))
```

**Hint:** what does `screen.fill` do to everything drawn before it?

<p class="mini-q">Write the fixed code:</p>

<div class="write-space"></div>

<p class="mini-q">Why was it wrong? Why does your fix work?</p>

<div class="write-space"></div>

**Bug E** — This is from your own file. Three enemies cross the bottom on the same frame. The score only goes up by 2, and one enemy stays in the game invisibly — it can still end your game.

```python
for enemy in enemies:
    if enemy[1] > S_HEIGHT:
        enemies.remove(enemy)
        score += 1
```

**Hint:** you have seen this exact shape already today.

<p class="mini-q">Write the fixed code:</p>

<div class="write-space short"></div>

<p class="mini-q">Why was it wrong? Why does your fix work?</p>

<div class="write-space"></div>

---

## 7 · Explain the Code 📖

Your own lines from today. Answer from reading only.

```python
bullet_x = player_x + (player_width // 2) - (bullet_width // 2)
```

<p class="mini-q">Step 1 — What does <code>player_x + (player_width // 2)</code> point at?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Why subtract half the bullet width after that?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — What would the bullet look like if you deleted the whole subtraction?</p>

<div class="write-space short"></div>

```python
for bullet in bullets[:]:
    for enemy in enemies[:]:
```

<p class="mini-q">Both lists carry <code>[:]</code>. Explain what would break if you removed it from just one of them.</p>

<div class="write-space"></div>

```python
if bullet_rect.colliderect(enemy_rect):
    bullets.remove(bullet)
    enemies.remove(enemy)
    score = score + 10
    break
```

<p class="mini-q">Step 1 — What exactly does <code>break</code> stop?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Two enemies overlap each other and one bullet hits both. Without <code>break</code>, which line crashes, and what is the error called?</p>

<div class="write-space"></div>

```python
enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
```

<p class="mini-q">This line is inside the loop, not above it. Explain why it cannot be written once outside.</p>

<div class="write-space"></div>

---

## 8 · Code It 💻

Open `main.py` in the IDE at **app.english-coding.co.uk**. One task at a time. Run the game after every task.

**Task 1 — Count your misses.**

<div class="steps"><span class="lab">Steps</span>
<ol>
<li>Above the game loop, make a variable <code>misses = 0</code>.</li>
<li>Find the loop that deletes bullets leaving the top of the screen.</li>
<li>A bullet leaving the top means you missed. Add 1 to <code>misses</code> there.</li>
<li>Print <code>misses</code> at the same moment, so you can watch it in the console.</li>
</ol>
</div>

<div class="check"><span class="lab">You know it works when</span> firing straight up with no enemy around makes the number climb, and hitting an enemy does not.</div>

**Task 2 — Show it on screen.**

<div class="steps"><span class="lab">Steps</span>
<ol>
<li>You already build <code>score_surface</code> with <code>game_font.render</code>. Copy that pattern for misses.</li>
<li>Blit it under the score, not on top of it — change the second number in the position.</li>
<li>Run it. Both lines should be readable at the same time.</li>
</ol>
</div>

<div class="check"><span class="lab">You know it works when</span> score and misses both show, and neither one overlaps the other.</div>

**Task 3 — Double barrel.**

<div class="steps"><span class="lab">Steps</span>
<ol>
<li>Find the SPACE block where you append one bullet.</li>
<li>Append a second bullet in the same block, a little to the left.</li>
<li>Move the first one a little to the right, so they leave from both wings.</li>
<li>Run it. Both bullets should fly up together and both should be able to hit.</li>
</ol>
</div>

<div class="check"><span class="lab">You know it works when</span> one press of SPACE puts two bullets on screen, and shooting one enemy with both does not crash the game.</div>

<div class="stuck"><span class="lab">Stuck on any task?</span> Print the value you are unsure about — <code>print(misses)</code>, <code>print(len(bullets))</code> — run the game and read the console. If a change breaks everything, undo it and make a smaller change.</div>

**Write your plan here before you code.**

<div class="write-space tall" style="min-height: 280px"></div>

---

## 9 · Explain Your Code 🎥

Record a short video on your phone explaining the code **you** wrote. Try to use these words: **list**, **copy**, **index**, **cooldown**, **collide**, **remove**.

> 1. Fire once and point at the line that made the bullet.
> 2. Point at the line that moves it and say why it is a minus.
> 3. Show your cooldown line and say what would happen without it.
> 4. Show one place you wrote <code>[:]</code> and explain what it protects you from.
> 5. Show your misses counter working.

**Plan what you will say here before you record.**

<div class="write-space tall" style="min-height: 280px"></div>

---

### Submit ✅

Send this worksheet + your video or photo to teacher on KakaoTalk.
