# 🧨 Minesweeper AI Benchmark

A benchmarking simulation comparing three AI agent architectures on an 8×8 Minesweeper board — from pure random guessing to constraint-based logical inference. Built to measure both **win rate accuracy** and **computational cost** across varying mine densities.

-----

## 📸 Results

![Benchmark Results](minesweeper_benchmark.png)

-----

## 🤖 Agent Architectures

### `random` — Baseline Agent

Selects uniformly at random from all unrevealed cells. No logic, no memory. Used as a performance floor.

### `rule1` — Flag-Safe Deduction

Applies **Rule 1**: if a numbered cell’s mine count equals its flagged neighbours, all remaining hidden neighbours are safe to reveal. Falls back to random when no deduction is available.

### `rule2` — Subset Constraint Inference

Extends Rule 1 with **Rule 2**: if the hidden neighbours of cell A are a strict subset of cell B’s hidden neighbours, and their remaining mine counts match, the cells in B but not A are guaranteed safe. Falls back through rule1 → random.

-----

## 📊 Key Findings

|Mine Count|Random|Rule 1|Rule 2|
|----------|------|------|------|
|1         |~73%  |~100% |~100% |
|5         |~1%   |~97%  |~98%  |
|9         |~0%   |~60%  |~78%  |
|13        |~0%   |~29%  |~42%  |
|17+       |0%    |≤5%   |≤9%   |

- **Rule 2 outperforms Rule 1 by ~10–18%** in the critical 9–13 mine range
- All agents converge to ~0% beyond ~17 mines (~26% board density)
- Rule 2 is the most computationally expensive but delivers the best accuracy

-----

## 🗂️ Project Structure

```
minesweeper-ai/
├── minesweeper.py              # Main simulation + benchmark runner
├── minesweeper_benchmark.png   # Output chart (generated on run)
├── requirements.txt
├── .gitignore
└── README.md
```

-----

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/HtetMyatAungg/minesweeper-ai.git
cd minesweeper-ai
pip install -r requirements.txt
```

### Run

```bash
python minesweeper.py
```

This will simulate 100 games per mine count for each agent and save `minesweeper_benchmark.png` to the working directory.

-----

## ⚙️ Configuration

At the top of `minesweeper.py`:

```python
rows, cols = 8, 8          # Board dimensions
games_per_step = 100        # Games simulated per (agent, mine_count) pair
mine_range = range(1, 30, 4) # Mine counts to benchmark
```

Increase `games_per_step` for smoother curves at the cost of runtime.

-----

## 🧠 How It Works

1. **Board generation** — mines placed randomly; each non-mine cell stores its adjacent mine count
1. **First-move guarantee** — if the first chosen cell isn’t a `0`-cell, the board is regenerated until it is (mirrors real Minesweeper UX)
1. **Flood fill** — revealing a `0`-cell recursively reveals all connected safe cells
1. **Flag placement** — before each move, rule-based agents scan the board and flag cells that are provably mines
1. **Win condition** — all non-mine cells revealed without hitting a mine

-----

## 📈 Potential Extensions

- **Rule 3** — probability-based guessing using mine density estimates for unresolved cells
- **CSP solver** — full constraint satisfaction to maximise deterministic coverage
- **Larger boards** — 16×16 or 30×16 (intermediate/expert Minesweeper standard)
- **Visualiser** — step-through game replay with board state rendering

-----

## 📄 License

MIT License — see [`LICENSE`](LICENSE)

-----

## 👤 Author

**Henry (Htet Myat Aung)**  
BSc Computer Science (AI) — Royal Holloway, University of London  
[GitHub](https://github.com/HtetMyatAungg) · [LinkedIn](https://linkedin.com/in/htet-myat-aung-4a370932a)
