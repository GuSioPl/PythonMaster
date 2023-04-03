### Metody specjalne
"""
* `__new__`
* `__init__`
* `__del__`
* `__str__`
* `__repr__`
* `__len__`
* `__bool__`
"""

## __new__() + __init__()
class Company:
    """ The Company class docs."""

    def __init__(self, name):
        self.name = name

company = Company('Microsoft')
print(Company.__dict__)
company2 = Company.__new__(Company)
print(company.__dict__)

print(dir(company))

print("\n ===============Przykład=============== \n")
##Sama metoda new jest żadko implementowana
class Student:

    students = []
    limit = 3

    def __new__(cls):
        if len(cls.students) >= cls.limit:
            raise RuntimeError(f"Instance limit reached: {cls.limit}")
        instance = object.__new__(cls)
        cls.students.append(instance)
        return instance

s1 = Student()
s2 = Student()
s3 = Student()
print(Student.__dict__) #'students': [<__main__.Student object at 0x000001E064370898>, <__main__.Student object at 0x000001E064370908>, <__main__.Student object at 0x000001E064370CC0>]
s4 = Student()