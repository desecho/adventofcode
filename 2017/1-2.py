f = open('1.txt')
line = f.read()

n = 0
line_length = len(line)
half = int(line_length / 2)

line += line
for x in range(0, line_length):
    i = x + half
    if line[x] == line[i]:
        n += int(line[x])

print(n)