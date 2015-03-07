# tests for number guessing game numgame.py
import unittest
from numgame import *

class NumgameTestCase(unittest.TestCase):
    def setUp(self):
       new_game()

    def test_new_game(self):
        self.assertTrue((target >= 0) & (target <= 100))

    def test_range1000(self):
        range1000()
        self.assertTrue(max_range == 1000)
        

if __name__ == "__main__":
    unittest.main()

    
