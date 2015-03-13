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
        game.range1000()
        self.assertTrue(game.target >= 0)
        self.assertTrue(game.target <= 1000)
 
if __name__ == "__main__":
    unittest.main()

    
