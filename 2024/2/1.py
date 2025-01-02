FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def check_if_gradually_increasing(numbers):
    for i in range(1, len(numbers)):
        n1 = numbers[i-1]
        n2 = numbers[i]
        x = n2 - n1
        if x < 1 or x > 3:
            return False
    return True

def check_if_gradually_decreasing(numbers):
    for i in range(1, len(numbers)):
        n1 = numbers[i-1]
        n2 = numbers[i]
        x = n2 - n1
        if x > 0:
            return False
        x = abs(x)
        if x < 1 or x > 3:
            return False
    return True

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    reports = []
    for line in lines:
        numbers = line.split(" ")
        numbers = [int(number) for number in numbers]
        reports.append(numbers)

    result = 0
    for report in reports:
        if check_if_gradually_increasing(report) or check_if_gradually_decreasing(report):
            result += 1

    print(result)
