import tkinter as tk
from tkinter import messagebox
import time
from sudoku import *
from informed_solver import hill_climbing
from optimal_solver import a_star
from PIL import Image, ImageTk

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
            value = grid[i][j]
            labels[i][j].config(
                text=str(value) if value != 0 else "",
                fg="black" if value != 0 else "gray"
            )

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

# Menu page
def show_menu():
    menu = tk.Tk()
    menu.title("Sudoku Solver Menu")
    menu.geometry("400x300")
    menu.configure(bg="#d9f2fa")  # Soft pastel blue background

    # Center the window
    menu.update_idletasks()
    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2)  # 400 is the width of the menu
    y = (screen_height // 2) - (300 // 2)  # 300 is the height of the menu
    menu.geometry(f"400x300+{x}+{y}")

    # Load the .png file as an icon
    icon = ImageTk.PhotoImage(Image.open("sudoku_icon.png"))
    menu.iconphoto(True, icon)

    # Title
    tk.Label(menu, text="Welcome to Sudoku Solver", font=("Arial", 18, "bold"), bg="#d9f2fa", fg="#333").pack(pady=20)

    # Buttons
    tk.Button(menu, text="Start", font=("Arial", 14), bg="#4CAF50", fg="white", command=lambda: [menu.destroy(), show_dashboard()]).pack(pady=10)
    tk.Button(menu, text="Exit", font=("Arial", 14), bg="#f44336", fg="white", command=menu.destroy).pack(pady=10)

    menu.mainloop()


# Main Sudoku solver dashboard
def show_dashboard():
    global root, grid_labels, selected_cell, user_entries, solution_grid

    root = tk.Tk()
    root.title("Sudoku Solver Dashboard")
    root.configure(bg="#d9f2fa")

    # Center the window
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 600
    window_height = 700
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    icon = ImageTk.PhotoImage(Image.open("sudoku_icon.png"))
    root.iconphoto(True, icon)

    tk.Label(root, text="Sudoku Solver", font=("Arial", 24, "bold"), bg="#d9f2fa", fg="#333").pack(pady=10)

    wrapper = tk.Frame(root, bg="#ffffff")
    wrapper.pack(pady=20)

    grid_labels = [[None for _ in range(9)] for _ in range(9)]
    user_entries = [[False for _ in range(9)] for _ in range(9)]
    selected_cell = [None, None]

    # Get the solution grid using your a_star solver
    solution_grid, _ = a_star(initial_grid)

    def check_win():
        for i in range(9):
            for j in range(9):
                user_val = grid_labels[i][j].cget("text")
                sol_val = str(solution_grid[i][j])
                if user_val != sol_val:
                    return False
        return True

    def cell_click(event, i, j):
        selected_cell[0], selected_cell[1] = i, j
        for x in range(9):
            for y in range(9):
                grid_labels[x][y].config(bg="#f9f9f9")
        grid_labels[i][j].config(bg="#ffe082")  # Highlight selected cell

    def key_press(event):
        i, j = selected_cell
        if i is not None and j is not None and initial_grid[i][j] == 0:
            if event.char in "123456789":
                correct = (int(event.char) == solution_grid[i][j])
                color = "green" if correct else "red"
                grid_labels[i][j].config(text=event.char, fg=color)
                user_entries[i][j] = True
                if check_win():
                    messagebox.showinfo("Congratulations!", "You are a winner!")
            elif event.keysym in ("BackSpace", "Delete"):
                grid_labels[i][j].config(text="", fg="black")
                user_entries[i][j] = False

    for big_row in range(3):
        for big_col in range(3):
            block = tk.Frame(wrapper, highlightbackground="black", highlightthickness=2, bg="#ffffff")
            block.grid(row=big_row, column=big_col, padx=2, pady=2)
            for i in range(3):
                for j in range(3):
                    row = big_row * 3 + i
                    col = big_col * 3 + j
                    value = initial_grid[row][col]
                    label = tk.Label(block, width=4, height=2, font=("Arial", 16),
                                     borderwidth=1, relief="solid", bg="#f9f9f9",
                                     text=str(value) if value != 0 else "",
                                     fg="black")
                    label.grid(row=i, column=j)
                    label.bind("<Button-1>", lambda e, x=row, y=col: cell_click(e, x, y))
                    grid_labels[row][col] = label

    root.bind("<Key>", key_press)

    # Difficulty dropdown
    difficulty_frame = tk.Frame(root, bg="#d9f2fa")
    difficulty_frame.pack(pady=5)

    tk.Label(difficulty_frame, text="Difficulty:", bg="#d9f2fa", fg="#333").pack(side="left")
    difficulty_var = tk.StringVar(value=current_difficulty)
    difficulty_menu = tk.OptionMenu(difficulty_frame, difficulty_var, *puzzles.keys(), command=update_difficulty)
    difficulty_menu.config(bg="#4CAF50", fg="white", font=("Arial", 12))
    difficulty_menu.pack(side="left")

    # Buttons
    button_frame = tk.Frame(root, bg="#d9f2fa")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Run Hill Climbing", font=("Arial", 12), bg="#4CAF50", fg="white", command=run_hill_climbing).grid(row=0, column=0, padx=20)
    tk.Button(button_frame, text="Run A* Search", font=("Arial", 12), bg="#2196F3", fg="white", command=run_a_star).grid(row=0, column=1, padx=20)

    # Show initial grid
    display_grid(initial_grid, grid_labels)

    # Run app
    root.mainloop()

# Start the application with the menu
show_menu()