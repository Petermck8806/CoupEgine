
class Player:
    def __init__(self, identity, cards=[]):
        self.influence = cards
        self.coins = 2
        self.player_id = identity
        self.out = False

    def __str__(self):
        return "Influence %"

    # should change this to allow the player to choose the lost influence
    def lose_influence(self):
        if len(self.influence) != 0:
            if len(self.influence) == 1:
                self.out = True
                return self.influence.pop()
            elif len(self.influence) > 1:
                return self.influence
        elif not self.out:
            self.out = True
