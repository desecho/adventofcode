
FILENAME_SEEDS = 'seeds.txt'
FILENAME_1 = 'see_soi.txt'
FILENAME_2 = 'soi_fer.txt'
FILENAME_3 = 'fer_wat.txt'
FILENAME_4 = 'wat_lig.txt'
FILENAME_5 = 'lig_tem.txt'
FILENAME_6 = 'tem_hum.txt'
FILENAME_7 = 'hum_loc.txt'

# FILENAME_SEEDS = 'seeds0.txt'
# FILENAME_1 = 'see_soi0.txt'
# FILENAME_2 = 'soi_fer0.txt'
# FILENAME_3 = 'fer_wat0.txt'
# FILENAME_4 = 'wat_lig0.txt'
# FILENAME_5 = 'lig_tem0.txt'
# FILENAME_6 = 'tem_hum0.txt'
# FILENAME_7 = 'hum_loc0.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_value_from_range(value, range):
    for r in range:
        if value >= r[1] and value < r[1] + r[2]:
            val = value - r[1] + r[0]
            return val
    return value


def load_range(filename):
    lines = load_lines(filename)
    final = []
    for line in lines:
        r = line.split(" ")
        final.append([int(x) for x in r])
    return final

def get_seeds(lines):
    for line in lines:
        r = line.split(" ")
        r = [int(x) for x in r]
        for i in range(r[0], r[1]+ r[0]):
            yield i

if __name__ == '__main__':
    lines = load_lines(FILENAME_SEEDS)
    seeds = list(get_seeds(lines))
    result = 99999999999999999999999999999
    r1 = load_range(FILENAME_1)
    r2 = load_range(FILENAME_2)
    r3 = load_range(FILENAME_3)
    r4 = load_range(FILENAME_4)
    r5 = load_range(FILENAME_5)
    r6 = load_range(FILENAME_6)
    r7 = load_range(FILENAME_7)
    i = 0
    for seed in seeds:
        i += 1
        seed = get_value_from_range(seed, r1)
        seed = get_value_from_range(seed, r2)
        seed = get_value_from_range(seed, r3)
        seed = get_value_from_range(seed, r4)
        seed = get_value_from_range(seed, r5)
        seed = get_value_from_range(seed, r6)
        seed = get_value_from_range(seed, r7)
        if seed < result:
            result = seed
        print(i / len(seeds)*100)
    print(result)
