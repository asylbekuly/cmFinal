import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define function
def f(x):
    return x**4 - 10*x**2 + 9

# Bisection method
def bisection(a, b, tol=1e-5):
    if f(a) * f(b) > 0:
        return None
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

# Function to plot graph
def plot_graph():
    ax.clear()
    x_vals = np.linspace(-4, 4, 400)
    y_vals = f(x_vals)
    ax.plot(x_vals, y_vals, label='f(x) = x^4 - 10x^2 + 9')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.grid(True)
    ax.legend()
    canvas.draw()

# Function to find root and calculate error
def compute_root():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        numerical_root = bisection(a, b)
        if numerical_root is None:
            result_label.config(text='Invalid interval!')
            return
        approx_root = -3  # Example approximation from graph (to be refined manually)
        abs_error = abs(numerical_root - approx_root)
        result_label.config(text=f'Numerical Root: {numerical_root:.5f}\nAbsolute Error: {abs_error:.5f}')
    except ValueError:
        result_label.config(text='Enter valid numbers!')

# GUI Setup
root = tk.Tk()
root.title("Graphical Root Finder")

frame = tk.Frame(root)
frame.pack()

fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

btn_plot = tk.Button(root, text="Plot Function", command=plot_graph)
btn_plot.pack()

frame_inputs = tk.Frame(root)
frame_inputs.pack()

lbl_a = tk.Label(frame_inputs, text="Interval Start (a):")
lbl_a.grid(row=0, column=0)
entry_a = tk.Entry(frame_inputs)
entry_a.grid(row=0, column=1)

lbl_b = tk.Label(frame_inputs, text="Interval End (b):")
lbl_b.grid(row=1, column=0)
entry_b = tk.Entry(frame_inputs)
entry_b.grid(row=1, column=1)

btn_compute = tk.Button(root, text="Find Root & Error", command=compute_root)
btn_compute.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()