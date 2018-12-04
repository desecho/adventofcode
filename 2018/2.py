f = open('2.txt')
lines = f.read().splitlines()

twos = 0
threes = 0

for value in lines:
    two = False
    three = False
    for char in value:
        n = value.count(char)
        if n == 2:
            two = True
        if n == 3:
            three = True

    if two:
        twos += 1
    if three:
        threes += 1

print(twos * threes)

# ---------------------------------------------------

def get_answer():
    value_length = len(lines[0])
    needed_similarity = value_length - 1

    for value1 in lines:
        for value2 in lines:
            sim_num = 0
            answer = ''
            for i in range(0, value_length):
                if value1[i] == value2[i]:
                    sim_num += 1
                    answer += value1[i]
            if sim_num == needed_similarity:
                return answer


print(get_answer())
