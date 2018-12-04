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

def get_seconds(dots):
    min_area = 99999999999
    # Min area is supposed to be dropping until it reaches the minumum and then it is supposed to rise again
    i = 0
    while True:
        i += 1
        dots = calculate_change(dots)
        area = get_area(dots)
        if area < min_area:
            min_area = area
        else:
            return i - 1

print(get_seconds(dots))
