FILENAME = "input.txt"


def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()



def has_number(n, x):
    n = str(n)
    n1 = n[0]
    n2 = n[1]
    try:
        i = x.index(n1)
    except ValueError:
        return False
    indexes = [i for i, z in enumerate(x) if z == n2]
    for j in indexes:
        if j > i:
            return True

    return False


def get_max(n):
    for x in range(99, 9, -1):
        if "0" in str(x):
            continue
        if has_number(x, n):
            return x
    raise Exception("FAILED")


if __name__ == "__main__":
    data = load_data()
    sum = 0
    for x in data:
        z = get_max(x)
        sum += z

    print(sum)
