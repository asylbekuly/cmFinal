import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Function to define the differential equation (dy/dx = x + y)
def f(x, y):
    return x + y


# Picard's method
def picard_method(x0, y0, x_end, n_iterations=4):
    x_values = np.linspace(x0, x_end, 100)
    y_values = np.zeros((n_iterations, len(x_values)))

    # Initial condition
    y_values[0, :] = y0

    # Iteratively calculate approximations
    for n in range(1, n_iterations):
        for i, x in enumerate(x_values):
            # Compute integral of f(t, y_n(t)) from 0 to x
            integral_value, _ = quad(lambda t: f(t, y_values[n-1, np.searchsorted(x_values, t)]), x0, x, limit=100)
            y_values[n, i] = y0 + integral_value

    return x_values, y_values


# Function to compute the value of y at x = 0.2
def compute_value_at_x0_2():
    try:
        # Get initial guess and number of iterations from user inputs
        x0 = 0.0  # fixed initial condition for this problem
        y0 = 1.0  # initial value for y(0)
        x_end = 0.2
        n_iterations = 4

        # Apply Picard's method to solve the equation
        x_values, y_values = picard_method(x0, y0, x_end, n_iterations)

        # Get the value of y at x = 0.2
        y_at_x_02 = y_values[-1, np.searchsorted(x_values, 0.2)]

        result_label.config(text=f"Value of y at x = 0.2: {y_at_x_02:.5f}")

        # Plot the iterations
        ax.clear()
        for i in range(n_iterations):
            ax.plot(x_values, y_values[i, :], label=f'Iteration {i + 1}')
        ax.legend()
        ax.set_xlabel('x')
        ax.set_ylabel('y(x)')
        ax.grid(True)
        canvas.draw()

    except ValueError:
        result_label.config(text="Please enter valid numbers.")


# GUI Setup
root = tk.Tk()
root.title("Picard's Method for Solving Differential Equations")

# Frame for input fields
frame_inputs = tk.Frame(root)
frame_inputs.pack()

# Labels and entry fields for x and y data points
lbl_x0 = tk.Label(frame_inputs, text="Initial guess x0:")
lbl_x0.grid(row=0, column=0)
entry_x0 = tk.Entry(frame_inputs)
entry_x0.grid(row=0, column=1)

lbl_y0 = tk.Label(frame_inputs, text="Initial guess y0:")
lbl_y0.grid(row=1, column=0)
entry_y0 = tk.Entry(frame_inputs)
entry_y0.grid(row=1, column=1)

# Button to perform the Picard's method
btn_compute = tk.Button(root, text="Compute y at x=0.2", command=compute_value_at_x0_2)
btn_compute.pack()

# Label to display results
result_label = tk.Label(root, text="")
result_label.pack()

# Frame for displaying the plot
frame_plot = tk.Frame(root)
frame_plot.pack()

# Set up matplotlib figure and canvas for plotting
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_plot)
canvas.get_tk_widget().pack()

root.mainloop()
