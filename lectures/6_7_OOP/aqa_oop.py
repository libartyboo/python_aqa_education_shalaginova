class Person:
    """
    Class specified for...
    """
    course = "Python"
    person_list = []

    # def __new__(cls, *args, **kwargs):
    #     print("New")
    #     return .__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        # print("Init")
        self.name = name
        self.age = age
        self.exp = None
        Person.person_list.append(self)

    def do_smt(self, action):
        print(f"{self.name} doing {action}")

    def additional(self, value):
        self.exp = value

    def info(self):
        print(f"{self.name} {self.age} {self.exp}")

    def __str__(self):
        return f"{self.name} {self.age} {self.exp}"

    @classmethod
    def cls_method(cls):
        print(cls.course)

    @staticmethod
    def gen_method():
        return Person("sdsd", 50)


person1 = Person("John", 30)
person2 = Person("Jack", 25)


print(Person.cls_method())
print(person2.cls_method())

person3 = Person.gen_method()
print(person3)



# person.do_smt("nothing")
# Person.do_smt(person, "something")
