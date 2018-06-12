# check input age
def ask_age(task, minimum_age=18):
    while True:
        age = ""
        while not age:
            age = input("How old are you? ")
        age = int(age)
        if age > minimum_age:
            print("Awesome, you're old enough to", task + "!")
            return True
        if age < minimum_age:
            print("Sorry, a little too young to", task + "!")
            return False


ask_age("drink", 18)
ask_age("have sex", 16)
