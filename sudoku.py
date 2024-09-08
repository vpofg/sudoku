import math
import random
import numpy as np

sudokuGrid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0]])

for row in range(0, 3):
    for column in range(0, 3):
        sudokuGrid[row, column:column + 1] = np.random.randint(1, 10, 1)

for row in range(3, 6):
    for column in range(3, 6):
        sudokuGrid[row, column:column + 1] = np.random.randint(1, 10, 1)
        
for row in range(6, 9):
    for column in range(6, 9):
        sudokuGrid[row, column:column + 1] = np.random.randint(1, 10, 1)


for row in range(0, 9):
    for column in range(0, 9):
        print(sudokuGrid[row][column], end=" ")
    print()