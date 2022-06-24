import numpy as np
import matplotlib.pyplot as plt

figure = np.array([
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
])

plt.fill(figure[:, 0], figure[:, 1])
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
