# Conway's game of life
# My implementation... doesn't quite work
import time, copy, random, sys
WIDTH = 60
HEIGHT = 20

# Create initial list
nextCells = []
for i in range(WIDTH):
    column = []
    for j in range(HEIGHT):
        if random.randint(0, 1) == 1:
            # Cell is alive
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)

# Main Program
try:
    while True:
        print('\n\n\n\n\n')  # Separate each step with newlines.
        currentCells = copy.deepcopy(nextCells)
        
        # Print currentCells on the screen:
        for j in range(HEIGHT):
            for i in range(WIDTH):
                print(currentCells[i][j], end='') # Print the # or space.
            print() # Print a newline at the end of the row.

        # Should've used wrap-around conditions here

        # Check neighbours
        for i in range(WIDTH):
            for j in range(HEIGHT):
                numAlive = 0
                if i > 0 and currentCells[i-1][j] == '#':
                    numAlive += 1
                if i > 0 and j > 0 and currentCells[i-1][j-1] == '#':
                    numAlive += 1
                if i > 0 and j < HEIGHT-1 and currentCells[i-1][j+1] == '#':
                    numAlive += 1
                if i < WIDTH-1 and currentCells[i+1][j] == '#':
                    numAlive += 1
                if i < WIDTH-1 and j > 0 and currentCells[i+1][j-1] == '#':
                    numAlive += 1
                if i < WIDTH-1 and j < HEIGHT-1 and currentCells[i+1][j+1] == '#':
                    numAlive += 1
                if j > 0 and currentCells[i][j-1] == '#':
                    numAlive += 1
                if j < HEIGHT-1:
                    numAlive += 1

                # Modify state
                if currentCells[i][j] == '#' and (numAlive == 2 or numAlive == 3):
                    nextCells[i][j] = '#'
                elif currentCells[i][j] == '#' and numAlive == 3:
                    nextCells[i][j] = '#'
                else:
                    nextCells[i][j] = ' '
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()