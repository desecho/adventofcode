import re

f = open('16.txt')
lines = f.read().splitlines()

MIN_OPCODES = 3

def get_samples():
    n = 0
    samples = []
    while True:
        sample = []
        for x in range(0, 4):
            line = lines[n]
            if x == 0:
                match = re.match(r'Before: \[(\d+), (\d+), (\d+), (\d+)\]', line)
                if match is None:
                    return samples
                result = [int(x) for x in match.groups()]
                sample.append(result)
            elif x == 1:
                match = re.match(r'(\d+) (\d+) (\d+) (\d+)', line)
                result = [int(x) for x in match.groups()]
                sample.append(result)
            elif x == 2:
                match = re.match(r'After:  \[(\d+), (\d+), (\d+), (\d+)\]', line)
                result = [int(x) for x in match.groups()]
                sample.append(result)
            elif x == 3:
                pass
            n += 1
        samples.append(sample)

def addr(registers, values):
    a, b, c = values
    result = registers[a] + registers[b]
    registers[c] = result
    return registers

def addi(registers, values):
    a, b, c = values
    result = registers[a] + b
    registers[c] = result
    return registers

def mulr(registers, values):
    a, b, c = values
    result = registers[a] * registers[b]
    registers[c] = result
    return registers

def muli(registers, values):
    a, b, c = values
    result = registers[a] * b
    registers[c] = result
    return registers

def banr(registers, values):
    a, b, c = values
    result = registers[a] & registers[b]
    registers[c] = result
    return registers

def bani(registers, values):
    a, b, c = values
    result = registers[a] & b
    registers[c] = result
    return registers

def borr(registers, values):
    a, b, c = values
    result = registers[a] | registers[b]
    registers[c] = result
    return registers

def bori(registers, values):
    a, b, c = values
    result = registers[a] | b
    registers[c] = result
    return registers

def setr(registers, values):
    a, b, c = values
    registers[c] = registers[a]
    return registers

def seti(registers, values):
    a, b, c = values
    registers[c] = a
    return registers

def gtir(registers, values):
    a, b, c = values
    if a > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def gtri(registers, values):
    a, b, c = values
    if registers[a] > b:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def gtrr(registers, values):
    a, b, c = values
    if registers[a] > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def eqir(registers, values):
    a, b, c = values
    if a == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def eqri(registers, values):
    a, b, c = values
    if registers[a] == b:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def eqrr(registers, values):
    a, b, c = values
    if registers[a] == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def get_number_of_opcodes(sample):
    n = 0
    registers, instruction, sample_result = sample
    values = instruction[1:]
    for opcode in opcodes:
        result = opcode(list(registers), values)
        if result == sample_result:
            n += 1
    return n


opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
samples = get_samples()

result = 0
for sample in samples:
    number = get_number_of_opcodes(sample)
    if number >= MIN_OPCODES:
        result += 1

print(result)