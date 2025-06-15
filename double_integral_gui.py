import numpy as np
from scipy import integrate
import tkinter as tk
from tkinter import messagebox

# Define the function to integrate
def f(x, y):
    return x**2 + y**2

# Integration limits
x_lower = 0
x_upper = 1
y_lower = lambda x: 0
y_upper = lambda x: 1

# Build the procedure as a string
procedure = """
Step-by-step procedure to evaluate the double integral:

1. Define the region R:
   R = [0, 1] × [0, 1] (a square from x=0 to 1 and y=0 to 1)

2. Define the function:
   f(x, y) = x² + y²

3. Set up the double integral:
   ∬_R (x² + y²) dx dy
   = ∫₀¹ ∫₀¹ (x² + y²) dy dx

4. Solve the inner integral with respect to y:
   ∫₀¹ (x² + y²) dy = [x²y + (1/3)y³] from y=0 to y=1
                    = x²(1) + (1/3)(1)³ = x² + 1/3

5. Solve the outer integral with respect to x:
   ∫₀¹ (x² + 1/3) dx = ∫₀¹ x² dx + ∫₀¹ 1/3 dx
                     = (1/3) + (1/3) = 2/3

6. Exact result:
   ∬_R (x² + y²) dx dy = 2/3 ≈ 0.666666...
"""

result, error = integrate.dblquad(f, x_lower, x_upper, y_lower, y_upper)

root = tk.Tk()
root.withdraw()  

messagebox.showinfo("Procedure", procedure)

messagebox.showinfo(
    "Double Integral Result",
    f"Computed integral: {result:.10f}\nEstimated error: {error:.2e}"
)
