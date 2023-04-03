class Point:

    def __init__(self, *coords):
        for val in coords:
            if not isinstance(val,(int,float)):
                raise ValueError("Cordinates need be of type float or int.")
        self._coords = coords

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x + y for x, y in zip(self.coords, other.coords))
        return Point(*coords) #Mamy tutaj tuple pod coords więc musimy ją jeszcze rozpakować

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x - y for x, y in zip(self.coords, other.coords))
        return Point(*coords) #Mamy tutaj tuple pod coords więc musimy ją jeszcze rozpakować

    def __repr__(self):
        return f"Point(cords={self._coords})"

    @property
    def coords(self):
        return self._coords

p1 = Point(2, 3) #bez adda nie można dodać
p2 = Point(1, 3)
p3 = p1 - p2
print(p3.__repr__())
print(p3.__dict__)

class Point:

    def __init__(self, *coords):
        for val in coords:
            if not isinstance(val,(int,float)):
                raise ValueError("Cordinates need be of type float or int.")
        self._coords = coords

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x + y for x, y in zip(self.coords, other.coords))
        return Point(*coords) #Mamy tutaj tuple pod coords więc musimy ją jeszcze rozpakować

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x - y for x, y in zip(self.coords, other.coords))
        return Point(*coords) #Mamy tutaj tuple pod coords więc musimy ją jeszcze rozpakować

    def __mul__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x * y for x, y in zip(self.coords, other.coords))
        return Point(*coords) #Mamy tutaj tuple pod coords więc musimy ją jeszcze rozpakować

    def __repr__(self):
        return f"Point(cords={self._coords})"

    @property
    def coords(self):
        return self._coords

p1 = Point(2, 3)
p2 = Point(1, 3)
p3 = p1 * p2
print(p3.__repr__())
print(p3.__dict__)