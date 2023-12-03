import re
from itertools import chain

from utils import load_input


def find_match_in_range(digits_list, line, position):
    line = digits_list[line]
    for digit in line:
        if position in range(*digit.span()):
            return digit
    return None


def find_adjacent_numbers(symbols_list, digits_list):
    matches = []
    for line_idx, values in enumerate(symbols_list):
        for gear in values:
            adjacent_numbers = []
            for i in range(-1, 2):
                current_line = line_idx + i
                for j in range(-1, 2):
                    current_pos = gear.span()[0] + j
                    adjacent = find_match_in_range(digits_list, current_line, current_pos)

                    if adjacent and adjacent not in adjacent_numbers:
                        adjacent_numbers.append(adjacent)
            matches.append(adjacent_numbers)
    return matches


digits = []
symbols = []
gears = []

lines = load_input('3/input.txt')

for line_idx in lines:
    digits.append(list(re.finditer(r'\d+', line_idx.strip())))
    symbols.append(list(re.finditer(r'[^\d.\n]+', line_idx.strip())))
    gears.append(list(re.finditer(r'\*', line_idx.strip())))

# ---- FIRST PUZZLE ----
adjacent_numbers = find_adjacent_numbers(symbols, digits)
flattened_list = chain.from_iterable(adjacent_numbers)
first_puzzle = sum(map(lambda x: int(x.group()), flattened_list))
print(f'First puzzle: {first_puzzle}')

# ---- SECOND PUZZLE ----
adjacent_numbers = find_adjacent_numbers(gears, digits)
adjacent_numbers = [adjacent for adjacent in adjacent_numbers if len(adjacent) == 2]
second_puzzle = sum(map(lambda x: int(x[0].group()) * int(x[1].group()), adjacent_numbers))
print(f'Second puzzle: {second_puzzle}')
