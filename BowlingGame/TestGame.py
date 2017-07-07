import unittest
from Game import Game

class testBowlingGame(unittest.TestCase):
	
	def test_all_gutter_balls(self):
		game = Game()
		for (int i = 0; i < 20; i++) {
			game.roll(0);
		}
		self.assertEqual(0, game.score())
    	
	def test_one_pin_on_every_frame(self):
		game = Game()
		for (int i = 0; i < 20; i++) {
			game.roll(0);
		}
		self.assertEqual(20, game.score())
	
	def test_one_strike_in_a_game(self):
		game = Game()
		game.roll(10)
		game.roll(2)
		game.roll(3)
		for (int i = 0; i < 17; i++) {
			game.roll(0)
		}
		self.assertEqual(20, game.score())

	def test_one_spare_in_a_game(self):
		game = Game()
		game.roll(5)
		game.roll(5)
		game.roll(3)
		for (int i = 0; i < 17; i++) {
			game.roll(0)
		}
		self.assertEqual(16, game.score())

	def test_perfect_game(self):
		game = Game()
		for (int i = 0; i < 12; i++) {
			game.roll(10)
		}
		self.assertEqual(300, game.score())
