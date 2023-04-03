#Kalsa abstrakcyjna to taka która nie może mieć reprezentacji pod postaci obiektów
#jest uogólnieniem innych klas np figura ->trójkąt,koło
#Ma choć jedną metode abstrakcyjną którą nie implementujemy w klasie abstrakcyhneh tylko w klsach pochodnych

import abc, math

print(help(abc.ABC))
print(help(abc.abstractmethod))

from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def permiter(self):
        pass


class Square(Figure):

    def __init__(self, a=1):
        self.a = a

    def area(self):
        return self.a * self.a

    def permiter(self):
        return self.a * 4


#f = Figure() #TypeError: Can't instantiate abstract class Figure with abstract methods area

class Circle(Figure):

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def permiter(self):
        return 2 * self.radius * math.pi

figures = [Square(), Square(5), Square(10),Circle(), Circle(5), Circle(10)]

for figure in figures:
    print(f"Permiter of figure {figure.permiter():.4f}")
    print(f"Area of figure {figure.area():.4f}\n")

class Triangle(Figure):

    def __init__(self,a=1,b=1,c=1):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b /2

    def permiter(self):
        return self.a + self.b + self.c

print("\n ========Example======= \n")

class Vehicle(ABC):

    @abstractmethod
    def show_activity(self):
        pass

class Plane(Vehicle):

    def show_activity(self):
        print(f'{self.__class__.__name__} ->I can fly')

class Car(Vehicle):

    def show_activity(self):
        print(f'{self.__class__.__name__} ->I can Drive')

vehicles = [Car(),Plane()]
for veh in vehicles:
    veh.show_activity()

