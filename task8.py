import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


# Simpson's 1/3 Rule Function
def simpsons_1_3(func, a, b, n):
    if n % 2 != 0:  # Ensure n is even
        raise ValueError("n must be even")

    h = (b - a) / n
    result = func(a) + func(b)

    # Odd-indexed terms (multiplied by 4)
    for i in range(1, n, 2):
        result += 4 * func(a + i * h)

    # Even-indexed terms (multiplied by 2)
    for i in range(2, n, 2):
        result += 2 * func(a + i * h)

    result *= h / 3
    return result


# Exact integral value for comparison (∫0^π sin(x) dx = 2)
def exact_integral():
    return 2


# Function to plot the graph of sin(x)
def plot_graph():
    x_vals = np.linspace(0, np.pi, 400)
    y_vals = np.sin(x_vals)

    plt.plot(x_vals, y_vals, label="f(x) = sin(x)")
    plt.fill_between(x_vals, y_vals, alpha=0.3)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.legend()
    plt.title("Graph of sin(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()


# Function to execute the calculation and display the result
def compute_result():
    try:
        a = 0
        b = np.pi
        n = int(entry_subintervals.get())

        if n % 2 != 0:
            result_label.config(text="Error: n must be even")
            return

        # Compute integral using Simpson's 1/3 Rule
        numerical_result = simpsons_1_3(np.sin, a, b, n)

        # Compare with exact value
        exact_value = exact_integral()
        error = abs(numerical_result - exact_value)

        result_label.config(
            text=f"Numerical Result: {numerical_result:.5f}\nExact Result: {exact_value}\nError: {error:.5e}")

    except ValueError as ve:
        result_label.config(text=f"Error: {ve}")


# GUI Setup
root = tk.Tk()
root.title("Simpson's 1/3 Rule Integration")

frame_inputs = tk.Frame(root)
frame_inputs.pack()

# Interval start and end (fixed for this case)
lbl_a = tk.Label(frame_inputs, text="Interval Start (a):")
lbl_a.grid(row=0, column=0)
entry_a = tk.Label(frame_inputs, text="0")
entry_a.grid(row=0, column=1)

lbl_b = tk.Label(frame_inputs, text="Interval End (b):")
lbl_b.grid(row=1, column=0)
entry_b = tk.Label(frame_inputs, text="π")
entry_b.grid(row=1, column=1)

# Number of subintervals
lbl_n = tk.Label(frame_inputs, text="Number of Subintervals (n):")
lbl_n.grid(row=2, column=0)
entry_subintervals = tk.Entry(frame_inputs)
entry_subintervals.grid(row=2, column=1)

btn_compute = tk.Button(root, text="Compute Integral", command=compute_result)
btn_compute.pack()

btn_plot = tk.Button(root, text="Plot Graph", command=plot_graph)
btn_plot.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
