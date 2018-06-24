import numpy as np
# four lines
x = np.arange(1, 101)
condlist = [(x % 3 == 0) & (x % 5 == 0), x % 3 == 0, x % 5 == 0, x]
choicelist = ["fizzbuzz", "fizz", "buzz", x]
print(np.select(condlist, choicelist))

# faster!
x = np.arange(1, 101)
print(np.select([(x % 3 == 0) & (x % 5 == 0), x % 3 == 0, x % 5 == 0],
                ["fizzbuzz", "fizz", "buzz"], default=x))
