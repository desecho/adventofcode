import re

FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    pattern = re.compile(r'([\d]+)   ([\d]+)')
    ids1 = []
    ids2 = []
    for line in lines:
        match = pattern.match(line)
        id1 = int(match.group(1))
        id2 = int(match.group(2))
        ids1.append(id1)
        ids2.append(id2)

    ids1.sort()
    ids2.sort()

    result = 0
    for i in range(len(ids1)):
        result += abs(ids1[i] - ids2[i])

    print(result)
