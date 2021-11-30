from collections import deque
from math import pi

print('''
        More on Lists ''')
mylist = [1, 2, 3, "A", "B", "C"]
print(mylist)
mylist.append("X")
print(mylist)
mylist.extend(mylist[-1])
print(mylist)
print(mylist.count("X"))
mylist.remove("X")
print(mylist)
print(mylist.pop(3))
print(mylist)
print(mylist.index("B"))
print(mylist.index(2, 0, 3))
mylist.clear()
print(mylist)
mylist = [1, 2, 3, 8, 10, 139, 0, 22]
mylist.sort(reverse=True)
print(mylist)
print(sorted(mylist))
mylist.reverse()
print(mylist)
newlist = mylist.copy()
print(newlist)
print('''
        Using Lists as Queues ''')
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")                       # Terry arrives
print(queue)
queue.append("Graham")                      # Graham arrives
print(queue)
print(queue.popleft())                      # The first to arrive now leaves
print(queue)
print(queue.popleft())                      # The second to arrive now leaves
print(queue)                                # Remaining queue in order of arrival
print('''
        List Comprehensions ''')
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

combine_lists = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combine_lists)

combine_lists = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combine_lists.append((x, y))
print(combine_lists)

vec = [-4, -2, 0, 2, 4]
print(vec)
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = ['  banana', '   loganberry', ' passion fruit   ']
print(freshfruit)
print([weapon.strip() for weapon in freshfruit])

list_of_two_tuples = [(x, x**2) for x in range(6)]
print(list_of_two_tuples)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

print([str(round(pi, i)) for i in range(1, 6)])
