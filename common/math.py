import math

from common.units import Unit


class Measure:

    def __init__(self, value, symbol):
        self.value, self.symbol = value, symbol

    @property
    def unit(self):
        return Unit(self.symbol)

    def __round__(self, p=None):
        return self.__class__(round(self.value, p), self.symbol)

    def __str__(self):
        return f'{self.value}{self.symbol}'

    def convert(self, symbol):
        conversion = self.unit.conversion(Unit(symbol))
        value = conversion(self.value)
        return self.__class__(value=value, symbol=symbol)


class Percentage(Measure):

    def __init__(self, value):
        super().__init__(value, '%')

    def __int__(self):
        return self.value

    def __float__(self):
        return self.value / 100


class Vector:

    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def from_angled_magnitude(magnitude, angle):
        x = magnitude * math.cos(angle)
        y = magnitude * math.sin(angle)
        return Vector(x, y)

    def __round__(self, p):
        return self.__class__(round(self.x, p), round(self.y, p))
