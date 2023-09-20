import random
import tkinter as tk
from tkinter import messagebox

def generate_random_number():
    try:
        min_range = int(min_entry.get())
        max_range = int(max_entry.get())
        if min_range >= max_range:
            messagebox.showerror("Error", "Invalid range. The minimum number should be less than the maximum number.")
            return

        random_number = random.randint(min_range, max_range)
        result_label.config(text=f"Random number between {min_range} and {max_range}: {random_number}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")

# Create and configure GUI elements
min_label = tk.Label(root, text="Enter the minimum number:")
min_label.pack()
min_entry = tk.Entry(root)
min_entry.pack()

max_label = tk.Label(root, text="Enter the maximum number:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.pack()

generate_button = tk.Button(root, text="Generate Random Number", command=generate_random_number)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
