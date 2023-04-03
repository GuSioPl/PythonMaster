class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        return (f"Calling from ..... {self.__class__.__name__} \n")

class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        super().__init__(brand,year)
        self.horsepower = horsepower

    def show_details(self):
        result = super().show_details()
        return result + f'Calling from derived class {self.__class__.__name__} \n'

class RacingCar(Car):


    def show_details(self):
        result = super().show_details()
        return result + f'Calling from ..... {self.__class__.__name__} \n'

v1 = Vehicle("tesla",2020)
print(v1.show_details())
c1 = Car("Ford",2019,200)
print(c1.show_details())
r1 = RacingCar("Peguot",2010,300)
print(r1.show_details())
print("\n ========Example======= \n")

class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        return (f"Calling from ..... {self.__class__.__name__} \n")

class Car(Vehicle): #Treaz bez show_details w srodku

    def __init__(self, brand, year, horsepower):
        super().__init__(brand,year)
        self.horsepower = horsepower

class RacingCar(Car):


    def show_details(self):
        result = super().show_details()
        return result + f'Calling from ..... {self.__class__.__name__} \n'

v1 = Vehicle("tesla",2020)
print(v1.show_details())
c1 = Car("Ford",2019,200)
print(c1.show_details())
r1 = RacingCar("Peguot",2010,300)
print(r1.show_details())