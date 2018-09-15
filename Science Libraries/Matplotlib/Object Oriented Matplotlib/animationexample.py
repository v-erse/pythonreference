import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure with black background colour
fig = plt.figure(facecolor="black")

# Create ax with no frame
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2), frameon=False)
# and no ticks
ax.set_xticks([])
ax.set_yticks([])

# Create line
line, = ax.plot([], [], lw=2, color="white")


def init():
    line.set_data([], [])
    return line,


def animate(framenumber):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2*np.pi*(x-0.01*framenumber))
    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=100, interval=20, blit=True)


plt.show()
