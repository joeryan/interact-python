# tests for number guessing game numgame.py
import unittest
from numgame import *

class NumgameTestCase(unittest.TestCase):
    def setUp(self):
<<<<<<< HEAD
       new_game()

    def test_new_game(self):
        self.assertTrue((target >= 0) & (target <= 100))

    def test_range1000(self):
        range1000()
        self.assertTrue(max_range == 1000)
        
=======
        pass 

    def test_new_game_100(self):
        #  game.new_game()
        game = numgame.NumGame()
        self.assertTrue(game.target >= 0)
        self.assertTrue(game.target <= 100)
>>>>>>> a35fdb67b5fc861aeb580887e9021774ca45d280

    def test_range1000(self):
        game = numgame.NumGame()
        game.range1000()
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

    
