FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


# Function made with AI
def transpose(x):
    return list(map(list, zip(*x)))


if __name__ == "__main__":
    data = load_data()
    data2 = []
    for x in data:
        values = x.split(' ')
        values = [v for v in values if v.strip()]
        data2.append(values)

    symbols = data2[-1]
    data2 = data2[:-1]
    numbers = []
    for x in data2:
        numbers.append([int(z) for z in x])

    numbers = transpose(numbers)

    sum = 0
    for i, x in enumerate(numbers):
        s = symbols[i]
        r = 1  # s == "*"
        if s == "+":
            r = 0

        for v in x:
            if s == "+":
                r += v
            else:
                r *= v

        sum += r

    print(sum)
