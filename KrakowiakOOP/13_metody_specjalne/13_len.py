print(help(len))

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

p = Point(3, 5, 5)
print(p)
print(p.coords)
print(p.__dict__)
##print(len(p)) normalnie to wywali

class Point2:


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

q = Point2(3,4,7)
print(q)
print(len(q))
print(q.__len__())

g = Point2()
print(g.coords)
print(g.__len__())
print(g.__dict__)
