from sudoku import *
from informed_solver import hill_climbing
from optimal_solver import a_star
import time
import tkinter as tk
from tkinter import messagebox

# Difficulty-based Sudoku grids
puzzles = {
    "Easy": [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ],
    "Moderate": [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ],
    "Difficult": [
        [0, 0, 0, 0, 0, 7, 0, 0, 9],
        [0, 3, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 9, 6, 0, 0, 5, 0, 0],
        [0, 0, 5, 3, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 2],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 1, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 3, 0, 0]
    ],
    "Expert": [
        [0, 0, 0, 0, 0, 0, 1, 0, 7],
        [2, 0, 0, 3, 0, 0, 0, 5, 0],
        [0, 6, 1, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 2],
        [0, 0, 5, 0, 0, 0, 3, 0, 0],
        [4, 0, 0, 0, 5, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 3, 8, 0, 1, 0, 0, 0],
        [6, 0, 9, 0, 0, 0, 0, 0, 1]    
    ]
}
# Set default difficulty
current_difficulty = "Easy"
initial_grid = puzzles[current_difficulty]

# Display the grid
def display_grid(grid, labels):
    for i in range(9):
        for j in range(9):
            labels[i][j].config(text=str(grid[i][j]) if grid[i][j] != 0 else "")

# Update grid when difficulty is changed
def update_difficulty(new_difficulty):
    global current_difficulty, initial_grid
    current_difficulty = new_difficulty
    initial_grid = puzzles[new_difficulty]
    display_grid(initial_grid, grid_labels)

# Solver functions
def run_hill_climbing():
    start_time = time.time()
    hc_grid, hc_iterations, hc_conflicts = hill_climbing(initial_grid)
    hc_time = time.time() - start_time
    display_grid(hc_grid, grid_labels)
    messagebox.showinfo("Hill Climbing Result", f"Iterations: {hc_iterations}\nConflicts: {hc_conflicts}\nTime: {hc_time:.2f}s")

def run_a_star():
    start_time = time.time()
    a_star_grid, a_star_iterations = a_star(initial_grid)
    a_star_time = time.time() - start_time
    display_grid(a_star_grid, grid_labels)
    messagebox.showinfo("A* Search Result", f"Iterations: {a_star_iterations}\nTime: {a_star_time:.2f}s")

# GUI setup
root = tk.Tk()
root.title("Sudoku Solver Dashboard")

# Grid wrapper
wrapper = tk.Frame(root)
wrapper.pack(pady=20)

# 9x9 Sudoku grid using 3x3 blocks
grid_labels = [[None for _ in range(9)] for _ in range(9)]
for big_row in range(3):
    for big_col in range(3):
        block = tk.Frame(wrapper, highlightbackground="black", highlightthickness=2)
        block.grid(row=big_row, column=big_col, padx=1, pady=1)
        for i in range(3):
            for j in range(3):
                row = big_row * 3 + i
                col = big_col * 3 + j
                label = tk.Label(block, width=4, height=2, font=("Arial", 16),
                                 borderwidth=1, relief="solid", bg="white")
                label.grid(row=i, column=j)
                grid_labels[row][col] = label

# Difficulty dropdown
difficulty_frame = tk.Frame(root)
difficulty_frame.pack(pady=5)

tk.Label(difficulty_frame, text="Difficulty:").pack(side="left")
difficulty_var = tk.StringVar(value=current_difficulty)
difficulty_menu = tk.OptionMenu(difficulty_frame, difficulty_var, *puzzles.keys(), command=update_difficulty)
difficulty_menu.pack(side="left")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Run Hill Climbing", command=run_hill_climbing).grid(row=0, column=0, padx=20)
tk.Button(button_frame, text="Run A* Search", command=run_a_star).grid(row=0, column=1, padx=20)

# Show initial grid
display_grid(initial_grid, grid_labels)

# Run app
root.mainloop()