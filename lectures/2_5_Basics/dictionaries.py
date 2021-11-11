birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {8.9: 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}
another_empty_dict = dict()

print(type(birds))
print(type(prices))
print(type(empty_dict))
print(type(another_empty_dict))

prices_with_constr = dict({'espresso': 5.0}, americano=8.0, latte=10, pastry='various prices')
print(prices_with_constr)

# Wrong
# d1 = dict(888=8.0)
# d2 = dict("americano"=8.0)
# d3 = dict(["americano", "filter"]=8.0)
# d4 = dict(the best americano=8.0)

my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}
digits = {1: {'Word': 'one', 'Roman': 'I'},
          2: {'Word': 'two', 'Roman': 'II'},
          3: {'Word': 'three', 'Roman': 'III'},
          4: {'Word': 'four', 'Roman': 'IV'},
          5: {'Word': 'five', 'Roman': 'V'}}

my_pet = {}
my_pet['name'] = 'Dolly'
my_pet['animal'] = 'dog'
my_pet['breed'] = 'collie'
print(my_pet)
print(my_pet['name'])

planets = {'Venus', 'Earth', 'Jupiter'}
planets_dict = dict.fromkeys(planets)
print(planets_dict)

value = 'planet'
planets_dict = dict.fromkeys(planets, value)
print(planets_dict)

planets_dict['Jupiter'] = "giant " + planets_dict['Jupiter']
print(planets_dict)

planets = {'Venus', 'Earth', 'Jupiter'}
satellites = ['Moon', 'Io', 'Europa']
planets_dict = dict.fromkeys(planets, [])
print(planets_dict)

planets_dict['Earth'].append(satellites[0])
planets_dict['Jupiter'].append(satellites[1])
planets_dict['Jupiter'].append(satellites[2])
print(planets_dict)

planets_dict = {key: [] for key in planets}
print(planets_dict)


testable = {'September': '16°C', 'December': '-10°C'}
another_dictionary = {'June': '21°C'}
testable.update(another_dictionary)
testable.update(October='10°C')
print(testable)

testable = {'September': '16°C', 'December': '-10°C'}
testable.update(December='-20°C')
print(testable)

testable = {}
testable['September'] = '16°C'
print(testable['September'])
# print(testable['June'])
print(testable.get('September'))
print(testable.get('June'))
print(testable.get('June', 'no temperature'))

testable = {'September': '16°C', 'December': '-10°C'}
return_value = testable.pop('December')
print(return_value)
print(testable)

testable = {'September': '16°C', 'December': '-10°C'}
return_value = testable.popitem()
print(return_value)
print(testable)

testable = {}
return_value = testable.popitem()

testable = {'September': '16°C', 'December': '-10°C', 'July': '23°C'}
del testable['September']
print(testable)
del testable
print(testable)

testable = {'September': '16°C', 'December': '-10°C', 'July': '23°C'}
testable.clear()
print(testable)

testable = {'December': '-10°C', 'July': '23°C'}
another_testable = testable
testable = {}
print(testable)
print(another_testable)

testable = {'December': '-10°C', 'July': '23°C'}
another_testable = testable
testable.clear()
print(testable)
print(another_testable)

catalog = {'green table': 5000, 'brown chair': 1500, 'blue sofa': 15000, 'wardrobe': 10000}
print('blue sofa' in catalog)
print('green table' not in catalog)

tiny_dict = {'a': 1, 'b': 2, 'c': 3}
for obj in tiny_dict:
    print(obj)

print(tiny_dict.keys())

for obj in tiny_dict.keys():
    print(obj)

for value in tiny_dict.values():
    print(value)

print(tiny_dict.values())

for obj in tiny_dict.items():
    print(obj)

print(tiny_dict.items())

dictionary = {key + 5: 'some_value' for key in range(3)}
print(dictionary)

dictionary = {n + 10: n + 100 for n in range(5)}
print(dictionary)

planets_diameter_km = {'Earth': 12742, 'Mars': 6779}

# correct but long way
planets_diameter_mile = {}
for key, value in planets_diameter_km.items():
    planets_diameter_mile[key] = round(value / 1.60934, 2)

print(planets_diameter_mile)

planets_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in
                         planets_diameter_km.items()}
print(planets_diameter_mile)

planets_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in
                         planets_diameter_km.items() if value > 10000}
print(planets_diameter_mile)