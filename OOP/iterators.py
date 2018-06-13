# The iterator protocol is based on the iter() and __next__() functions.
# We can define these functions in our classes to make their instances iterable

# The __iter__() method must be defined to return an object that implements the __next__()
# method. If the class itself defines __next__(), then __iter__() can just return self
# To end iteration, we raise the StopIteration exception


class LetterByLetter:
    """Iterable class that loops over each letter in a given word in 
    alphabetical order"""  # this is a doc string btw

    def __init__(self, word):
        self.word = word
        self.orderedword = sorted(word)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.orderedword):
            self.index += 1
            return self.orderedword[self.index-1]
        raise StopIteration


alphabetical = LetterByLetter("alphabetical")
for char in alphabetical:
    print(char)
