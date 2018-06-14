import sys

# Run this file and give arguments in the command line, the line below will
# print them out in a list
print(sys.argv)

# use sys to write to print stuff out
sys.stdout.write("\nHello, world!")
sys.stderr.write("ERROR!")

# and to terminate the script
while True:
    sys.exit()
