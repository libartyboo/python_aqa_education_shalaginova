func = lambda x: x ** 2
print((lambda x: x ** 2)(7))
print(func(8))

func1 = lambda x, y: x + y
print(func1(5, 6))


def func2(x, n):
    return x ** n


def gen_func(n):
    return lambda x: x ** n


double = gen_func(2)
triple = gen_func(3)
print(double(10))
print(triple(10))

my_list = [1, 2, 3, 4]
m = map(lambda x: x ** 2, my_list)
print(list(m))
m = map(triple, my_list)
print(list(m))
f = filter(lambda x: x % 2, my_list)
cl = [i for i in my_list if i % 2]
print(list(f))
print(cl)


def func5(func, some_list):
    res = []
    for i in some_list:
        res.append(func(i))
    return res


m = func5(triple, my_list)
print(m)

m = func5(double, my_list)
print(m)
