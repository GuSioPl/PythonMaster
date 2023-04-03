class Vechicle(object): ##Nie musimy tego pisać w pythonie 3 to default
    pass

help(Vechicle) ##mimo że nie mamy np hash to jesteśmy w stanie to urchuomic
print(hash(Vechicle()))


class LandVechicle(Vechicle): ##2 spacje przerwy
    pass


class AirVechicle(Vechicle):
    pass


class WaterVechicle(Vechicle):
    pass

vechicles = [Vechicle(), LandVechicle(), AirVechicle(), WaterVechicle()]
print('\n'.join(str(vechicles).split(',')))
print(issubclass(WaterVechicle, Vechicle))
print(issubclass(AirVechicle, Vechicle))
print(issubclass(Vechicle, object))
print(issubclass(AirVechicle, (WaterVechicle, Vechicle))) #wystarczy że tylko jednka klasa jest pochodna i true można dodawać więcej
##Zadanie


class LandVechicle(Vechicle):
    pass


class Bike(LandVechicle):
    pass


class Car(LandVechicle):
    pass


class Truck(LandVechicle):
    pass

class AirVechicle(Vechicle):
    pass


class Plane(AirVechicle):
    pass


class Helicopter(AirVechicle):
    pass


class WaterVechicle(Vechicle):
    pass