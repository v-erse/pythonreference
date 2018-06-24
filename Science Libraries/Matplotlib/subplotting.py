import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
# you can use ** or np.square(), but theres a difference in
# completion time
y = x**2

# height 2, width 1, activate first plot
# I.e. in a virtual grid of 2 rows and 1 column, activate the first plot,
# starting from the top. A new plot starts in the next row
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('first')

# height 2, width 1, activate second plot
plt.subplot(2, 1, 2)
plt.plot(x, y)
plt.title('second')

plt.show()
