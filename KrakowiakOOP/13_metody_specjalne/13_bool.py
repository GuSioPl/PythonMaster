#Jeżeli nie ma tej metody to używamy funkcji len i jak len > 0 to prawda w przeciwnym razie false
#Jak nie ma len to wszystkie instancje tej klasy są uważane za prawde
class Point:

    def __init__(self, *coords):
        for val in coords:
            if not isinstance(val,(int,float)):
                raise ValueError("Cordinates need be of type float or int.")
        self._coords = coords

    def __repr__(self):
        return f"Point(cords={self._coords})"

    def __len__(self):
        return len(self._coords)

    @property
    def coords(self):
        return self._coords

p = Point()
p2 = Point(1, 3)
print(bool(p),bool(p2))

class Point:

    def __init__(self, *coords):
        for val in coords:
            if not isinstance(val,(int,float)):
                raise ValueError("Cordinates need be of type float or int.")
        self._coords = coords

    def __repr__(self):
        return f"Point(cords={self._coords})"

    @property
    def coords(self):
        return self._coords

p = Point()
p2 = Point(1, 3)
print(bool(p),bool(p2))


class Point:

    def __init__(self, *coords):
        for val in coords:
            if not isinstance(val,(int,float)):
                raise ValueError("Cordinates need be of type float or int.")
        self._coords = coords

    def __repr__(self):
        return f"Point(cords={self._coords})"

    def __bool__(self):
        return sum(self._coords) != 0

    @property
    def coords(self):
        return self._coords

p = Point()
p2 = Point(1, 3)
p3 = Point(1, -3, 2)
print(bool(p),bool(p2), bool(p3))