phrase = "Let it be"


def global_printer():
    print(phrase)  # we can use phrase because it's a global variable


global_printer()  # Let it be is printed
print(phrase)  # we can also print it directly

phrase = "Hey Jude"

global_printer()  # Hey Jude is now printed because we changed the value of phrase


def printer():
    local_phrase = "Yesterday"
    print(local_phrase)  # local_phrase is a local variable


printer()  # Yesterday is printed as expected

# print(local_phrase)  # NameError is raised

x = "global"


def outer():
    # x = "outer local"

    def inner():
        # x = "inner local"

        def func():
            # x = "func local"
            print(x)

        func()

    inner()


outer()  # "func local"


x = 1


def print_global():
    print(x)


print_global()  # 1


def modify_global():
    global x
    print(x)
    x = x + 1
    print(x)


modify_global()


def func():
    x = 1

    def inner():
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)


def nonlocal_func():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)


func()
nonlocal_func()
