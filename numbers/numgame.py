# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random

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

# http://www.codeskulptor.org/#user39_xebz8UsTuy_7.py


