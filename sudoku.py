# sudoku.py
import copy

GRID_SIZE = 9
SUBGRID_SIZE = 3

def is_valid(grid, row, col, num):
    for i in range(GRID_SIZE):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row = row - row % SUBGRID_SIZE
    start_col = col - col % SUBGRID_SIZE
    for i in range(SUBGRID_SIZE):
        for j in range(SUBGRID_SIZE):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return (i, j)
    return None

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()