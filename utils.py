import json
from functools import wraps
from character import CharMaker

FACTORY_MAP = {
    "warrior": CharMaker.create_warrior,
    "knight": CharMaker.create_knight,
    "defender": CharMaker.create_defender,
    "vampire": CharMaker.create_vampire,
    "lancer": CharMaker.create_lancer,
    "healer": CharMaker.create_healer,
}


def create_fighter(char_params):
    return FACTORY_MAP[char_params.char_type](name=char_params.char_name)


def make_log(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        log = f(*args, **kwargs)
        return json.dumps(log)
    return wrapper
