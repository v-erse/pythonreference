pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five")]
print("Unsorted", pairs, sep="\n")

# Below, sort each pair alphabetically
# using the lambda function to return the word
pairs.sort(key=lambda pair: pair[1])
print("\nSorted", pairs, sep="\n")
