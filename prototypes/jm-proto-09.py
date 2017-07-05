# 9 - Add function to remove, drop and refill jewels

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
    for coords in remove_list:
        grid[coords[0]][coords[1]] = ' '

    return grid

# If a jewel is removed, move above jewels down one
def drop_jewels(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if(grid[y][x] == ' '):
                if(y > 0):
                    pos = y
                    # Move jewels down and empty space up
                    while(pos > 0):
                        grid[pos][x], grid[pos - 1][x] = grid[pos - 1][x], grid[pos][x]

                        pos -= 1
                else:
                    pass
            else:
                pass

    return grid

# Find any blank spots and fill with jewels
def fill_empty(jewels, grid):
    for row in grid:
        for x in range(len(row)):
            if(row[x] == ' '):
                row[x] = random.choice(jewels)

    return grid

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
    # Check vertically
    x, y = 0, 0
    while(x < len(grid[y])):
        matches, start_y, char_match = 1, 0, ''

        while(y < len(grid)):
            if(char_match != grid[y][x]):
                char_match = grid[y][x]
                matches = 1
                start_y = y
            else:
                matches += 1

                if((y < (len(grid) - 1)) and (grid[y+1][x] != char_match)) or ((y == (len(grid) - 1))):
                    if(matches > 2):
                        for z in range(matches):
                            destroy_list.append([start_y + z, x])

            y += 1
        y = 0
        x += 1

    return destroy_list

# Remove jewels marked by destroy_list and re-populate
def prepare_field(jewels, grid, destroy_list):
    grid = remove_jewels(grid, destroy_list)
    grid = drop_jewels(grid)
    grid = fill_empty(jewels, grid)

    return grid

# Main loop
def main():
    jewel_list = ['X', 'O', '#', '@', '%', '=']

    playfield = create_playfield(jewel_list, 10)
    display_playfield(playfield)

    remove_list = find_matches(playfield)
    prepare_field(jewel_list, playfield, remove_list)

    print('')

    display_playfield(playfield)

main()
