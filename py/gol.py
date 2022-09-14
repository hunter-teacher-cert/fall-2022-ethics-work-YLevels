# gol.py
# Yeidy Levels
# CSCI 77800 Fall 2022
# collaborators: just me
# consulted: ThinkPython; w3schools

# use python random module
import random as r

# initialize our states
ALIVE = 'X'
DEAD = ' '

# create, initialize, and return empty board (all cells dead)
def createNewBoard (rows, cols):
  for i in range(rows):
