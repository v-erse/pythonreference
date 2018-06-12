def number():
    while True:
        try:
            x = int(input("Please enter a number: "))
            print(x)
            break
        except ValueError as err:
            print("Not a valid number, an exception was caught:", err, sep="\n")


# Here, the ValueError exception is raise either if we don't put in 1,
# or as normal, when some value that isn't a number is put in int()
def checkIf1():
    while True:
        try:
            x = int(input("Please enter the number 1: "))
            if x is 1:
                print(x)
                break
            else:
                raise ValueError
        except ValueError:
            print("You didn't input a 1")
        finally:
            print("Executing finally clause")


checkIf1()
