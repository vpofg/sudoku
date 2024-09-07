import math
import random
import numpy as np

sudokuGrid = [[1, 2, 3, 0, 0, 0, 0, 0, 0], 
[4, 5, 6, 0, 0, 0, 0, 0, 0], 
[7, 8, 9, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0]]

for row in range(0, 3):
    for column in range(0, 3):
        row = np.random.randint(10, size=(3)) 



for row in range(0, 9):
    for column in range(0, 9):
        print(sudokuGrid[row][column], end=" ")
    print()