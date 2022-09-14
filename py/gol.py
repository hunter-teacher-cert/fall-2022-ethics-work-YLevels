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
def createNewBoard(rows, cols):
  board = []
  
  for i in range(rows):
    board.append([])
    for j in range(cols):
      board[i].append(DEAD)

  return board

# print the board
def printBoard(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == DEAD:
        print(".", end=" ")
      else:
        print(board[i][j], end=" ")
  print()

board = createNewBoard(5,5)
printBoard(board)


