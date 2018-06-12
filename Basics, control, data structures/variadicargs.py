# variadic arguments
def listThese(*args):
    for i in range(len(args)):
        print(args[i])


print("print 1-4")
listThese(1, 2, 3, 4)  # => will list each number on its own line

print("\nprint 0-99, unpacked from a list")
numbers = list(range(100))  # => a list of numbers 0-99
# => will list each number in the list 'numbers' on a new line
listThese(*numbers)
