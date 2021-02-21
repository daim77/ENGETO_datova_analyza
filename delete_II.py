import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)

y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)
y10 = np.arcsin(x)
y11 = np.arccos(x)
y12 = np.arctan(x)

functions = np.array([
    ['sinus', 'kosinus', 'tangens'],
    ['arc sinus', 'arc kosinus', 'arc tangens']
])
values = np.array([[y0, y1, y2], [y10, y11, y12]])

fig, axes = plt.subplots(2, 3, figsize=(12, 6))

for i, row in enumerate(axes):
    for j, ax in enumerate(row):
        ax.plot(x, values[i, j])
        ax.set_title(functions[i, j], fontsize=14)
        ax.set_xlabel('interval (-2π, 2π)', fontsize=12)
        ax.set_ylabel(f'hodnoty {functions[i, j]}', fontsize=12)
        ax.grid()

plt.tight_layout()
plt.show()
