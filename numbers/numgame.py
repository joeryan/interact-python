# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random

<<<<<<< HEAD
secret_number = 0
max_range = 100
guess_message = "Number range 0 - 100"
remaining_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number
    global remaining_guesses
    
    secret_number = random.randint(0, max_range)
    if max_range == 100:
        remaining_guesses = 7
    else:
        remaining_guesses = 10
    print("New game. " + guess_message)
    remaining()



# define event handlers for control panel
def range100():
    global max_range 
    max_range = 100
    new_game()
=======
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
>>>>>>> a35fdb67b5fc861aeb580887e9021774ca45d280
    

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
<<<<<<< HEAD

# http://www.codeskulptor.org/#user39_xebz8UsTuy_7.py


=======
    game = NumGame()
    print(game.target)
    game.range1000()
    print(game.target)
    game.range100()
    print(game.target)
# always remember to check your completed program against the grading rubric
>>>>>>> a35fdb67b5fc861aeb580887e9021774ca45d280
