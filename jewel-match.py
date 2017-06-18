import random

# Create and populate jewel grid
def create_playfield(width, height):
    jewels = ['X', 'O', '#', '@', '%']

    return [[random.choice(jewels) for x in range(width)] for y in range(height)]

# Find any blank spots and fill with jewels
def fill_empty(playfield):
    jewels = ['X', 'O', '#', '@', '%']

    for row in playfield:
        for x in range(len(row)):
            if(row[x] == ' '):
                row[x] = random.choice(jewels)

    return playfield

# Output the playfield
def display_playfield(playfield):
    for row in playfield:
        for elem in row:
            print(elem, end='  ')

        print('\n')

# TEST: Remove a jewel to test check_field()
def remove_jewels(playfield, remove_list):
    for c in remove_list:
        playfield[c[0]][c[1]] = ' '

    return playfield

# Swap a jewel with either its left or right neighbour
def swap_jewels(playfield):
    while(True):
        try:
            x = int(input("X of jewel to swap: "))
            y = int(input("Y of jewel to swap: "))
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
def check_field(playfield):
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

    for y in range(len(playfield)):
        matches, start_x, char_match = 1, 0, ''

        for x in range(len(playfield[y])):
            print("X: {}, Y: {}".format(x, y)) # DEBUG
            # Check horizontally
            if(char_match != playfield[y][x]):
                print("Held: {}, Cur: {}".format(char_match, playfield[y][x])) # DEBUG

                # Char to match next char against
                char_match = playfield[y][x]
                matches = 1
                start_x = x
            else:
                matches += 1
                print("Matches += 1, Val: {}".format(matches)) # DEBUG

                if((x < 7) and (playfield[y][x+1] != char_match)) or ((x == 7)):
                    # If there were more than 3 in a row
                    if(matches > 2):
                        # Append all coords from stored position to destroy list
                        for z in range(matches):
                            destroy_list.append([y, start_x + z])
                            print("Appending values...") # DEBUG

            # Check vertically

    return destroy_list

playfield = create_playfield(8, 8)
display_playfield(playfield)

print('Created playfield\n') # DEBUG

ret_list = find_matches(playfield)
print(ret_list)

print('\nReturned coords of jewels to remove\n') # DEBUG

playfield = remove_jewels(playfield, ret_list)
display_playfield(playfield)

print('Removed jewels\n') # DEBUG

playfield = check_field(playfield)
display_playfield(playfield)

print('Playfield checked\n') # DEBUG

playfield = fill_empty(playfield)
display_playfield(playfield)

print('Jewels added\n') # DEBUG
