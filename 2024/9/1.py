FILENAME = "input0.txt"


def load_data(filename):
    with open(filename) as file:
        return file.read().splitlines()[0]


def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    data = load_data(FILENAME)
    print(data)

    result1 = ""
    id = 0
    for i in range(1, len(data)+1):
        n = int(data[i-1])
        if not is_even(i):
            result1 += str(id) * n
            id += 1
        else:
            result1 += '.' * n
        print(result1)

    print(result1)
