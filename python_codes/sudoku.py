import tkinter as tk
from tkinter import messagebox
import random

# Sudoku Solver and Generator

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def sudoku_solver(board):
    empty = find_empty_location(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if sudoku_solver(board):
                return True
            board[row][col] = 0

    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku():
    base = 3
    side = base * base
    def pattern(r, c): return (base * (r % base) + r // base + c) % side
    def shuffle(s): return random.sample(s, len(s)) 
    rBase = range(base)
    rows  = [ g * base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
    cols  = [ g * base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1, base * base + 1))
    board = [ [nums[pattern(r, c)] for c in cols] for r in rows ]
    squares = base * base
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0
    return board

def check_solution(board):
    for i in range(9):
        if len(set(board[i])) != 9 or len(set(row[i] for row in board)) != 9:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = set(board[i+x][j+y] for x in range(3) for y in range(3))
            if len(block) != 9:
                return False

    return True

# GUI Code

class SudokuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku")
        self.geometry("300x300")
        self.board = generate_sudoku()
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                e = tk.Entry(self, width=2, font=('Arial', 16), justify='center')
                e.grid(row=i, column=j, padx=5, pady=5)
                if self.board[i][j] != 0:
                    e.insert(tk.END, str(self.board[i][j]))
                    e.config(state='disabled')
                self.entries[i][j] = e

        solve_button = tk.Button(self, text="Check", command=self.check_solution)
        solve_button.grid(row=10, column=0, columnspan=9)

    def get_board(self):
        return [[int(self.entries[i][j].get() or 0) for j in range(9)] for i in range(9)]

    def check_solution(self):
        board = self.get_board()
        if check_solution(board):
            messagebox.showinfo("Solution", "Congratulations! The solution is correct.")
        else:
            messagebox.showerror("Error", "The solution is incorrect. Try again.")

if __name__ == "__main__":
    app = SudokuApp()
    app.mainloop()


"""
Sudoku - Fill a 9x9 grid so that each column, row, and 3x3 subgrid contains all numbers from 1 to 9. give code as major project using jango
ChatGPT said:
ChatGPT
To create a Sudoku game with Django, you'll build a web application that allows users to interact with a Sudoku puzzle. This project will involve:

Setting up a Django project.
Creating a Sudoku app with views, models, and templates.
Implementing Sudoku puzzle generation, validation, and solving.
Displaying the Sudoku puzzle and handling user input through web forms.
Here's a step-by-step guide to create a Sudoku game using Django:

Step 1: Set Up Your Django Project
Install Django:

If you haven't installed Django yet, do so with pip:

bash
Copy code
pip install django
Create a New Django Project:

bash
Copy code
django-admin startproject sudoku_project
cd sudoku_project
Create a New Django App:

bash
Copy code
python manage.py startapp sudoku
Add the App to INSTALLED_APPS:

Open sudoku_project/settings.py and add 'sudoku' to the INSTALLED_APPS list:

python
Copy code
INSTALLED_APPS = [
    # other apps
    'sudoku',
]
Step 2: Define Sudoku Logic
Create a file sudoku/utils.py for Sudoku logic, including generating and validating puzzles:

python
Copy code
import random

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def sudoku_solver(board):
    empty = find_empty_location(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if sudoku_solver(board):
                return True
            board[row][col] = 0

    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku():
    base = 3
    side = base * base
    def pattern(r, c): return (base * (r % base) + r // base + c) % side
    def shuffle(s): return random.sample(s, len(s))
    rBase = range(base)
    rows  = [ g * base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
    cols  = [ g * base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1, base * base + 1))
    board = [ [nums[pattern(r, c)] for c in cols] for r in rows ]
    squares = base * base
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0
    return board

def check_solution(board):
    for i in range(9):
        if len(set(board[i])) != 9 or len(set(row[i] for row in board)) != 9:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = set(board[i+x][j+y] for x in range(3) for y in range(3))
            if len(block) != 9:
                return False

    return True
Step 3: Create Models
In sudoku/models.py, create a model to store the Sudoku board if needed. For simplicity, we can manage the puzzle in-memory in this example, but you could add a model if you want to store puzzles in the database.

Step 4: Create Views
In sudoku/views.py, define views to handle displaying and solving the Sudoku puzzle:

python
Copy code
from django.shortcuts import render, redirect
from .utils import generate_sudoku, sudoku_solver, check_solution

def index(request):
    if 'board' not in request.session:
        request.session['board'] = generate_sudoku()
    
    board = request.session.get('board')
    
    if request.method == 'POST':
        for i in range(9):
            for j in range(9):
                value = request.POST.get(f'cell-{i}-{j}')
                if value:
                    board[i][j] = int(value)
        
        if check_solution(board):
            message = "Congratulations! The solution is correct."
        else:
            message = "The solution is incorrect. Try again."

        request.session['board'] = board
    
    return render(request, 'sudoku/index.html', {'board': request.session.get('board'), 'message': message if 'message' in locals() else ''})
Step 5: Set Up URLs
Create sudoku/urls.py:

python
Copy code
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
Include this in the main project’s urls.py (sudoku_project/urls.py):

python
Copy code
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sudoku.urls')),
]
Step 6: Create Templates
Create a template file sudoku/templates/sudoku/index.html:

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sudoku</title>
    <style>
        table { border-collapse: collapse; }
        td { width: 30px; height: 30px; text-align: center; }
        input { width: 100%; height: 100%; text-align: center; }
        .highlight { background-color: #f0f0f0; }
    </style>
</head>
<body>
    <h1>Sudoku</h1>
    <form method="post">
        {% csrf_token %}
        <table border="1">
            {% for i in 0|range:9 %}
                <tr>
                    {% for j in 0|range:9 %}
                        <td>
                            <input type="text" name="cell-{{ i }}-{{ j }}" 
                                   value="{{ board.i.j|default_if_none:'' }}" 
                                   {% if board.i.j %}readonly{% endif %} />
                        </td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </table>
        <button type="submit">Check Solution</button>
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
Step 7: Run Your Django Server
Apply Migrations:

bash
Copy code
python manage.py migrate
Run the Server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to interact with the Sudoku puzzle.

This Django application allows users to view a Sudoku puzzle, fill in their answers, and check if the solution is correct. It provides a basic foundation, and you can extend it by adding features like puzzle generation, user authentication, or saving and loading puzzles from a database.
"""