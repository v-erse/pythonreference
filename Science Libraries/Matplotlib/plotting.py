import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 13)
y = np.arange(1, 13)
yover2 = y/2
ytimes2 = y*2
xsquared = np.square(x)

plt.plot(x, xsquared)
plt.plot(x, yover2)
plt.plot(x, ytimes2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('a graph')
plt.legend(['exponential', 'gradient of 0.5', 'gradient of 2'])
plt.grid(linestyle='dotted')
plt.show()
