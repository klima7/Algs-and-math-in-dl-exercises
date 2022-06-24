import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

# figure definition
cube = np.array([
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
])

# plotting
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection='3d')
ax.set_xlim3d([-5, 5])
ax.set_ylim3d([-5, 5])
ax.set_zlim3d([-5, 5])
ax.set_title('Cube')
plotted_figure = ax.scatter(*cube.T)


# transformation
def transform(figure, angle_deg):
    angle_rad = np.deg2rad(angle_deg)
    transformation = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad), 0],
        [np.sin(angle_rad), np.cos(angle_rad), 0],
        [0, 0, 1],
    ])

    fig_trans = transformation @ figure.T
    return fig_trans


# animation callback
def animate(i):
    transformed_figure = transform(cube, angle_deg=i * 1)
    plotted_figure._offsets3d = transformed_figure
    plt.draw()


# animation start
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=360, interval=10, repeat=False)
plt.show()
