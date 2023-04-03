class Vehicle:

    def __init__(self, category=None): ##za każdym razem jak dodajemy def metody magicznej to naspiusujemy metode dzieczoną z class object
        self.category = category if category else "land"

    def __repr__(self):
        return f"{self.__class__.__name__} (Category='{self.category}')" ##Zamiast dodawać Repr do każdej funkcji możemy nazwe klasy pozyskać tak

    def display_info(self):
        print(f"Vechicle category: {self.category}")

vechicle = Vehicle("land")

class LandVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    pass

vehicles = [Vehicle(),LandVehicle("Motor"),AirVehicle('Apache')]

for veh in vehicles:
    veh.display_info()
    print(veh.__class__.__mro__)