import pytest

from puzzles import puzzles
from solvers import BacktrackingSolver, DFSSolver
from optimal_solver import a_star
from informed_solver import count_conflicts


def is_solved(grid, puzzle):
    groups = [row for row in grid]
    groups += [[grid[r][c] for r in range(9)] for c in range(9)]
    groups += [
        [grid[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
        for br in range(0, 9, 3) for bc in range(0, 9, 3)
    ]
    if any(sorted(g) != list(range(1, 10)) for g in groups):
        return False
    # Givens must be preserved
    return all(puzzle[r][c] in (0, grid[r][c]) for r in range(9) for c in range(9))


@pytest.mark.parametrize("difficulty", list(puzzles))
def test_backtracking(difficulty):
    grid, _ = BacktrackingSolver(puzzles[difficulty]).solve()
    assert is_solved(grid, puzzles[difficulty])


@pytest.mark.parametrize("difficulty", list(puzzles))
def test_dfs(difficulty):
    grid, _ = DFSSolver(puzzles[difficulty]).solve()
    assert is_solved(grid, puzzles[difficulty])


def test_a_star_easy():
    grid, _ = a_star(puzzles["Easy"])
    assert is_solved(grid, puzzles["Easy"])


def test_solver_does_not_mutate_puzzle():
    original = [row[:] for row in puzzles["Easy"]]
    BacktrackingSolver(puzzles["Easy"]).solve()
    assert puzzles["Easy"] == original


def test_count_conflicts_on_solution_is_zero():
    grid, _ = BacktrackingSolver(puzzles["Easy"]).solve()
    assert count_conflicts(grid) == 0
