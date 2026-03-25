FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().split(",")


if __name__ == "__main__":
    data = load_data()
    data = [int(x) for x in data]
    # data[1] = 12
    # data[2] = 2
    i = 0

    while i < len(data):
        op = data[i]
        if op == 99:
            break
        v1 = data[data[i+1]]
        v2 = data[data[i+2]]
        v3 = data[i+3]
        if len(str(op)) == 1:
            if op == 1:
                shift = 4
                data[v3] = v2 + v3
            elif op == 2:
                shift = 4
                data[v3] = v2 * v3
            elif op == 3:
                shift = 2
                data[v3] = v2 * v3
