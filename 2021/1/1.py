FILENAME = "input.txt"


def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == "__main__":
    data = load_lines(FILENAME)
    data = [int(x) for x in data]
    counter = 0
    prev_value = None
    for x in data:
        if prev_value is not None:
            if x > prev_value:
                counter += 1
        prev_value = x


    print(counter)
