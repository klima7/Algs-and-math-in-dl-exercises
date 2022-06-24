import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.patches import Circle

with open('animals.npz', 'rb') as f:
  animals = np.load(f)['animals']

images = [matplotlib.image.imread(path) for path in animals[:, -1]]
heights = animals[:, 3].astype(np.float_).flatten()
weights = animals[:, 2].astype(np.float_).flatten()
annotations = []
circles = []

fig, ax = plt.subplots(figsize=(10, 7))
s = ax.scatter(weights, heights)

ax.set_xlabel('Waga')
ax.set_ylabel('Wzrost')

for weight, height, image in zip(weights, heights, images):
  imagebox = OffsetImage(image, zoom=0.2)
  imagebox.image.axes = ax

  ab = AnnotationBbox(imagebox, (weight, height),
                      xybox=(70, -30),
                      xycoords='data',
                      boxcoords="offset points",
                      pad=0.5,
                      )

  ab.set_visible(False)
  ax.add_artist(ab)
  annotations.append(ab)

  circle = Circle((weight, height), 0.001, alpha=0)
  ax.add_patch(circle)
  circles.append(circle)


def hover(event):
  for circle, annotation in zip(circles, annotations):
    contains, _ = circle.contains(event, 30)
    annotation.set_visible(contains)
    fig.canvas.draw_idle()


fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
