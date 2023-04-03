#Method resolution order

class Vechicle(object):
    pass

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

print(help(Plane))

"""
class Plane(AirVechicle)
 |  Method resolution order:   ||
 |      Plane                  ||
 |      AirVechicle            ||
 |      Vechicle               \/
 |      builtins.object
"""
print(Plane.mro())