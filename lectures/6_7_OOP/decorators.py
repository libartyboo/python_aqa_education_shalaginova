class CharType:

    @staticmethod
    def get_type(char):
        if char.isalpha():
            return 'letter'
        elif char.isdigit():
            return 'digit'
        else:
            return 'other'


print(CharType.get_type('a'))
print(CharType().get_type('1'))


class User(object):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        return self.name + ' (' + self.surname + ')'

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    @classmethod
    def from_string(cls, data):
        name, surname = data.split(' ')
        return cls(name, surname)


user = User.from_string('John Doe')
user.name = 'Jane'
print(user.get_info())
print(user.full_name)
