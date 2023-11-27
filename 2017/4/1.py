FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    counter = 0
    for line in lines:
        words = line.split(" ")
        if len(words) == len(set(words)):
            counter += 1

    print(counter)
