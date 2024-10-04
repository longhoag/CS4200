import tkinter as tk
from tkinter import messagebox
import random

# Function to check if the current position is safe for placing the queen
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve the 8-Queens problem
def solve_nqueens(board, col):
    if col >= len(board):
        return True

    rows = list(range(len(board)))
    random.shuffle(rows)  # Shuffle rows to get different solutions

    for i in rows:
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens(board, col + 1):
                return True
            board[i][col] = 0

    return False

# Function to visualize the board
def show_solution(board):
    canvas.delete("all")  # Clear the previous solution
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                canvas.create_rectangle(j*50, i*50, j*50+50, i*50+50, fill="red")
            else:
                color = "white" if (i+j) % 2 == 0 else "black"
                canvas.create_rectangle(j*50, i*50, j*50+50, i*50+50, fill=color)

# Button click event to solve the problem
def solve():
    board = [[0]*8 for _ in range(8)]
    if solve_nqueens(board, 0):
        show_solution(board)
    else:
        messagebox.showinfo("No solution", "No solution exists")

# Setting up the GUI window
root = tk.Tk()
root.title("8 Queens Problem")

# Creating a canvas to display the chessboard
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Solve button
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.pack()

root.mainloop()