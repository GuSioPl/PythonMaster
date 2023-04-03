help(int.__truediv__)
help(int.__floordiv__)

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

    def __truediv__(self, other):
        return '__truediv__ called ...'

    def __floordiv__(self, other):
        return '__floordiv__ called ...'

    def __repr__(self):
        return f"Point(cords={self._coords})"

    @property
    def coords(self):
        return self._coords

p1 = Point(2, 3)
p2 = Point(1, 3)
print(p1/p2)
print(p1//p2)

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

    def __truediv__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        for coord in other.coords:
            if coord == 0:
                raise ZeroDivisionError("Division by Zero.")
        coords = tuple(x / y for x, y in zip(self.coords, other.coords))
        return Point(*coords)


    def __floordiv__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        for coord in other.coords:
            if coord == 0:
                raise ZeroDivisionError("Division by Zero.")
        coords = tuple(x // y for x, y in zip(self.coords, other.coords))
        return Point(*coords)

    def __repr__(self):
        return f"Point(cords={self._coords})"

    @property
    def coords(self):
        return self._coords

p1 = Point(2, 2)
p2 = Point(1, 3)
print("__floordiv__",p1/p2)
print("__truediv__",p1//p2)