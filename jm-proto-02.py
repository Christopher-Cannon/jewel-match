# 2 - Get input from the player

import random

# Create and populate jewel grid
def create_playfield(jewels, size):
    return [[random.choice(jewels) for x in range(size)] for y in range(size)]

# Number guides along top or bottom
def numbers_x(grid):
    return 0

# Output the playfield with number guides
def display_playfield(grid):
    for row in range(len(grid)):
        for elem in grid[row]:
            print(elem, end=' ')

        print('')

# Remove jewels marked in remove_list
def remove_jewels(grid, remove_list):
    return 0

# If a jewel is removed, move above jewels down one
def drop_jewels(grid):
    return 0

# Find any blank spots and fill with jewels
def fill_empty(jewels, grid):
    return 0

# Swap a jewel with either its left or right neighbour
def swap_jewels(grid):
    while(True):
        try:
            # Allow user to start at 1 rather than 0
            print("Range: 1 - {}".format(len(grid)))
            x = int(input("X of jewel to swap: "))
            y = int(input("Y of jewel to swap: "))

            x -= 1
            y -= 1

            if(not(0 <= x < len(grid)) or not(0 <= y < len(grid))):
                print("Invalid input, please try again")
                continue
            else:
                print("x:", x, "y:", y) # DEBUG
        except:
            print("Invalid input, please try again")
            continue

# Attempt to find continuous rows or columns of 3 or more matching jewels and remove them
def find_matches(grid):
    return 0

# Remove jewels marked by destroy_list and re-populate
def prepare_field(jewels, grid, destroy_list):
    return 0

# Main loop
def main():
    jewels = ['X', 'O', '#', '@', '%', '=']

    playfield = create_playfield(jewels, 8)
    display_playfield(playfield)

    swap_jewels(playfield)

main()
