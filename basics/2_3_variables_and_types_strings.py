mystring = 'spam eggs'               # single quotes
print(mystring)
mystring = 'doesn\'t'                # use \' to escape the single quote...
print(mystring)
mystring = "doesn't"                 # ...or use double quotes instead
print(mystring)
mystring = '"Yes," they said.'
print(mystring)
mystring = "\"Yes,\" they said."
print(mystring)
mystring = '"Isn\'t," they said.'
print(mystring)

print(" ")
print('\tFirst line.\n\tSecond line.')
print(r'\tFirst line.\n\tSecond line.')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(" ")
print(3 * 'un' + 'ium')             # 3 times 'un', followed by 'ium'
print('Py' 'thon')

print(" ")
mystring = ('Put several strings within parentheses '
           'to have them joined together.')
print(mystring)

print(" ")
mystring = 'Py'
print(mystring + 'thon')

print(" ")
mystring = 'Python'
print(mystring[0] + ' ' + mystring[5])
print(mystring[-1] + ' ' + mystring[-2] + ' ' + mystring[-6])
print(mystring[0:2] + ' ' + mystring[2:5])
print(mystring[:2] + ' ' + mystring[4:] + ' ' + mystring[-2:])
print(mystring[:2] + mystring[2:])
print(mystring[:4] + mystring[4:])
print('J' + mystring[1:])
print(mystring[:2] + 'py')
print(len(mystring))

