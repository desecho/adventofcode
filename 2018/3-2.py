# use 1001 (+1) because it says at least 1000 which means it can be more and my code fails if I make it less than 1000
canvas_width = 1001

# Fill canvas with zero values
canvas = {}
for x in range(0, canvas_width):
    canvas[x] = {}
    for y in range(0, canvas_width):
        canvas[x][y] = 0

# Fill canvas_ids canvas with empty values
canvas_ids = {}
for x in range(0, canvas_width):
    canvas_ids[x] = {}
    for y in range(0, canvas_width):
        canvas_ids[x][y] = ''


f = open('3.txt')
lines = f.read().splitlines()

def parse_line(line):
    line = line.split(' @ ')
    id_ = line[0].replace('#', '')
    coords_measures = line[1]
    coords, measures = coords_measures.split(': ')
    x, y = coords.split(',')
    x = int(x)
    y = int(y)
    width, height = measures.split('x')
    width = int(width)
    height = int(height)
    return id_, x, y, width, height

# Claims are stored in this format: (id, x, y, width, height)
claims = []

# Claims with ids are stored in this format: {id: (x, y, width, height)}
claims_with_ids = {}

for line in lines:
    claims.append(parse_line(line))

for claim in claims:
    claims_with_ids[claim[0]] = claim[1:]

for claim in claims:
    id_, x, y, width, height = claim
    for g in range(x, x + width):
        for h in range(y, y + height):
            canvas[g][h] += 1
            canvas_ids[g][h] = id_

claims_to_check = set()
for x in range(0, canvas_width):
    for y in range(0, canvas_width):
        if canvas[x][y] == 1:
            claims_to_check.add(canvas_ids[x][y])

def test_claim(claim):
    x, y, width, height = claim
    for g in range(x, x + width):
        for h in range(y, y + height):
            if canvas[g][h] != 1:
                claims_to_check.discard(id_)
                return

for id_ in list(claims_to_check):
    test_claim(claims_with_ids[id_])

print(list(claims_to_check)[0])