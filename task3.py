import tkinter as tk
from tkinter import ttk


# Relaxation method function
def relaxation_method(omega, tol, max_iter, x0, y0, z0):
    x, y, z = x0, y0, z0
    iteration = 0
    errors = []

    # Iterate until convergence or max iterations
    for _ in range(max_iter):
        # Update each variable based on its respective equation
        x_new = omega * (10 - y - z) + (1 - omega) * x
        y_new = omega * (8 - z) + (1 - omega) * y
        z_new = omega * (6 - x) + (1 - omega) * z

        # Calculate the absolute errors
        error_x = abs(x_new - x)
        error_y = abs(y_new - y)
        error_z = abs(z_new - z)

        # Store the max error (convergence criterion)
        max_error = max(error_x, error_y, error_z)
        errors.append(max_error)

        # Check for convergence
        if max_error < tol:
            break

        # Update the values for the next iteration
        x, y, z = x_new, y_new, z_new
        iteration += 1

    return x, y, z, iteration, errors


# Function to calculate and display results
def compute_solution():
    try:
        omega = float(entry_omega.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())
        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        z0 = float(entry_z0.get())

        # Call relaxation method
        x, y, z, iterations, errors = relaxation_method(omega, tol, max_iter, x0, y0, z0)

        # Display results
        result_label.config(text=f"Solution: x = {x:.5f}, y = {y:.5f}, z = {z:.5f}\nIterations: {iterations}")
        error_label.config(text=f"Final Error: {errors[-1]:.5e}")

    except ValueError:
        result_label.config(text="Please enter valid numbers!")


# GUI setup
root = tk.Tk()
root.title("Relaxation Method Solver")

# Frame for inputs
frame_inputs = tk.Frame(root)
frame_inputs.pack()

# Labels and entries for initial guesses and parameters
lbl_omega = tk.Label(frame_inputs, text="Relaxation Parameter (ω):")
lbl_omega.grid(row=0, column=0)
entry_omega = tk.Entry(frame_inputs)
entry_omega.grid(row=0, column=1)

lbl_tol = tk.Label(frame_inputs, text="Tolerance:")
lbl_tol.grid(row=1, column=0)
entry_tol = tk.Entry(frame_inputs)
entry_tol.grid(row=1, column=1)

lbl_max_iter = tk.Label(frame_inputs, text="Max Iterations:")
lbl_max_iter.grid(row=2, column=0)
entry_max_iter = tk.Entry(frame_inputs)
entry_max_iter.grid(row=2, column=1)

lbl_x0 = tk.Label(frame_inputs, text="Initial Guess x₀:")
lbl_x0.grid(row=3, column=0)
entry_x0 = tk.Entry(frame_inputs)
entry_x0.grid(row=3, column=1)

lbl_y0 = tk.Label(frame_inputs, text="Initial Guess y₀:")
lbl_y0.grid(row=4, column=0)
entry_y0 = tk.Entry(frame_inputs)
entry_y0.grid(row=4, column=1)

lbl_z0 = tk.Label(frame_inputs, text="Initial Guess z₀:")
lbl_z0.grid(row=5, column=0)
entry_z0 = tk.Entry(frame_inputs)
entry_z0.grid(row=5, column=1)

# Button to compute the solution
btn_compute = tk.Button(root, text="Solve System", command=compute_solution)
btn_compute.pack()

# Labels to display results
result_label = tk.Label(root, text="")
result_label.pack()

error_label = tk.Label(root, text="")
error_label.pack()

root.mainloop()
