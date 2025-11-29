from collections import defaultdict

FILENAME = "input.txt"


def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == "__main__":
    data = load_lines(FILENAME)
    r = defaultdict(list)
    for x in data:
        for i in range(len(x)):
            r[i].append(x[i])

    result1 = ''
    result2 = ''
    for x in r.values():
        zeros_count = x.count('0')
        ones_count = x.count('1')
        if zeros_count > ones_count:
            result1 += '0'
            result2 += '1'
        else:
            result2 += '0'
            result1 += '1'

    print(result1, result2)

    r1 = int(result1, 2)
    r2 = int(result2, 2)

    result = r1 * r2
    print(result)
