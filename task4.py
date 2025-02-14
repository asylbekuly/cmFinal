import numpy as np
import tkinter as tk
from tkinter import ttk


# Power Method function to find largest eigenvalue
def power_method(A, tol=1e-6, max_iter=1000):
    n = A.shape[0]
    # Initial guess: a random vector
    v = np.ones(n)
    v = v / np.linalg.norm(v)  # Normalize the initial vector

    eigenvalue = 0
    for i in range(max_iter):
        # Matrix-vector multiplication
        v_new = np.dot(A, v)

        # Compute the Rayleigh quotient (approximate eigenvalue)
        eigenvalue_new = np.dot(v_new, v) / np.dot(v, v)

        # Normalize the new vector
        v_new = v_new / np.linalg.norm(v_new)

        # Check for convergence
        if abs(eigenvalue_new - eigenvalue) < tol:
            break

        # Update the eigenvalue and vector for the next iteration
        eigenvalue = eigenvalue_new
        v = v_new

    return eigenvalue, v, i + 1  # Return eigenvalue, eigenvector, and iterations


# Function to compute and display results
def compute_eigenvalue():
    try:
        # Define the matrix A
        A = np.array([[6, 2, 3],
                      [2, 6, 4],
                      [3, 4, 6]])

        # Tolerance and maximum iterations from user input
        tol = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        # Call the power method
        eigenvalue, eigenvector, iterations = power_method(A, tol, max_iter)

        # Display the results
        result_label.config(text=f"Eigenvalue: {eigenvalue:.5f}")
        eigenvector_label.config(text=f"Eigenvector: {eigenvector}")
        iterations_label.config(text=f"Iterations: {iterations}")

    except ValueError:
        result_label.config(text="Please enter valid numbers!")


# GUI Setup
root = tk.Tk()
root.title("Power Method for Eigenvalue")

# Frame for inputs
frame_inputs = tk.Frame(root)
frame_inputs.pack()

# Labels and entries for user inputs
lbl_tol = tk.Label(frame_inputs, text="Tolerance:")
lbl_tol.grid(row=0, column=0)
entry_tol = tk.Entry(frame_inputs)
entry_tol.grid(row=0, column=1)

lbl_max_iter = tk.Label(frame_inputs, text="Max Iterations:")
lbl_max_iter.grid(row=1, column=0)
entry_max_iter = tk.Entry(frame_inputs)
entry_max_iter.grid(row=1, column=1)

# Button to compute the eigenvalue
btn_compute = tk.Button(root, text="Find Eigenvalue", command=compute_eigenvalue)
btn_compute.pack()

# Labels to display results
result_label = tk.Label(root, text="")
result_label.pack()

eigenvector_label = tk.Label(root, text="")
eigenvector_label.pack()

iterations_label = tk.Label(root, text="")
iterations_label.pack()

root.mainloop()
