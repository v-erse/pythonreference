# Import deque, i.e. double ended queue
from collections import deque

# numbers.extend(numbers_two) will add each item from numbers_two onto numbers
numbers = [1, 2, 3, 4, 5, 6]
numbers_two = [7, 8, 9, 10]

numbers.extend(numbers_two)
print(numbers)

# numbers.pop will return the last item in the list, and remove it
print(numbers.pop(), numbers)
print(numbers.pop(), numbers)

# del allows you to delete a number at a specific index
del numbers[6]
print(numbers)
del numbers[6]
print(numbers)

# loop through and display the indexes too
print("\nLoop through and display the indexes with values")
for i, v in enumerate(numbers):
    print(i, v)

print("\nLoop through and display the indexes with values, in reverse")
for i, v in enumerate(reversed(numbers)):
    print(i, v)

# Using lists as stacks
print("\nUsing lists as stacks:")
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack, "<- a stack")
print(stack.pop(), "<- pop from stack")
print(stack, "<- remaining stack")

# Using lists as queues
print("\nUsing lists as queues")
queue = deque(["jerry", "rick", "morty"])
print(queue, "<- a queue")
queue.append("beth")
queue.append("summer")
print(queue, "<- beth and summer arrive")
print(queue.popleft(), "<- jerry's been waiting the longest, he leaves")
print(queue, "<- remaining queue")
