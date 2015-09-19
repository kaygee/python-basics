import random

MATRIX_X = 5
MATRIX_Y = 5

chosen_cells = dict()

def initialize_locations():
    monster = get_random_unique_location("MONSTER", MATRIX_X, MATRIX_Y)
    door = get_random_unique_location("DOOR", MATRIX_X, MATRIX_Y)
    start = get_random_unique_location("PLAYER", MATRIX_X, MATRIX_Y)

    # return monster, door, start
    return monster, door, start

def get_random_unique_location(label, x, y):
    candidate_x = random.randint(0, x - 1)
    candidate_y = random.randint(0, y - 1)

    # First entry. Proceed.
    if len(chosen_cells.keys()) == 0:
        chosen_cells[label] = (candidate_x, candidate_y)
    else:
        locations = []
        for key in chosen_cells.keys():
            locations.append(chosen_cells[key])
        for location in locations:
            while (location[0] == candidate_x) and (location[1] == candidate_y):
                candidate_x = random.randint(0, x - 1)
                candidate_y = random.randint(0, y - 1)
        chosen_cells[label] = (candidate_x, candidate_y)

def move_player(location, move):
    current_location_x = location[0]
    current_location_y = location[1]
    if move == 'L':
        chosen_cells['PLAYER'] = (current_location_x, current_location_y - 1)
    if move == 'R':
        chosen_cells['PLAYER'] = (current_location_x, current_location_y + 1)
    if move == 'U':
        chosen_cells['PLAYER'] = (current_location_x - 1, current_location_y)
    if move == 'D':
        chosen_cells['PLAYER'] = (current_location_x + 1, current_location_y)

def get_moves(location):
    MOVES = ['L', 'R', 'U', 'D']
    if location[1] == 0:
        MOVES.remove('L')
    if location[0] == 0:
        MOVES.remove('U')
    if location[1] == MATRIX_Y - 1:
        MOVES.remove('R')
    if location[0] == MATRIX_X - 1:
        MOVES.remove('D')
    return MOVES

def print_matrix():
    player_location = chosen_cells['PLAYER']
    door_location = chosen_cells['DOOR']
    monster_location = chosen_cells['MONSTER']

    MATRIX = [[0 for x in range(5)] for x in range(5)]

    MATRIX[player_location[0]][player_location[1]] = 1
    MATRIX[door_location[0]][door_location[1]] = 2
    MATRIX[monster_location[0]][monster_location[1]] = 3

    for x in list(range(MATRIX_X)):
        for y in list(range(MATRIX_Y)):
            print("{} ".format(MATRIX[x][y]), end="")
        print("\n", end="")



# Start out by assigning the locations.
initialize_locations()
print(chosen_cells)
print("Welcome to the dungeon!")

while True:
    print("You're currently in room {}".format(chosen_cells['PLAYER']))
    print_matrix()
    print("You can move {}".format(get_moves(chosen_cells['PLAYER'])))
    print("Enter Q to quit.")

    move = input("> ")
    move = move.upper()

    if move == 'Q':
        break

    if move in get_moves(chosen_cells['PLAYER']):
        move_player(chosen_cells['PLAYER'], move)
    else:
        print("Sorry, I don't undestand {}".format(move))
        continue

    if chosen_cells['PLAYER'] == chosen_cells['DOOR']:
        print("You've escaped!")
        break

    if chosen_cells['PLAYER'] == chosen_cells['MONSTER']:
        print("You were eaten by a monster! O noes!")
        break
