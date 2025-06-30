from sys import argv, exit
from classes import *
from helper_functions import *
from Element import *

def main():
    #incorrect input handling
    if len(argv) != 2:
        print ("Usage: python3 main.py number_of_players_as_a_numeral")
        exit (1)

    #sets number of players in an instance 
    number_of_players = int(argv[1], base=10)

    #error handling for too many or too few players
    if number_of_players < 2:
        print("Must have at least two players")
        exit (1)
    elif number_of_players > 5:
        print("Must have no more than five players")
        exit (1)
    
    #setting up the players
    player1 = Player(input("Enter player one's name: "))
    player2 = Player(input("Enter player two's name: "))
    if number_of_players > 2:
        player3 = Player(input("Enter player three's name: "))
    if number_of_players > 3:
        player4 = Player(input("Enter player four's name: "))
    if number_of_players > 4:
        player5 = Player(input("Enter player five's name: "))
    
    #choice menu
    print ("\nYour choices are:\nEARTH.\nFIRE.\nWATER.\nAIR.\nSPIRIT.\n")

    p1_choice = input(f"Make your choice {player1.return_name()}: ").upper()
    while not player1.return_choice():
        try:
            player1.set_choice(Element[p1_choice])
        except:
            p1_choice = input(f"Not a valid choice. Make your choice {player1.return_name()}: ").upper()

    p2_choice = input(f"Make your choice {player2.return_name()}: ").upper()
    while not player2.return_choice():
        try:
            player2.set_choice(Element[p2_choice])
        except:
            p2_choice = input(f"Not a valid choice. Make your choice {player2.return_name()}: ").upper()

    if number_of_players > 2:
        p3_choice = input(f"Make your choice {player3.return_name()}: ").upper()
        while not player3.return_choice():
            try:
                player3.set_choice(Element[p3_choice])
            except:
                p3_choice = input(f"Not a valid choice. Make your choice {player3.return_name()}: ").upper()

    if number_of_players > 3:
        p4_choice = input(f"Make your choice {player4.return_name()}: ").upper()
        while not player4.return_choice():
            try:
                player4.set_choice(Element[p4_choice])
            except:
                p4_choice = input(f"Not a valid choice. Make your choice {player4.return_name()}: ").upper()
    
    if number_of_players > 4:
        p5_choice = input(f"Make your choice {player5.return_name()}: ").upper()
        while not player5.return_choice():
            try:
                player5.set_choice(Element[p5_choice])
            except:
                p5_choice = input(f"Not a valid choice. Make your choice {player5.return_name()}: ").upper()

    print ("\n------------------------------------\n")
    #two player combat
    if number_of_players == 2:
        print (two_player_combat(player1, player2))

    #three player combat
    elif number_of_players == 3:
        print (three_player_combat(player1, player2, player3))

    #four player combat
    elif number_of_players == 4:
        print (four_player_combat(player1, player2, player3, player4))

    #five player combat
    elif number_of_players == 5:
        print (five_player_combat(player1, player2, player3, player4, player5))

    #error handling
    else:
        print ("Error in combat logic, try again")
        exit (1)
    print ("\n------------------------------------\n")

if __name__ == "__main__":
    main()