import numpy as np

x = np.arange(1, 101)
condlist = [(x % 3 == 0) & (x % 5 == 0), x % 3 == 0, x % 5 == 0, x]
choicelist = ["fizzbuzz", "fizz", "buzz", x]
print(np.select(condlist, choicelist))
