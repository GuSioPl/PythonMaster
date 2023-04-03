class Vehicle:

    year = 2010

    def info(self):
        print(f'{self.__class__.__name__.upper()} from {Vehicle.year}.')

    def better_info(self):
        print(f'{self.__class__.__name__.upper()} from {self.__class__.year}.')

    def better_info2(self):
        print(f'{self.__class__.__name__.upper()} from {type(self).year}.') #tez git

class Car(Vehicle):

    year = 2020

vehicles = [Vehicle(),Car()]
for veh in vehicles:
    veh.info() ##zbiera z klasy Vechicle
    veh.better_info()
    veh.better_info2()