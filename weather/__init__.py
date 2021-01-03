import api, os
from geo import GeoPoint as gp
from files import cache
from datetime import datetime as dt

from .celestial import Sun
from .climate import Temp, Pressure, Humidity, Wind, CloudCover, Visibility, Precipitation



class Description:

    def __init__(self, data):
        self.simple  =  data.pop('main').lower()
        self.verbose =  data.pop('description').lower()
        self._id     =  data.pop('id')
        self.icon    =  data.pop('icon')


class Hour:
    
    def __init__(self, data):
        self.temp = Temp(data.pop('temp'), 'F')
        self.temp_feel = Temp(data.pop('feels_like'), 'F')
        
        self.pressure   = Pressure(data.pop('pressure'), 'hPa')
        self.humidity   = Humidity(data.pop('humidity'))
        self.dewpoint   = Temp(data.pop('dew_point'), 'F')
        self.clouds     = CloudCover(data.pop('clouds'))
        self.visibility = Visibility(data.pop('visibility', None), 'm')
        self.uvi        = data.pop('uvi')

        self.wind = Wind.from_angled_magnitude(
            magnitude=data.pop('wind_speed'),
            angle=data.pop('wind_deg'),
            unit = 'mph'
        )

        self.description = Description(data.pop('weather').pop())

        self.precipitation = [Precipitation('rain', data.pop('rain', []))
                              for cat in ('rain', 'snow') if cat in data.keys()]

    def __str__(self):
        return f'{self.temp}'


class Report:

    def __init__(self):
        data = load()
        self.datetime = dt.fromtimestamp(data['current'].pop('dt'))
        self.sun = Sun(
            arrival=dt.fromtimestamp(data['current'].pop('sunrise')),
            departure=dt.fromtimestamp(data['current'].pop('sunset'))
        )
        self.current = Hour(data['current'])
        self.hourly = {dt.fromtimestamp(hour.pop('dt')): Hour(hour) for hour in data.pop('hourly')}

    def __str__(self):
        ret  = f'{self.datetime.strftime("%a, %b %d %Y [%H:%M]")}\n'
        ret += f'{self.sun}'
        return ret



def fetch():
    response = api.GET(
        endpoint='http://api.openweathermap.org/data/2.5/onecall',
        APPID=os.environ["WEATHER_KEY"], **dict(gp.fetch()), units='imperial'
    ).json()
    # open cache file for writing and dump to cache
    cache.dump_json('weather.json', response)
    # return the response in case we still want it
    return response


def load():
    data = cache.load_json('weather.json')
    # otherwise, fetch, cache, and return new weather data
    return data or fetch()
