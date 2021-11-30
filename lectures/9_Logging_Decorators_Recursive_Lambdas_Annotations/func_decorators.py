def our_decorator(other_func):
    def wrapper(args_for_function):
        print('This happens before we call the function')
        return other_func(args_for_function)

    return wrapper


@our_decorator
def greet(name):
    print('Hello,', name)


greet('Vlad')

import time


def func1(args_for_function):
    start = time.time()  # gets the current time
    a = [i for i in range(100)]                  # something happens here
    end = time.time()
    print('func1 takes', end - start, 'seconds')


def func2(args_for_function):
    start = time.time()
    a = [i for i in range(1000)]
    end = time.time()
    print('func2 takes', end - start, 'seconds')


func1(4)
func2(5)

def timer(func):
    def wrapper(*args_for_function):
        start = time.time()
        func(*args_for_function)
        end = time.time()
        print('func takes', end - start, 'seconds')

    return wrapper


@timer
def func1(args_for_function):
    x = [i for i in range(100)]   # something happens here


@timer
def addition(a: int, b: float) -> float:
    x = [i for i in range(100000)]
    return a + b


func1(1)
addition(5, 0.7)

import this