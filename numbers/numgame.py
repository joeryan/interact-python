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
    if (guess < self.target): 
      return -1
    elif (guess > self.target):
      return 1
    else:
      return 0

    # main game logic goes here	
    
# create frame for graphical game play


# register event handlers for control elements and start frame


# call new_game 
if __name__ == "__main__":
    game = NumGame()
    print(game.target)
    game.range1000()
    print(game.target)
    game.range100()
    print(game.target)
# always remember to check your completed program against the grading rubric
