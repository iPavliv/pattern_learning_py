from character import CharMaker

FACTORY_MAP = {
    "warrior": CharMaker.create_warrior,
    "knight": CharMaker.create_knight,
    "defender": CharMaker.create_defender,
    "vampire": CharMaker.create_vampire,
    "lancer": CharMaker.create_lancer,
    "healer": CharMaker.create_healer,
}


def create_fighter(char_type, char_name):
    return FACTORY_MAP[char_type](name=char_name)
