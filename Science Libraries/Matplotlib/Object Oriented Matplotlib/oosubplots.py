import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 15, 100)
y = x + np.random.randint(1, 15, 100)
data = np.column_stack((x, y))

# Here we initialise two Axes objects in a grid (1 row, 2 columns)
# The Axes objects are returned in an array, which we can unpack like this
fig, (ax1, ax2) = plt.subplots(1, 2)

# For a larger array, you can unpack by flattening it:
# ax1, ax2, ax3, ax4 = ax.flatten()

# And then use the getters and setters to change attributes and plot
ax1.scatter(x, y, marker='o', color="b")
ax1.set_title('Scatter: $x$ versus $y$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')

ax2.hist(data, label=('x', 'y'), bins=np.arange(data.min(), data.max()))
ax2.legend(loc=(0.65, 0.8))
ax2.set_title('Frequencies of $x$ and $y$')
ax2.yaxis.tick_right()

plt.show()
