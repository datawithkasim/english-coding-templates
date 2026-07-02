# Python: Fixing Common Errors 🐍

When your code does not run, it is almost always one of these small things.
Check this list first!

---

## ✅ Error 1: Indentation (the spaces in front of a line)

Python uses **spaces in front of a line** to know what belongs inside a block.

These three things always need the lines under them to be **indented** (pushed in):

- `def` (a function)
- `if`
- `while` / `for` loops

### ❌ Wrong (not indented)
```python
def on_chat():
forward = 5
```

### ✅ Right (indented)
```python
def on_chat():
    forward = 5
```

👉 The line `forward = 5` is **inside** the function, so it must be pushed in.

**How to indent:**
- Press **Enter** to make a new line.
- Press **Tab** to push the line in (indent).
- Press **Backspace** to pull the line back out.

---

## ✅ Error 2: Don't forget the `:` (colon)

`def`, `if`, `while`, and `for` lines must **end with a colon `:`**

### ❌ Wrong
```python
while True
if forward == 5
```

### ✅ Right
```python
while True:
if forward == 5:
```

👉 No colon = error. Always check the end of the line.

---

## ✅ Error 3: Keep the function name on the same line as `def`

The function name goes **right after `def`, on the same line**, ending with `()` and `:`

### ❌ Wrong
```python
def
on_chat():
```

### ✅ Right
```python
def on_chat():
```

---

## ✅ Error 4: Match your indentation

Lines inside the **same block** must line up with the same number of spaces.

### ❌ Wrong (lines don't line up)
```python
def on_chat():
    forward = 5
      agent.move(FORWARD, forward)
```

### ✅ Right (lines line up)
```python
def on_chat():
    forward = 5
    agent.move(FORWARD, forward)
```

👉 A loop inside a function gets indented **again**:
```python
def on_chat():
    for layer in range(3):
        agent.move(FORWARD, 5)
```

---

# 🎯 Practice Exercises

Fix each one. The error is written above it.

### Exercise 1 — Missing colon
```python
def on_chat()
    agent.move(FORWARD, 3)
player.on_chat("go", on_chat)
```

### Exercise 2 — Not indented
```python
def on_chat():
agent.move(UP, 1)
player.on_chat("up", on_chat)
```

### Exercise 3 — Missing colon on the loop
```python
def on_chat():
    for i in range(4)
        agent.move(FORWARD, 1)
        agent.turn(TurnDirection.LEFT)
player.on_chat("square", on_chat)
```

### Exercise 4 — Wrong indentation (lines don't line up)
```python
def on_chat():
    forward = 5
      agent.move(FORWARD, forward)
player.on_chat("run", on_chat)
```

### Exercise 5 — Loop not indented inside the function
```python
def on_chat():
for layer in range(3):
    agent.move(UP, 1)
player.on_chat("tower", on_chat)
```

---

# ✅ Answer Key

### Exercise 1
```python
def on_chat():
    agent.move(FORWARD, 3)
player.on_chat("go", on_chat)
```

### Exercise 2
```python
def on_chat():
    agent.move(UP, 1)
player.on_chat("up", on_chat)
```

### Exercise 3
```python
def on_chat():
    for i in range(4):
        agent.move(FORWARD, 1)
        agent.turn(TurnDirection.LEFT)
player.on_chat("square", on_chat)
```

### Exercise 4
```python
def on_chat():
    forward = 5
    agent.move(FORWARD, forward)
player.on_chat("run", on_chat)
```

### Exercise 5
```python
def on_chat():
    for layer in range(3):
        agent.move(UP, 1)
player.on_chat("tower", on_chat)
```

---

# 🌟 Remember the 4 checks

1. **Indent** the lines inside `def`, `if`, `while`, `for` (press Tab).
2. End `def` / `if` / `while` / `for` lines with **`:`**
3. Keep the function name **next to `def`**.
4. Make lines in the same block **line up**.

Press **Enter** for a new line, **Tab** to indent, **Backspace** to go back.
