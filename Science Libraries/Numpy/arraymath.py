import numpy as np

print("Array Math:")
# Basic mathematical functions operate on ndarrays in an elementwise fashion
a = np.arange(10).reshape(2, 5)
b = np.arange(10).reshape(2, 5)
print(a + b)
print(a*b)

# We can use the dot function to find dot products of vectors and multiply
# matrices (the matrixmultiplication.jpg file in this folder explains matrix
# multiplication)
# We can also use the T attribute to access the transposed version of b, which
# would be the same as b.reshape(5, 2)
print(np.dot(a, b.T))

# Sum will find the sum of all the numbers in an array, column, or row
print(np.sum(a))
print(np.sum(a, axis=0))  # sum of each column
print(np.sum(a, axis=1))  # sum of each row


print("\n\nBroadcasting:")
# Numpy broadcasting allows us to take 'shortcuts' around some possible
# obstacles when doing array math
x = np.arange(1, 13).reshape(4, 3)
print(x)
y = np.array([1, 2, 1])
# In this example, y will be treated as if it has been stacked 4 times, to
# match the shape of x. This is broadcasting
print(x + y)
