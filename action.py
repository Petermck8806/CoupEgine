from enumerations import ActionType
import coup


class Action:
    name = ""
    desc = ""
    counteraction = []
    coins_required = 0
    type = None
    challenge = False

    def __str__(self):
        return self.__class__.__name__

    def effect(self, player, affected=None):
        return False, None


# General Actions
class Income(Action):
    name = "Income"
    desc = "Take 1 coin"
    type = ActionType.General
    challenge = False

    def effect(self, player, affected=None):
        player.coins += 1
        return True, "Successful"


class ForeignAid(Action):
    name = "Foreign Aid"
    desc = "Take 2 coins"
    type = ActionType.General
    challenge = False

    def effect(self, player, affected=None):
        player.coins += 2
        return True, "Successful"


class Coup(Action):
    name = "Coup"
    desc = "Pay 7 coins. Choose player to lose influence."
    type = ActionType.General
    coins_required = 7
    challenge = False

    def effect(self, player, affected): #  this needs work still
        if player.coins < self.coins_required:
            return False, "Failed"
        else:
            player.coins -= self.coins_required
            return affected.lose_influence()

        return True, "Successful"

# Character Actions
class Duke(Action):
    name = "Tax"
    desc = "Take 3 coins"
    type = ActionType.Character
    counteraction = ["Foreign Aid"]
    challenge = True

    def effect(self, player, affected=None):
        player.coins += 3
        return True, "Successful"


class Assassin(Action):
    name = "Assassinate"
    desc = "Pay 3 coins. Choose player to lose influence."
    type = ActionType.Character
    coins_required = 3
    counteraction = []
    challenge = True

    def effect(self, player, affected):
        if player.coins < self.coins_required:
            return False, "Failed"
        else:
            player.coins -= self.coins_required
            affected.lose_influence()

        return True, "Successful"


class Ambassador(Action):
    name = "Exchange"
    desc = "Exchange cards with Court Deck"
    type = ActionType.Character
    counteraction = ["Steal"]
    challenge = True

    def effect( self, player, affected=None):
        if len(coup.Coup.court_deck) < 2:
            return [], "Failed"

        options = coup.Coup.draw_exchange().append(player.influence)
        return options

class Contessa(Action):
    name = "Contessa"
    desc = "Blocks Assassination"
    type = ActionType.Character
    counteraction = ["Assassinate"]
    challenge = True

    def effect(self, player, affected=None):
        return True, "Successful"


class Captain(Action):
    name = "Steal"
    desc = "Take 2 coins from another player."
    type = ActionType.Character
    counteraction = ["Steal"]
    challenge = True

    def effect(self, player, affected):
        if affected.coins >= 2:
            player.coins += 2
            affected.coins -= 2
        elif affected.coins == 1:
            player.coins += 1
            affected.coins -= 1
