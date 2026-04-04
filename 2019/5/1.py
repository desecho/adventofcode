FILENAME = "input.txt"
INPUT = 1

def load_data():
    with open(FILENAME) as file:
        return file.read().split(",")


if __name__ == "__main__":
    data = load_data()
    data = [int(x) for x in data]
    i = 0
    output = []

    while i < len(data):
        op = data[i]
        if op == 99:
            print(output[-1])
            break
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
                data[v1] = INPUT
            elif op == 4:
                shift = 2
                v1 = data[i+1]
                output.append(data[v1])
                # print(data[v1])
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
            if op < 3:
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
                # v1 = data[i+1]
                data[v1] = INPUT
                if m1 == 0:
                    raise(Exception("error"))
            elif op == 4:
                shift = 2
                output.append(data[v1])
                # print(data[v1])

        i += shift
