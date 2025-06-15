import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import tkinter as tk
from tkinter import messagebox

# Define the function
def f(x, y):
    return x**2 - y**2

# Define the region
x_lower, x_upper = -1, 1
y_lower = lambda x: -1
y_upper = lambda x: 1

# Compute the integral
result, error = integrate.dblquad(f, x_lower, x_upper, y_lower, y_upper)

# Display result in a message box
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Double Integral Result",
                    f"Computed integral: {result:.10f}\nEstimated error: {error:.2e}")

# Plot the surface
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Surface: f(x, y) = x² - y²')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.show()
