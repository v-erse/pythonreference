import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim((-1, 1))
ax.set_ylim((-1, 1))
ax.set_zlim((-1, 1))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

x, z = np.meshgrid(np.linspace(-1, 1, 500), np.linspace(-1, 1, 500))
ax.plot_surface(x, 0, z)

plt.show()
