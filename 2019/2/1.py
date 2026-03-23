FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().split(",")


if __name__ == "__main__":
    data = load_data()
    data = [int(x) for x in data]
    data[1] = 12
    data[2] = 2
    for i in range(0, len(data), 4):
        v1 = data[i]
        if v1 == 99:
            break
        v2 = data[data[i+1]]
        v3 = data[data[i+2]]
        v4 = data[i+3]
        if v1 == 1:
            data[v4] = v2 + v3
        elif v1 == 2:
            data[v4] = v2 * v3

    print(data[0])
