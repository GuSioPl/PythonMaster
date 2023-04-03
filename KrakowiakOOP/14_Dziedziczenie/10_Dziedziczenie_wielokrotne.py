class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Department:

    def __init__(self, dept_name):
        self.dept_name = dept_name

class Worker(Person, Department): ##W tym przypadku nie czerpiemy nic z klasy department
    pass

worker = Worker('grzgegorz','Kopec',30)

print(help(Worker))
print(Worker.__dict__)

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Department:

    def __init__(self, dept_name):
        self.dept_name = dept_name

class Worker(Person, Department): ##W tym przypadku nie czerpiemy nic z klasy department

    def __init__(self, first_name, last_name, age, dept_name, hours_per_day=8):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name)
        self.hours_per_day = hours_per_day


worker = Worker('Grzgegorz','Kopec',30, 'IT')
print(worker.__dict__)
class Menager(Person, Department): ##W tym przypadku nie czerpiemy nic z klasy department

    def __init__(self, first_name, last_name, age, dept_name, is_founder = False):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name)
        self.is_founder = is_founder

menager = Menager('Grzgegorz','Kopec',30, True)
print(menager.__dict__)

class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower

v1 = Vehicle('Tesla', 'red', 2020)
c1 = Car('Tesla', 'red', 2020, 300)

print(v1.__dict__)
print(c1.__dict__)