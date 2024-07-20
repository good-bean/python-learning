####################################################################################
# Project           : Conway's Game of Life
#
# Program name      : conway.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240702
#
# Purpose           : An example of cellular automata
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('0') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists

while True: # Main program loop
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or the space
        print() # Print a newline at the end of the row
    
    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '0':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '0':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '0':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '0':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '0':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '0':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '0':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '0':
                numNeighbors += 1 # Bottom-right neighbor is alive.
            
            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '0' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '0'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '0'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering