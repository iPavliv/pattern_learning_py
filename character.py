from enum import Enum


class CharType(Enum):
    WARRIOR = 1
    KNIGHT = 2
    DEFENDER = 3
    VAMPIRE = 4
    LANCER = 5
    HEALER = 6


class Character:
    def __init__(self, *args, **kwargs):
        self.health = kwargs.get("health", 50)
        self.damage = kwargs.get("damage", 5)
        self.defence = kwargs.get("defence", 0)
        self.vampirism = kwargs.get("vampirism", 0)
        self.heal_power = kwargs.get("heal_power", 0)

    @property
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):
        pass
