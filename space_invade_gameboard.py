from __future__ import print_function
import random

def main():
    # the playable spaces (20x10)
    width = 20
    height = width//2

    # the boundary: "+2" for vertical/horizontal boundary
    boundary_width = width + 2 
    boundary_height = height + 2

    # we determine where to start the enemy
    enemy_y = height//2 # this determines which KEY
    enemy_x = width//2  # this determines which INDEX of the list inside the VALUE

    print("Welcome to Cosmos Raiders, the very awful knock-off version of Space Invaders.")
    print("In this game, E stands for Enemy. And H stands for Hero (aka you, the player!)")

    gameboard = initialize_game(width, height, boundary_width, boundary_height, enemy_x, enemy_y)
    show_game(gameboard)

    enemy_direction = "left"
    moving = enemy_moves(boundary_width, enemy_x, enemy_direction)
    for x in range(10):
        if x % 2 == 0:
            enemy_direction = "right"
        else:
            enemy_direction = "left"
        new_gameboard = initialize_game(width, height, boundary_width, boundary_height, moving, enemy_y)
        show_game(new_gameboard)
        moving = enemy_moves(boundary_width, moving, enemy_direction)
        

def initialize_game(width, height, boundary_width, boundary_height, enemy_x, enemy_y):
    top_border = []
    for x in range(boundary_width):
        top_border.append("_")

    bottom_border = []
    for x in range(boundary_width):
        bottom_border.append("-")

    center_row = []
    for x in range(boundary_width):
        center_row.append(" ")
    center_row[0] = "|"
    center_row[-1] = "|"

    gameboard = {}

    for x in range(boundary_height):
        if x == 0:
            gameboard[x] = top_border
        elif x < boundary_height - 1:
            gameboard[x] = center_row
        else:
            gameboard[x] = bottom_border
    
    # we put the enemy on the game board
    enemy_row = center_row[:]
    enemy_row[enemy_x] = "E"
    gameboard[enemy_y] = enemy_row

    return gameboard

def show_game(gameboard):
    for k, v in gameboard.items():
        print(''.join(v))

def enemy_moves(boundary_width, enemy_x, enemy_direction):
    #We need to keep track of how far enemy can move.
    #We -1/-2 because enemy cannot be ON boundary, must be INSIDE.'''
    enemy_left_space = enemy_x - 1
    enemy_right_space = (boundary_width - enemy_x) - 2
    print(f"Enemy is able to move left {enemy_left_space} spaces.")
    print(f"Enemy is able to move right {enemy_right_space} spaces.")
    
    if enemy_direction == "left":
        # randint starts w/ 1 because the enemy should move at least +1
        enemy_moves = random.randint(1, enemy_left_space)
        print(f"Enemy will move {enemy_moves} to the {enemy_direction}.")
        # we subtract since we are moving left
        enemy_x = enemy_x - enemy_moves
    else:
        enemy_moves = random.randint(1, enemy_right_space)
        print(f"Enemy will move {enemy_moves} to the {enemy_direction}.")
        # we add since we are moving right
        enemy_x = enemy_x + enemy_moves

    return enemy_x

main()
