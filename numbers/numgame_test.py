# tests for number guessing game numgame.py
import unittest
import numgame

class NumgameTestCase(unittest.TestCase):
    def setUp(self):
        pass 

    def test_new_game_100(self):
        #  game.new_game()
        game = numgame.NumGame()
        self.assertTrue(game.target >= 0)
        self.assertTrue(game.target <= 100)

    def test_range1000(self):
        game = numgame.NumGame()
        game.new_game(1000)
        self.assertTrue(game.target >= 0)
        self.assertTrue(game.target <= 1000)

    def test_check_guess_actual(self):
        game = numgame.NumGame()
        game.target = 55
        self.assertTrue(game.check_guess(55) == 0)
 
    def test_check_guess_lower(self):
        game = numgame.NumGame()
        game.target = 55
        self.assertTrue(game.check_guess(54) == -1)
 
    def test_check_guess_higher(self):
        game = numgame.NumGame()
        game.target = 55
        self.assertTrue(game.check_guess(56) == 1)
 
if __name__ == "__main__":
    unittest.main()

    
