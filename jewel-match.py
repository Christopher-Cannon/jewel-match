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

playfield = create_playfield(8, 8)
display_playfield(playfield)
