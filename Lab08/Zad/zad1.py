import numpy as np
import matplotlib.pyplot as plt


def my_meshgrid(x, y):
    X = np.array([x] * len(y))
    Y = np.array([y] * len(x)).T
    return X, Y


def f(x, y):
    return 0.5*np.sin(x**3) + 0.25*np.sin((y + np.pi)**2)

n = 100
x = np.linspace(-np.pi/2, np.pi/2, n)
y = np.linspace(-np.pi, np.pi/2, n)

# Uzupełnij
X, Y = my_meshgrid(x, y)
z = f(X, Y)

plt.contourf(x, y, z, cmap='jet')
plt.contour(x, y, z)
plt.show()
