# There are multiple ways to do this. One of them is to use the
# multiprocessing module. This method uses a threadpool and the map function
# to spread execution across each processor, and then return theresults in a
# list
from multiprocessing.dummy import Pool as ThreadPool


def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1


# Create an instance of ThreadPool
pool = ThreadPool(4)
# Then, pool.map will take in the function as the first argument and the list
# of parameters to pass into it in the second
results = pool.map(factorial, [10, 4, 3])
print(results)
