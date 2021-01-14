from files import DATA

UNIT_ROOT = DATA / 'units'

class Unit:

    symbol: str
    name: str
    category: str

    def __init__(self, symbol):
        self.symbol = symbol
        directory = UNIT_ROOT.load('directory.json')
        for category, symbols in directory.items():
            if symbol in symbols:
                self.category = category
                break
        else:
            raise ValueError('unit symbol not handled')
        data = UNIT_ROOT.load(f'{self.category}.json').get(self.symbol)
        self.name = data.get('name')
        self.factor = data.get('factor')
        self.offset = data.get('offset')

    def conversion(self, target):
        if target.category != self.category:
            raise TypeError('wrong unit category')
        return lambda value: (target.factor * (value - self.offset) / self.factor) + target.offset
