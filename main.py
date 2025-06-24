from sys import argv, exit
from classes import *

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
    
    print ("\nYour choices are:\nEARTH.\nFIRE.\nWATER.\nAIR.\nSPIRIT.\n")
    p1_choice = input(f"Make your choice {player1.return_name()}: ").upper()
    while not player1.return_choice():
        try:
            player1.set_choice(Element[p1_choice])
        except:
            print("not a valid choice")
    p2_choice = input(f"Make your choice {player2.return_name()}: ").upper()
    while not player2.return_choice():
        try:
            player2.set_choice(Element[p2_choice])
        except:
            print("not a valid choice")

    print(player1.return_winner(player2))

    print ("------------------------------------\n")
    if number_of_players == 2:
        print(f"{player1.return_name()} chose {player1.return_choice()} and {player1.return_winner(player2)} the match against {player2.return_name()} who chose {player2.return_choice()}.")
    else:
        print("Error in combat logic, try again")
        exit (1)
    print ("\n------------------------------------\n")

if __name__ == "__main__":
    main()