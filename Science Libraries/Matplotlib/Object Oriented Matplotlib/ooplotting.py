import matplotlib.pyplot as plt
import numpy as np

# Matplotlib uses an object oriented approach under the hood
# it is the foundation for the convenience of pyplot as it's used in the other
# files

# We have Axis objects, inside Axes objects, inside Figure objects. We use
# getter and setter methods to modify these objects.


# Defining a mathematical function
def func(x):
    return 2*x**2 + 1


# Creating values
x_vals = np.arange(1, 10)
y_vals = func(x_vals)


# Here we unpack the result of plt.subplots() to obtain a Figure and Axes
# object
fig, ax = plt.subplots()


# Then we plot and use the getter and setter methods to change attributes
ax.plot(x_vals, y_vals)
ax.set_title("2x^2 + 1")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
