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


class Warrior(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_type = CharType.WARRIOR


class Knight(Character):
    def __init__(self, *args, damage=7, **kwargs):
        super().__init__(damage=damage, **kwargs)
        self.char_type = CharType.KNIGHT


class Defender(Character):
    def __init__(self, *args, health=60, damage=3, defence=2, **kwargs):
        super().__init__(health=health, damage=damage, defence=defence, **kwargs)
        self.char_type = CharType.DEFENDER


class Vampire(Character):
    def __init__(self, *args, health=40, damage=4, vampirism=50, **kwargs):
        super().__init__(health=health, damage=damage, vampirism=vampirism, **kwargs)
        self.char_type = CharType.VAMPIRE


class Lancer(Character):
    def __init__(self, *args, damage=6, **kwargs):
        super().__init__(damage=damage, **kwargs)
        self.char_type = CharType.LANCER


class Healer(Character):
    def __init__(self, *args, health=60, heal_power=2, **kwargs):
        super().__init__(health=health, heal_power=heal_power, **kwargs)
        self.char_type = CharType.HEALER
