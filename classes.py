from enum import Enum
from methods import choose_winner

#Enum to define the element choices
class Element(Enum):
    EARTH = "earth"
    FIRE = "fire"
    WATER = "water"
    AIR = "air"
    SPIRIT = "spirit"

class Player:
    #defines self
    def __init__(self, name):
        self.__name = name
        self.__choice = None
        self.__exists = True
        self.winner = 3
    
    #sets player choice
    def set_choice(self, var):
        self.__choice = var

    #returns name of player
    def return_name(self):
        return self.__name
    
    #returns player choice
    def return_choice(self):
        return self.__choice

    #returns existance
    def return_exists(self):
        return self.__exists
    
    #returns win status
    def return_winner_var(self):
        return self.winner
    
    #returns whether the player won or lost
    def return_winner(player1, player2):
        win_number = choose_winner(player1, player2)
        if win_number == 0:
            player2.winner == 1
            return "lost"
        elif win_number == 1:
            player1.winner == 1
            return "won"
        elif win_number == 2:
            player2.winner == 2
            player1.winner == 2
            return "tied"
        else:
            return "** an error has occurred in return_winner **"