# 4 - Attempt to find consecutive rows of 3 or more matching jewels - horizontal

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
        except:
            print("Invalid input, please try again")
            continue

        # If there is space on either side of chosen jewel, we can swap either side
        if(0 < x < len(grid) - 1):
            while(True):
                try:
                    choice = input("Which direction to swap, left or right? ")
                except:
                    print("Invalid input, please try again")
                    continue

                if(choice.lower() == "right"):
                    print("Swapping right...\n")
                    grid[y][x], grid[y][x + 1] = grid[y][x + 1], grid[y][x]
                elif(choice.lower() == "left"):
                    print("Swapping left...\n")
                    grid[y][x], grid[y][x - 1] = grid[y][x - 1], grid[y][x]
                else:
                    print("Invalid input, please try again")
                    continue

                return grid

        elif(x == 0):
            print("Swapping right...\n")
            grid[y][x], grid[y][x + 1] = grid[y][x + 1], grid[y][x]
        else:
            print("Swapping left...\n")
            grid[y][x], grid[y][x - 1] = grid[y][x - 1], grid[y][x]

        return grid

# Attempt to find continuous rows or columns of 3 or more matching jewels and remove them
def find_matches(grid):
    # Store coordinates to remove after one pass
    destroy_list = []
    # Check horizontally
    for y in range(len(grid)):
        matches, start_x, char_match = 1, 0, ''

        for x in range(len(grid[y])):
            if(char_match != grid[y][x]):
                # Char to match next char against
                char_match = grid[y][x]
                matches = 1
                start_x = x
            else:
                matches += 1
                # Check matches count if next char is different or if current position is the very end
                if((x < (len(grid) - 1)) and (grid[y][x+1] != char_match)) or ((x == (len(grid) - 1))):
                    # If there were more than 3 in a row
                    if(matches > 2):
                        # Append all coords from stored position to destroy list
                        for z in range(matches):
                            destroy_list.append([y, start_x + z])

    return destroy_list

# Remove jewels marked by destroy_list and re-populate
def prepare_field(jewels, grid, destroy_list):
    return 0

# Main loop
def main():
    jewels = ['X', 'O', '#', '@', '%', '=']

    playfield = create_playfield(jewels, 10)
    display_playfield(playfield)

    print(find_matches(playfield))

main()
