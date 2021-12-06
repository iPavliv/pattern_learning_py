from statistics import Statistics


def vampire_health_restoration(target, damage):
    vamp_restoration = int(round((damage * target.vampirism) / 100))
    target.health = min(target.health + vamp_restoration, target.max_health)


def fight(fighter_1, fighter_2):
    fight_log = []
    attacker = fighter_1
    defender = fighter_2

    while True:
        damage = attacker.attack - defender.defence
        if damage > 0:
            defender.health -= damage
            vampire_health_restoration(target=attacker, damage=damage)
            fight_log.append(f"{damage} damage to {defender.name} {defender.char_type}, health: {defender.health}")

            if not defender.is_alive:
                fight_log.append(f"{attacker.name} {attacker.char_type} wins!")  # defender == fighter_2
                return fight_log

        attacker, defender = defender, attacker


class FightAdapter:
    def __init__(self, fighter_1, fighter_2):
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.result = None

    def fight(self):
        """
        :return: True if first fighter won, False otherwise
        """
        fight_log = fight(self.fighter_1, self.fighter_2)
        name, char_type, _ = fight_log[-1].split(' ')
        self.result = name == self.fighter_1.name and char_type == self.fighter_1.char_type

        stats = Statistics.get_instance()
        stats.increase_score(self.result)

        return self.result


def battle(army_1, army_2):
    army_1.prepare_to_battle()
    army_2.prepare_to_battle()

    while army_1.anyone_alive:
        unit_1 = army_1.units[0]
        if army_2.anyone_alive:
            unit_2 = army_2.units[0]
            fight_adpt = FightAdapter(unit_1, unit_2)
            first_won = fight_adpt.fight()

            if first_won:
                army_2.units.pop(unit_2)
            else:
                army_1.units.pop(unit_1)
        else:
            return True
    return False
