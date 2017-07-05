# 14 - Add scoring and move replenishment

import random

# Create and populate jewel grid
def create_playfield(jewels, size):
    return [[random.choice(jewels) for x in range(size)] for y in range(size)]

# Number guides along top or bottom
def numbers_x(grid):
    print('', end='   ')

    for y in [x + 1 for x in range(len(grid))]:
        print(y, end=' ')
    print('\n')

# Output the playfield with number guides
def display_playfield(grid):
    numbers_x(grid)

    for row in range(len(grid)):
        if(row + 1 < 10):
            print(row + 1, end='  ')
        else:
            print(row + 1, end=' ')

        for elem in grid[row]:
            print(elem, end=' ')

        print('', row + 1)
    print('')

    numbers_x(grid)

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
    moves, score, jewel_list = 3, 0, ['X', 'O', '#', '@', '%', '=']
    # Create playfield
    playfield = create_playfield(jewel_list, 10)

    remove_list = find_matches(playfield)

    # Ensure that playfield contains no combos when the game starts
    while(remove_list != []):
        playfield = prepare_field(jewel_list, playfield, remove_list)
        remove_list = find_matches(playfield)

    # Display playfield
    display_playfield(playfield)

    # Continue game loop while player has moves remaining
    while(moves > 0):
        # Output game info
        jewels_marked, combo = 0, 0
        print("Moves remaining: {}".format(moves))
        print("Current score: {}".format(score))

        # Let player choose a jewel to swap and deduct a move
        playfield = swap_jewels(playfield)
        moves -= 1

        # Attempt to find matches
        remove_list = find_matches(playfield)
        jewels_marked = len(remove_list)

        # Continue removing jewels until no matches remain
        while(remove_list != []):
            combo += 1

            playfield = prepare_field(jewel_list, playfield, remove_list)
            remove_list = find_matches(playfield)
            jewels_marked += len(remove_list)

        # Add score and moves if jewels were destroyed
        if(jewels_marked > 0):
            score += (jewels_marked * combo) * 10

            # Output score info
            print("Matched {} jewels!".format(jewels_marked))
            print("x{} combo!".format(combo))
            print("+{} score!".format((jewels_marked * combo) * 10))

            # Determine moves to award
            if(jewels_marked < 6):
                moves += 1
                print("+1 moves!\n")
            elif(6 <= jewels_marked < 10):
                moves += 2
                print("+2 moves!\n")
            else:
                moves += 3
                print("+3 moves!\n")
        else:
            pass

        # Display playfield
        display_playfield(playfield)

    # Show final score if player runs out of moves
    print("Out of moves")
    print("Final score: {}".format(score))

main()
