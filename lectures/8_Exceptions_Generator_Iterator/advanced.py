def reg_multi(base, number):
    i = 1
    res = []
    while i <= number:
        res.append(base * i)
        i += 1
    return res


print(reg_multi(2, 1000000))


# Generators
def multi(base, number):
    i = 1
    while i <= number:
        yield base * i
        i += 1


generator = multi(2, 4)
print(type(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

numbers = [1, 2, 3, 4, 5, 6]

num3 = []
for n in numbers:
    if n % 2 == 0:
        num3.append(n ** 3)
print(num3)

q = [n ** 3 for n in numbers if n % 2 == 0]
print(q)
q = [n ** 3 if n % 2 == 0 else n + 1 for n in numbers]
print(q)

q_gen = (n ** 3 for n in numbers)
print(next(q_gen))
print(next(q_gen))
print(next(q_gen))
print(next(q_gen))
print(next(q_gen))
print(next(q_gen))
print(next(q_gen))

print(type(q_gen))

a, *b, c = q_gen
print(a, b, c)
print(*q_gen)
print(dir(q_gen))

for n in q_gen:
    print(n)

numbers = [1, 2, 3]
iterator = iter(numbers)

print(type(iterator))
print(dir(list))
for n in numbers:
    print(n)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Enumerate
numbers = [1, 2, 3, 4]
words = ['one', 'two', 'three', 'four']
floats = [5.6, 7.8, 8.9]
for num, word, float_num in zip(numbers, words, floats):
    print(num, word, float_num)
print(zip(numbers, words))

for ind, word in enumerate(words, start=10):
    print(ind, word)

print(type(enumerate(words, start=10)))

# Chain from itertools
import itertools

numbers = [1, 2, 3]
words = ['one', 'two', 'three']
floats = [5.6, 7.8, 8.9]
p = itertools.chain(numbers, floats, words)
print(p)
print(list(p))

for item in itertools.chain(numbers, floats, words):
    print(item)

# Product from itertools
numbers = range(100000000) # [1, 2, 3]
words = ['one', 'two', 'three', 'four']
floats = [5.6, 7.8, 8.9]
for first, second, float_num in itertools.product(numbers, words, floats):
    print(first, second, float_num)

p = itertools.product(numbers, words, floats)
for _ in range(10):
    print(next(p))


# Combinations from itertools
words = ['one', 'two', 'three', 'four']
for first, second, three in itertools.combinations(words, 3):
    print(first, second, three)
print(itertools.combinations(words, 2))

# Ordered dictionary
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['one'] = 1
ordered_dict['two'] = 2
ordered_dict['three'] = 3
ordered_dict[0] = 4
print(ordered_dict)
print(ordered_dict['one'])
print(ordered_dict.popitem(last=False))
print(ordered_dict)
print(type(ordered_dict))

d = {'one': 1, 'two': 2, 'three': 3}
d = OrderedDict(d)
print(d)
d.move_to_end('two', last=False)
print(d)
d.move_to_end('one', last=True)
print(d)
print(dir(d))

# Named tuple
from collections import namedtuple

person = namedtuple('Person', 'first_name, last_name, age')
print(person)
print(type(person))
print(person.first_name)
john = person(first_name='John', last_name='Johnson', age=35)
jack = person._make(['Jack', 'Jackson', 25])
jack = jack._replace(age=30)
print(john[2])
print(john.age)
print(jack[2])
print(jack.age)
for field in jack:
    print(field)

# Chained Map
from collections import ChainMap

laptop_labels = {'Lenovo': 600, 'Dell': 2000, 'Asus': 354, 'NIX': 1000}
operating_system = {'Windows': 2500, 'Linux': 400, 'MacOS': 54, 'NIX': 900}
chain = ChainMap(laptop_labels, operating_system)
print(chain)
print(chain['NIX'])

operating_system['Linux'] = 450
print(chain['Linux'])

processor = {'Celeron': 600, 'Pentium': 2000, 'Ryzen 5': 354}
new_chain = chain.new_child(processor)
print(new_chain)

without_first = new_chain.parents
print(without_first)

import collections
print(dir(collections))


from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)

d.popleft()
print(d)
