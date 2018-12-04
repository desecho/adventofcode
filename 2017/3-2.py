f = open('3.txt')
target = int(f.read())

busy_squares = [(0, 0)]

def get_move(prev_move):
    if prev_move == 'right':
        return 'up'
    elif prev_move == 'up':
        return 'left'
    elif prev_move == 'left':
        return 'down'
    elif prev_move == 'down':
        return 'right'

def is_valid_move(move, coord):
    new_coord = globals()[f'move_{move}'](*coord)
    return new_coord not in canvas

def move_right(x, y):
    return x + 1, y

def move_left(x, y):
    return x - 1, y

def move_up(x, y):
    return x, y + 1

def move_down(x, y):
    return x, y - 1

def calculate_value(coord):
    n = 0
    coord_up = move_up(*coord)
    if coord_up in canvas:
        n += canvas[coord_up]
    coord_down = move_down(*coord)
    if coord_down in canvas:
        n += canvas[coord_down]
    coord_right = move_right(*coord)
    if coord_right in canvas:
        n += canvas[coord_right]
    coord_left = move_left(*coord)
    if coord_left in canvas:
        n += canvas[coord_left]

    coord_up_left = move_left(*move_up(*coord))
    if coord_up_left in canvas:
        n += canvas[coord_up_left]
    coord_up_right = move_right(*move_up(*coord))
    if coord_up_right in canvas:
        n += canvas[coord_up_right]

    coord_down_left = move_left(*move_down(*coord))
    if coord_down_left in canvas:
        n += canvas[coord_down_left]
    coord_down_right = move_right(*move_down(*coord))
    if coord_down_right in canvas:
        n += canvas[coord_down_right]
    return n

move = 'down'
coord = (0, 0)
canvas = {(0,0): 1}
value = 1
while value < target:
    next_move = get_move(move)
    if is_valid_move(next_move, coord):
        move = next_move
    coord = globals()[f'move_{move}'](*coord)
    value = calculate_value(coord)
    canvas[coord] = value

print(value)