from coup import Coup
from sys import stdin


def main():
    print("Enter number of players")
    player_count = stdin.readline()

    all_actions = Coup.get_all_actions()  # general actions and character actions

    Coup.set_players(2)
    Coup.init_coup()

    print("Please enter the action you would like to take: 1-7")
    selection = stdin.readline()

    #  request block from the player who is targeted
    #  if no block is issued take the action
    #  if no challenge is issued take the action

    current_player = Coup.get_player_turn()

    #  check to see if action requires an affected player

    current_player.coins = 9
    if int(selection) in all_actions:
        influence = all_actions[int(selection)].effect(current_player, Coup.players[-1])
        Coup.remove_influence(Coup.players[-1], influence[-1])

        [print(c) for c in Coup.players[-1].influence]
    else:
        print("Invalid action chosen.")

    return

main()
