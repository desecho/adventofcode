FILENAME = "input.txt"


def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == "__main__":
    data = load_lines(FILENAME)
    data = [int(x) for x in data]
    counter = 0
    prev_sum = None
    for i in range(2, len(data)):
        sum = data[i] + data[i-1] + data[i-2]
        if prev_sum is not None:
            if sum > prev_sum:
                counter += 1
        prev_sum = sum


    print(counter)
