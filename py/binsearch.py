# binsearch.py
# Yeidy Levels
# CSCI 77800 Fall 2022
# collaborators: just me
# consulted: ThinkPython; w3schools
# translated from: SortSearch.java in my github

def binSearch(list, target):
  low = 0
  high = len(list) -1
  middle = 0

  while low <= high:
    middle = (low + high) // 2

    if (list[middle] == target):
      return middle
    elif ((list[middle]) > target):
      high = middle - 1
    elif ((list[middle]) < target):
      low = middle + 1

  return -1

list = [5, 10, 15, 20, 40, 80, 100]
print(binSearch(list, 40))
  