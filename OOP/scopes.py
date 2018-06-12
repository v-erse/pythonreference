def scope_test():
    word = "hello"

    def print_local():
        word = "local"
        print(word, "<- the value of this is local to print_local()")

    def print_nonlocal():
        nonlocal word
        word = "nonlocal"
        print(word, "<- the value of word is changed from within print_nonlocal()")

    def set_global():
        global word
        word = "global"

    print_local()
    print(word, "<- the value of this is local to scope_test()")
    print_nonlocal()
    set_global()


scope_test()
print(word, "<- set_global() changed the value of word from within scope_test(), globally")
