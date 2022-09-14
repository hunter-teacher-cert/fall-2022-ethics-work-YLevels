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
        print(".", end=" ") #just so we can see them
      else:
        print(board[i][j], end=" ")
  print()

# set cell (r,c) to val
def setCell(board, r, c, val):
  board[r][c] = val

# return number of living neighbours of board[r][c]
def countNeighbours(board, r, c):
  counter = 0
  rows = len(board)
  cols = len(board[0])

  # r = row, c = column

  # r-1, c-1 | r-1, c | r-1, c+1
  # r, c-1   | r, c   | r, c+1
  # r+1, c-1 | r+1, c | r+1, c+1

  # local rows: r-1, r, r+1
  # local cols: c-1, c, c+1

  # go through local rows
  for i in range(r-1, r+2):
    # make sure row is valid
    if i >= 0 and i < rows:
      # go through local cols
      for j in range(c-1, c+2):
        # make sure col value is valid
        if j >=0 and j < cols:
          # check that we're not in the center
          if not(i == r and j == c):
            # if neighbour is alive, count them!
            if board[i][j] == ALIVE:
              counter = counter + 1
              
    return counter

# precond: given a board and a cell
# postcond: return next generation cell state based on CGOL rules (alive 'X', dead ' ')
def getNextGenCell (board, r, c):
  currentStatus = board[r][c];
  aliveNeighbours = countNeighbours(board, r, c)

  if (currentStatus == DEAD and aliveNeighbours == 3):
    return ALIVE
  if (currentStatus == ALIVE) and (aliveNeighbours == 2 or aliveNeighbours == 3):
    return ALIVE
  return DEAD

# generate and return a new board representing next generation
def generateNextBoard(board):
  rows = len(board)
  cols = len(board[0])
  nextBoard = createNewBoard(rows, cols)

  for i in range(rows):
    for j in range(cols):
      setCell(nextBoard, i, j, getNextGenCell(board, i, j))

  return nextBoard
  
# test statements
board = createNewBoard(25,25)
printBoard(board)
# setCell(board, 0, 0, ALIVE)
# setCell(board, 0, 1, ALIVE)
# setCell(board, 1, 0, ALIVE)
# printBoard(board)
# print(countNeighbours(board, 2, 2))

for i in range(len(board)):
  for j in range(len(board[0])):
    if r.random() > 0.5:
      setCell (board, i, j, ALIVE)

print("Generation 0")
printBoard(board)
print("-----\n\n")

for i in range(10):
  board = generateNextBoard(board)
  print("Generation" + str(i))
  printBoard(board)
  print("-------\n\n")