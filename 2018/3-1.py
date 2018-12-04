# use 1001 (+1) because it says at least 1000 which means it can be more and my code fails if I make it less than 1000
canvas_width = 1001

# Fill canvas with zero values
canvas = {}
for x in range(0, canvas_width):
    canvas[x] = {}
    for y in range(0, canvas_width):
        canvas[x][y] = 0

f = open('3.txt')
lines = f.read().splitlines()

def parse_line(line):
    line = line.split('@ ')[-1]
    coords, measures = line.split(': ')
    x, y = coords.split(',')
    x = int(x)
    y = int(y)
    width, height = measures.split('x')
    width = int(width)
    height = int(height)
    return x, y, width, height

# Claims are stored in this format: (x, y, width, height)
claims = []

for line in lines:
    claims.append(parse_line(line))

for claim in claims:
    x, y, width, height = claim
    for g in range(x, x + width):
        for h in range(y, y + height):
            canvas[g][h] += 1

n = 0
for x in range(0, canvas_width):
    for y in range(0, canvas_width):
        if canvas[x][y] > 1:
            n += 1

print(n)