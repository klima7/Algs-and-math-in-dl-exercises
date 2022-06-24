import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

# figure definition
square = np.array([
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
])

# plotting
fig, ax = plt.subplots(figsize=(7, 7))
trans_poly = ax.fill(square[:, 0], square[:, 1])
ax.set_xlim([-5, 30])
ax.set_ylim([-5, 30])
ax.set_aspect('equal', adjustable='box')
ax.set_title('Translation and rotation')


# transformation
def transform(figure, rot_angle, shift_x, shift_y):
    angle_rad = np.deg2rad(rot_angle)
    transformation = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad), shift_x],
        [np.sin(angle_rad), np.cos(angle_rad), shift_y],
        [0, 0, 1],
    ])

    fig_ext = np.c_[figure, np.ones((figure.shape[0], 1))]
    fig_ext_trans = fig_ext @ transformation.T
    fig_trans = fig_ext_trans[:, :-1]
    return fig_trans


# animation callback
def animate(i):
    transformed_figure = transform(square, rot_angle=i * 1, shift_x=i * 0.1, shift_y=i * 0.1)
    trans_poly[0].set_xy(transformed_figure)


# animation start
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=360, interval=10, repeat=False)
plt.show()
