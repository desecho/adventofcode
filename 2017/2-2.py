f = open('2.txt')
lines = f.read().splitlines()


def get_value(numbers):
    for x in numbers:
        for y in numbers:
            if x == y:
                continue
            val = x / y
            if val.is_integer():
                return int(val)
    return 1  # Could happen only if there is a same number in a row twice

n = 0
for line in lines:
    numbers = line.split(' ')
    numbers_list = []
    for number in numbers:
        number = number.strip()
        if number:
            numbers_list.append(int(number))
    x = get_value(numbers_list)
    n += x

print(n)