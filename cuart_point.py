import numpy as np
from scipy import integrate
import tkinter as tk
from tkinter import messagebox

# Function to integrate
def f(x, y):
    return np.exp(x + y)

# Integration limits
x_lower = 0
x_upper = np.log(2)
y_lower = lambda x: 0
y_upper = lambda x: np.log(3)

# Compute the double integral
result, error = integrate.dblquad(f, x_lower, x_upper, y_lower, y_upper)

# Show result in a message box
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Double Integral Result",
    f"Computed integral: {result:.10f}\nEstimated error: {error:.2e}")