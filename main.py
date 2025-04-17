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

# Create a grid of labels for displaying the Sudoku grid
grid_labels = [[tk.Label(root, width=2, height=1, font=("Arial", 18), borderwidth=1, relief="solid") 
                for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        grid_labels[i][j].grid(row=i, column=j)

# Display the initial grid
display_grid(initial_grid, grid_labels)

# Add buttons for selecting the solving method
hill_climbing_button = tk.Button(root, text="Run Hill Climbing", command=run_hill_climbing)
hill_climbing_button.grid(row=10, column=0, columnspan=4, pady=10)

a_star_button = tk.Button(root, text="Run A* Search", command=run_a_star)
a_star_button.grid(row=10, column=5, columnspan=4, pady=10)

# Run the Tkinter event loop
root.mainloop()