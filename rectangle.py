import numpy as np
import matplotlib.pyplot as plt

# Límites
x = [0, np.log(2)]
y = [0, np.log(3)]

# Crear la figura
fig, ax = plt.subplots()
ax.set_xlim(0, np.log(2) + 0.2)
ax.set_ylim(0, np.log(3) + 0.2)

# Dibujar el rectángulo de integración
rectangle = plt.Rectangle((0, 0), np.log(2), np.log(3), color='orange', alpha=0.5)
ax.add_patch(rectangle)

# Etiquetas
ax.set_title("Integration Region R")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)

# Añadir líneas guía
ax.axvline(np.log(2), color='gray', linestyle='--')
ax.axhline(np.log(3), color='gray', linestyle='--')
ax.text(np.log(2)+0.02, 0, r'$\ln 2$', va='center')
ax.text(0, np.log(3)+0.02, r'$\ln 3$', ha='center')

# Guardar figura
plt.savefig("region_rectangle.png")
plt.show()
