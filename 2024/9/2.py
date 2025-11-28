FILENAME = "input.txt"


def load_data(filename):
    with open(filename) as file:
        return file.read().splitlines()[0]


def is_even(n):
    return n % 2 == 0


def find_subsequence(arr, sub):
    for i in range(len(arr) - len(sub) + 1):
        if arr[i : i + len(sub)] == sub:
            return i
    return -1


def get_max(x):
    x = [z for z in x if z != "."]
    return max(x)


def defrag(x):
    max_id = get_max(x)
    for i in range(max_id, 0, -1):
        print(i / max_id)
        n = x.count(i)
        l = find_subsequence(x, list("." * n))
        z = x.index(i)
        if l != -1 and z > l:
            for j in range(l, l + n):
                x[j] = i
            for j in range(z, z + n):
                x[j] = "."


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
                result1.append(".")

    print("Phase1 complete")
    print(result1)

    defrag(result1)

    print("Phase2 complete")

    print(result1)

    result2 = 0

    for i in range(len(result1)):
        value = result1[i]
        if value != ".":
            result2 += i * int(value)

    print(result2)
