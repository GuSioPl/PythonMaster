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
        self.radius = value
        self.area

    @radius.getter
    def radius(self):
        self.area
        return self._radius

    @property
    def area(self):
        if not self._area:
            self._area = (self.radius**2)*math.pi

circle = Circle(3)
circle.radius
print(f'{circle._area:.4f}')

