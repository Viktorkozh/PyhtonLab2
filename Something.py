import random
import tkinter as tk
from tkinter import messagebox

def generate_random_numbers():
    try:
        min_range = int(min_entry.get())
        max_range = int(max_entry.get())
        num_of_numbers = int(num_entry.get())
        if min_range >= max_range:
            messagebox.showerror("Error", "Invalid range. The minimum number should be less than the maximum number.")
            return

        random_numbers = [random.randint(min_range, max_range) for _ in range(num_of_numbers)]
        result_label.config(text=f"Random numbers between {min_range} and {max_range}: {random_numbers}")
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

num_label = tk.Label(root, text="Enter the number of random numbers to generate:")
num_label.pack()
num_entry = tk.Entry(root)
num_entry.pack()

generate_button = tk.Button(root, text="Generate Random Numbers", command=generate_random_numbers)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
