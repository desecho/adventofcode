from datetime import datetime


f = open('4-0.txt')
lines = f.read().splitlines()

output = []
for line in lines:
    date = line.split(']')[0][1:]
    date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    output.append((date, line))

output.sort(key=lambda x: x[0])

for x in output:
    f = open('4.txt', 'a')
    f.write(x[1] + "\n")
