import numpy as np
import matplotlib.pyplot as plt


def f(x, y, t):
    return 0.5*np.sin(x**3) + 0.25*np.sin((y - t)**2)

# meshgrid
n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(0,np.pi*1.5,n)
X, Y = np.meshgrid(x, y)


# axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# limits
ax.set_xlim3d([-np.pi/2,np.pi/2])
ax.set_ylim3d([0,np.pi*1.5])

z = f(X, Y, 0)
ax.plot_surface(X, Y, z, cmap='jet')

def animate(i):
    global contour, contourf

    for coll in contour.collections:
        plt.gca().collections.remove(coll)

    for coll in contourf.collections:
        plt.gca().collections.remove(coll)

    z = f(X, Y, i)
    contour = ax.contourf(X, Y, z, cmap='gist_ncar')
    contourf = ax.contour(X, Y, z)

plt.show()
