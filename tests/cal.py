import tkinter as tk
import math

class Calc:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")

        # Create an entry widget for input
        self.entry = tk.Entry(root, width=20, borderwidth=2)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons for calculator functions
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('AC', 1, 0), ('%', 1, 1), ('/', 1, 2), ('*', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('=', 4, 3),
            ('0', 5, 0), ('.', 5, 1),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2),
            ('log', 7, 0), ('exp', 7, 1), ('sqrt', 7, 2)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(self.root, text=text, command=self.evaluate)
            elif text == 'AC':
                button = tk.Button(self.root, text=text, command=self.clear)
            else:
                button = tk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        current_text = self.entry.get()
        if button_text in ['+', '-', '*', '/']:
            if current_text and current_text[-1] in ['+', '-', '*', '/']:
                current_text = current_text[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text + button_text)
        elif button_text in ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt']:
            self.entry.insert(tk.END, button_text + '(')
        else:
            self.entry.insert(tk.END, button_text)

    def evaluate(self):
        try:
            expression = self.entry.get()
            expression = expression.replace('%', '/100')  # Convert percentage to decimal
            # Handle trigonometric functions and log
            expression = expression.replace('sin(', 'math.sin(math.radians(')
            expression = expression.replace('cos(', 'math.cos(math.radians(')
            expression = expression.replace('tan(', 'math.tan(math.radians(')
            expression = expression.replace('log(', 'math.log10(')
            expression = expression.replace('exp(', 'math.exp(')
            expression = expression.replace('sqrt(', 'math.sqrt(')
            expression += ')'
            result = eval(expression, {"math": math})
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Create the calculator instance
calc = Calc(root)

# Run the application
root.mainloop()
