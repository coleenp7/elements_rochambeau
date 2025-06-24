from enum import Enum
from dataclasses import dataclass
import pprint

#Enum to define the element choices
class Element(Enum):
    EARTH = 1
    FIRE = 2
    WATER = 3
    AIR = 4
    SPIRIT = 5

@dataclass()
class Elements:
    first: Element
    second: Element

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

    def return_exists(self):
        return self.__exists
    
    #returns whether the player won or lost
    def return_winner(self, other):
        self.choose_winner(other)
        if self.winner == 0:
            return "lost"
        elif self.winner == 1:
            return "won"
        elif self.winner == 2:
            return "tied"
        else:
            return "an error has occurred"

    #win logic, 0 = lose, 1 = win, 2 = tie, 3 = didn't switch
    def choose_winner(self, other):

        print(f'calculating victory:')


        match(self.__choice):
            case Element.EARTH:
                match(other.return_choice()):
                    case Element.EARTH:
                        self.winner = 2
                    case Element.FIRE:
                        self.winner = 1
                    case Element.WATER:
                        self.winner = 0
                    case Element.AIR:
                        self.winner = 0
                    case Element.SPIRIT:
                        self.winner = 1
            case Element.FIRE:
                match(other.return_choice()):
                    case Element.EARTH:
                        self.winner = 0
                    case Element.FIRE:
                        self.winner = 2
                    case Element.WATER:
                        self.winner = 0
                    case Element.AIR:
                        self.winner = 1
                    case Element.SPIRIT:
                        self.winner = 1
            case Element.WATER:
                match(other.return_choice()):
                    case Element.EARTH:
                        self.winner = 1
                    case Element.FIRE:
                        self.winner = 1
                    case Element.WATER:
                        self.winner = 2
                    case Element.AIR:
                        self.winner = 0
                    case Element.SPIRIT:
                        self.winner = 0
            case Element.AIR:
                match(other.return_choice()):
                    case Element.EARTH:
                        self.winner = 1
                    case Element.FIRE:
                        self.winner = 0
                    case Element.WATER:
                        self.winner = 1
                    case Element.AIR:
                        self.winner = 2
                    case Element.SPIRIT:
                        self.winner = 0
            case Element.SPIRIT:
                match(other.return_choice()):
                    case Element.EARTH:
                        self.winner = 0
                    case Element.FIRE:
                        self.winner = 0
                    case Element.WATER:
                        self.winner = 1
                    case Element.AIR:
                        self.winner = 1
                    case Element.SPIRIT:
                        self.winner = 2