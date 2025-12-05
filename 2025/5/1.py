FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def in_ranges(x, ranges):
    for r in ranges:
        if x >= r[0] and x <= r[1]:
            return True

    return False

if __name__ == "__main__":
    # load data
    data = load_data()

    data1 = []
    data2 = []
    for x in data:
        if x == "":
            break
        data1.append(x)

    go = False
    for x in data:
        if go:
            data2.append(x)
        if not go:
            go = x == ""

    # pre-process data
    numbers = [int(x) for x in data2]
    ranges = []

    for x in data1:
        r1, r2 = x.split('-')
        ranges.append((int(r1), int(r2)))

    # process

    counter = 0
    for x in numbers:
        if in_ranges(x, ranges):
            counter += 1

    print(counter)
