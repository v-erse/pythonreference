# demonstrating how we can use Python to construct JSON objects
import json
dictionary = {x: chr(x) for x in range(ord('a'), ord('z')+1)}

# open a file and make it writable
jsonfile = open(
    "Reference/Input, output, errors, and exceptions/jsonobjects.json", 'r+')

# dump some json into it
# json.dump(dictionary, jsonfile, indent=4)

# # the file must be readable to load the json
print(json.load(jsonfile))
