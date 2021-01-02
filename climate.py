import math
import api, os
from geo import GeoPoint as gp
from utils import Measure, Vector
from files import cache
from datetime import datetime as dt, timedelta as td


class Temp(Measure):
    pass


class Wind(Measure):

    def from_angled_magnitude(mag, angle, unit):
        angle = math.radians(angle + 90)
        vector = Vector.from_angled_magnitude(mag, angle)
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
        


class CelestialBody:

    arrival: dt
    departure: dt

    period = property(lambda self: self.departure - self.arrival)


class Sun(CelestialBody):
    pass


class Moon(CelestialBody):

    phase: str
    name: str


class Report:

    def __init__(self):
        data = load().get('current')
        self.datetime = dt.fromtimestamp(data.get('dt'))

    def __str__(self):
        ret = f'{self.datetime.strftime("[%H:%M] %a, %b %d %Y")}'
        return ret


class Forecast:
    pass


def fetch():
    response = api.GET(
        endpoint='http://api.openweathermap.org/data/2.5/onecall',
        APPID=os.environ["WEATHER_KEY"], **dict(gp.fetch())
    ).json()
    # open cache file for writing and dump to cache
    cache.dump_json('weather.json', response)
    # return the response in case we still want it
    return response


def load():
    data = cache.load_json('weather.json')
    # otherwise, fetch, cache, and return new weather data
    return data or fetch()
