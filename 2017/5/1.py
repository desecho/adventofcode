FILENAME = 'input0.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])

    steps = 0
    i = 0
    while i < len(lines) and i >=0:
        steps += 1
        lines[i] += 1
        i += lines[i]
        print(lines)
        print(steps)
        print("i -", i)
    print(steps)
