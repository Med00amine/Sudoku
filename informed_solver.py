import random
from sudoku import *

def count_conflicts(grid):
    conflicts = 0
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = grid[row][col]
            if num != 0:
                grid[row][col] = 0
                if(is_valid(grid, row, col, num))==False:
                    conflicts += 1
                grid[row][col] = num
    return conflicts

def fill_grid_randomly(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(GRID_SIZE):
        used = [num for num in new_grid[i] if num != 0]
        options = [num for num in range(1, 10) if num not in used]
        for j in range(GRID_SIZE):
            if new_grid[i][j] == 0:
                new_grid[i][j] = options.pop(random.randint(0, len(options) - 1))
    return new_grid

def generate_neighbor(grid):
    neighbor = copy.deepcopy(grid)
    row = random.randint(0, GRID_SIZE - 1)
    col1, col2 = random.sample(range(GRID_SIZE), 2)
    neighbor[row][col1], neighbor[row][col2] = neighbor[row][col2], neighbor[row][col1]
    return neighbor

def hill_climbing(start_grid, max_iterations=1000):
    current = fill_grid_randomly(start_grid)
    current_conflicts = count_conflicts(current)
    iterations = 0
    while iterations < max_iterations and current_conflicts > 0:
        neighbor = generate_neighbor(current)
        neighbor_conflicts = count_conflicts(neighbor)
        if neighbor_conflicts < current_conflicts:
            current = neighbor
            current_conflicts = neighbor_conflicts
        iterations += 1
    return current, iterations, current_conflicts