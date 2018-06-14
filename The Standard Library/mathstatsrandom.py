import math
import random
import statistics

# The math module provides the standard math operations and stuff
print("Math:")
print(math.pi)
print(math.cos(1))

# The random module is for randomization
print("\nRandom:")
# Use it to choose one element from a list like this:
print(random.choice(['a', 'e', 'i', 'o', 'u']))
# Or to take some numbers from a range
print(random.sample(range(100), 10))
# Or to produce a random float
print(random.random())
# Or to take one number from a range
print(random.randrange(10))

# The statistics module
print("\nStatistics:")
# If we make a random set of sample data
data = random.sample(range(100), 10)
print(data)
# we can use statistics to find mean, variance, median
print("Mean: {}\nMedian: {}\nVariance: {}".format(
    statistics.mean(data), statistics.median(data), statistics.variance(data)))
