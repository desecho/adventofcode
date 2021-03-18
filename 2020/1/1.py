YEAR = 2020
FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_product(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == YEAR:
                return i * j

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    numbers = [int(x) for x in lines]
    print(get_product(numbers))
