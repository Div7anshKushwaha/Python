import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()

# Display section
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, justify='right')
entry_field.grid(columnspan=4, ipadx=10, ipady=15)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, command=equal, width=10, height=3)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: press(t), width=10, height=3)

    btn.grid(row=row, column=col)

# Clear button
clear_btn = tk.Button(root, text="Clear", command=clear, width=44, height=2)
clear_btn.grid(row=5, columnspan=4)

root.mainloop()






















