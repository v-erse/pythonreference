# open a file
f = open("Reference/Input, output, errors, and exceptions/filereadwrite.txt",
         "r+")
print(f.read())

# print each line on a file
for line in f:
    print(line)

f.write("\nthis is a line I added in python")
