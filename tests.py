import unittest
from classes import *
from helper_functions import *

class TestPlay(unittest.TestCase):
    #test logic for underlying logic

    def test_two_player_earth_tie(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.EARTH)
        self.assertEqual(player1.return_winner(player2), "tied")

    def test_two_player_water_tie(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.WATER)
        self.assertEqual(player1.return_winner(player2), "tied")
    
    def test_two_player_air_tie(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.AIR)
        self.assertEqual(player1.return_winner(player2), "tied")

    def test_two_player_fire_tie(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.FIRE)
        self.assertEqual(player1.return_winner(player2), "tied")

    def test_two_player_spirit_tie(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(player1.return_winner(player2), "tied")

    def test_two_player_earth_fire(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.FIRE)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_earth_water(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.WATER)
        self.assertEqual(player1.return_winner(player2), "lost")
    
    def test_two_player_earth_air(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.AIR)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_earth_spirit(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_fire_earth(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.EARTH)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_fire_water(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.WATER)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_fire_air(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.AIR)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_fire_spirit(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_water_earth(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.EARTH)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_water_fire(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.FIRE)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_water_air(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.AIR)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_water_spirit(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_air_earth(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.EARTH)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_air_fire(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.FIRE)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_air_water(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.WATER)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_air_spirit(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_spirit_earth(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.EARTH)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_spirit_fire(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.FIRE)
        self.assertEqual(player1.return_winner(player2), "lost")

    def test_two_player_spirit_water(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.WATER)
        self.assertEqual(player1.return_winner(player2), "won")

    def test_two_player_spirit_air(self):
        player1 = Player("Ally")
        player2 = Player("Billy")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.AIR)
        self.assertEqual(player1.return_winner(player2), "won")

    #test logic for plaintext enum
    def test_enum_earth(self):
        player1 = Player("Addie")
        player1.set_choice(Element.EARTH)
        self.assertEqual(player1.return_choice_text(), "earth")

    def test_enum_air(self):
        player1 = Player("Addie")
        player1.set_choice(Element.AIR)
        self.assertEqual(player1.return_choice_text(), "air")

    def test_enum_fire(self):
        player1 = Player("Addie")
        player1.set_choice(Element.FIRE)
        self.assertEqual(player1.return_choice_text(), "fire")

    def test_enum_water(self):
        player1 = Player("Addie")
        player1.set_choice(Element.WATER)
        self.assertEqual(player1.return_choice_text(), "water")

    def test_enum_spirit(self):
        player1 = Player("Addie")
        player1.set_choice(Element.SPIRIT)
        self.assertEqual(player1.return_choice_text(), "spirit")

    #test logic for two player combat
    def test_two_player_logic_earth_one(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.EARTH)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose earth and tied the match against Blake who chose earth.")
    
    def test_two_player_logic_earth_two(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.AIR)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose earth and lost the match against Blake who chose air.")

    def test_two_player_logic_earth_three(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose earth and won the match against Blake who chose spirit.")
    
    def test_two_player_logic_earth_four(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.WATER)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose earth and lost the match against Blake who chose water.")
    
    def test_two_player_logic_earth_five(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.FIRE)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose earth and won the match against Blake who chose fire.")
    
    def test_two_player_logic_fire_one(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.AIR)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose fire and won the match against Blake who chose air.")
    
    def test_two_player_logic_fire_two(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.FIRE)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose fire and tied the match against Blake who chose fire.")
    
    def test_two_player_logic_fire_three(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.WATER)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose fire and lost the match against Blake who chose water.")
    
    def test_two_player_logic_fire_four(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.EARTH)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose fire and lost the match against Blake who chose earth.")
    
    def test_two_player_logic_fire_five(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.FIRE)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose fire and won the match against Blake who chose spirit.")
    
    def test_two_player_logic_water_one(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.EARTH)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose water and won the match against Blake who chose earth.")
    
    def test_two_player_logic_water_two(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.FIRE)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose water and won the match against Blake who chose fire.")
    
    def test_two_player_logic_water_three(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.WATER)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose water and tied the match against Blake who chose water.")

    def test_two_player_logic_water_four(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.AIR)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose water and lost the match against Blake who chose air.")

    def test_two_player_logic_water_five(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.WATER)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose water and lost the match against Blake who chose spirit.")
    
    def test_two_player_logic_air_one(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.EARTH)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose air and won the match against Blake who chose earth.")

    def test_two_player_logic_air_two(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.FIRE)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose air and lost the match against Blake who chose fire.")
    
    def test_two_player_logic_air_three(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.WATER)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose air and won the match against Blake who chose water.")
    
    def test_two_player_logic_air_four(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.AIR)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose air and tied the match against Blake who chose air.")
    
    def test_two_player_logic_air_five(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.SPIRIT)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose air and lost the match against Blake who chose spirit.")

    def test_two_player_logic_spirit_one(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.EARTH)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose spirit and lost the match against Blake who chose earth.")

    def test_two_player_logic_spirit_two(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.FIRE)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose spirit and lost the match against Blake who chose fire.")

    def test_two_player_logic_spirit_three(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.WATER)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose spirit and won the match against Blake who chose water.")

    def test_two_player_logic_spirit_four(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.AIR)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose spirit and won the match against Blake who chose air.")

    def test_two_player_logic_spirit_five(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.SPIRIT)
        player2.set_choice(Element.EARTH)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose spirit and lost the match against Blake who chose earth.")

    #test logic for three player combat
    def test_three_player_logic_tie(self):
        player1 = Player("Alexander")
        player2 = Player("Brooklyn")
        player3 = Player("Camden")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.EARTH)
        player3.set_choice(Element.EARTH)
        self.assertEqual(three_player_combat(player1, player2, player3), "Alexander chose earth and tied the match against Brooklyn who chose earth.\nThere was a tie. No second match.\n")

    def test_three_player_logic_one(self):
        player1 = Player("Alexander")
        player2 = Player("Brooklyn")
        player3 = Player("Camden")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.AIR)
        player3.set_choice(Element.FIRE)
        self.assertEqual(three_player_combat(player1, player2, player3), "Alexander chose earth and lost the match against Brooklyn who chose air.\nBrooklyn chose air and lost the match against Camden who chose fire.\n")

    def test_three_player_logic_two(self):
        player1 = Player("Alexander")
        player2 = Player("Brooklyn")
        player3 = Player("Camden")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.WATER)
        player3.set_choice(Element.SPIRIT)
        self.assertEqual(three_player_combat(player1, player2, player3), "Alexander chose earth and lost the match against Brooklyn who chose water.\nBrooklyn chose water and lost the match against Camden who chose spirit.\n")

    def test_three_player_logic_three(self):
        player1 = Player("Alexander")
        player2 = Player("Brooklyn")
        player3 = Player("Camden")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.AIR)
        player3.set_choice(Element.WATER)
        self.assertEqual(three_player_combat(player1, player2, player3), "Alexander chose earth and lost the match against Brooklyn who chose air.\nBrooklyn chose water and won the match against Camden who chose spirit.\n")

    def test_three_player_logic_four(self):
        player1 = Player("Alexander")
        player2 = Player("Brooklyn")
        player3 = Player("Camden")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.SPIRIT)
        player3.set_choice(Element.FIRE)
        self.assertEqual(three_player_combat(player1, player2, player3), "Alexander chose earth and won the match against Brooklyn who chose spirit.\nAlexander chose earth and won the match against Camden who chose fire.\n")


    def test_three_player_logic_five(self):
        player1 = Player("Alexander")
        player2 = Player("Brooklyn")
        player3 = Player("Camden")
        player1.set_choice(Element.AIR)
        player2.set_choice(Element.WATER)
        player3.set_choice(Element.SPIRIT)
        self.assertEqual(three_player_combat(player1, player2, player3), "Alexander chose air and won the match against Brooklyn who chose water.\nAlexander chose air and lost the match against Camden who chose spirit.\n")

    #test logic for four player combat
    def test_four_player_logic_tie(self):
        player1 = Player("Archer")
        player2 = Player("Bryce")
        player3 = Player("Cora")
        player4 = Player("Daxton")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.EARTH)
        player3.set_choice(Element.WATER)
        player4.set_choice(Element.AIR)
        self.assertEqual(four_player_combat(player1, player2, player3, player4), "Archer chose earth and tied the match against Bryce who chose earth.\nCora chose water and lost the match against Daxton who chose air.\nThere was a tie. No third match.\n")


    def test_four_player_logic_one(self):
    def test_four_player_logic_two(self):
    def test_four_player_logic_three(self):
    def test_four_player_logic_four(self):
    def test_four_player_logic_five(self):

    #test logic for five player combat
    def test_five_player_logic_tie(self):
    def test_five_player_logic_one(self):
    def test_five_player_logic_two(self):
    def test_five_player_logic_three(self):
    def test_five_player_logic_four(self):
    def test_five_player_logic_five(self):