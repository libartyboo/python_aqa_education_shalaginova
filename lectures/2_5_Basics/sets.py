empty_set = set()
print(type(empty_set))

empty_dict = {}
print(type(empty_dict))

flowers = {'rose', 'lilac', 'daisy'}
print(flowers)
letters = set('philharmonic')
print(letters)

letters = set('Hello')
print(len(letters))
print(letters)

states = ['Ukraine', 'USA', 'USA', 'Germany', 'Italy']
print(set(states))

set1 = {'A', 'B', 'C'}
set2 = {'B', 'C', 'A'}
print(set1 == set2)

nums = {1, 2, 2, 3}
print(1 in nums, 4 not in nums)

nums = {1, 2, 2, 3}
nums.add(5)
print(nums)
#
another_nums = {6, 7}
nums.update(another_nums)
print(nums)
#
text = ['how', 'are', 'you']
nums.update(text)
print(nums)
#
word = 'hello'
nums.add(word)
print(nums)
#
nums.remove(2)
print(nums)
#
empty_set = set()
empty_set.discard(2)
# empty_set.remove(2)
#
nums = {'trrth', 'ty', '4445', -2, 6}
print(nums)
nums.pop()
print(nums)

empty_frozenset = frozenset()
print(empty_frozenset)
#
frozenset_from_set = frozenset({1, 2, 3})
print(frozenset_from_set)
#
frozenset_from_list = frozenset(['how', 'are', 'you'])
print(frozenset_from_list)
#
# # Error
# empty_frozenset.add('some_text')
#
text = {'hello', 'world'}
nested_text = {'!'}
# nested_text.add(text)
# #
some_frozenset = frozenset(text)
nested_text.add(some_frozenset)
print(nested_text)

democrats = {'Kennedy', 'Obama'}
republicans = {'Trump', 'Lincoln'}
presidents = democrats.union(republicans)
print(presidents)

democrats = {'Kennedy', 'Obama'}
republicans = {'Trump', 'Lincoln'}
# operator
presidents = democrats | republicans
print(presidents)
# # method
also_presidents = democrats.union(republicans)
# let's compare
print(presidents == also_presidents)

ghostbusters = {'Peter', 'Raymond', 'Egon'}
soldiers = {'Winston'}
secretaries = {'Janine'}

ghostbusters |= soldiers
ghostbusters.update(secretaries)
print(ghostbusters)

light_side = {'Obi-Wan', 'Anakin'}
dark_side = {'Palpatine', 'Anakin'}
both_sides = light_side.intersection(dark_side)
print(both_sides)
print(light_side & dark_side)

creatures = {'human', 'rabbit', 'cat'}
pets = {'rabbit', 'cat'}
creatures.intersection_update(pets)
print(creatures)
beasts = {'crocodile', 'cat'}
creatures &= beasts
print(creatures)

painters = {'Klimt', 'Michelangelo', 'Picasso'}
ninja_turtles = {'Michelangelo', 'Leonardo'}
print(painters.difference(ninja_turtles))
print(painters - ninja_turtles)

criminals = {'Al Capone', 'Blackbeard', 'Bonnie and Clyde'}
gangsters = {'Al Capone'}
pirates = {'Blackbeard'}

criminals.difference_update(gangsters)
criminals -= pirates
print(criminals)
# print(hash(-6))
#
# for i in range(100000):
#     s = {-6, -11, 8, 9, 'thf', 0}
#     s.pop()
#     if 0 not in s:
#         print(s)
