FILENAME = "input.txt"


def load_data():
    with open(FILENAME) as file:
        return file.read().split('-')


def two_adjacent(x):
    x = str(x)
    r1 = x[0] == x[1] and x[2] != x[1]
    r2 = x[1] == x[2] and x[3] != x[2] and x[0] != x[2]
    r3 = x[2] == x[3] and x[4] != x[3] and x[1] != x[3]
    r4 = x[3] == x[4] and x[5] != x[4] and x[2] != x[4]
    r5 = x[4] == x[5] and x[3] != x[4] and x[3] != x[4]
    return r1 or r2 or r3 or r4 or r5

def never_decrease(x):
    x = str(x)
    x0 = int(x[0])
    x1 = int(x[1])
    x2 = int(x[2])
    x3 = int(x[3])
    x4 = int(x[4])
    x5 = int(x[5])
    return x0 <= x1 and x1 <= x2 and x2 <= x3 and x3 <= x4 and x4 <= x5


def is_valid_password(x):
    return two_adjacent(x) and never_decrease(x)


if __name__ == "__main__":
    data = load_data()
    x1, x2 = data
    x1 = int(x1)
    x2 = int(x2)

    result = 0
    for x in range(x1, x2 + 1):
        if is_valid_password(x):
            result += 1

    print(result)
