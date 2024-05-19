FILENAME = 'input.txt'

CARDS = "J23456789TQKA"

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_unique_cards(cards_set):
    unique_cards = []
    for card in cards_set:
        if card not in unique_cards:
            unique_cards.append(card)
    return unique_cards

def process_set(cards_set):
    if cards_set == "JJJJJ":
        return ["JJJJJ"]
    output_sets = []
    unique_cards = get_unique_cards(cards_set)
    if "J" not in unique_cards:
        return [cards_set]
    unique_cards.remove("J")
    for card in unique_cards:
        cards_set_copy = cards_set.replace("J", card)
        output_sets.append(cards_set_copy)
    return output_sets

def is_five_of_a_kind(sets):
    for set in sets:
        if set[0] == set[1] == set[2] == set[3] == set[4]:
            return True
    return False

def is_four_of_a_kind(sets):
    for set in sets:
        for card in set:
            if set.count(card) == 4:
                return True
    return False

def is_full_house(sets):
    for set in sets:
        for card in set:
            if set.count(card) == 3:
                set_copy = set.replace(card, "")
                if set_copy[0] == set_copy[1]:
                    return True
    return False

def is_three_of_a_kind(sets):
    for set in sets:
        for card in set:
            if set.count(card) == 3:
                return True
    return False

def is_two_pairs(sets):
    for set in sets:
        for card in set:
            if set.count(card) == 2:
                set_copy = set.replace(card, "")
                return is_one_pair([set_copy])
    return False

def is_one_pair(sets):
    for set in sets:
        for card in set:
            if set.count(card) == 2:
                return True
    return False

def get_score(set):
    score = 0
    set = set[::-1]
    for x in range(len(set)):
        score += CARDS.index(set[x]) * (100 ** (x+1))
    return score

def get_sort_value(set):
    processed_set = process_set(set[0])
    unprocessed_set = [set[0]]
    if is_five_of_a_kind(processed_set):
        return 900000000000000000000000000000000000000000000 + get_score(set[0])
    elif is_four_of_a_kind(processed_set):
        return 80000000000000000000 + get_score(set[0])
    elif is_full_house(processed_set):
        return 600000000000000000 + get_score(set[0])
    elif is_three_of_a_kind(processed_set):
        return 6000000000000 + get_score(set[0])
    elif is_two_pairs(processed_set):
        return 4000000000000 + get_score(set[0])
    elif is_one_pair(processed_set):
        return 2000000000000 + get_score(set[0])

    else:
        return get_score(set[0])
if __name__ == '__main__':
    lines = load_lines(FILENAME)
    sets = []
    for line in lines:
        set = line.split(" ")
        sets.append(set)
    sets.sort(key=get_sort_value)
    result = 0
    for x in range(1, len(sets) + 1):
        # print(x, sets[x-1])
        result += x * int(sets[x-1][1])
    print(result)
