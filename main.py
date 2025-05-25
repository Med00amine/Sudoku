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

    # Load images for buttons (make them bigger)
    start_img = Image.open("start.png")
    start_img = start_img.resize((80, 80), Image.LANCZOS)
    start_photo = ImageTk.PhotoImage(start_img)

    exit_img = Image.open("exit.png")
    exit_img = exit_img.resize((80, 80), Image.LANCZOS)
    exit_photo = ImageTk.PhotoImage(exit_img)

    # Start button (image only, bigger)
    start_btn = tk.Button(
        menu,
        image=start_photo,
        borderwidth=0,
        highlightthickness=0,
        bg="#d9f2fa",
        activebackground="#e0e0e0",
        command=lambda: [menu.destroy(), show_dashboard()],
        cursor="hand2",
        width=90,  # slightly bigger than image
        height=90
    )
    start_btn.image = start_photo  # Prevent garbage collection
    start_btn.pack(pady=15)

    # Exit button (image only, bigger)
    exit_btn = tk.Button(
        menu,
        image=exit_photo,
        borderwidth=0,
        highlightthickness=0,
        bg="#d9f2fa",
        activebackground="#e0e0e0",
        command=menu.destroy,
        cursor="hand2",
        width=90,
        height=90
    )
    exit_btn.image = exit_photo  # Prevent garbage collection
    exit_btn.pack(pady=15)

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
    window_height = 680  # height
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    icon = ImageTk.PhotoImage(Image.open("sudoku_icon.png"))
    root.iconphoto(True, icon)

    # Back to Menu button (top-right) with ONLY retour.png as the button
    router_img = Image.open("retour.png")
    router_img = router_img.resize((32, 32), Image.LANCZOS)
    router_photo = ImageTk.PhotoImage(router_img)

    def on_enter(e):
        back_btn.config(bg="#e0e0e0")  # Light hover effect

    def on_leave(e):
        back_btn.config(bg="#d9f2fa")  # Match dashboard bg

    back_btn = tk.Button(
        root,
        image=router_photo,
        bg="#d9f2fa",  # Match dashboard background
        activebackground="#e0e0e0",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [root.destroy(), show_menu()],
        cursor="hand2"
    )
    back_btn.image = router_photo  # Prevent garbage collection
    back_btn.place(x=window_width-50, y=20, width=40, height=40)
    back_btn.bind("<Enter>", on_enter)
    back_btn.bind("<Leave>", on_leave)

    tk.Label(root, text="Sudoku Solver", font=("Arial", 24, "bold"), bg="#d9f2fa", fg="#333").pack(pady=10)

    # Timer label
    timer_label = tk.Label(root, text="Time: 00:00", font=("Arial", 14), bg="#d9f2fa", fg="#333")
    timer_label.pack(pady=5)
    timer_running = [False]
    start_time = [None]

    def update_timer():
        if timer_running[0]:
            elapsed = int(time.time() - start_time[0])
            mins, secs = divmod(elapsed, 60)
            timer_label.config(text=f"Time: {mins:02d}:{secs:02d}")
            root.after(1000, update_timer)

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
            if not timer_running[0]:
                timer_running[0] = True
                start_time[0] = time.time()
                update_timer()
            if event.char in "123456789":
                correct = (int(event.char) == solution_grid[i][j])
                color = "green" if correct else "red"
                grid_labels[i][j].config(text=event.char, fg=color)
                user_entries[i][j] = True
                if check_win():
                    timer_running[0] = False
                    messagebox.showinfo("Congratulations!", f"You are a winner!\nTime: {timer_label.cget('text')[6:]}")
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

    # Difficulty dropdown + Solver buttons
    difficulty_frame = tk.Frame(root, bg="#d9f2fa")
    difficulty_frame.pack(pady=5)

    tk.Label(difficulty_frame, text="Difficulty:", bg="#d9f2fa", fg="#333").pack(side="left")
    difficulty_var = tk.StringVar(value=current_difficulty)
    difficulty_menu = tk.OptionMenu(difficulty_frame, difficulty_var, *puzzles.keys(), command=update_difficulty)
    difficulty_menu.config(bg="#4CAF50", fg="white", font=("Arial", 12))
    difficulty_menu.pack(side="left", padx=(0, 10))

    # Solver buttons next to difficulty
    tk.Button(difficulty_frame, text="Run Hill Climbing", font=("Arial", 12), bg="#4CAF50", fg="white", command=run_hill_climbing).pack(side="left", padx=5)
    tk.Button(difficulty_frame, text="Run A* Search", font=("Arial", 12), bg="#2196F3", fg="white", command=run_a_star).pack(side="left", padx=5)

    # Show initial grid
    display_grid(initial_grid, grid_labels)

    root.mainloop()

# Start the application with the menu
show_menu()