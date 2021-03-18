YEAR = 2020
FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_product(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == YEAR:
                    return i * j * k

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    numbers = [int(x) for x in lines]
    print(get_product(numbers))
