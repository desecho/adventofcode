FILENAME1 = 'input-1.txt'
FILENAME2 = 'input-2.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def load_rules(lines):
    result = []
    for line in lines:
        result.append(line.split("|"))
    return result

def load_prints(lines):
    result = []
    for line in lines:
        result.append(line.split(","))
    return result

def is_valid_print(print, rules):
    for rule in rules:
        if rule[0] in print and rule[1] in print:
            if print.index(rule[0]) > print.index(rule[1]):
                return False
    return True

def process_prints(prints, rules):
    output = []
    for print in prints:
        if is_valid_print(print, rules):
            output.append(print)
    return output

if __name__ == '__main__':
    lines = load_lines(FILENAME1)
    rules = load_rules(lines)

    lines = load_lines(FILENAME2)
    prints = load_prints(lines)

    prints = process_prints(prints, rules)

    result = 0
    for p in prints:
        n = len(p) // 2
        result += int(p[n])
    print(result)
