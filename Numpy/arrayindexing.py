import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr)

# Slicing is similar to normal python lists. But since arrays can be
# multidimensional, each dimension can be sliced differently

# Note: The first number defines the ROW, and the second defines the COLUMN

# In this example, take out the first two rows of the above array, and columns
# 1 and 2
slicedarr = arr[:2, 1:3]
print(slicedarr)

# The new sliced array is not its own array, but a cropped view of the first
# one, as such, editing it will edit the original data too
slicedarr[0, 0] = 100
print(arr)

# You can also use this to cut out whole columns and rows
print("First row:", arr[0, :])
print("First column:", arr[:, 0])
