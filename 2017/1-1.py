f = open('1.txt')
line = f.read()

line += line[0]

n = 0
prev_char = False
for char in line:
    if prev_char:
        if char == prev_char:
            n += int(char)
    prev_char = char

print(n)