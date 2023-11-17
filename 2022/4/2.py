FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_numbers_from_pair(pair):
    numbers = []
    for i in range (int(pair[0]), int(pair[1]) + 1):
        numbers.append(i)
    return numbers

def does_overlap(numbers1, numbers2):
    for number in numbers1:
        if number in numbers2:
            return True
    return False

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    result = 0
    for line in lines:
        pairs = line.split(',')
        pair1 = pairs[0].split('-')
        pair2 = pairs[1].split('-')
        numbers1 = get_numbers_from_pair(pair1)
        numbers2 = get_numbers_from_pair(pair2)
        if does_overlap(numbers1, numbers2):
            result += 1
    print(result)
