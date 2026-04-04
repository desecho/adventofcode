from itertools import permutations

FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().split(",")


def calc(data, inputs):
    i = 0
    output = []

    while i < len(data):
        op = data[i]
        if op == 99:
            return output[-1]
        str_op = str(op)
        if len(str_op) == 1:
            if op == 1:
                shift = 4
                v1 = data[data[i+1]]
                v2 = data[data[i+2]]
                v3 = data[i+3]

                data[v3] = v1 + v2
            elif op == 2:
                shift = 4
                v1 = data[data[i+1]]
                v2 = data[data[i+2]]
                v3 = data[i+3]

                data[v3] = v1 * v2
            elif op == 3:
                shift = 2
                v1 = data[i+1]
                data[v1] = inputs.pop()
            elif op == 4:
                shift = 2
                v1 = data[i+1]
                output.append(data[v1])
            elif op == 5:
                shift = 3
                v1 = data[i+1]
                if v1 != 0:
                    i = data[i+2]
                    continue
            elif op == 6:
                shift = 3
                v1 = data[i+1]
                if v1 == 0:
                    i = data[i+2]
                    continue
            elif op == 7:
                shift = 4
                v1 = data[data[i+1]]
                v2 = data[data[i+2]]
                v3 = data[i+3]
                if v1 < v2:
                    data[v3] = 1
                else:
                    data[v3] = 0
            elif op == 8:
                shift = 4
                v1 = data[data[i+1]]
                v2 = data[data[i+2]]
                v3 = data[i+3]
                if v1 == v2:
                    data[v3] = 1
                else:
                    data[v3] = 0

        else:
            op = int(str_op[-2:])
            modes = str_op[:-2]
            if len(modes) == 1:
                modes = '00' + modes
            elif len(modes) == 2:
                modes = '0' + modes
            m1 = int(modes[-1])
            m2 = int(modes[-2])
            m3 = int(modes[-3])
            if m1 == 1:
                v1 = data[i+1]
            else:
                v1 = data[data[i+1]]
            if op < 3 or op > 4:
                if m2 == 1:
                    v2 = data[i+2]
                else:
                    v2 = data[data[i+2]]
                if m3 == 1:
                    raise(Exception("error"))
                else:
                    v3 = data[i+3]
            shift = 4
            if op == 1:
                data[v3] = v1 + v2
            elif op == 2:
                data[v3] = v1 * v2
            elif op == 3:
                shift = 2
                data[v1] = inputs.pop()
                if m1 == 0:
                    raise(Exception("error"))
            elif op == 4:
                shift = 2
                output.append(data[v1])
            elif op == 5:
                shift = 3
                if v1 != 0:
                    i = v2
                    continue
            elif op == 6:
                shift = 3
                if v1 == 0:
                    i = v2
                    continue
            elif op == 7:
                if v1 < v2:
                    data[v3] = 1
                else:
                    data[v3] = 0
            elif op == 8:
                if v1 == v2:
                    data[v3] = 1
                else:
                    data[v3] = 0

        i += shift



if __name__ == "__main__":
    data = load_data()
    data = [int(x) for x in data]

    phases = [3,1,2,4,0]
    perms = permutations(phases, 5)
    max = 0
    for p in perms:
        a = calc(data, [0, p[0]])
        b = calc(data, [a, p[1]])
        c = calc(data, [b, p[2]])
        d = calc(data, [c, p[3]])
        e = calc(data, [d, p[4]])
        if e > max:
            max = e

    print(max)
