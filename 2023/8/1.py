import re
from itertools import cycle

FILENAME = 'input.txt'
FILENAME_INSTRUCTIONS = 'instr.txt'

pattern = re.compile(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)')


def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()



def get_direction(directions):
    for direction in cycle(directions):
        yield direction

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    map = {}
    for line in lines:
        match = pattern.match(line)
        map[match.group(1)] = (match.group(2), match.group(3))
    instructions = load_lines(FILENAME_INSTRUCTIONS)[0]
    direction_gen = get_direction(instructions)

    current = 'AAA'
    counter = 0
    while current != 'ZZZ':
        counter += 1
        direction = next(direction_gen)
        if direction == 'L':
            current = map[current][0]
        else:
            current = map[current][1]
    print(counter)
