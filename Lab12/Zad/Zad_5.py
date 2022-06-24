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

# edges between points
edges = np.array([
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],

    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],

    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
])

# figure
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection='3d')


def transform(figure, angle_deg):
    angle_rad = np.deg2rad(angle_deg)
    transformation = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad), 0],
        [np.sin(angle_rad), np.cos(angle_rad), 0],
        [0, 0, 1],
    ])

    fig_trans = (transformation @ figure.T).T
    return fig_trans


def draw_figure(figure):
    ax.clear()

    ax.scatter(*figure.T)

    for start_index, end_index in edges:
        start_point, end_point = figure[start_index], figure[end_index]
        ax.plot(*zip(start_point, end_point), 'b')

    ax.set_xlim3d([-5, 5])
    ax.set_ylim3d([-5, 5])
    ax.set_zlim3d([-5, 5])
    ax.set_title('Cube')


def animate(i):
    transformed_figure = transform(cube, angle_deg=i * 1)
    draw_figure(transformed_figure)


draw_figure(cube)
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=360, interval=1, repeat=True)
plt.show()
