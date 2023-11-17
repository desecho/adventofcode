FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()


def get_score(char):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38

if __name__ == '__main__':
    sum = 0
    lines = load_lines(FILENAME)
    for i in range(1, len(lines) + 1):
        if i % 3 == 0:
            for char in lines[i-1]:
                if char in lines[i-2]:
                    if char in lines[i-3]:
                        score = get_score(char)
                        sum += score
                        break

    print(sum)
