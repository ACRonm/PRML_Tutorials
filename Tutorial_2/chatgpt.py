import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the current equation or result
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create and place buttons
for label, row, col in buttons:
    button = tk.Button(root, text=label, padx=20, pady=20, command=lambda label=label: button_click(
        label) if label != "=" else button_equal())
    button.grid(row=row, column=col)

# Create Clear button
clear_button = tk.Button(root, text="C", padx=20,
                         pady=20, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=3)

# Run the GUI event loop
root.mainloop()
