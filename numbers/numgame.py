# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random

target = 0
max_range = 100

# helper function to start and restart the game
def new_game():
    global target
    target = random.randint(0, max_range)


# define event handlers for control panel
def range100():
    global max_range 
    max_range = 100
    new_game()
    

def range1000():
    global max_range
    max_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    pass

    
# create frame


# register event handlers for control elements and start frame


# call new_game 
if __name__ == "__main__":
    new_game()
    print(target)
    range1000()
    print(target)
    range100()
    print(target)
# always remember to check your completed program against the grading rubric
