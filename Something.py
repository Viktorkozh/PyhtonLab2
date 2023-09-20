import random
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics

def generate_random_numbers():
    try:
        min_range = float(min_entry.get())
        max_range = float(max_entry.get())
        num_of_numbers = int(num_entry.get())
        data_type = data_type_var.get()

        if min_range >= max_range:
            messagebox.showerror("Error", "Invalid range. The minimum number should be less than the maximum number.")
            return

        if data_type == "Integer":
            random_numbers = [random.randint(int(min_range), int(max_range)) for _ in range(num_of_numbers)]
        else:
            random_numbers = [random.uniform(min_range, max_range) for _ in range(num_of_numbers)]

        result_label.config(text=f"Random {data_type} numbers between {min_range} and {max_range}: {random_numbers}")

        save_to_file(random_numbers)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def save_to_file(numbers):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt")],
                                            title="Save Random Numbers",
                                            initialfile="random_numbers.txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(",".join(map(str, numbers)))
            messagebox.showinfo("Info", f"Random numbers saved to {file_path}")

def plot_histogram():
    try:
        min_range = float(min_entry.get())
        max_range = float(max_entry.get())
        num_of_numbers = int(num_entry.get())
        data_type = data_type_var.get()

        if min_range >= max_range:
            messagebox.showerror("Error", "Invalid range. The minimum number should be less than the maximum number.")
            return

        if data_type == "Integer":
            random_numbers = [random.randint(int(min_range), int(max_range)) for _ in range(num_of_numbers)]
        else:
            random_numbers = [random.uniform(min_range, max_range) for _ in range(num_of_numbers)]

        plt.figure()
        plt.hist(random_numbers, bins=20, color='blue', edgecolor='black')
        plt.xlabel(f'Random {data_type} Numbers')
        plt.ylabel('Frequency')
        plt.title(f'Random {data_type} Number Histogram ({num_of_numbers} samples)')
        plt.grid(True)

        canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def calculate_statistics():
    try:
        min_range = float(min_entry.get())
        max_range = float(max_entry.get())
        num_of_numbers = int(num_entry.get())
        data_type = data_type_var.get()

        if min_range >= max_range:
            messagebox.showerror("Error", "Invalid range. The minimum number should be less than the maximum number.")
            return

        if data_type == "Integer":
            random_numbers = [random.randint(int(min_range), int(max_range)) for _ in range(num_of_numbers)]
        else:
            random_numbers = [random.uniform(min_range, max_range) for _ in range(num_of_numbers)]

        mean = statistics.mean(random_numbers)
        median = statistics.median(random_numbers)
        stdev = statistics.stdev(random_numbers)

        messagebox.showinfo("Statistics", f"Mean: {mean}\nMedian: {median}\nStandard Deviation: {stdev}")

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

data_type_var = tk.StringVar()
data_type_var.set("Integer")  # Default choice
data_type_label = tk.Label(root, text="Select data type:")
data_type_label.pack()

integer_radio = tk.Radiobutton(root, text="Integer", variable=data_type_var, value="Integer")
integer_radio.pack()

float_radio = tk.Radiobutton(root, text="Float", variable=data_type_var, value="Float")
float_radio.pack()

generate_button = tk.Button(root, text="Generate Random Numbers", command=generate_random_numbers)
generate_button.pack()

plot_button = tk.Button(root, text="Plot Histogram", command=plot_histogram)
plot_button.pack()

statistics_button = tk.Button(root, text="Calculate Statistics", command=calculate_statistics)
statistics_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
