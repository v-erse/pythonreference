# you can load a file into the python interpreter with:
#   python -i filename.py


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()
