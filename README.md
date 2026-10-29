![Sudoku dashboard](https://github.com/user-attachments/assets/13e701ce-b4ff-40eb-83be-7141dc08e6f7)

# Sudoku Solver: Search Algorithms Compared

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Tests](https://github.com/Med00amine/Sudoku/actions/workflows/tests.yml/badge.svg)

A desktop Sudoku game built with Tkinter. You can play puzzles yourself, or let one of several AI search algorithms solve the board and compare how they perform (iterations and time).

## Features

- **Play**: four difficulty levels (Easy, Moderate, Difficult, Expert)
- **Live feedback**: correct entries turn green, wrong ones red
- **Pencil marks**: press `P` on a cell to add candidate numbers
- **Helpers**: row, column and box highlighting, a timer with pause/resume, clear and reset
- **AI solvers**: pick an algorithm and see its result with stats

## Algorithms

| Algorithm | File | Type | Notes |
|---|---|---|---|
| Backtracking | `solvers.py` | Uninformed, recursive | Fills cells in order and undoes a choice when it hits a dead end. Fast and always correct. |
| DFS | `solvers.py` | Uninformed, explicit stack | Same search as backtracking but uses an explicit stack of board states. |
| BFS | `solvers.py` | Uninformed, queue | Disabled in the GUI: the number of states grows exponentially, so it freezes on real puzzles. Kept here for comparison. |
| A* | `optimal_solver.py` | Informed | Priority queue ordered by cost + number of empty cells. |
| Hill Climbing | `informed_solver.py` | Local search | Fills each row randomly, then swaps cells to reduce conflicts. Fast, but can get stuck in a local minimum (the result shows the remaining conflicts). |

Hill climbing shows how local search behaves on a problem full of constraints. It often stops with a few conflicts left, while the systematic searches always find the solution.

## Getting Started

```bash
git clone https://github.com/Med00amine/Sudoku.git
cd Sudoku
pip install -r requirements.txt
python main.py
```

Tkinter comes with most Python installs. On Debian/Ubuntu, install it with `sudo apt install python3-tk`.

## Controls

| Action | How |
|---|---|
| Select a cell | Click it |
| Enter a number | `1`–`9` |
| Erase | `Backspace` / `Delete` |
| Pencil marks | `P` |
| Solve with AI | Choose an algorithm, then click the AI button |

## Project Structure

```text
.
├── main.py             # Tkinter GUI (menu + dashboard)
├── puzzles.py          # Built-in puzzles by difficulty
├── sudoku.py           # Shared grid helpers (validity checks, etc.)
├── solvers.py          # Backtracking, DFS, BFS solvers
├── optimal_solver.py   # A* search
├── informed_solver.py  # Hill climbing
├── tests/              # pytest suite for the solvers
└── *.png               # UI icons
```

## Running Tests

```bash
pip install -r requirements-dev.txt
pytest
```

The tests check that Backtracking and DFS solve every built-in puzzle, that A* solves the easy one, that the original puzzle is never modified, and that a solved grid has zero conflicts. GitHub Actions runs them on every push.

## Possible Improvements

- Random puzzle generator with a guaranteed unique solution
- Step-by-step animation of the solver (`InstrumentedBacktrackingSolver` already provides the hooks)
- Constraint propagation (MRV heuristic) to speed up the search
