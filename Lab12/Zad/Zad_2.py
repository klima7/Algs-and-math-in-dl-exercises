import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

# figure definition
figure = np.array([
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
])

# plotting
fig, axs = plt.subplots(1, 3, figsize=(10, 3))
rot_poly = axs[0].fill(figure[:, 0], figure[:, 1])
scale_poly = axs[1].fill(figure[:, 0], figure[:, 1])
shear_poly = axs[2].fill(figure[:, 0], figure[:, 1])

# plot decoration
titles = ['Rotation', 'Scaling', 'Sheering']
for ax, title in zip(axs, titles):
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(title)

# transformed figures
fig_rotated = figure.copy()
fig_scaled = figure.copy()
fig_sheared = figure.copy()

# rotation matrix
angle_rad = np.deg2rad(1)
rot_matrix = np.array([
    [np.cos(angle_rad), -np.sin(angle_rad)],
    [np.sin(angle_rad), np.cos(angle_rad)]
])

# scaling matrix
scale_matrix = np.array([
    [1.01, 0],
    [0, 1]
])


# shearing matrix
shear_matrix = np.array([
    [1, 0],
    [0.01, 1]
])


# animation callback
def animate(i):
    global fig_rotated, fig_scaled, fig_sheared

    fig_rotated = fig_rotated@rot_matrix
    fig_scaled = fig_scaled@scale_matrix
    fig_sheared = fig_sheared@shear_matrix

    rot_poly[0].set_xy(fig_rotated)
    scale_poly[0].set_xy(fig_scaled)
    shear_poly[0].set_xy(fig_sheared)


# animation start
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=3600, interval=10, repeat=False)
plt.show()
