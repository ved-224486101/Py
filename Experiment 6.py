import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        product = num1 * num2
        result_label.config(text="Product: " + str(product))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Product Calculator")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window width and height
window_width = 1000
window_height = 600

# Calculate x and y coordinates for the window to appear at the center
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set window position
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Configure rows and columns to expand with window
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create labels and entry fields
num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

# Create calculate button with fancy appearance
calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product, bg="black", fg="red", font=("Arial", 12, "bold"), relief=tk.RAISED, bd=5)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

# Create label to display result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)

# Start the Tkinter event loop
root.mainloop()
