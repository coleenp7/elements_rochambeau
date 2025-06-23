from enum import Enum

#Enum to define the element choices
class Element(Enum):
    EARTH = 1
    FIRE = 2
    WATER = 3
    AIR = 4
    SPIRIT = 5

class Player:
    #defines self
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.winner = 0
    
    #sets player choice
    def set_choice(self, var):
        self.choice = var

    #returns name of player
    def return_name(self):
        return self.name
    
    #returns player choice
    def return_choice(self):
        return self.choice
    
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

    #win logic, 0 = lose, 1 = win, 2 = tie
    def choose_winner(self, other):
        match(self.choice):
            case Element.EARTH:
                match(other.choice):
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
                match(other.choice):
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
                match(other.choice):
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
                match(other.choice):
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
                match(other.choice):
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
            case _:
                print("Invalid choice")