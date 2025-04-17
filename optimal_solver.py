import heapq
from sudoku import *

def heuristic(grid):
    return sum(row.count(0) for row in grid)

def generate_successors(grid):
    successors = []
    empty = find_empty(grid)
    if empty is None:
        return successors
    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            new_grid = copy.deepcopy(grid)
            new_grid[row][col] = num
            successors.append(new_grid)
    return successors

def is_complete(grid):
    return all(all(cell != 0 for cell in row) for row in grid)

def a_star(start_grid):
    frontier = [(heuristic(start_grid), 0, start_grid)]
    iterations = 0
    while frontier:
        _, cost, current = heapq.heappop(frontier)
        if is_complete(current):
            return current, iterations
        for successor in generate_successors(current):
            heapq.heappush(frontier, (cost + heuristic(successor), cost + 1, successor))
        iterations += 1
    return start_grid, iterations
