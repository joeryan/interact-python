# rpsls.py      implementation of rock-paper-scissors-lizard-spock
# in support of coursera.org online course
# by Joe Ryan 25 FEB 2014

from math import floor
from random import random

def name_to_number(name):
  if (name == 'rock'):
    return 0
  elif (name == 'spock'):
    return 1
  elif (name == 'paper'):
    return 2
  elif (name == 'lizard'):
    return 3
  elif (name == 'scissors'):
    return 4
  else:
    return -1

def number_to_name(number):
  if (number == 0):
    return 'rock'
  elif (number == 1):
    return 'spock'
  elif (number == 2):
    return 'paper'
  elif (number == 3):
    return 'lizard'
  elif (number == 4):
    return 'scissors'
  else:
    return None

def rpsls(choice):
  computer_choice = floor(random()*5)
  player = name_to_number(choice)
  computer = number_to_name(computer_choice)
  print("Player chooses " + choice)
  print("Computer chooses " + computer)
  
  if (computer_choice == player):
    print("Tie!")
  else:
    result = ((computer_choice - player) % 4)
    if (result < 2):
      print("Computer wins!")
    else:
      print("Player wins!")

if __name__ == '__main__':
  rpsls('scissors')
  rpsls('lizard')
  rpsls('paper')
  rpsls('spock')
  rpsls('rock')
