# We can use the timeit module (importing the Timer class), to test how long
# our functions take to execute, allowing us to assess performance easily
from timeit import Timer


def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1


# First we make a Timer instance. The first parameter is the statement that is
# to be tested, the second parameter is setup code
test = Timer("factorial(10)", "from __main__ import factorial")
print(test.timeit())
