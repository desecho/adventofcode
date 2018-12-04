# This task will require a manual step of transferring a message from an image to text because it is easi

import re

f = open('10.txt')
lines = f.read().splitlines()

dots = []
for line in lines:
    match = re.match(r'position=<(.+), (.+)> velocity=<(.+), (.+)>', line)
    x, y, vx,vy = match.groups()
    dots.append(((int(x), int(y)), (int(vx), int(vy))))


def calculate_change(dots):
    output = []
    for dot in dots:
        x, y = dot[0]
        vx, vy = dot[1]
        x += vx
        y += vy
        output.append(((x, y), (vx, vy)))
    return output

def calculate_area(coord1, coord2, coord3, coord4):
    def calc(coord1, coord2):
        return coord1[0] * coord2[1] - coord1[1] * coord2[0]

    return abs((calc(coord1, coord2) + calc(coord2, coord3) + calc(coord3, coord4) + calc(coord4, coord1)) / 2)

def get_area(dots):
    min_x = 9999999999999999999999
    max_x = 0
    min_y = 9999999999999999999999
    max_y = 0
    for dot in dots:
        x = dot[0][0]
        y = dot[0][1]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    coord1 = (min_x, min_y)
    coord2 = (min_x, max_y)
    coord3 = (max_x, max_y)
    coord4 = (max_x, min_y)
    return calculate_area(coord1, coord2, coord3, coord4)

def find_min_x_and_y(dots):
    min_x = 9999999999999999999999
    min_y = 9999999999999999999999
    for dot in dots:
        x = dot[0]
        y = dot[1]
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
    return min_x, min_y

def find_max_x_and_y(dots):
    max_x = 0
    max_y = 0
    for dot in dots:
        x = dot[0]
        y = dot[1]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return max_x, max_y

def offset_dots(dots, min_x, min_y):
    output = []
    for dot in dots:
        x = dot[0] - min_x
        y = dot[1] - min_y
        output.append((x, y))
    return output

def get_gots_min_area(dots):
    min_area = 99999999999
    # We can get rid of velocities at that point.
    # Min area is supposed to be dropping until it reaches the minumum and then it is supposed to rise again
    while True:
        dots = calculate_change(dots)
        area = get_area(dots)
        if area < min_area:
            min_area = area
            dots_min_area = [dot[0] for dot in dots]
        else:
            return dots_min_area

dots_min_area = get_gots_min_area(dots)
# Print the first available dots so that we get a general idea of where the dots are located.
# Comment it out for now.
# print(dots_min_area)

# Now that we see that all dots have positive values we can easily offset the coordinates as follows:

# Offset the coordinates so that it appears from (0, 0)

min_x, min_y = find_min_x_and_y(dots_min_area)
dots = offset_dots(dots_min_area, min_x, min_y)

# We know that the minimum values for x and y are 0.
# We need to find the maximum values for x and y to be able to print it.

max_x, max_y = find_max_x_and_y(dots)

for y in range(0, max_y + 1):
    line = ''
    for x in range(0, max_x + 1):
        if (x, y) in dots:
            char = 'X'
        else:
            char = ' '
        line += char
    print(line)