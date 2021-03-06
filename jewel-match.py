import random

# Determine size of playfield
def get_size():
    while(True):
        try:
            print("Choose a grid size")
            size = int(input("7 - 10: "))

            if(7 <= size <= 10):
                print('')
                return size
            else:
                print("Invalid input, please try again")
                continue
        except:
            print("Invalid input, please try again")
            continue

# Create and populate jewel grid
def create_playfield(jewels, size):
    return [[random.choice(jewels) for x in range(size)] for y in range(size)]

# Find any blank spots and fill with jewels
def fill_empty(jewels, playfield):
    for row in playfield:
        for x in range(len(row)):
            if(row[x] == ' '):
                row[x] = random.choice(jewels)

    return playfield

# Number guides along top or bottom
def numbers_x(playfield):
    print('', end='   ')

    for y in [x + 1 for x in range(len(playfield))]:
        print(y, end=' ')
    print('\n')

# Output the playfield with number guides -- god this is a mess
def display_playfield(playfield):
    numbers_x(playfield)

    for row in range(len(playfield)):
        if(row + 1 < 10):
            print(row + 1, end='  ')
        else:
            print(row + 1, end=' ')

        for elem in playfield[row]:
            print(elem, end=' ')

        print('', row + 1)
    print('')

    numbers_x(playfield)

# Remove jewels marked in remove_list
def remove_jewels(playfield, remove_list):
    for c in remove_list:
        playfield[c[0]][c[1]] = ' '

    return playfield

# Swap a jewel with either its left or right neighbour
def swap_jewels(playfield):
    while(True):
        try:
            # Allow user to start at 1 rather than 0
            print("Range: 1 - {}".format(len(playfield)))
            x = int(input("X of jewel to swap: "))
            y = int(input("Y of jewel to swap: "))

            x -= 1
            y -= 1

            if(not(0 <= x < len(playfield)) or not(0 <= y < len(playfield))):
                print("Invalid input, please try again")
                continue
        except:
            print("Invalid input, please try again")
            continue

        # If there is space on either side of chosen jewel, we can swap either side
        if(0 < x < len(playfield) - 1):
            while(True):
                try:
                    choice = input("Which direction to swap, left or right? ")
                except:
                    print("Invalid input, please try again")
                    continue

                if(choice.lower() == "right"):
                    print("Swapping right...\n")
                    playfield[y][x], playfield[y][x + 1] = playfield[y][x + 1], playfield[y][x]
                elif(choice.lower() == "left"):
                    print("Swapping left...\n")
                    playfield[y][x], playfield[y][x - 1] = playfield[y][x - 1], playfield[y][x]
                else:
                    print("Invalid input, please try again")
                    continue

                return playfield

        elif(x == 0):
            print("Swapping right...\n")
            playfield[y][x], playfield[y][x + 1] = playfield[y][x + 1], playfield[y][x]
        else:
            print("Swapping left...\n")
            playfield[y][x], playfield[y][x - 1] = playfield[y][x - 1], playfield[y][x]

        return playfield

# If a jewel is removed, move above jewels down one
def drop_jewels(playfield):
    for y in range(len(playfield)):
        for x in range(len(playfield[y])):
            if(playfield[y][x] == ' '):
                if(y > 0):
                    pos = y
                    # Move jewels down and empty space up
                    while(pos > 0):
                        playfield[pos][x], playfield[pos - 1][x] = playfield[pos - 1][x], playfield[pos][x]

                        pos -= 1
                else:
                    pass
            else:
                pass

    return playfield

# Attempt to find continuous rows or columns of 3 or more matching jewels and remove them
def find_matches(playfield):
    # Store coordinates to remove after one pass
    destroy_list = []
    # Check horizontally
    for y in range(len(playfield)):
        matches, start_x, char_match = 1, 0, ''

        for x in range(len(playfield[y])):
            if(char_match != playfield[y][x]):
                # Char to match next char against
                char_match = playfield[y][x]
                matches = 1
                start_x = x
            else:
                matches += 1
                # Check matches count if next char is different or if current position is the very end
                if((x < (len(playfield) - 1)) and (playfield[y][x+1] != char_match)) or ((x == (len(playfield) - 1))):
                    # If there were more than 3 in a row
                    if(matches > 2):
                        # Append all coords from stored position to destroy list
                        for z in range(matches):
                            destroy_list.append([y, start_x + z])
    # Check vertically
    x, y = 0, 0
    while(x < len(playfield[y])):
        matches, start_y, char_match = 1, 0, ''

        while(y < len(playfield)):
            if(char_match != playfield[y][x]):
                # Char to match next char against
                char_match = playfield[y][x]
                matches = 1
                start_y = y
            else:
                matches += 1
                # Check matches count if next char is different or if current position is the very end
                if((y < (len(playfield) - 1)) and (playfield[y+1][x] != char_match)) or ((y == (len(playfield) - 1))):
                    # If there were more than 3 in a row
                    if(matches > 2):
                        # Append all coords from stored position to destroy list
                        for z in range(matches):
                            destroy_list.append([start_y + z, x])

            y += 1
        y = 0
        x += 1

    return destroy_list

# Remove jewels marked by destroy_list and re-populate
def prepare_field(jewels, playfield, destroy_list):
    playfield = remove_jewels(playfield, destroy_list)
    playfield = drop_jewels(playfield)
    playfield = fill_empty(jewels, playfield)

    return playfield

# Main loop
def main():
    moves, score, jewels = 3, 0, ['X', 'O', '#', '@', '%', '=']
    size = get_size()
    playfield = create_playfield(jewels, size)

    destroy_list = find_matches(playfield)
    # Ensure that playfield has no combos before starting
    while(destroy_list != []):
        playfield = prepare_field(jewels, playfield, destroy_list)
        destroy_list = find_matches(playfield)

    display_playfield(playfield)
    # Continue while player has moves remaining
    while(moves > 0):
        jewels_marked, combo = 0, 0
        print("Moves remaining: {}".format(moves))
        print("Current score: {}".format(score))

        playfield = swap_jewels(playfield)
        moves -= 1

        destroy_list = find_matches(playfield)
        jewels_marked = len(destroy_list)

        # Check for matches
        while(destroy_list != []):
            combo += 1

            playfield = prepare_field(jewels, playfield, destroy_list)
            destroy_list = find_matches(playfield)
            jewels_marked += len(destroy_list)
        # Add score/moves if jewels were destroyed
        if(jewels_marked > 0):
            score += (jewels_marked * combo) * 10

            print("Matched {} jewels!".format(jewels_marked))
            print("x{} combo!".format(combo))
            print("+{} score!".format((jewels_marked * combo) * 10))

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

        display_playfield(playfield)

    print("Out of moves")
    print("Final score: {}".format(score))

main()
