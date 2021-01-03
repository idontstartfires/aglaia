from datetime import datetime as dt, timedelta as td


class CelestialBody:

    arrival: dt
    departure: dt

    duration = property(lambda self: self.departure - self.arrival)

    def __init__(self, arrival: dt, departure: dt):
        self.arrival, self.departure = arrival, departure


class Sun(CelestialBody):

    @property
    def period(self):
        now = dt.now()
        tr = td(minutes=10)
        if self.up + tr < now < self.down - tr:
            return 'day'
        if self.up - tr < now < self.up + tr:
            return 'dawn'
        if self.down - tr < now < self.down + tr:
            return 'dusk'
        else:
            return 'night'


    def __str__(self):
        return (
            f'sunrise @ {self.arrival.time()}\n'
            f'sunset  @ {self.departure.time()}'
        )

class Moon(CelestialBody):

    phase: str
    name: str

    def __str__(self):
        return (
            f'moonrise @ {self.arrival.time()}\n'
            f'moonset  @ {self.departure.time()}'
        )
