# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random


class NumGame:
  def  __init__(self):
    self.max_range = 100
    self.target =  random.randint(0, self.max_range)
#    self.new_game()

  # helper function to start and restart the game
  def new_game(self):
    self.target = random.randint(0, self.max_range)

  # define event handlers for control panel
  def range100(self):
    self.max_range = 100
    self.new_game()

  def range1000(self):
    self.max_range = 1000
    self.new_game()
    
  def check_guess(self, guess):
    return guess - self.target




    
# create frame for graphical game play


# register event handlers for control elements and start frame


# call new_game 
if __name__ == "__main__":
    # http://www.codeskulptor.org/#user39_xebz8UsTuy_7.py
    game = NumGame()
    print(game.target)
    game.range1000()
    print(game.target)
    game.range100()
    print(game.target)

