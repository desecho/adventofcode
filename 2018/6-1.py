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

# represented like this: {(x, y): id}
coords_with_ids = {}

for x in range(0, len(coords)):
    coords_with_ids[coords[x]] = x

crazy_big_value = 999999999999999999999999999999999999999999999999999999999999999999999999999

# fill canvas
# {coord: (id, distance_value)}
canvas = {}
for x in range(0, max_coord_value):
    for y in range(0, max_coord_value):
        canvas[(x, y)] = ('x', crazy_big_value)

for coord in coords:
    canvas[coord] = (coords_with_ids[coord], 0)


for coord in canvas:
    for coord_target in coords:
        distance = calculate_distance(coord_target, coord)
        canvas_coord_distance = canvas[coord][1]
        if distance < canvas_coord_distance:
            canvas[coord] = (coords_with_ids[coord_target], distance)
        if distance == canvas_coord_distance and distance != 0:
            # use a different id here other than x just to make sure the code works as expected
            canvas[coord] = ('z', distance)

areas_count = defaultdict(int)

for coord in canvas:
    id_, _ = canvas[coord]
    areas_count[id_] += 1

# Write canvas to debug
# f = open('6-debug.txt', 'w')
# for x in range(0, max_coord_value):
#     line = ''
#     for y in range(0, max_coord_value):
#         line += ' ' + str(canvas[(x, y)][0])
#     f.write(line + '\n')

# Repeat some code but change max_coord_value and lower point in canvas (make canvas bigger for both sides)
# to make sure we don't count unlimited values

# fill canvas
# {coord: (id, distance_value)}
canvas = {}
shift = 100

for x in range(0 - shift, max_coord_value + shift):
    for y in range(0 - shift, max_coord_value + shift):
        canvas[(x, y)] = ('x', crazy_big_value)

for coord in coords:
    canvas[coord] = (coords_with_ids[coord], 0)


for coord in canvas:
    for coord_target in coords:
        distance = calculate_distance(coord_target, coord)
        canvas_coord_distance = canvas[coord][1]
        if distance < canvas_coord_distance:
            canvas[coord] = (coords_with_ids[coord_target], distance)
        if distance == canvas_coord_distance and distance != 0:
            # use a different id here other than x just to make sure the code works as expected
            canvas[coord] = ('z', distance)

areas_count_big = defaultdict(int)

for coord in canvas:
    id_, _ = canvas[coord]
    areas_count_big[id_] += 1

values = []
for id_ in areas_count:
    if id_ != 'x' and id_ != 'z' and areas_count[id_] == areas_count_big[id_]:
        values.append(areas_count[id_])

print(max(values))

