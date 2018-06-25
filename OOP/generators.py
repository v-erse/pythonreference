# Generators can do what a class-based iterator can, in fewer lines
# the __iter__ and __next__ methods are created automatically, and the
# StopIteration exception is automatically raised as well


def letter_by_letter(word):
    for i in range(len(word)):
        # the yield keyword is specifically for generators, otherwise,
        # they are just like regular functions
        yield sorted(word)[i]


for char in letter_by_letter("alphabetical"):
    print(char)


# Generator expressions
# Some simple generators can be coded in a similar to way to list
# comprehensions, but with round brackets

# this makes a generator object and stores it in sumofsquares
sumofsquares = (i*i for i in range(10))
# to access its contents we loop through it
for i in sumofsquares:
    print(i)
