import matplotlib.pyplot as plt

# We can use grids to layout our Axes objects, this is kind of similar to
# HTML bootstrap

gridsize = (3, 3)

fig = plt.figure(figsize=(9, 9))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=3)
ax2 = plt.subplot2grid(gridsize, (1, 0), colspan=2)
ax3 = plt.subplot2grid(gridsize, (1, 2), rowspan=2)
ax4 = plt.subplot2grid(gridsize, (2, 0))
ax5 = plt.subplot2grid(gridsize, (2, 1))

plt.show()
