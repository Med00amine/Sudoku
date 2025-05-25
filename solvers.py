from collections import deque
import copy

class SolverBase:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.steps = 0
        self.solved_grid = None

    def solve(self):
        raise NotImplementedError

    def get_steps(self):
        return self.steps

    def get_solution(self):
        return self.solved_grid

class BacktrackingSolver(SolverBase):
    def solve(self):
        self.solved_grid = copy.deepcopy(self.grid)
        self.steps = 0
        self._backtrack(0, 0)
        return self.solved_grid, self.steps

    def _backtrack(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return self._backtrack(row + 1, 0)
        if self.solved_grid[row][col] != 0:
            return self._backtrack(row, col + 1)
        for num in range(1, 10):
            if self._is_valid(row, col, num):
                self.solved_grid[row][col] = num
                self.steps += 1
                if self._backtrack(row, col + 1):
                    return True
                self.solved_grid[row][col] = 0
        return False

    def _is_valid(self, row, col, num):
        for i in range(9):
            if self.solved_grid[row][i] == num or self.solved_grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.solved_grid[start_row + i][start_col + j] == num:
                    return False
        return True

class DFSSolver(SolverBase):
    def solve(self):
        self.solved_grid = copy.deepcopy(self.grid)
        self.steps = 0
        stack = [(self.solved_grid, 0, 0)]
        while stack:
            grid, row, col = stack.pop()
            self.steps += 1
            if row == 9:
                self.solved_grid = grid
                return self.solved_grid, self.steps
            if col == 9:
                stack.append((grid, row + 1, 0))
                continue
            if grid[row][col] != 0:
                stack.append((grid, row, col + 1))
                continue
            for num in range(1, 10):
                if BacktrackingSolver(grid)._is_valid(row, col, num):
                    new_grid = copy.deepcopy(grid)
                    new_grid[row][col] = num
                    stack.append((new_grid, row, col + 1))
        return self.solved_grid, self.steps

class BFSSolver(SolverBase):
    def solve(self):
        self.solved_grid = copy.deepcopy(self.grid)
        self.steps = 0
        queue = deque([(self.solved_grid, 0, 0)])
        while queue:
            grid, row, col = queue.popleft()
            self.steps += 1
            if row == 9:
                self.solved_grid = grid
                return self.solved_grid, self.steps
            if col == 9:
                queue.append((grid, row + 1, 0))
                continue
            if grid[row][col] != 0:
                queue.append((grid, row, col + 1))
                continue
            for num in range(1, 10):
                if BacktrackingSolver(grid)._is_valid(row, col, num):
                    new_grid = copy.deepcopy(grid)
                    new_grid[row][col] = num
                    queue.append((new_grid, row, col + 1))
        return self.solved_grid, self.steps

class InstrumentedBacktrackingSolver:
    def __init__(self, grid, ui_callback=None):
        self.grid = [row[:] for row in grid]
        self.visited_cells = [[0]*9 for _ in range(9)]
        self.path_history = []
        self.steps_taken = 0
        self.backtracks = 0
        self.ui_callback = ui_callback  # function to call after each step

    def solve(self):
        self._backtrack(0, 0)
        return self.grid

    def _backtrack(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return self._backtrack(row + 1, 0)
        if self.grid[row][col] != 0:
            return self._backtrack(row, col + 1)
        for num in range(1, 10):
            if self._is_valid(row, col, num):
                self.grid[row][col] = num
                self.visited_cells[row][col] += 1
                self.path_history.append((row, col))
                self.steps_taken += 1
                if self.ui_callback:
                    self.ui_callback(row, col, self)
                if self._backtrack(row, col + 1):
                    return True
                self.grid[row][col] = 0
                self.backtracks += 1
        return False

    def _is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True