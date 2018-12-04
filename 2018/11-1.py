f = open('11.txt')
serial = int(f.read())

def get_hundred_digit(x):
    if x > 999:
        return get_hundred_digit(int(str(x)[1:]))
    if x < 100:
        return 0
    else:
        return int(str(x)[0])

def get_power(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = get_hundred_digit(power)
    return power - 5

def is_valid_box(x, y):
    return (x + 2, y + 2) in powers

def sum_box(x, y):
    result = 0
    for ax in range(0, 3):
        for ay in range(0, 3):
            result += powers[(x + ax, y + ay)]
    return result

powers = {}
for x in range(1, 301):
    for y in range(1, 301):
        powers[(x, y)] = get_power(x, y)

sum_powers = {}
for x in range(1, 301):
    for y in range(1, 301):
        if is_valid_box(x, y):
            sum_powers[(x, y)] = sum_box(x, y)

max_sum = 0
coord = (0, 0)

for x, y in sum_powers:
    if sum_powers[(x, y)] > max_sum:
        max_sum = sum_powers[(x, y)]
        coord = (x, y)

print('{},{}'.format(coord[0], coord[1]))