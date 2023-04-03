import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.area

    @radius.getter
    def radius(self):
        if not self._area:
            self.area
        return self.radius

    def area(self):
        self._area = self.radius ** 2 * math.pi


circle = Circle(3)
print(circle.radius)
print(circle._area)