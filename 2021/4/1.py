FILENAME = "input.txt"

# Function made with AI
def transpose(x):
    return list(map(list, zip(*x)))


def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()


def load_data(filename):
    with open(filename) as file:
        return file.read()

def mark_number(b, n):
    for i in b:
        for j in i:
            if j[0] == n:
                j[1] = True


def is_winning(b):
    for l in b:
        if all([z[1] for z in l]):
            return True

    b2 = transpose(b)
    for l in b2:
        if all([z[1] for z in l]):
            return True

    return False

def calculate_answer(b, n):
    sum = 0
    for i in b:
        for j in i:
            if not j[1]:
                sum += j[0]
    return sum * n


def solve(boards, numbers):
    for n in numbers:
        for b in boards:
            mark_number(b, n)
            win = is_winning(b)
            if win:
                return(calculate_answer(b, n))


if __name__ == "__main__":
    # load numbers:
    data = load_lines(FILENAME)
    numbers = data[0].split(',')
    numbers = [int(x) for x in numbers]

    # load boards:
    data = load_data(FILENAME)
    data = data.split('\n\n')
    data = data[1:]

    boards = []
    for x in data:
        b = x.split('\n')
        r = []
        for z in b:
            m = [[int(k), False] for k in z.split(' ') if k]
            if m:
                r.append(m)
        boards.append(r)

    print(solve(boards, numbers))
