import numpy as np

# A numpy array is a grid of values, all of the same type, and is indexed by a
# tuple of nonnegative integers (sort of like coordinates)
# The number of dimensions is the array's rank, and it's shape is a tuple with
# values that show the size of the array along each dimension

# a rank 1 array
arr = np.array([1, 2, 3])
# we can access a numpy arrays elements like a normal array
print(arr[0])

# a rank 2 array (note: the parameter passed in is a list of lists)
rank2arr = np.array([[1, 2, 3], [3, 4, 5]])
print(f'\nrank2arr:\nShape:\n{rank2arr.shape}\nContents:\n{rank2arr}')

rank3arr = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]
])
print(f'\n\nrank3arr:\n{rank3arr}')

# Numpy provides some functions to create certain kinds of arrays:
print('\n\nFunctions for array creation:')
# Note the parameter below is a tuple
zeros = np.zeros((5, 5))
print(zeros)

identitymatrix = np.eye(4)
print(identitymatrix)

randarr = np.random.random((2, 3))
print(randarr)
