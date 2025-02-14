import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Add this import


# Define the exponential function for fitting
def exponential_func(x, a, b):
    return a * np.exp(b * x)


# Function to perform curve fitting and plot the result
def perform_curve_fitting():
    # Get data from input fields
    try:
        x_data = np.array([float(entry_x1.get()), float(entry_x2.get()), float(entry_x3.get()), float(entry_x4.get())])
        y_data = np.array([float(entry_y1.get()), float(entry_y2.get()), float(entry_y3.get()), float(entry_y4.get())])
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        return

    # Fit the data to the exponential function
    params, covariance = curve_fit(exponential_func, x_data, y_data)

    # Extract fitted parameters
    a_fitted, b_fitted = params

    # Generate fitted curve for plotting
    x_fit = np.linspace(min(x_data), max(x_data), 100)
    y_fit = exponential_func(x_fit, a_fitted, b_fitted)

    # Update result display
    result_label.config(text=f"Fitted a: {a_fitted:.3f}\nFitted b: {b_fitted:.3f}")
    equation_label.config(text=f"Equation: y = {a_fitted:.3f}e^({b_fitted:.3f}x)")

    # Plot the original data and fitted curve
    ax.clear()
    ax.plot(x_data, y_data, 'ro', label='Data points')
    ax.plot(x_fit, y_fit, label=f'Fitted Curve: y = {a_fitted:.3f}e^{b_fitted:.3f}x')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    canvas.draw()


# GUI Setup
root = tk.Tk()
root.title("Exponential Curve Fitting")

# Frame for input fields
frame_inputs = tk.Frame(root)
frame_inputs.pack()

# Labels and entry fields for x and y data points
lbl_x1 = tk.Label(frame_inputs, text="x1:")
lbl_x1.grid(row=0, column=0)
entry_x1 = tk.Entry(frame_inputs)
entry_x1.grid(row=0, column=1)

lbl_y1 = tk.Label(frame_inputs, text="y1:")
lbl_y1.grid(row=0, column=2)
entry_y1 = tk.Entry(frame_inputs)
entry_y1.grid(row=0, column=3)

lbl_x2 = tk.Label(frame_inputs, text="x2:")
lbl_x2.grid(row=1, column=0)
entry_x2 = tk.Entry(frame_inputs)
entry_x2.grid(row=1, column=1)

lbl_y2 = tk.Label(frame_inputs, text="y2:")
lbl_y2.grid(row=1, column=2)
entry_y2 = tk.Entry(frame_inputs)
entry_y2.grid(row=1, column=3)

lbl_x3 = tk.Label(frame_inputs, text="x3:")
lbl_x3.grid(row=2, column=0)
entry_x3 = tk.Entry(frame_inputs)
entry_x3.grid(row=2, column=1)

lbl_y3 = tk.Label(frame_inputs, text="y3:")
lbl_y3.grid(row=2, column=2)
entry_y3 = tk.Entry(frame_inputs)
entry_y3.grid(row=2, column=3)

lbl_x4 = tk.Label(frame_inputs, text="x4:")
lbl_x4.grid(row=3, column=0)
entry_x4 = tk.Entry(frame_inputs)
entry_x4.grid(row=3, column=1)

lbl_y4 = tk.Label(frame_inputs, text="y4:")
lbl_y4.grid(row=3, column=2)
entry_y4 = tk.Entry(frame_inputs)
entry_y4.grid(row=3, column=3)

# Button to perform the curve fitting
btn_compute = tk.Button(root, text="Fit Exponential Curve", command=perform_curve_fitting)
btn_compute.pack()

# Label to display results
result_label = tk.Label(root, text="")
result_label.pack()

equation_label = tk.Label(root, text="")
equation_label.pack()

# Frame for displaying the plot
frame_plot = tk.Frame(root)
frame_plot.pack()

# Set up matplotlib figure and canvas for plotting
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_plot)
canvas.get_tk_widget().pack()

root.mainloop()
