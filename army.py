class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, number):
        for unit in range(number):
            self.units.append(unit_type())

    def prepare_to_battle(self):
        self.units = self.units[::-1]

    @property
    def anyone_alive(self):
        return len(self.units) > 0
