from statistics import StatisticsError
import statistics

print(statistics.median.__doc__)


def median(data):
    """Return the median (middle value) of numeric data.

    When the number of data points is odd, return the middle data point.
    When the number of data points is even, the median is interpolated by
    taking the average of the two middle values:

    >>> median([1, 3, 5])
    3
    >>> median([1, 3, 5, 7])
    4.0

    """
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2


def count_factorial(num):
    """Return the factorial of the number."""
    if num == 0:
        return 1
    else:
        return num * count_factorial(num - 1)


print(count_factorial.__doc__)


def count_factorial(num):
    """Return the factorial of the number.

    Arguments:
    num -- an integer to count the factorial of.
    Return values:
    The integer factorial of the number.
    """
    if num == 0:
        return 1
    else:
        return num * count_factorial(num-1)


def count_factorial_less(num):
    """
    Return the factorial of the number.

    The rest of the doctsring.
    """
    pass


# information.py module
"""The functionality for manipulating the user-related information."""


class Person:
    """The creation of the Person object and the related functionality."""

    def __init__(self, name, surname, birthdate):
        """The initializer for the class.

        Arguments:
        name -- a string representing the person's name.
        surname -- a string representing the person's surname.
        birthdate -- a string representing the person's birthdate.
        """
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

    def calculate_age(self):
        """Return the current age of the person."""
        # the body of the method
        ...


help(Person)


def square_aria(side: 'length of square side') -> 'result of side ** 2':
    return side ** 2


print(square_aria.__annotations__)


def func(x: 'annotating x', y: 'annotating y', z: int) -> float:
    return x + y + z


print(func.__annotations__)


def multiplication(a, b):
    """Multiply a by b
    args:
        a - the multiplicand
        b - the multiplier
    return:
        the result of multiplying a by b
    """
    return a * b


print(multiplication.__annotations__)


def multiplication(a: 'the multiplicand', b: 'the multiplier') -> 'the result of multiplying a by b':
    """Multiply a by b"""
    return a * b


print(multiplication.__annotations__)


def multiplication(a: dict(description='the multiplicand', type=int),
                   b: dict(description='the multiplier', type=int)) \
        -> dict(description='the result of multiplying a by b', type=int):
    """Multiply a by b"""
    return a * b


print(multiplication.__annotations__)


def addition(a: int, b: float) -> float:
    return a + b


print(addition.__annotations__)

print(addition("5", "5"))
