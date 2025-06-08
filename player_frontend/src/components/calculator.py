import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")  # Set window title
root.geometry("350x450")  # Set window size
root.configure(bg="#2E2E2E")  # Set background color

# Create an entry field for user input
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify="right", bg="#D3D3D3", bd=8)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Define button functions
def on_button_click(value):
    """Append button value to input field."""
    entry_var.set(entry_var.get() + str(value))

def calculate():
    """Evaluate the expression and display the result."""
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear():
    """Clear the input field."""
    entry_var.set("")

# Button styling
button_bg = "#4A4A4A"
button_fg = "white"
button_font = ("Arial", 18)
button_padx = 20
button_pady = 20

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create buttons dynamically using grid layout
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(root, text=btn_text, font=button_font, bg=button_bg, fg=button_fg, 
                        padx=button_padx, pady=button_pady, relief="raised", bd=5,
                        command=lambda val=btn_text: on_button_click(val) if val not in ['C', '='] else (clear() if val == 'C' else calculate()))
        btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)

# Make buttons expand when window is resized
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()