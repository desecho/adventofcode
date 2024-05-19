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

def all_positions_end_with_z(positions):
    for pos in positions:
        if pos[-1] != "Z":
            return False
    return True

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    map = {}
    for line in lines:
        match = pattern.match(line)
        map[match.group(1)] = (match.group(2), match.group(3))
    instructions = load_lines(FILENAME_INSTRUCTIONS)[0]
    direction_gen = get_direction(instructions)

    starting_positions = []
    for key in map:
        if key[-1] == "A":
            starting_positions.append(key)

    # for i, position in enumerate(starting_positions):
    #     print(i, position)

    positions = starting_positions

    counter = 0
    while not all_positions_end_with_z(positions):
        counter += 1
        direction = next(direction_gen)
        if direction == 'L':
            for i, pos in enumerate(positions):
                positions[i] = map[positions[i]][0]
        else:
            for i, pos in enumerate(positions):
                positions[i] = map[positions[i]][1]
        print(counter)
    print("answer")
    print(counter)
