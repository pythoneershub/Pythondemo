import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create a tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Create a display widget
display = tk.Entry(root, width=20, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 15),
                       command=lambda text=text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 15),
                         command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Equal button
equal_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 15),
                         command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Run the main loop
root.mainloop()


