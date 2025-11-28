FILENAME = "input.txt"


def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == "__main__":
    data = load_lines(FILENAME)

    x = 0
    y = 0
    aim = 0
    for d in data:
        direction, value = d.split(' ')
        value = int(value)
        if direction == "forward":
            x += value
            y += aim * value
        elif direction == "backward":
            x -= value
            y -= aim * value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value

    result = x * y
    print(result)
