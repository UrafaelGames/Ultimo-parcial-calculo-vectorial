import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import tkinter as tk
from tkinter import messagebox

# Función a integrar
def f(x, y):
    return x * y

# Límites de integración: x va de 0 a 1, y va de 0 a x (triángulo)
x_lower = 0
x_upper = 1
y_lower = lambda x: 0
y_upper = lambda x: x

# Cálculo numérico con scipy
result, error = integrate.dblquad(f, x_lower, x_upper, y_lower, y_upper)

# Crear ventana UI para mostrar procedimiento y resultado
root = tk.Tk()
root.withdraw()

procedure = """
Step-by-step for ∬_R xy dx dy, where R is triangle with vertices (0,0), (1,0), (1,1):

1. Region R: bounded by y=0 and y=x from x=0 to x=1

2. Rewrite as iterated integral:
   ∫₀¹ ∫₀ˣ xy dy dx

3. Inner integral:
   ∫₀ˣ xy dy = x ∫₀ˣ y dy = x[x²/2] = x³/2

4. Outer integral:
   ∫₀¹ x³/2 dx = (1/2) ∫₀¹ x³ dx = (1/2)(1/4) = 1/8

Exact value: 1/8 = 0.125
"""

messagebox.showinfo("Procedure", procedure)
messagebox.showinfo(
    "Double Integral Result",
    f"Computed integral: {result:.10f}\nEstimated error: {error:.2e}"
)

# --- Gráfico de la región triangular ---
x = np.linspace(0, 1, 100)
y = x

fig, ax = plt.subplots()
ax.plot([0, 1, 1, 0], [0, 0, 1, 0], 'k--', label="Bounding Box")
ax.fill_between(x, 0, x, color='orange', alpha=0.5, label="Region R")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Region of Integration: Triangle R')
ax.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
