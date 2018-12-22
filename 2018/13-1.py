f = open('13.txt')
lines = f.read().splitlines()

canvas = {}
carts = []

# On the intersection it turns left, goes straight, turns right and then left again.

y = 0
for line in lines:
    x = 0
    for char in line:
        if char in '^v><':
            carts.append((char, (x, y), 'left'))
            if char in '^v':
                actual_char = '|'
            elif char in '><':
                actual_char = '-'
        else:
            actual_char = char
        canvas[(x, y)] = actual_char
        x += 1
    y += 1


def move_left(coord):
    x = coord[0]
    y = coord[1]
    return x - 1, y

def move_right(coord):
    x = coord[0]
    y = coord[1]
    return x + 1, y

def move_up(coord):
    x = coord[0]
    y = coord[1]
    return x, y - 1

def move_down(coord):
    x = coord[0]
    y = coord[1]
    return x, y + 1

def get_next_turn(turn):
    if turn == 'left':
        return 'straight'
    elif turn == 'straight':
        return 'right'
    elif turn == 'right':
        return 'left'

def get_moved_cart(cart):
    char = cart[0]
    coord = cart[1]
    turn = cart[2]
    if char == '<':
        next_coord = move_left(coord)
    elif char == '>':
        next_coord = move_right(coord)
    elif char == 'v':
        next_coord = move_down(coord)
    elif char == '^':
        next_coord = move_up(coord)
    next_char = canvas[next_coord]
    if char == '<':
        if next_char == '\\':
            next_cart_char = '^'
        elif next_char == '/':
            next_cart_char = 'v'
        elif next_char == '+':
            if turn == 'straight':
                next_cart_char = '<'
            elif turn == 'left':
                next_cart_char = 'v'
            elif turn == 'right':
                next_cart_char = '^'
            turn = get_next_turn(turn)
        elif next_char == '-':
            next_cart_char = '<'
    elif char == '>':
        if next_char == '/':
            next_cart_char = '^'
        elif next_char == '\\':
            next_cart_char = 'v'
        elif next_char == '+':
            if turn == 'straight':
                next_cart_char = '>'
            elif turn == 'left':
                next_cart_char = '^'
            elif turn == 'right':
                next_cart_char = 'v'
            turn = get_next_turn(turn)
        elif next_char == '-':
            next_cart_char = '>'
    elif char == 'v':
        if next_char == '\\':
            next_cart_char = '>'
        elif next_char == '/':
            next_cart_char = '<'
        elif next_char == '+':
            if turn == 'straight':
                next_cart_char = 'v'
            elif turn == 'left':
                next_cart_char = '>'
            elif turn == 'right':
                next_cart_char = '<'
            turn = get_next_turn(turn)
        elif next_char == '|':
            next_cart_char = 'v'
    elif char == '^':
        if next_char == '/':
            next_cart_char = '>'
        elif next_char == '\\':
            next_cart_char = '<'
        elif next_char == '+':
            if turn == 'straight':
                next_cart_char = '^'
            elif turn == 'left':
                next_cart_char = '<'
            elif turn == 'right':
                next_cart_char = '>'
            turn = get_next_turn(turn)
        elif next_char == '|':
            next_cart_char = '^'
    return (next_cart_char, next_coord, turn)


def get_crash_coord(carts_initial, carts_moved):
    carts = carts_initial + carts_moved
    for cart in carts:
        carts_copy = list(carts)
        carts_copy.remove(cart)
        coord = cart[1]
        coords_copy = [x[1] for x in carts_copy]
        if coord in coords_copy:
            return coord

def get_first_crash(carts):
    while True:
        carts.sort(key=lambda x: (x[1][0], x[1][1]))
        carts_initial = list(carts)
        carts_moved = []
        for cart in carts:
            carts_initial.remove(cart)
            carts_moved.append(get_moved_cart(cart))
            crash_coord = get_crash_coord(carts_initial, carts_moved)
            if crash_coord:
                return crash_coord
        carts = carts_moved


first_crash = get_first_crash(carts)
print('{},{}'.format(first_crash[0], first_crash[1]))