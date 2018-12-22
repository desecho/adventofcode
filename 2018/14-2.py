f = open('14.txt')
recipes = f.read()
recipes_sequence = []
for r in recipes:
    recipes_sequence.append(int(r))

LAST_RECIPES_NUMBER = 10
STEP = 1
recipes = [3, 7]

def get_valid_pos(pos):
    if pos >= len(recipes):
        pos -= len(recipes)
        return get_valid_pos(pos)
    return pos

def find_answer():
    elf1 = 0
    elf2 = 1
    while True:
        sum_ = str(recipes[elf1] + recipes[elf2])
        if len(sum_) == 2:
            recipes.append(int(sum_[0]))
            if recipes_sequence == recipes[-len(recipes_sequence):]:
                return len(recipes) - len(recipes_sequence)
            recipes.append(int(sum_[1]))
        else: # 1
            recipes.append(int(sum_))
        if recipes_sequence == recipes[-len(recipes_sequence):]:
            return len(recipes) - len(recipes_sequence)

        elf1 = get_valid_pos(recipes[elf1] + STEP + elf1)
        elf2 = get_valid_pos(recipes[elf2] + STEP + elf2)

print(find_answer())