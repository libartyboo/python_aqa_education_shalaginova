def add(a, b, *args):
    total = a + b
    for n in args:
        total += n
    return total


def will_survive(*names):
    print(names)
    for name in names:
        if name == "Ned Stark":
            print("Sean Bean heroes die in every movie.")
        print(f"{name} will survive.")


will_survive("Daenerys Targaryen", "Arya Stark", "Brienne of Tarth", "Ned Stark", 4)


def recipe(*args, sep=" or "):
    return sep.join(args)


print(recipe("meat", "fish", "vegetables"))
print(recipe("meat", "fish", sep=" and "))

print(*"fun", sep='\n')
print('f', 'u', 'n', sep='\n')
print(*[5, 10, 15])


def add_more(*args):
    total = 0
    for n in args:
        total += n
    return total


small_numbers = [1, 2, 3]
large_numbers = [9999999, 1111111]
#
print(add_more(*small_numbers))
print(add_more(*large_numbers))


my_tuple = 'hello', 'world', 123, [1, 2, 3]


def someth():
    return 4, 5, 'fghfh'


n, m, x = someth()
print(n, m, x)

a, b, c, d = my_tuple
print(a)
print(b)
print(c)
print(d)

a, b, c = 'hello', 'world', 123, [1, 2, 3]

a, b, c, d, e = 'hello', 'world', 123, [1, 2, 3]

start, *middle, end = [1, 2, 3, 4, 5]
print(start)
print(end)
print(middle)


my_list = [1, 2, 3, 4, 5]
start = my_list[0]
end = my_list[-1]
middle = my_list[1:len(my_list)-1]

print(start)
print(end)
print(middle)

start, *middle, end = [1, 2]
print(start)
print(end)
print(middle)


*my_range, = range(5)
a = iter(range(5))
print(next(a))
print(next(a))
print(my_range)


sequence = range(1, 8)

first, rest = sequence[0], sequence[1:]
print(first, rest)
first, *rest = sequence
print(first, rest)


rest, last = sequence[:-1], sequence[-1]
print(rest, last)
*rest, last = sequence
print(rest, last)


my_dict = {'apple': 1, 'banana': 2, 'pear': 3}
print(*my_dict)

# Error
my_dict = {'apple': 1, 'banana': 2, 'pear': 3}
# start, **middle, end = my_dict


my_dict = {'apple': 1, 'banana': 2, 'pear': 3}


def fruit_sum(apple, banana, pear):
    return apple + banana + pear


print(fruit_sum(**my_dict))


dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'one': 'two', 'three': 'four'}
dict_3 = {**dict_1, **dict_2}
print(dict_3)

my_dict = {'apple': 1, 'banana': 2, 'pear': 3}
my_dict_updated = {**my_dict, 'strawberry': 4}
print(my_dict_updated)


def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, "is the capital city of", key)


capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")


def func(positional_args, defaults, *args, **kwargs):
    pass


def example_func(a, b, c, d='smt', *args, **kwargs):
    pass


def say_bye(**names):
    for name in names:
        print("Au revoir,", name)
        print("See you on", names[name]["next appointment"])
        print()


humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}

say_bye(**humans)
