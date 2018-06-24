import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr)

# Slicing is similar to normal python lists. But since arrays can be
# multidimensional, each dimension can be sliced differently
print("\n\nSlicing:")
# Note: The first number defines the ROW, and the second defines the COLUMN

# In this example, take out the first two rows of the above array, and columns
# 1 and 2
slicedarr = arr[:2, 1:3]
print(slicedarr)

# The new sliced array is not its own array, but a cropped view of the first
# one, therefore, editing it will edit the original data too
slicedarr[0, 0] = 100
print(arr)

# You can also use this to cut out whole columns and rows
print("First row:", arr[0, :])
print("First column:", arr[:, 0])


print("\n\nInteger Array Indexing:")
# We can also select elements within a higher rank array like this:
print(arr[[0, 0, 0, 0], [0, 1, 2, 3]])
# This is the same as below
print(np.array([arr[0, 0], arr[0, 1], arr[0, 2], arr[0, 3]]))
# The difference is that we are able to access what we need using only the two
# index arguments passable to arr[]

# We can use this along with arange, zeros, full, or another array constructor,
# to make our lives easier:
# print(arr[np.zeros((4, ), dtype=int), np.arange(4)])
# Note: we can pass in an int argument to specify the datatype we need, as
# zeros usually returns a list of float values
print(arr[np.zeros(4, int), np.arange(4)])
# we can use this for mutation as well
arr[np.full(4, 2), np.arange(4)] += 10
print(arr)


print("\n\nBoolean Indexing:")
# Input a statement that returns a boolean, and numpy will apply it to every
# element in the array
print("Elements larger than 10:", arr > 10,     sep="\n")
print("Elements divisible by 3:", arr % 3 == 0, sep="\n")
# We can also use these boolean statements as a type of filter
print("Elements larger than 10:", arr[arr % 3 == 0], sep="\n")


# Understanding indexing for n-dimensional arrays:
three_d = np.arange(24).reshape(2, 3, 4)
print(f'\n\nWe start with a 3D array, three_d:\n{three_d}')
print(f'Indexing once (three_d[0]) will give us a 2D array:\n{three_d[0]}')
print(
    f'Indexing again(three_d[0][0]) will give us a 1D array:\n{three_d[0][0]}')
print(
    f'Indexing a third time, will give us a single value:\n{three_d[0][0][0]}')
