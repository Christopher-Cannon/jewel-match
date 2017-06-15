import random

# Create and populate jewel grid
def create_playfield(width, height):
    jewels = ['X', 'O', '#', '@']

    return [[random.choice(jewels) for x in range(width)] for y in range(height)]

# Find any blank spots and fill with jewels
def fill_empty(playfield):
    jewels = ['X', 'O', '#', '@']

    for row in playfield:
        for x in range(len(row)):
            if(row[x] == ''):
                row[x] = random.choice(jewels)

    return playfield

# Output the playfield
def display_playfield(playfield):
    for row in playfield:
        for elem in row:
            print(elem, end='  ')

        print('\n')

# TEST: Remove a jewel to test check_field()
def remove_jewel(playfield):
    x = int(input("X to remove: "))
    y = int(input("Y to remove: "))

    playfield[y][x] = ''

    return playfield

# If a jewel is removed, move above jewels down one
def check_field(playfield):
    for y in range(len(playfield)):
        for x in range(len(playfield[y])):
            if(playfield[y][x] == ''):
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

playfield = create_playfield(8, 8)
display_playfield(playfield)

playfield = remove_jewel(playfield)
display_playfield(playfield)

check_field(playfield)
display_playfield(playfield)
