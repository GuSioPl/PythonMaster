class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        self.brand = brand
        self.year = year
        self.horsepower = horsepower


v1 = Vehicle("tesla",2020)
print(v1.__dict__)
c1 = Car("Ford",2019,200)
print(c1.__dict__)


class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        print(f"calling from {self.__class__.__name__}")
        print(f"brand = '{self.brand}',\nyear = '{self.year}',\n")

class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        super().__init__(brand,year)
        self.horsepower = horsepower

    def show_details(self):
        super().show_details()
        print(f"Extended calling from {self.__class__.__name__}")
        print(f"horsepower = '{self.horsepower}'")

v1 = Vehicle("tesla",2020)
v1.show_details()
c1 = Car("Ford",2019,200)
c1.show_details()

print("\n ========Example======= \n")

class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        print(f"calling from {self.__class__.__name__}")
        print(f"brand = '{self.brand}',\nyear = '{self.year}',\n")

class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        super().__init__(brand,year)
        self.horsepower = horsepower

    def show_details(self):
        print(f"Extended calling from {self.__class__.__name__}")
        print(f"horsepower = '{self.horsepower}'")
        super().show_details()

v1 = Vehicle("tesla",2020)
v1.show_details()
c1 = Car("Ford",2019,200)
c1.show_details()

print("\n ========Example======= \n")

class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        return (f"calling from {self.__class__.__name__}")

class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        super().__init__(brand,year)
        self.horsepower = horsepower

    def show_details(self):
        result = super().show_details()
        return result + f'Calling from derived class {self}'

v1 = Vehicle("tesla",2020)
print(v1.show_details())
c1 = Car("Ford",2019,200)
print(c1.show_details())


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:

    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Department):

    def __init__(self, first_name, last_name, age, dept_name, short_dept_name):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name, short_dept_name)


w1 = Worker('John', 'Doe', 30, 'Information Technology', 'IT')
print(w1.__dict__)