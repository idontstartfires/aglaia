import json, os
from pathlib import Path


class Directory:

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        return iter(os.listdir(self.path))

    def __len__(self):
        return len(os.listdir(self.path))

    def __contains__(self, fn):
        return os.path.exists(self.path / fn)

    def __str__(self):
        return str(self.path)

    def load(self, fn):
        if fn not in self:
            return None
        basename, *ext = fn.split('.')

        with open(self.path / fn, 'r') as cache_file:
            if ext and ext[-1] == 'json':
                return json.load(cache_file)
            else:
                return cache_file.readlines()

    def save(self, fn, data):
        basename, *ext = fn.split('.')
        with open(self.path / fn, 'w') as cache_file:
            if ext and ext[-1] == 'json':
                json.dump(data, cache_file)
            else:
                cache_file.writelines(data)

    def __truediv__(self, child):
        return Directory(self.path / child)


DATA = Directory(Path.cwd() / 'data')
HOME = Directory(Path.home())
CACHE = HOME / '.cache'
