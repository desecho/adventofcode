FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def calculate(x, sum):
    z = x // 3 - 2
    if z <=0:
        return sum
    sum += z
    return calculate(z, sum)

if __name__ == "__main__":
    data = load_data()
    result = 0
    for x in data:
        result += calculate(int(x), 0)

    print(result)
