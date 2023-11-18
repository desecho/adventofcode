import re

FILENAME = 'input.txt'

stacks = [
    ["D", "M", "S", "Z", "R", "F", "W", "N"],
    ["W", "P", "Q", "G", "S"],
    ["W", "R", "V", "Q", "F", "N", "J", "C"],
    ["F", "Z", "P", "C", "G", "D", "L"],
    ["T", "P", "S"],
    ["H", "D", "F", "W", "R", "L"],
    ["Z", "N", "D", "C"],
    ["W", "N", "R", "F", "V", "S", "J", "Q"],
    ["R", "M", "S", "G", "Z", "W", "V"]
]

pattern = r'move (\d+) from (\d+) to (\d+)'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    result = ""
    lines = load_lines(FILENAME)
    for line in lines:
        match = re.match(pattern, line)
        amount = int(match.group(1))
        source = int(match.group(2)) - 1
        destination = int(match.group(3)) - 1
        to_move = stacks[source][-amount:]
        stacks[destination].extend(to_move)
        stacks[source] = stacks[source][:-amount]
    for stack in stacks:
        result += stack[-1]

    print(result)
