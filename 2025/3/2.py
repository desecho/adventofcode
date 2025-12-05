FILENAME = "input.txt"
DIGITS = 12

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def get_max(n, answer):
    if len(answer) == 12:
        return int(answer)
    for x in range(9, 0, -1):
        indexes = [i for i, z in enumerate(n) if int(z) == x]
        for i in indexes:
            if i + DIGITS <= len(n) + len(answer):
                answer += str(x)
                return get_max(n[i+1:], answer)

if __name__ == "__main__":
    data = load_data()
    sum = 0
    for x in data:
        z = get_max(x, "")
        sum += z

    print(sum)
