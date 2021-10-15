"""
Basic Python import. Modules
"""
import math
from math import pi as PI
import imports_packages
from imports_packages import europe
import imports_packages.europe.spain
from imports_packages.europe import norway

print(math.pi)
print(dir())
print(dir(math))
print(PI)

"""
Basic Python import. Packages
"""
print(imports_packages)
print(imports_packages.africa)
print(europe.greece)
print(europe.spain)
print(norway)


"""
Basic Python import. Absolute and Relative Imports
"""
# from . import africa == from imports_packages import africa