import math
from common.math import Measure, Percentage, Vector


class Temp(Measure): pass


class Pressure(Measure): pass


class Humidity(Percentage): pass


class CloudCover(Percentage): pass


class Visibility(Measure): pass


class Wind(Measure):

    def from_angled_magnitude(magnitude, angle, unit):
        angle = math.radians(angle + 90)
        vector = Vector.from_angled_magnitude(magnitude, angle)
        return round(Wind(vector, unit), 2)

    @property
    def cardinal(self):
        components = []
        if self.value.x:
            card = 'E' if self.value.x >= 0 else 'W'
            components.append(f'{abs(self.value.x)} {card}')
        if self.value.y:
            card = 'N' if self.value.y >= 0 else 'S'
            components.append(f'{abs(self.value.y)} {card}')
        return ' '.join(components)


class Precipitation:

    def __init__(self, category, content):
        self.category = category
        self.volume = (content if isinstance(content, (int, float))
                  else content['1h'] if isinstance(content, dict) and '1h' in content.keys()
                  else 0)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.category == other
        elif isinstance(other, (int, float)):
            return self.volume == other
