# make a list of squares
squares = list(map(lambda x: x**2, range(10)))

# make a list of squares using a list comprehension
squares = [x**2 for x in range(10)]

# fizzbuzz using list comprehensions
fizzlist = [x for x in range(100) if x % 3 == 0]
buzzlist = [x for x in range(100) if x % 5 == 0]

for n in range(100):
    if n in fizzlist and n in buzzlist:
        print(n, "fizzbuzz")
    elif n in fizzlist:
        print(n, "fizz")
    elif n in buzzlist:
        print(n, "buzz")
    else:
        print(n)
