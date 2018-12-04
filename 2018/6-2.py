from collections import defaultdict

def calculate_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def get_coords():
    f = open('6.txt')
    lines = f.read().splitlines()
    coords = []
    for line in lines:
        coord = line.split(', ')
        coord = (int(coord[0]), int(coord[1]))
        coords.append(coord)
    return coords

def get_max_coord_value():
    max_coord_value = 0
    for coord in coords:
        if coord[0] > max_coord_value:
            max_coord_value = coord[0]
        if coord[1] > max_coord_value:
            max_coord_value = coord[1]
    return max_coord_value

coords = get_coords()
max_coord_value = get_max_coord_value()

def calculate_value(coord):
    n = 0
    for c in coords:
        n += calculate_distance(c, coord)
    return n

max_value = 10000

canvas = {}
area = 0
for x in range(0, max_coord_value):
    for y in range(0, max_coord_value):
        coord = (x, y)
        n = calculate_value(coord)
        if n < max_value:
            area += 1

print(area)