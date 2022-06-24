import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation


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
plot = ax.plot_surface(X, Y, z, cmap='gist_ncar')

def animate(i):
    global plot

    ax.collections.clear()

    z = f(X, Y, i/10)
    plot = ax.plot_surface(X, Y, z, cmap='gist_ncar')

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=False)
plt.show()
