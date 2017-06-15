import random

def create_playfield(width, height):
    jewels = ['X', 'O', '#', '@']

    return [[random.choice(jewels) for x in range(width)] for y in range(height)]

def display_playfield(playfield):
    for row in playfield:
        for elem in row:
            print(elem, end='  ')

        print('\n')

playfield = create_playfield(8, 8)
display_playfield(playfield)
