# nim.py
# Yeidy Levels
# CSCI 77800 Fall 2022
# collaborators: just me
# consulted: ThinkPython; w3schools

import random as r  #alias for random module

stones = 12

while stones > 0:
  stones_taken = int(input("How many would you like to take? You may take 1, 2, or 3 stones"))
  print(f"You took {stones_taken} stones")
  stones = stones - stones_taken
  print(f"There are {stones} stones left.")
  if stones == 0:
    print("You took the last stone. You won!")
  else:
    print("It is now the computer's turn.")
    stones_taken = r.randrange(1,4)
    print(f"The computer took {stones_taken} stones.")
    stones = stones - stones_taken
    if stones == 0:
      print("The computer wins")
    else:
      print(f"There are {stones} stones left")