import math


class Measure:

    def __init__(self, value, unit):
        self.value, self.unit = value, unit

    def __round__(self, p):
        return self.__class__(round(self.value, p), self.unit)

class Vector:

    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def from_angled_magnitude(mag, angle):
        x = mag * math.cos(angle)
        y = mag * math.sin(angle)
        return Vector(x, y)

    def __round__(self, p):
        return self.__class__(round(self.x, p), round(self.y, p))
