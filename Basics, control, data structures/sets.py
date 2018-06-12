setone = set([1, 2, 3, 4, 5])
print(setone)

settwo = set("hello")
print(settwo)

setthree = set("monday")
print(setthree)

print(setthree & settwo)

# you can also make a set with curly braces
curlyset = {'a', 'e', 'i', 'o', 'u'}
print(curlyset ^ settwo, "<- letters in curlyset or settwo but not in both")

# also, set comprehensions
evens = {x for x in range(20) if x % 2 == 0}
print(evens)
print(2 in evens, "<- is two in evens")
