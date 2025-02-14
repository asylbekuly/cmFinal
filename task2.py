import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Define function and its derivative
def f(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6


def f_prime(x):
    return 3 * x ** 2 - 12 * x + 11


# Bisection method
def bisection(a, b, tol=1e-5):
    iterations = 0
    errors = []
    if f(a) * f(b) > 0:
        return None, iterations, errors
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c, iterations, errors
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
        errors.append(abs(b - a) / abs(c))
    return (a + b) / 2.0, iterations, errors


# Newton-Raphson method
def newton_raphson(x0, tol=1e-5):
    iterations = 0
    errors = []
    while abs(f(x0)) > tol:
        x1 = x0 - f(x0) / f_prime(x0)
        iterations += 1
        errors.append(abs(x1 - x0) / abs(x1))
        x0 = x1
    return x0, iterations, errors


# Function to plot graph
def plot_graph():
    ax.clear()
    x_vals = np.linspace(-1, 4, 400)
    y_vals = f(x_vals)
    ax.plot(x_vals, y_vals, label='f(x) = x³ - 6x² + 11x - 6')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.grid(True)
    ax.legend()
    canvas.draw()


# Function to compute root and errors
def compute_root():
    try:
        method = method_var.get()
        tol = float(entry_tol.get())
        if method == "Bisection":
            a = float(entry_a.get())
            b = float(entry_b.get())
            root, iterations, errors = bisection(a, b, tol)
        elif method == "Newton-Raphson":
            x0 = float(entry_x0.get())
            root, iterations, errors = newton_raphson(x0, tol)

        if root is None:
            result_label.config(text="No root found or invalid interval!")
            return

        # Ensure errors list is not empty before accessing the last element
        if errors:
            result_label.config(text=f"Root: {root:.5f}\nIterations: {iterations}\nFinal Error: {errors[-1]:.5e}")
        else:
            result_label.config(text=f"Root: {root:.5f}\nIterations: {iterations}\nNo Error Data")

        plot_graph()

    except ValueError:
        result_label.config(text="Enter valid numbers!")

# GUI Setup
root = tk.Tk()
root.title("Root-Finding Methods")

frame = tk.Frame(root)
frame.pack()

fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

btn_plot = tk.Button(root, text="Plot Function", command=plot_graph)
btn_plot.pack()

frame_inputs = tk.Frame(root)
frame_inputs.pack()

method_var = tk.StringVar(value="Bisection")

# Dropdown to choose method
method_label = tk.Label(frame_inputs, text="Choose Method:")
method_label.grid(row=0, column=0)
method_dropdown = ttk.Combobox(frame_inputs, textvariable=method_var, values=["Bisection", "Newton-Raphson"])
method_dropdown.grid(row=0, column=1)

# Inputs for Bisection Method
lbl_a = tk.Label(frame_inputs, text="Interval Start (a):")
lbl_a.grid(row=1, column=0)
entry_a = tk.Entry(frame_inputs)
entry_a.grid(row=1, column=1)

lbl_b = tk.Label(frame_inputs, text="Interval End (b):")
lbl_b.grid(row=2, column=0)
entry_b = tk.Entry(frame_inputs)
entry_b.grid(row=2, column=1)

# Inputs for Newton-Raphson Method
lbl_x0 = tk.Label(frame_inputs, text="Initial Guess (x₀):")
lbl_x0.grid(row=3, column=0)
entry_x0 = tk.Entry(frame_inputs)
entry_x0.grid(row=3, column=1)

# Tolerance input
lbl_tol = tk.Label(frame_inputs, text="Tolerance:")
lbl_tol.grid(row=4, column=0)
entry_tol = tk.Entry(frame_inputs)
entry_tol.grid(row=4, column=1)

# Button to compute root
btn_compute = tk.Button(root, text="Find Root & Error", command=compute_root)
btn_compute.pack()

# Result display
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
