from sys import argv, exit
from classes import *

def main():
    print('game started')
    #incorrect input handling
    if len(argv) != 2:
        print ("Usage: python3 main.py number_of_players_as_a_numeral")
        exit (1)

    #sets number of players in an instance 
    number_of_players = int(argv[1], base=10)
    print(number_of_players)

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
    if number_of_players >= 2:
        player3 = Player(input("Enter player three's name: "))
    if number_of_players >=3:
        player4 = Player(input("Enter player four's name: "))
    if number_of_players >=4:
        player5 = Player(input("Enter player five's name: "))
    
    #test case, printing names
    print(f"player 1: {player1.return_name}")
    print(f"player 2: {player2.return_name}")

if __name__ == "__main__":
    main()