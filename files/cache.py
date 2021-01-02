from pathlib import Path
import json, os


CACHE_PATH = Path.home() / '.cache'


def load_json(path):
    if os.path.exists(CACHE_PATH / path):
        with open(CACHE_PATH / path, 'r') as cache_file:
            return json.load(cache_file)


def dump_json(path, obj):
    with open(CACHE_PATH / path, 'w') as cache_file:
        json.dump(obj, cache_file)
