from classes import *
from Element import *

#win logic, 0 = lose, 1 = win, 2 = tie, 3 = didn't switch
def choose_winner(player1, player2):
    match(player1.return_choice()):
        case Element.EARTH:
            match(player2.return_choice()):
                case Element.EARTH:
                    return 2
                case Element.FIRE:
                    return 1
                case Element.WATER:
                    return 0
                case Element.AIR:
                    return 0
                case Element.SPIRIT:
                    return 1
        case Element.FIRE:
            match(player2.return_choice()):
                case Element.EARTH:
                    return 0
                case Element.FIRE:
                    return 2
                case Element.WATER:
                    return 0
                case Element.AIR:
                    return 1
                case Element.SPIRIT:
                    return 1
        case Element.WATER:
            match(player2.return_choice()):
                case Element.EARTH:
                    return 1
                case Element.FIRE:
                    return 1
                case Element.WATER:
                    return 2
                case Element.AIR:
                    return 0
                case Element.SPIRIT:
                    return 0
        case Element.AIR:
            match(player2.return_choice()):
                case Element.EARTH:
                    return 1
                case Element.FIRE:
                    return 0
                case Element.WATER:
                    return 1
                case Element.AIR:
                    return 2
                case Element.SPIRIT:
                    return 0
        case Element.SPIRIT:
            match(player2.return_choice()):
                case Element.EARTH:
                    return 0
                case Element.FIRE:
                    return 0
                case Element.WATER:
                    return 1
                case Element.AIR:
                    return 1
                case Element.SPIRIT:
                    return 2

def two_player_combat(player1, player2):
    return (f"{player1.return_name()} chose {player1.return_choice_text()} and {player1.return_winner(player2)} the match against {player2.return_name()} who chose {player2.return_choice_text()}.\n")

def three_player_combat (player1, player2, player3):
    combat1 = two_player_combat(player1, player2)
        
    if player1.return_winner_var() == 1:
        combat2 = two_player_combat(player1, player3)
        return (f"{combat1}{combat2}")
    elif player2.return_winner_var() == 1:
        combat2 = two_player_combat(player2, player3)
        return (f"{combat1}{combat2}")
    elif player2.return_winner_var() == 2 or player1.return_winner_var() == 2:
        combat2 = "There was a tie. No second match.\n"
        return (f"{combat1}{combat2}")
    else:
        print("There was an error in three person combat system.")

def four_player_combat(player1, player2, player3, player4):
        combat1 = two_player_combat(player1, player2)
        combat2 = two_player_combat(player3, player4)
        
        if player1.return_winner_var() == 1 and player3.return_winner_var() == 1:
            combat3 = two_player_combat(player1, player3)
            return (f"{combat1}{combat2}{combat3}")
        elif player2.return_winner_var() == 1 and player3.return_winner_var() == 1:
            combat3 = two_player_combat(player2, player3)
            return (f"{combat1}{combat2}{combat3}")
        elif player1.return_winner_var() == 1 and player4.return_winner_var() == 1:
            combat3 = two_player_combat(player1, player4)
            return (f"{combat1}{combat2}{combat3}")
        elif player2.return_winner_var() == 1 and player4.return_winner_var() == 1:
            combat3 = two_player_combat(player2, player4)
        elif player2.return_winner_var() == 2 or player3.return_winner_var() == 2:
            combat3 = "There was a tie. No third match.\n"
            return (f"{combat1}{combat2}{combat3}")
        else:
            print("There was an error in the four person combat system.")

def five_player_combat(player1, player2, player3, player4, player5):
        combat1 = two_player_combat(player1, player2)
        combat2 = two_player_combat(player3, player4)
        
        if player1.return_winner_var() == 1:
            combat3 = two_player_combat(player1, player5)
        elif player2.return_winner_var() == 1:
            combat3 = two_player_combat(player2, player5)
        else:
            print("There was an error in the first 5th player match")
        
        if player5.return_winner_var() == 1:
            if player3.return_winner_var() == 1:
                combat4 = two_player_combat(player3, player5)
            elif player4.return_winner_var == 1:
                combat4 = two_player_combat(player4, player5)
            else:
                print("There was an error in the second 5th player match")

        if player1.return_winner_var() == 1:
            if player3.return_winner_var() == 1:
                combat5 = two_player_combat(player1, player3)
                return (f"{combat1}{combat2}{combat3}{combat4}{combat5}")
            elif player4.return_winner_var() == 1:
                combat5 = two_player_combat(player1, player4)
                return (f"{combat1}{combat2}{combat3}{combat4}{combat5}")
            else:
                print("There was an error in player 1 match 3")
        
        if player2.return_winner_var() == 1:
            if player3.return_winner_var() == 1:
                combat5 = two_player_combat(player2, player3)
                return (f"{combat1}{combat2}{combat3}{combat4}{combat5}")
            elif player4.return_winner_var() == 1:
                combat5 = two_player_combat(player2, player4)
                return (f"{combat1}{combat2}{combat3}{combat4}{combat5}")
            else:
                print("There was an error in player 2 match 3")