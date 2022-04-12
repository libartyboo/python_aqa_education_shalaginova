class Person:
    # __slots__ = 'name', 'age', 'new_attr'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.new_attr = None

    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value

    @property
    def full_info(self):
        return f"{self.name}, age {self.age}"

    def mess(self):
        print("Message from Person")


class Student(Person):
    def mess(self):
        print("Message from Student")
        super().mess()


class Programmer(Person):
    def mess(self):
        print("Message from Programmer")
        super().mess()


class StudentProgrammer(Programmer, Student):
    def mess(self):
        print("Message from StudentProgrammer")
        super().mess()


student_programmer = StudentProgrammer("John", 23)
# print(student_programmer.full_info)
# student_programmer.name = "Bob"
# print(student_programmer.full_info)

# print(type(student_programmer) == StudentProgrammer)
# print(type(student_programmer) == Student)
# print()
# print(isinstance(student_programmer, StudentProgrammer))
# print(isinstance(student_programmer, Student))
# print(isinstance(student_programmer, Programmer))
# print(isinstance(student_programmer, Person))
#
# print(StudentProgrammer.__slots__)
print(StudentProgrammer.__mro__)
print(student_programmer.name)
student_programmer.mess()
