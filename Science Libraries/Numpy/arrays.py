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

rank2arr2 = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]
])
print(f'\n\nrank2arr2:\n{rank2arr2}')

# a rank 3 array (i.e. a 3d array):
rank3arr = np.array([
    [[1, 2, 3],
     [3, 4, 5],
     [6, 7, 8]],
    [[1, 2, 3],
     [3, 4, 5],
     [6, 7, 8]]
])
print(f'\n\nrank3arr: \n{rank3arr}')
# this 3d arrays shape is (2, 3, 3), this means that it has 2 rows, of 3 rows
# of 3 columns
print(rank3arr.shape)

# Numpy provides some functions to create certain kinds of arrays:
print('\n\nFunctions for array creation:')
# Note the parameter below is a tuple
zeros = np.zeros((5, 5))
print(zeros)

identitymatrix = np.eye(4)
print(identitymatrix)

randarr = np.random.random((2, 3))
print(randarr)
