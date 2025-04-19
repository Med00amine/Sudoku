from sudoku import *
from informed_solver import hill_climbing
from optimal_solver import a_star
import time
import tkinter as tk
from tkinter import messagebox

# Function to display the Sudoku grid in the UI
def display_grid(grid, labels):
    for i in range(9):
        for j in range(9):
            value = grid[i][j]
            labels[i][j].config(text=str(value) if value != 0 else "")

# Function to run Hill Climbing and display the result
def run_hill_climbing():
    start_time = time.time()
    hc_grid, hc_iterations, hc_conflicts = hill_climbing(initial_grid)
    hc_time = time.time() - start_time
    display_grid(hc_grid, grid_labels)
    messagebox.showinfo("Hill Climbing Result", 
                        f"Iterations: {hc_iterations}\nConflicts: {hc_conflicts}\nTime: {hc_time:.2f}s")

# Function to run A* Search and display the result
def run_a_star():
    start_time = time.time()
    a_star_grid, a_star_iterations = a_star(initial_grid)
    a_star_time = time.time() - start_time
    display_grid(a_star_grid, grid_labels)
    messagebox.showinfo("A* Search Result", 
                        f"Iterations: {a_star_iterations}\nTime: {a_star_time:.2f}s")

# Initial Sudoku grid
initial_grid = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver Dashboard")


# Wrapper frame to center the whole grid
wrapper = tk.Frame(root)
wrapper.pack(pady=20)

# Sudoku Grid (3x3 blocks of 3x3 labels)
grid_labels = [[None for _ in range(9)] for _ in range(9)]
for big_row in range(3):
    for big_col in range(3):
        block = tk.Frame(wrapper, highlightbackground="black", highlightthickness=2)
        block.grid(row=big_row, column=big_col, padx=1, pady=1)
        for i in range(3):
            for j in range(3):
                row = big_row * 3 + i
                col = big_col * 3 + j
                label = tk.Label(
                    block,
                    width=4,
                    height=2,
                    font=("Arial", 16),
                    borderwidth=1,
                    relief="solid",
                    bg="white"
                )
                label.grid(row=i, column=j)
                grid_labels[row][col] = label

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
display_grid(initial_grid, grid_labels)

hill_climbing_button = tk.Button(button_frame, text="Run Hill Climbing", command=run_hill_climbing)
hill_climbing_button.grid(row=0, column=0, padx=20)

a_star_button = tk.Button(button_frame, text="Run A* Search", command=run_a_star)
a_star_button.grid(row=0, column=1, padx=20)

# Run the Tkinter event loop
root.mainloop()