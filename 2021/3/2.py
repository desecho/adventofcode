from copy import deepcopy

FILENAME = "input.txt"


def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()


def process(n, data, l):
    r = []
    m = None
    for x in data:
        r.append(x[n])
    zeros_count = r.count('0')
    ones_count = r.count('1')
    if l == '0':
        if zeros_count > ones_count:
            m = '0'
        else:
            m = '1'
    else:
        if ones_count >= zeros_count:
            m = '0'
        else:
            m = '1'

    return m

if __name__ == "__main__":
    data = load_lines(FILENAME)
    data_copy = deepcopy(data)

    for x in range(len(data[0])):
        m = process(x, data, '0')
        data = [z for z in data if z[x] == m]
        if len(data) == 1:
            break

    print(data)

    for x in range(len(data_copy[0])):
        m = process(x, data_copy, '1')
        data_copy = [z for z in data_copy if z[x] == m]
        if len(data_copy) == 1:
            break

    print(data_copy)

    r1 = int(data[0], 2)
    r2 = int(data_copy[0], 2)
    print(r1, r2)

    result = r1 * r2
    print(result)
