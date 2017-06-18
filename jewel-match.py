import random

# Determine size of playfield
def get_size():
    while(True):
        try:
            print("Choose a grid size")
            size = int(input("8 - 24: "))

            if(8 <= size <= 24):
                return size
            else:
                print("Invalid input, please try again")
                continue
        except:
            print("Invalid input, please try again")
            continue

# Create and populate jewel grid
def create_playfield(size):
    jewels = ['X', 'O', '#', '@', '%']

    return [[random.choice(jewels) for x in range(size)] for y in range(size)]

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
            print(elem, end=' ')

        print('')

# Remove jewels marked in remove_list
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

                if((x < 7) and (playfield[y][x+1] != char_match)) or ((x == 7)):
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

                if((y < 7) and (playfield[y+1][x] != char_match)) or ((y == 7)):
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
def prepare_field(playfield, destroy_list):
    playfield = remove_jewels(playfield, destroy_list)
    playfield = drop_jewels(playfield)
    playfield = fill_empty(playfield)

    return playfield

def main():
    moves = 5
    size = get_size()
    playfield = create_playfield(size)

    destroy_list = find_matches(playfield)
    print(destroy_list)

    while(destroy_list != []):
        print(destroy_list == [])
        playfield = prepare_field(playfield, destroy_list)

        destroy_list = find_matches(playfield)
        print(destroy_list)

    display_playfield(playfield)

main()
