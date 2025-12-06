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
    numbers = data2[:-1]
    data = data[:-1]

    numbers = transpose(numbers)
    num_digits = []
    for x in numbers:
        digits = 0
        for z in x:
            if len(z) > digits:
                digits = len(z)
        num_digits.append(digits)

    numbers = []
    for x in data:
        values = []
        i = 0
        for n in num_digits:
            values.append(x[i:n+i])
            i = n + i + 1
        numbers.append(values)

    numbers = transpose(numbers)

    numbers_final = []
    for i, x in enumerate(numbers):
        ns = []
        for m in range(num_digits[i]):
            v = ""
            for z in x:
               v += z[m]
            v = int(v.strip())
            ns.append(v)
        numbers_final.append(ns)

    sum = 0
    for i, x in enumerate(numbers_final):
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
