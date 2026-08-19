# 📖 Extra — Café Menu: Four More Items

**Topic:** Dictionaries inside dictionaries · **Course:** Extra Worksheet · **Time:** about 30 minutes

Your café menu holds three items. Tonight it grows to seven, and every price gets its own variable.

> Keep these words handy: **dictionary**, **key**, **value**, **variable**, **f-string**.

---

## 1 · Read Your Own Code 👀

```python
starbucks = {
    "americano": {
        "price": 6000,
        "ingredients": ["coffee beans", "hot water", "ice"]
    },
    "peach ice tea": {
        "price": 3000,
        "ingredients": ["ice", "peach tea", "water"]
    },
    "apple pie": {
        "price": 4000,
        "ingredients": ["apple jam", "bread", "suger"]
    }
}

print("=== MENU ===")
for name, info in starbucks.items():
    print(f"{name} ..... {info['price']} won")
```

**How many lines print under `=== MENU ===`? Why that many?**

<div class="write-space short"></div>

**`starbucks["apple pie"]["price"]` gives you which number? Which key did each `[ ]` use?**

<div class="write-space short"></div>

---

## 2 · Plan Four New Items ✏️

Write four things your café will sell. Any prices you like.

<table style="width:100%; table-layout:fixed">
  <tr><th style='width:28%'>Name</th><th style='width:18%'>Price (won)</th><th style='width:54%'>Three ingredients</th></tr>
  <tr><td style='height:44px'></td><td></td><td></td></tr>
  <tr><td style='height:44px'></td><td></td><td></td></tr>
  <tr><td style='height:44px'></td><td></td><td></td></tr>
  <tr><td style='height:44px'></td><td></td><td></td></tr>
</table>

**Every new item must have: Circle one:** price only · price and ingredients · ingredients only

**Why does the loop above break if an item has no `"ingredients"`?**

<div class="write-space short"></div>

---

## 3 · Type The Four Items 💻

Copy this shape inside `starbucks`, once for each item you planned. Put a comma after the `}` of the item before it.

```python
    "mango juice": {
        "price": 5000,
        "ingredients": ["mango", "milk", "ice"]
    }
```

Press Run after each item. Seven lines under `=== MENU ===` means all four went in.

**Write your fourth item here, the way you typed it:**

<div class="write-space"></div>

---

## 4 · One Price, One Variable 💰

A variable holds one price, pulled out with the two keys you learned.

```python
mango_juice_price = starbucks["mango juice"]["price"]
```

The variable name is the menu name with `_` instead of spaces, plus `_price`. Inside the `[ ]` the name keeps its spaces.

**Write the seven variable lines you need, one per line:**

```
1.
2.
3.
4.
5.
6.
7.
```

---

## 5 · Print The Prices 🖨️

```python
print(americano_price)
print(peach_ice_tea_price)
print(apple_pie_price)
```

Add one `print` line for each item you planned, then Run.

**Your first three numbers are 6000, 3000, 4000. Write the four that follow:**

```
1.
2.
3.
4.
```

**One line printed the wrong thing, or an error appeared. What did you check first?**

<div class="write-space short"></div>

---

## 6 · Show Your Work 📸🎥

Open `main.py` so your seven menu items and your price lines are on screen, and press Run.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

1. Your code, and explain what your four new items are.
2. Your output, and explain what one variable line does.

**Fill the blanks:**

<div class="write-space tall" style="min-height: 340px"></div>

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.
>
> The most fun part was ______.
>
> Something new I learned was ______.

### Submit

Send the video and this worksheet to teacher on KakaoTalk.
