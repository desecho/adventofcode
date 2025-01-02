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

    result = 0
    for i in range(len(ids1)):
        n = ids1[i]
        n_count = ids2.count(n)
        result += n * n_count

    print(result)
