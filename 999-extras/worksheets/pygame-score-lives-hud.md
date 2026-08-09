<style>
.steps { border-left: 4px solid #6b4ee6; background: #f7f5ff; border-radius: 0 8px 8px 0; padding: 10px 14px; margin: 12px 0; }
.steps .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #6b4ee6; text-transform: uppercase; }
.steps ol { margin: 6px 0 0; padding-left: 20px; }
.steps li { margin: 3px 0; font-size: 14.5px; }
.stuck { border: 2px dashed #ffc75c; background: #fffdf3; border-radius: 8px; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.stuck .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #c07a00; text-transform: uppercase; display: block; margin-bottom: 3px; }
.check { border-left: 4px solid #2e9e5b; background: #f2fbf5; border-radius: 0 8px 8px 0; padding: 9px 14px; margin: 12px 0; font-size: 14px; }
.check .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #2e9e5b; text-transform: uppercase; display: block; margin-bottom: 3px; }
.mini-q { font-size: 14px; font-weight: 700; margin: 10px 0 2px; }
.info { border-left: 4px solid #38a8c8; background: #f1fafd; border-radius: 0 8px 8px 0; padding: 10px 14px; margin: 12px 0; font-size: 14.5px; }
.info .lab { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .06em; color: #1f7f9c; text-transform: uppercase; display: block; margin-bottom: 3px; }
.flipfig { margin-top: 10px; text-align: center; }
.flipfig .pane { display: inline-block; vertical-align: middle; border: 2px dashed #9fb3bd; border-radius: 8px; background: #fff; padding: 10px 16px; font-family: "Inter", sans-serif; font-size: 12.5px; color: #667; line-height: 1.5; }
.flipfig .pane.on { border-style: solid; border-color: #2e9e5b; color: #2e6b45; }
.flipfig .arrow { display: inline-block; vertical-align: middle; padding: 0 12px; font-family: "JetBrains Mono", monospace; font-size: 13px; font-weight: 700; color: #1f7f9c; }
</style>

# 🎮 Extra — Score, Lives, and the Game Loop

**Topic:** The Frame Loop · Timers · HUD · Debugging · **Course:** Extra Worksheet · **Time:** about 60 minutes

> Keep these words handy: **frame**, **game loop**, **modulo**, **timer**, **blit**, **HUD**, **freeze**

Your shooter now has lives, invincibility, a game-over screen, and a score. Everything in a game happens **once per frame**: read input, move things, check hits, draw, flip. This worksheet is about what belongs inside that one pass — and what happens when something loops forever inside it.

<div class="steps"><span class="lab">How to use this sheet</span>
<ol>
<li>Read on paper first. Do not open the IDE until section 5.</li>
<li>Every question has small steps under it. Do them in order.</li>
<li>If you are stuck, read the yellow box. It tells you where to look — not the answer.</li>
<li>Write something in every box. A wrong answer you can talk about beats an empty box.</li>
</ol>
</div>

---

## 1 · Predict 🔮

Read each block. Write what it does — just from reading.

<div class="steps"><span class="lab">Do this for every block</span>
<ol>
<li>Say out loud what the first line sets up.</li>
<li>Count how many times the loop runs.</li>
<li>Track the variables that change. Write them down as they change.</li>
<li>Then write the output.</li>
</ol>
</div>

```python
frames = 0
score = 0

for _ in range(31):
    if frames % 10 == 0:
        score += 10
    frames += 1

print(score)
```

<p class="mini-q">Step 1 — Which values of <code>frames</code> make <code>frames % 10 == 0</code> true? List them.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — How many are in your list?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — So what number prints?</p>

<div class="write-space short"></div>

<div class="stuck"><span class="lab">Stuck?</span> <code>%</code> gives the remainder after dividing. Try it with small numbers first: what is <code>0 % 10</code>, <code>5 % 10</code>, <code>10 % 10</code>?</div>

```python
enemies = [
    {"color": "RED", "speed": 10},
    {"color": "GREEN", "speed": 8},
]

for enemy in enemies:
    print(enemy["speed"])
```

<p class="mini-q">Step 1 — On the first turn, what is the whole value of <code>enemy</code>?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — What prints, line by line?</p>

<div class="write-space short"></div>

```python
invincible_timer = 8

while invincible_timer > 0:
    print(invincible_timer % 6 < 3)
    invincible_timer -= 1
```

<p class="mini-q">Step 1 — Write the timer values in order, from 8 down.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Under each one, write True or False.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — In your game, that True/False decides whether the player is drawn. So what does the player look like?</p>

<div class="write-space short"></div>

```python
enemy_h = 50

enemy_y = enemy_h
enemy_y2 = -enemy_h
```

<p class="mini-q">Step 1 — In pygame, y = 0 is the top of the window. Where is y = 50? Where is y = −50?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Which one starts the enemy off-screen, ready to fall in?</p>

<div class="write-space short"></div>

---

## 2 · One Frame, In Order 🎞️

Your game loop does the same five jobs every frame.

<div class="steps"><span class="lab">How to fill the table</span>
<ol>
<li>Open your <code>main.py</code> and scroll to <code>while running:</code>.</li>
<li>Read down the loop. Every block belongs to one of the five jobs.</li>
<li>In each row, write what your game does there, and name one line from your file.</li>
</ol>
</div>

<div style="page-break-inside:avoid; break-inside:avoid; margin:14px 0">
<table style="width:100%">
<tr><th>order</th><th>job</th><th>what happens in your game</th><th>one line from your file</th></tr>
<tr><td>1</td><td>read events</td><td style="height:38px">&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>2</td><td>move things</td><td style="height:38px">&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>3</td><td>check hits</td><td style="height:38px">&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>4</td><td>draw</td><td style="height:38px">&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>5</td><td>flip + tick</td><td style="height:38px">&nbsp;</td><td>&nbsp;</td></tr>
</table>
</div>

**`clock.tick(60)` runs once per frame. How many frames in 5 seconds?**

<div class="write-space short"></div>

**`INVINCIBILITY_FRAMES = 60`. Using your answer above, how many seconds is the player safe after a hit?**

<div class="write-space short"></div>

<div class="info"><span class="lab">What flip() does</span>
Pygame does not draw straight onto the window. Every <code>draw</code> and <code>blit</code> goes onto a <b>hidden page</b> that nobody can see yet. <code>pygame.display.flip()</code> swaps that hidden page onto the screen in one go — so the player never sees a half-drawn frame.
<div class="flipfig">
  <span class="pane">hidden page<br><b>you draw here</b></span>
  <span class="arrow">— flip() →</span>
  <span class="pane on">the window<br><b>player sees this</b></span>
</div>
</div>

**Why must `pygame.display.flip()` be the last job, not the first?**

<div class="write-space"></div>

<div class="stuck"><span class="lab">Stuck?</span> Think about what the screen would show if you flipped it before you drew this frame's enemies.</div>

---

## 3 · Spot the Bug 🐛

These four come from your own game. Work through the steps for each one.

<div class="steps"><span class="lab">Bug method — use it every time</span>
<ol>
<li>Say what this code is <b>supposed</b> to do.</li>
<li>Read it one line at a time and say what it <b>actually</b> does.</li>
<li>Circle the exact line where those two stop matching.</li>
<li>Write the fixed code.</li>
<li>Say why your fix works.</li>
</ol>
</div>

**Bug A** — The window opens, then freezes. Nothing draws. Nothing responds.

```python
## UPDATE SCORE ##
while True:
    if frames % 10 == 0:
        score += 10
    frames += 1
```

<p class="mini-q">Step 1 — What is this block supposed to do, in one sentence?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — What would end this <code>while</code> loop? Is there anything that can?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — The lines after it never run. Name two things that stop happening.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 4 — Write the fixed code.</p>

<div class="write-space"></div>

<p class="mini-q">Step 5 — Why does your fix work?</p>

<div class="write-space short"></div>

<div class="stuck"><span class="lab">Stuck?</span> The big <code>while running:</code> loop already repeats every frame. Ask yourself what this block still needs, once you are already inside something that repeats.</div>

**Bug B** — Lives and score print on top of each other, so both are unreadable.

```python
screen.blit(lives_surf, (10, 10))
screen.blit(scores_surf, (10, 10))
```

<p class="mini-q">Step 1 — What do the two numbers in <code>(10, 10)</code> mean?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Write the fixed code. Put score on the right side of the window.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — Why does your fix work?</p>

<div class="write-space short"></div>

<div class="stuck"><span class="lab">Stuck?</span> You already have <code>WIDTH</code>. A position can be worked out from it instead of typed by hand.</div>

**Bug C** — A bullet kills an enemy, but the enemy pops back near the top of the window instead of falling in from above.

```python
if bullet.colliderect(enemy["rect"]):
    enemy["rect"].y = enemy['h']
    enemy["rect"].x = random.randint(0, WIDTH - enemy['w'])
```

<p class="mini-q">Step 1 — Find the respawn lines in your ENEMY MOVEMENT section. Copy the <code>y</code> line here.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Put the two <code>y</code> lines side by side. What is different?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — Write the fixed code, and say why your fix works.</p>

<div class="write-space"></div>

**Bug D** — After GAME OVER, enemies keep jumping back to the top of the window.

```python
if not game_over:
    ...
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    ...

if invincible_timer > 0:
    invincible_timer -= 1
else:
    for enemy in enemies:
        if player_rect.colliderect(enemy["rect"]):
            lives -= 1
            enemy["rect"].y = -enemy["h"]
```

<p class="mini-q">Step 1 — When <code>game_over</code> is <code>True</code>, which of these blocks still runs?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — <code>player_rect</code> stops being updated. What value is it still holding?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — Write the fixed code, and say why your fix works.</p>

<div class="write-space"></div>

<div class="stuck"><span class="lab">Stuck?</span> Ask which jobs should pause on the game-over screen, and which should keep going. Then look at where the <code>if not game_over:</code> block ends.</div>

---

## 4 · Explain the Code 📖

Read your own lines. Answer from reading only.

```python
if invincible_timer == 0 or invincible_timer % 6 < 3:
    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
```

<p class="mini-q">Step 1 — When the timer is 0, is the player drawn? Say why.</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — For 6 frames in a row, how many frames is the player drawn, and how many not?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 3 — So what does the player look like right after being hit?</p>

<div class="write-space short"></div>

```python
if player_x < 0:
    player_x = WIDTH - PLAYER_WIDTH

if player_y < 0:
    player_y = 0
```

<p class="mini-q">The player walks off the left edge. Then off the top edge. Describe both, in your own words.</p>

<div class="write-space"></div>

```python
for bullet in bullets[:]:
```

<p class="mini-q">Step 1 — What does <code>bullets[:]</code> give you that <code>bullets</code> does not?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Inside that loop you call <code>bullets.remove(bullet)</code>. What goes wrong without the colon?</p>

<div class="write-space short"></div>

```python
enemies = [
    {"rect": ..., "color": RED, "speed": 10, "w": ENEMY_WIDTH, "h": ENEMY_HEIGHT},
]
```

<p class="mini-q">Step 1 — You could have used six separate variables per enemy. What does the list of dictionaries give you instead?</p>

<div class="write-space short"></div>

<p class="mini-q">Step 2 — Write the one line that adds a slow, wide, yellow enemy.</p>

<div class="write-space short"></div>

---

## 5 · Code It 💻

Now open `main.py` in the IDE at **app.english-coding.co.uk**. Do one task at a time. Run the game after every task.

**Task 1 — Fix the freeze.**

<div class="steps"><span class="lab">Steps</span>
<ol>
<li>Find the <code>## UPDATE SCORE ##</code> block.</li>
<li>Decide which lines must run <b>once per frame</b>, and keep only those.</li>
<li>Score should stop climbing when <code>game_over</code> is <code>True</code> — put the block where that already happens.</li>
<li>Run it. Watch the score on screen.</li>
</ol>
</div>

<div class="check"><span class="lab">You know it works when</span> the window responds to keys, the score climbs while you play, and it stops climbing on the GAME OVER screen.</div>

**Task 2 — Split the HUD.**

<div class="steps"><span class="lab">Steps</span>
<ol>
<li>Keep lives at the top left.</li>
<li>Move score to the top right. Work the x position out from <code>WIDTH</code>, do not type a number.</li>
<li>Change <code>WIDTH</code> to 700 and run. Then change it back.</li>
</ol>
</div>

<div class="check"><span class="lab">You know it works when</span> both are readable, and the score is still on screen after you change <code>WIDTH</code>.</div>

**Task 3 — Points for kills.**

<div class="steps"><span class="lab">Steps</span>
<ol>
<li>Find the line where a bullet hits an enemy.</li>
<li>Add points there. Start with a flat number for every enemy.</li>
<li>Run it and shoot one enemy. Did the score jump by the right amount?</li>
<li>Now make a faster enemy worth more. Each enemy already carries its own <code>"speed"</code>.</li>
</ol>
</div>

<div class="check"><span class="lab">You know it works when</span> shooting the green enemy and the magenta enemy give different points.</div>

**Write your plan here before you code.**

<div class="write-space tall" style="min-height: 280px"></div>

<div class="stuck"><span class="lab">Stuck on any task?</span> Print the value you are unsure about — <code>print(score)</code>, <code>print(frames)</code> — run the game, and read the console. If a change breaks the game, undo it and make a smaller change.</div>

---

## 6 · Explain Your Code 🎥

Record a short video on your phone explaining the code **you** wrote. Try to use these words: **frame**, **game loop**, **modulo**, **timer**, **blit**, **HUD**.

> 1. Run the game and lose one life. Point at the flicker and say what causes it.
> 2. Show the score line and explain when it goes up and when it stops.
> 3. Show one enemy dictionary and say what each key is for.
> 4. Show your fix for the freeze and explain what the old code did wrong.

**Plan what you will say here before you record.**

<div class="write-space tall" style="min-height: 280px"></div>

---

### Submit ✅

Send this worksheet + your video or photo to teacher on KakaoTalk.
