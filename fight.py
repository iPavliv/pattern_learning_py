from character import Warrior, Knight, Defender, Vampire, Lancer, Healer


def vampire_health_restoration(target, damage):
    vamp_restoration = int(round((damage * target.vampirism) / 100))
    target.health = min(target.health + vamp_restoration, target.max_health)


def fight(fighter_1, fighter_2, debug=False):
    attacker = fighter_1
    defender = fighter_2

    while True:
        damage = attacker.attack - defender.defence
        if damage > 0:
            defender.health -= damage
            vampire_health_restoration(target=attacker, damage=damage)
            if debug:
                print(f'damage: {damage} to {defender.char_type}, defenders health: {defender.health}')

            if not defender.is_alive:
                return f"defender {defender.char_type} died"  # defender == fighter_2

        attacker, defender = defender, attacker


war = Warrior()
kni = Knight()
defe = Defender()
vamp = Vampire()
lanc = Lancer()
heal = Healer()
result = fight(vamp, heal, True)
print(result)
