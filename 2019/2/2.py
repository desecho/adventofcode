from copy import deepcopy

FILENAME = "input.txt"

TARGET = 19690720

def load_data():
    with open(FILENAME) as file:
        return file.read().split(",")


def calculate(data, noun, verb):
    data[1] = noun
    data[2] = verb
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

    return data[0]


if __name__ == "__main__":
    data = load_data()
    data = [int(x) for x in data]

    for noun in range(0, 100):
        for verb in range(0,100):
            result = calculate(deepcopy(data), noun, verb)
            if result == TARGET:
                print(100 * noun + verb)
