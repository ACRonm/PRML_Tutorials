import tkinter as tk

# Define global variables
expression = ""

# Define functions to handle button clicks


def press(number):
    global expression
    expression += number
    input_field.delete(0, tk.END)
    input_field.insert(0, expression)


def clear():
    global expression
    expression = ""
    input_field.delete(0, tk.END)


def equal():
    global expression
    try:
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Invalid expression")


# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the input field
input_field = tk.Entry(window, width=30)
input_field.grid(row=0, column=0, columnspan=4)

# Create the buttons
btn_1 = tk.Button(window, text="1", command=lambda: press("1"))
btn_2 = tk.Button(window, text="2", command=lambda: press("2"))
btn_3 = tk.Button(window, text="3", command=lambda: press("3"))
btn_4 = tk.Button(window, text="4", command=lambda: press("4"))
btn_5 = tk.Button(window, text="5", command=lambda: press("5"))
btn_6 = tk.Button(window, text="6", command=lambda: press("6"))
btn_7 = tk.Button(window, text="7", command=lambda: press("7"))
btn_8 = tk.Button(window, text="8", command=lambda: press("8"))
btn_9 = tk.Button(window, text="9", command=lambda: press("9"))
btn_0 = tk.Button(window, text="0", command=lambda: press("0"))
btn_clear = tk.Button(window, text="Clear", command=clear)
btn_equal = tk.Button(window, text="=", command=equal)

# Add the buttons to the grid
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)
btn_0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)

# Start the main loop
window.mainloop()
