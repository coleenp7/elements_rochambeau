import unittest
from classes import *
from methods import *

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

    #test logic for two player combat
    def test_two_player_logic_one(self):
        player1 = Player("Aria")
        player2 = Player("Blake")
        player1.set_choice(Element.EARTH)
        player2.set_choice(Element.EARTH)
        self.assertEqual(two_player_combat(player1, player2), "Aria chose Element.EARTH and tied the match against Blake who chose Element.EARTH")