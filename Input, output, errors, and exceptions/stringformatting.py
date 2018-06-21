# the rjust, ljust, center methods can be run on strings
# rjust and ljust will justify left or right within the inputted column size
# center will center
print("num".center(7), "square".center(6), "cube".center(7))
# repr returns the string value of an object
for i in range(10):
    print(repr(i).rjust(5), repr(i*i).rjust(8), repr(i*i*i).rjust(6))


# the format method can be used like this
print("\nThe {1} {0}:".format("method", "format"))
print("Hello, my name is {name} and I am {age} years old!".format(
    name="Abdullah", age=20))

dictionary = {x: chr(x) for x in range(ord('a'), ord('z')+1)}
for number, letter in dictionary.items():
    print("{0:3d} -> {1:3}".format(number, letter))

# there are also f-strings (aka formatted string literals)
# similar to the format method, but slightly simpler. We can use the name and
# age example fro line 12 to demonstrate
name = 'Abdullah'
age = 20
print(f'Hello my name is {name} and I\'m {20} years old!')
