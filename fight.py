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
