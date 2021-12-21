from character import CharMaker
from fight import FightAdapter
from statistics import Statistics


class Menu:
    def __init__(self):
        self.stats = Statistics.get_instance()
        self.char_maker = CharMaker()

    def play(self):
        # create option to choose fighter
        fighter_1 = self.char_maker.create_knight(name='Joe')
        fighter_2 = self.char_maker.create_warrior(name='Jack')
        fight_adpt = FightAdapter(fighter_1, fighter_2)
        result = fight_adpt.fight()
        score = self.stats.show_score()
        return score


if __name__ == '__main__':
    menu = Menu()
    res = menu.play()
