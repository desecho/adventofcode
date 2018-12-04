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
    return new_coord not in busy_squares

def move_right(x, y):
    return x + 1, y

def move_left(x, y):
    return x - 1, y

def move_up(x, y):
    return x, y + 1

def move_down(x, y):
    return x, y - 1

move = 'down'
coord = (0, 0)
for n in range(2, target + 1):
    next_move = get_move(move)
    if is_valid_move(next_move, coord):
        move = next_move
    coord = globals()[f'move_{move}'](*coord)
    busy_squares.append(coord)

answer = abs(coord[0]) + abs(coord[1])
print(answer)