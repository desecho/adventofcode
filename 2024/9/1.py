FILENAME = "input.txt"


def load_data(filename):
    with open(filename) as file:
        return file.read().splitlines()[0]


def is_even(n):
    return n % 2 == 0


def find_last_value_and_remove(x):
    for i in range(len(x) -1, -1, -1):
        if x[i] != '.':
            old_value = x[i]
            x[i] = '.'
            return old_value

def defrag(x):
    l = find_last_value_and_remove(x)
    # Find first empty space available
    i = x.index('.')
    x[i] = l

if __name__ == "__main__":
    data = load_data(FILENAME)
    data = list(data)

    result1 = []
    id = 0
    for i in range(1, len(data) + 1):
        n = int(data[i - 1])
        if not is_even(i):
            for j in range(n):
                result1.append(id)
            id += 1
        else:
            for j in range(n):
                result1.append('.')

    print("Phase1 complete")
    print(result1)

    defragged = False
    while not defragged:
        defrag(result1)
        empty_spaces_count = result1.count('.')
        z = result1[-empty_spaces_count:].count('.')
        print(z/empty_spaces_count)
        if list("."*empty_spaces_count) == result1[-empty_spaces_count:]:
            defragged = True

    print("Phase2 complete")

    print(result1)

    result2 = 0

    for i in range(len(result1)):
        value = result1[i]
        if value != '.':
            result2 += i * int(value)

    print(result2)
