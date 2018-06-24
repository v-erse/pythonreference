import numpy as np
# four lines
x = np.arange(1, 101)
condlist = [(x % 3 == 0) & (x % 5 == 0), x % 3 == 0, x % 5 == 0, x]
choicelist = ["fizzbuzz", "fizz", "buzz", x]
# np.select allows us to select an array full of elements in choicelist, that
# depend on the conditions in condlist
print(np.select(condlist, choicelist))

# faster!
x = np.arange(1, 101)
# here, we can skip assigning each of the first arrays to their own variables,
# and use the 'default' argument to specify what to use if all conditions fail
print(np.select([(x % 3 == 0) & (x % 5 == 0), x % 3 == 0, x % 5 == 0],
                ["fizzbuzz", "fizz", "buzz"], default=x))
