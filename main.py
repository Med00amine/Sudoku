import tkinter as tk
from tkinter import messagebox, simpledialog
import time
from sudoku import *
from informed_solver import hill_climbing
from optimal_solver import a_star
from PIL import Image, ImageTk
from solvers import BacktrackingSolver, DFSSolver, BFSSolver

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
    menu.geometry("400x350")
    menu.configure(bg="#d9f2fa")

    # Center the window
    menu.update_idletasks()
    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2)
    y = (screen_height // 2) - (350 // 2)
    menu.geometry(f"400x350+{x}+{y}")

    icon = ImageTk.PhotoImage(Image.open("sudoku_icon.png"))
    menu.iconphoto(True, icon)

    tk.Label(menu, text="Welcome to Sudoku Solver", font=("Arial", 18, "bold"), bg="#d9f2fa", fg="#333").pack(pady=20)

    # Load images for buttons (bigger)
    start_img = Image.open("start.png").resize((90, 90), Image.LANCZOS)
    start_photo = ImageTk.PhotoImage(start_img)
    exit_img = Image.open("exit.png").resize((90, 90), Image.LANCZOS)
    exit_photo = ImageTk.PhotoImage(exit_img)

    # Frame for buttons, centered
    btn_frame = tk.Frame(menu, bg="#d9f2fa")
    btn_frame.pack(pady=10)

    start_btn = tk.Button(
        btn_frame,
        image=start_photo,
        borderwidth=0,
        highlightthickness=0,
        bg="#d9f2fa",
        activebackground="#e0e0e0",
        command=lambda: [menu.destroy(), show_dashboard()],
        cursor="hand2",
        width=90,
        height=90
    )
    start_btn.image = start_photo
    start_btn.grid(row=0, column=0, padx=20)

    exit_btn = tk.Button(
        btn_frame,
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
    exit_btn.image = exit_photo
    exit_btn.grid(row=0, column=1, padx=20)

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
    window_height = 650
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    icon = ImageTk.PhotoImage(Image.open("sudoku_icon.png"))
    root.iconphoto(True, icon)

    # Back to Menu button (top-left) with ONLY retour.png as the button
    router_img = Image.open("retour.png").resize((32, 32), Image.LANCZOS)
    router_photo = ImageTk.PhotoImage(router_img)

    def on_enter(e):
        back_btn.config(bg="#e0e0e0")

    def on_leave(e):
        back_btn.config(bg="#d9f2fa")

    back_btn = tk.Button(
        root,
        image=router_photo,
        bg="#d9f2fa",
        activebackground="#e0e0e0",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [root.destroy(), show_menu()],
        cursor="hand2"
    )
    back_btn.image = router_photo
    back_btn.place(x=10, y=10, width=40, height=40)
    back_btn.bind("<Enter>", on_enter)
    back_btn.bind("<Leave>", on_leave)

    tk.Label(root, text="Sudoku Solver", font=("Arial", 24, "bold"), bg="#d9f2fa", fg="#333").pack(pady=(10, 0))

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

    # Difficulty + Algorithm + Solver buttons in one frame
    top_frame = tk.Frame(root, bg="#d9f2fa")
    top_frame.pack(pady=5)

    tk.Label(top_frame, text="Difficulty:", bg="#d9f2fa", fg="#333").pack(side="left")
    difficulty_var = tk.StringVar(value=current_difficulty)
    difficulty_menu = tk.OptionMenu(top_frame, difficulty_var, *puzzles.keys(), command=update_difficulty)
    difficulty_menu.config(font=("Arial", 12))
    difficulty_menu.pack(side="left", padx=(0, 10))

    tk.Label(top_frame, text="Algorithm:", bg="#d9f2fa", fg="#333").pack(side="left")
    algo_var = tk.StringVar(value="Backtracking")
    algo_menu = tk.OptionMenu(top_frame, algo_var, "Backtracking", "DFS", "BFS", "A*", "Hill Climbing")
    algo_menu.config(font=("Arial", 12))
    algo_menu.pack(side="left", padx=5)

    def run_selected_solver():
        algo = algo_var.get()
        start = time.time()
        if algo == "Backtracking" or algo == "DFS":
            solver = BacktrackingSolver(initial_grid)
            grid, steps = solver.solve()
            elapsed = time.time() - start
            display_grid(grid, grid_labels)
            messagebox.showinfo(
                f"{algo} Result",
                f"Iterations: {steps}\nConflicts: N/A\nTime: {elapsed:.2f}s"
            )
        elif algo == "BFS":
            messagebox.showwarning(
                "BFS Not Supported",
                "BFS is not practical for Sudoku and is disabled to prevent freezing."
            )
        elif algo == "A*":
            grid, steps = a_star(initial_grid)
            elapsed = time.time() - start
            display_grid(grid, grid_labels)
            messagebox.showinfo(
                "A* Result",
                f"Iterations: {steps}\nConflicts: N/A\nTime: {elapsed:.2f}s"
            )
        elif algo == "Hill Climbing":
            grid, steps, conflicts = hill_climbing(initial_grid)
            elapsed = time.time() - start
            display_grid(grid, grid_labels)
            messagebox.showinfo(
                "Hill Climbing Result",
                f"Iterations: {steps}\nConflicts: {conflicts}\nTime: {elapsed:.2f}s"
            )

    tk.Button(top_frame, text="Solve", font=("Arial", 12), command=run_selected_solver).pack(side="left", padx=10)

    # Sudoku grid
    wrapper = tk.Frame(root, bg="#ffffff")
    wrapper.pack(pady=10)

    grid_labels = [[None for _ in range(9)] for _ in range(9)]
    user_entries = [[False for _ in range(9)] for _ in range(9)]
    pencil_marks = [[set() for _ in range(9)] for _ in range(9)]  # For pencil marks
    selected_cell = [None, None]
    move_stack = []  # For undo/redo
    redo_stack = []

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

    def highlight_related(i, j):
        for x in range(9):
            for y in range(9):
                grid_labels[x][y].config(bg="#f9f9f9")
        for k in range(9):
            grid_labels[i][k].config(bg="#e3f2fd")  # Row
            grid_labels[k][j].config(bg="#e3f2fd")  # Col
        block_row, block_col = i//3, j//3
        for x in range(block_row*3, block_row*3+3):
            for y in range(block_col*3, block_col*3+3):
                grid_labels[x][y].config(bg="#bbdefb")
        grid_labels[i][j].config(bg="#ffe082")  # Selected cell

    def cell_click(event, i, j):
        selected_cell[0], selected_cell[1] = i, j
        highlight_related(i, j)

    def update_pencil_marks(i, j):
        label = grid_labels[i][j]
        if pencil_marks[i][j]:
            label.config(text="\n".join(sorted(str(n) for n in pencil_marks[i][j])), fg="#888", font=("Arial", 8))
        else:
            label.config(text="", fg="black", font=("Arial", 16))

    def key_press(event):
        i, j = selected_cell
        if i is not None and j is not None and initial_grid[i][j] == 0:
            if not timer_running[0]:
                timer_running[0] = True
                start_time[0] = time.time()
                update_timer()
            if event.char in "123456789":
                prev = grid_labels[i][j].cget("text")
                move_stack.append((i, j, prev, set(pencil_marks[i][j])))
                redo_stack.clear()
                correct = (int(event.char) == solution_grid[i][j])
                color = "green" if correct else "red"
                grid_labels[i][j].config(text=event.char, fg=color, font=("Arial", 16))
                pencil_marks[i][j].clear()
                user_entries[i][j] = True
                if check_win():
                    timer_running[0] = False
                    for x in range(9):
                        for y in range(9):
                            grid_labels[x][y].config(bg="#c8e6c9")
                    messagebox.showinfo("Congratulations!", f"You are a winner!\nTime: {timer_label.cget('text')[6:]}")
            elif event.char == "p":  # Pencil mode
                num = simpledialog.askstring("Pencil Mark", "Enter number(s) 1-9 (comma separated):")
                if num:
                    prev = set(pencil_marks[i][j])
                    move_stack.append((i, j, grid_labels[i][j].cget("text"), prev))
                    redo_stack.clear()
                    pencil_marks[i][j] = set(n for n in num if n in "123456789")
                    update_pencil_marks(i, j)
            elif event.keysym in ("BackSpace", "Delete"):
                prev = grid_labels[i][j].cget("text")
                move_stack.append((i, j, prev, set(pencil_marks[i][j])))
                redo_stack.clear()
                grid_labels[i][j].config(text="", fg="black", font=("Arial", 16))
                pencil_marks[i][j].clear()
                user_entries[i][j] = False
                update_pencil_marks(i, j)

    def undo():
        if move_stack:
            i, j, prev_text, prev_pencil = move_stack.pop()
            redo_stack.append((i, j, grid_labels[i][j].cget("text"), set(pencil_marks[i][j])))
            grid_labels[i][j].config(text=prev_text, fg="black", font=("Arial", 16))
            pencil_marks[i][j] = set(prev_pencil)
            update_pencil_marks(i, j)

    def redo():
        if redo_stack:
            i, j, next_text, next_pencil = redo_stack.pop()
            move_stack.append((i, j, grid_labels[i][j].cget("text"), set(pencil_marks[i][j])))
            grid_labels[i][j].config(text=next_text, fg="black", font=("Arial", 16))
            pencil_marks[i][j] = set(next_pencil)
            update_pencil_marks(i, j)

    def clear_board():
        for i in range(9):
            for j in range(9):
                if initial_grid[i][j] == 0:
                    grid_labels[i][j].config(text="", fg="black", font=("Arial", 16))
                    pencil_marks[i][j].clear()
                    update_pencil_marks(i, j)
        move_stack.clear()
        redo_stack.clear()
        timer_running[0] = False
        timer_label.config(text="Time: 00:00")

    # Add control buttons
    control_frame = tk.Frame(root, bg="#d9f2fa")
    control_frame.pack(pady=5)
    tk.Button(control_frame, text="Undo", command=undo, font=("Arial", 12)).pack(side="left", padx=5)
    tk.Button(control_frame, text="Redo", command=redo, font=("Arial", 12)).pack(side="left", padx=5)
    tk.Button(control_frame, text="Clear", command=clear_board, font=("Arial", 12)).pack(side="left", padx=5)
    tk.Button(control_frame, text="Pause/Resume", font=("Arial", 12), command=lambda: [timer_running.__setitem__(0, not timer_running[0]), update_timer() if timer_running[0] else None]).pack(side="left", padx=5)

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
    display_grid(initial_grid, grid_labels)
    root.mainloop()

def update_ui(row, col, solver):
    # Color gradient for visited frequency
    freq = solver.visited_cells[row][col]
    blue = min(255, 50 + freq * 20)
    color = f'#{"%02x"%0}{"%02x"%0}{"%02x"%blue}'
    grid_labels[row][col].config(bg=color)
    # Highlight current cell
    grid_labels[row][col].config(relief="solid", bd=2)
    root.update()
    time.sleep(0.03)  # Control speed (replace with Tk.after for non-blocking)

# Start the application with the menu
show_menu()