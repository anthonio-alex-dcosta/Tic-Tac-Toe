<!-- ═══════════════════════════ HEADER ═══════════════════════════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:4338ca,100:ec4899&height=230&section=header&text=Tic%20%C3%97%20Tac%20%C3%97%20Toe&fontSize=60&fontColor=ffffff&fontAlignY=36&desc=Nine%20squares.%20Eight%20ways%20to%20win.%20Pure%20Python.&descAlignY=58&descSize=18&animation=fadeIn" alt="Tic-Tac-Toe banner" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2600&pause=700&color=F472B6&center=true&vCenter=true&width=600&lines=Player+1+is+X+%E2%9D%8C;Player+2+is+O+%E2%AD%95;Three+in+a+row+wins+%F0%9F%8F%86;Zero+dependencies+%E2%9A%A1" alt="Typing intro" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=gnubash&logoColor=white" alt="Terminal" />
  <img src="https://img.shields.io/badge/Dependencies-0-ec4899?style=for-the-badge" alt="Zero dependencies" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/anthonio-alex-dcosta/Tic-Tac-Toe?style=flat-square&color=4338ca" alt="Top language" />
  <img src="https://img.shields.io/github/last-commit/anthonio-alex-dcosta/Tic-Tac-Toe?style=flat-square&color=ec4899" alt="Last commit" />
</p>

---

## 🎮 Play

```text
$ python tictacktoe.py
Enter player 1's name: Alice
Enter player 2's name: Bob
Alice, your character is X
Bob, your character is O
-------------
| X | 2 | O |
|---|---|---|
| 4 | X | 6 |
|---|---|---|
| O | 8 | X |
-------------
Alice has won the game!!!!
```

Pick a square by typing its number, `1` to `9`:

<table align="center">
  <tr><td align="center" width="60"><b>1</b></td><td align="center" width="60"><b>2</b></td><td align="center" width="60"><b>3</b></td></tr>
  <tr><td align="center"><b>4</b></td><td align="center"><b>5</b></td><td align="center"><b>6</b></td></tr>
  <tr><td align="center"><b>7</b></td><td align="center"><b>8</b></td><td align="center"><b>9</b></td></tr>
</table>

---

## 🧠 How it thinks

The board isn't a grid of characters. It's **two parallel occupancy vectors**, one per player:

```python
xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]   # 1 where X has played
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]   # 1 where O has played
```

A player wins when any of the **8 winning lines** sums to `3` in their vector:

```python
wins = [[0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # columns
        [0,4,8],[2,4,6]]           # diagonals
```

```mermaid
flowchart LR
    A(["Start"]) --> B["Read names"]
    B --> C["Print board"]
    C --> D["Current player picks 1-9"]
    D --> E{"Move ≥ 5?"}
    E -- no --> F{"9 moves made?"}
    E -- yes --> G{"Any line sums to 3?"}
    G -- yes --> W(["🏆 Winner"])
    G -- no --> F
    F -- no --> C
    F -- yes --> DR(["🤝 Draw"])
```

> ⚡ **Early-exit check.** Nobody can win before the 5th move, so the game skips the win check until then.

---

## 🚀 Run it

```bash
git clone https://github.com/anthonio-alex-dcosta/Tic-Tac-Toe.git
cd Tic-Tac-Toe
python3 tictacktoe.py
```

No installs and no packages. Python 3 is all you need.

---

<p align="center">
  <a href="https://github.com/anthonio-alex-dcosta"><img src="https://img.shields.io/badge/Built_by-Anthonio_Alex_D_Costa-4338ca?style=for-the-badge&logo=github&logoColor=white" alt="Author" /></a>
  <a href="https://anthonio-alex-dcosta.github.io/portfolio/"><img src="https://img.shields.io/badge/Portfolio-ec4899?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:ec4899,50:4338ca,100:0f172a&height=120&section=footer" alt="footer" />
</p>
