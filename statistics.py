class Statistics:
    __instance = None

    def __init__(self):
        self.score_player = 0
        self.score_computer = 0
        Statistics.__instance = self

    @staticmethod
    def get_instance():
        if not Statistics.__instance:
            Statistics()
        return Statistics.__instance

    def increase_score(self, result):
        if result:
            self.score_player += 1
        else:
            self.score_computer += 1

    def show_score(self):
        return f'Player: {self.score_player}; Computer: {self.score_computer}'
