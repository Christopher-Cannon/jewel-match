# Prototype to iterate through a 2d array top down rather than left to right
import random

# Output the playfield
def display_playfield(playfield):
    for row in playfield:
        for elem in row:
            print(elem, end=' ')

        print('')

jewels = ['X', 'O', '#', '@', '%']

arr = [[random.choice(jewels) for x in range(8)] for y in range(8)]

display_playfield(arr)

x, y = 0, 0
while(x < len(arr[y])):
    while(y < len(arr)):
        print("X: {}, Y: {}, char: {}".format(x, y, arr[y][x]))

        y += 1
    y = 0
    x += 1
