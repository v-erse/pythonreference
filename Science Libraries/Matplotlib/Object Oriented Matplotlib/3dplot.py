import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(14, 6))
fig.suptitle("1D and 2D Gaussian Functions")


def func1d(x):
    a = 0.8
    b = 0
    c = 0.8
    return a*np.exp(-(x-b)**2 / 2*c**2)


ax1 = fig.add_subplot(121)
ax1.set_xlim((-5, 5))
ax1.set_ylim((0, 1))
x1d = np.linspace(-5, 5, 1000)
y1d = func1d(x1d)
ax1.plot(x1d, y1d, color='k')


def func2d(x, y):
    A = 0.8
    xo, yo = (0, 0)
    sigx, sigy = (0.8, 0.8)
    return A*np.exp(-1*((x-xo)**2/2*sigx**2 + (y-yo)**2/2*sigy**2))


ax2 = fig.add_subplot(122, projection="3d")
ax2.set_xlim((-5, 5))
ax2.set_ylim((-5, 5))
ax2.set_zlim((0, 1))
x2d = y2d = np.linspace(-5, 5, 500)
x2d, y2d = np.meshgrid(x2d, y2d)
z2d = func2d(x2d, y2d)
ax2.plot_surface(x2d, y2d, z2d, cmap=cm.viridis)

plt.show()
