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
    for line in lines:
        items_length = len(line) // 2
        list1 = line[:items_length]
        list2 = line[items_length:]
        for char in list1:
            if char in list2:
                score = get_score(char)
                sum += score
                break

    print(sum)
