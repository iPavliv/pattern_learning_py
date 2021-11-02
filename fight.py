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


def battle(army_1, army_2):
    army_1.prepare_to_battle()
    army_2.prepare_to_battle()
    while army_1.anyone_alive:
        unit_1 = army_1.units[0]
        if army_2.anyone_alive:
            unit_2 = army_2.units[0]
            if fight(unit_1, unit_2): # make adapter to make fight return bool value
                army_2.units.pop(unit_2)
            else:
                army_1.units.pop(unit_1)
        else:
            return True
    return False
