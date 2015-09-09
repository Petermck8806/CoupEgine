from player import Player
import action  # using from action import class causes circular reference.
from enumerations import GameType
from collections import deque
from random import shuffle


def detect_winner(players):
    if len(players) > 0:
        return len([p for p in players if not p.out]) == 1
    return False


def populate_deck():
        return [action.Captain(), action.Captain(), action.Captain(),
                        action.Duke(), action.Duke(), action.Duke(),
                        action.Ambassador(), action.Ambassador(), action.Ambassador(),
                        action.Assassin(), action.Assassin(), action.Assassin(),
                        action.Contessa(), action.Contessa(), action.Contessa()]
     # will work on this later, variant coup game should be made.


class Coup:
    def __init__(self):
        self.player_count = 0
        self.players = deque([])
        self.court_deck = deque([])
        self.treasury = 25
        self.court_deck_max = 15
        self.winner = detect_winner(self.players)

    def init_coup(self):
        deck = populate_deck()
        shuffle(deck)
        self.court_deck = deque(deck)

        if self.player_count > 1:
            [self.players.append(Player(item + 1, [self.draw(), self.draw()]))
                for item in range(0, self.player_count)]

    def set_players(self, player_count):
        self.player_count = player_count

    def get_player_turn(self):
        if len(self.players) < 1:
            return
        else:
            if not detect_winner(self.players):
                current_player = self.players.popleft()
                while current_player.out:
                    self.players.append(current_player)
                    current_player = self.players.popleft()
                return current_player

    def shuffle(self):
        shuffle(self.deck)

    def draw(self):
        if len(self.court_deck) == 0:
            return
        return self.court_deck.popleft()

    def return_cards(self, cards):
        if len(self.deck) >= self.court_deck_max:
            return
        self.deck.extend(cards)

    def draw_exchange(self):
        if len(self.deck) <= 1:
            return
        return [self.deck.draw(), self.deck.draw()]

    def distinct_general_actions(self):
        return [action.Income(), action.ForeignAid, action.Coup()]

    def distinct_character_actions(self):
        return list(set([a for a in self.court_deck if a.type == action.ActionType.Character]))

    def get_all_actions(self):
        return {1: action.Income(), 2: action.ForeignAid(), 3: action.Coup(),
                4: action.Duke(), 5: action.Assassin(), 6: action.Ambassador(),
                7: action.Captain()}

    def remove_influence(self, player, influence):
        player.influence.remove(influence)

# class CoupVariant:
#     def __init__(self):
#         self.player_count = 2 # 2 players only in the variant
#         self.players = []
#
#     def start_game(self):

Coup = Coup()


