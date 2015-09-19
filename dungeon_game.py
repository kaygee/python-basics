import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

chosen_cells = dict()

def initialize_locations():
    monster = get_random_unique_location("MONSTER", 3, 3)
    door = get_random_unique_location("DOOR", 3, 3)
    start = get_random_unique_location("PLAYER", 3, 3)

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
    # Get player's current location
    current_location_x = location[0]
    current_location_y = location[1]
    # If move is LEFT (y-1)
    if move == 'LEFT':
        chosen_cells['PLAYER'] = (current_location_x, current_location_y - 1)
    # If move is RIGHT (y+1)
    if move == 'RIGHT':
        chosen_cells['PLAYER'] = (current_location_x, current_location_y + 1)
    # If move is UP (x-1)
    if move == 'UP':
        chosen_cells['PLAYER'] = (current_location_x - 1, current_location_y)
    # If move is DOWN (x+1)
    if move == 'DOWN':
        chosen_cells['PLAYER'] = (current_location_x + 1, current_location_y)

def get_moves(location):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # If players y is 0, remove LEFT
    if location[1] == 0:
        MOVES.remove('LEFT')
    # If players x is 0, remove UP
    if location[0] == 0:
        MOVES.remove('UP')
    # If players y is 2, remove RIGHT
    if location[1] == 2:
        MOVES.remove('RIGHT')
    # If players x is 2, remove DOWN
    if location[0] == 2:
        MOVES.remove('DOWN')
    return MOVES

# Start out by assigning the locations.
initialize_locations()
print(chosen_cells)
print("Welcome to the dungeon!")

while True:
    print("You're currently in room {}".format(chosen_cells['PLAYER'])) # fill in with player position
    print(chosen_cells)
    print("You can move {}".format(get_moves(chosen_cells['PLAYER']))) # fill in with available moves
    print("Enter QUIT to quit.")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    move_player(chosen_cells['PLAYER'], move)

    # If it's a good move, change the players position.
    # If it's a bad move, don't change anything.
    # If the new player position is the door, they win!
    if chosen_cells['PLAYER'] == chosen_cells['DOOR']:
        print("You've escaped!")
        break
    # If the new player position is the monster, they lose!
    if chosen_cells['PLAYER'] == chosen_cells['MONSTER']:
        print("You were eaten by a monster! O noes!")
        break
    # Otherwise, continue
