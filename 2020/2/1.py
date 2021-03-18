FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_records(line_parts):
    records = []
    for line_parts in line_parts_collection:
        length_parts = line_parts[0].split('-')
        length = int(length_parts[0]), int(length_parts[1])
        letter = line_parts[1][0]
        password = line_parts[2]
        records.append({'length': length, 'letter': letter, 'password': password})
    return records

def get_number_of_valid_passwords(records):
    number_of_valid_passwords = 0
    for record in records:
        number_of_chars_of_the_letter = record['password'].count(record['letter'])
        if number_of_chars_of_the_letter >= record['length'][0] and number_of_chars_of_the_letter <= record['length'][1]:
            number_of_valid_passwords += 1
    return number_of_valid_passwords


if __name__ == '__main__':
    lines = load_lines(FILENAME)
    line_parts_collection = [line.split(' ') for line in lines]
    records = get_records(line_parts_collection)
    print(get_number_of_valid_passwords(records))
