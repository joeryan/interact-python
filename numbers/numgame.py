# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random


class NumGame:
  def  __init__(self, secret_range=100):
    self.max_range = secret_range
    self.target =  random.randint(0, self.max_range)
#    self.new_game()

  # helper function to start and restart the game
  def new_game(self, secret_range=100):
    self.max_range = secret_range
    self.target = random.randint(0, self.max_range)

  def check_guess(self, guess):
    return guess - self.target


# call new_game 
if __name__ == "__main__":
    # http://www.codeskulptor.org/#user39_xebz8UsTuy_7.py
    game = NumGame()
    print(game.target)
    print(game.max_range)
    game.new_game(1000)
    print(game.max_range)
    print(game.target)
    game.new_game(100)
    print(game.max_range)
    print(game.target)

# always remember to check your completed program against the grading rubric
