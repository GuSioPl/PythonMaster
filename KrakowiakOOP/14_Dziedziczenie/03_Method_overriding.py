class Vehicle:

    def __init__(self, category=None): ##za każdym razem jak dodajemy def metody magicznej to naspiusujemy metode dzieczoną z class object
        self.category = category if category else "land"

    def __repr__(self):
        return f"Vehicle (Category='{self.category}')"

vechicle = Vehicle("land")

print(Vehicle.mro())

class LandVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    pass

vechicle = [Vehicle(),LandVehicle("Motor"),AirVehicle('Apache')]
print(vechicle)

class Vehicle:

    def __init__(self, category=None): ##za każdym razem jak dodajemy def metody magicznej to naspiusujemy metode dzieczoną z class object
        self.category = category if category else "land"

    def __repr__(self):
        return f"{self.__class__.__name__} (Category='{self.category}')" ##Zamiast dodawać Repr do każdej funkcji możemy nazwe klasy pozyskać tak

vechicle = Vehicle("land")

class LandVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    pass

vechicle = [Vehicle(),LandVehicle("Motor"),AirVehicle('Apache')]
print(vechicle)