from copy import deepcopy
import sys

sys.setrecursionlimit(15000)

FILENAME = 'input.txt'


def load_lines(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        l = [char for char in line]
        output.append(l)
    return output

def find_start_pos(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == '^':
                return i, j

def no_obstacle(char):
    return char == '.' or char == 'X'

def is_in_bounds(i, j, map):
    if i < 0 or j < 0:
        return False
    if i > len(map) - 1 or j > len(map) - 1:
        return False
    return True

def move_left(i,j, map):
    if not is_in_bounds(i,j,map):
        return
    map[i][j] = "X"
    if not is_in_bounds(i,j-1,map):
        return

    if no_obstacle(map[i][j-1]):
        move_left(i, j-1, map)
    else:
        move_up(i,j, map)

def move_down(i, j, map):
    if not is_in_bounds(i,j,map):
        return

    map[i][j] = "X"
    if not is_in_bounds(i+1,j,map):
        return

    if no_obstacle(map[i+1][j]):
        move_down(i+1, j, map)
    else:
        move_left(i,j, map)

def move_right(i, j, map):
    if not is_in_bounds(i,j,map):
        return

    map[i][j] = "X"

    if not is_in_bounds(i,j+1,map):
        return

    if no_obstacle(map[i][j+1]):
        move_right(i, j+1, map)
    else:
        move_down(i, j, map)

def move_up(i, j, map):
    if not is_in_bounds(i,j,map):
        return

    map[i][j] = 'X'

    if not is_in_bounds(i-1,j,map):
        return

    if no_obstacle(map[i-1][j]):
        move_up(i-1,j, map)
    else:
        move_right(i,j, map)

def print_map(map):
    for line in map:
        s = "".join(line)
        print(s)

def get_x_coords(map, start_i, start_j):
    coords = []
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 'X':
                if i == start_i and j == start_j:
                    pass
                else:
                    coords.append((i,j))
    return coords

if __name__ == '__main__':
    map = load_lines(FILENAME)
    original_map = deepcopy(map)
    start_i, start_j = find_start_pos(map)
    move_up(start_i, start_j, map)

    # Get all coordinates of Xs excluding the starting point
    x_coords = get_x_coords(map, start_i, start_j)

    result = 0
    for coord in x_coords:
        map = deepcopy(original_map)
        map[coord[0]][coord[1]] = 'O'
        try:
            move_up(start_i, start_j, map)
        except RecursionError:
            result +=1

    print(result)
