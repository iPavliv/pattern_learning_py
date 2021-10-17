from enum import Enum

BASIC_DEFAULTS = {
    'health': 50,
    'attack': 5,
    'defence': 0,
    'vampirism': 0,
    'heal_power': 0,
}
BASIC_ATTRIBUTES = BASIC_DEFAULTS.keys()


class CharType(Enum):
    WARRIOR = 1
    KNIGHT = 2
    DEFENDER = 3
    VAMPIRE = 4
    LANCER = 5
    HEALER = 6


class Character:
    defaults = {**BASIC_DEFAULTS}

    def __init__(self, *args, **kwargs):
        for attr in BASIC_ATTRIBUTES:
            setattr(self, attr, kwargs.get(attr) or self.defaults.get(attr, 0))
        self.max_health = self.health

    @property
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):
        pass


class Warrior(Character):
    char_type = CharType.WARRIOR


class Knight(Character):
    char_type = CharType.KNIGHT
    defaults = {
        **BASIC_DEFAULTS,
        'attack': 7,
    }


class Defender(Character):
    char_type = CharType.DEFENDER
    defaults = {
        **BASIC_DEFAULTS,
        'health': 60,
        'attack': 3,
        'defence': 2,
    }


class Vampire(Character):
    char_type = CharType.VAMPIRE
    defaults = {
        **BASIC_DEFAULTS,
        'health': 40,
        'attack': 4,
        'vampirism': 50
    }


class Lancer(Character):
    char_type = CharType.LANCER
    defaults = {
        **BASIC_DEFAULTS,
        'attack': 6,
    }


class Healer(Character):
    char_type = CharType.HEALER
    defaults = {
        **BASIC_DEFAULTS,
        'health': 60,
        'attack': 0,
        'heal_power': 2,
    }


class CharMaker:
    def create_warrior(*args, **kwargs):
        return Warrior(*args, **kwargs)

    def create_knight(*args, **kwargs):
        return Knight(*args, **kwargs)

    def create_defender(*args, **kwargs):
        return Defender(*args, **kwargs)

    def create_vampire(*args, **kwargs):
        return Vampire(*args, **kwargs)

    def create_lancer(*args, **kwargs):
        return Lancer(*args, **kwargs)

    def create_healer(*args, **kwargs):
        return Healer(*args, **kwargs)
