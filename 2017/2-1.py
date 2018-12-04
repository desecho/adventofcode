f = open('2.txt')
lines = f.read().splitlines()

n = 0
for line in lines:
    numbers = line.split(' ')
    numbers_list = []
    for number in numbers:
        number = number.strip()
        if number:
            numbers_list.append(int(number))
    max_number = max(numbers_list)
    min_number = min(numbers_list)
    x = max_number - min_number
    n += x

print(n)