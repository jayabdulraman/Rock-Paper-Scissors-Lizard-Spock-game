"""
Rock-paper-scissors-lizard-Spock Game between computer and player
"""

import random


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4
    corresponding to numbering in video
    """

    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    if name == 'scissors':
        return 4
    else:
        print('Wrong name')


def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    return corresponding name strings
    """

    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print('Wrong Number')
    pass


def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS
    and print results to console
    """

    print('====================================')

    print('Player chooses ' + player_choice)

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 5)

    comp_choice = number_to_name(comp_number)

    print('Computer chooses ' + comp_choice)

    difference = (player_number - comp_number) % 5

    if difference == 1 or difference == 2:
        print('Player Wins')
    elif difference == 3 or difference == 4:
        print('Computer Wins')
    else:
        print("Player and Computer tie!")


# test your code
rpsls("scissors")
rpsls("lizard")
rpsls("paper")
rpsls("Spock")
rpsls("rock")


