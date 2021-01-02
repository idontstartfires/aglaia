import json
from pathlib import Path


DATA = Path.cwd() / 'data'


def make_path(*args):
    path = DATA
    for arg in args: path /= arg
    return path


def load(*args):
    fn = args.pop()
    path = make_path
    with open(path, 'r') as f:
        return json.load(f)
