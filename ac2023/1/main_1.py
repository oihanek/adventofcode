import re

from utils import load_input

counter = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
lines = load_input('1/input.txt')

# ---- FIRST PUZZLE ----

calibration_values = []
for parts in lines:
    line_digits = list(re.findall(r'\d', parts))
    calibration_value = int(line_digits[0] + line_digits[-1])
    calibration_values.append(calibration_value)

first_puzzle = sum(calibration_values)
print(f'First puzzle: {first_puzzle}')

# ---- SECOND PUZZLE ----

def convert_to_string_number(string):
  try:
    return counter[string]
  except KeyError as ex:
    return string


line_parts = []
for line in lines:
    parts = []
    numbers_as_numbers = list(re.finditer(r'\d', line))
    parts.extend(numbers_as_numbers)
    for key in counter:
        numbers_as_text = list(re.finditer(key, line))
        parts.extend(numbers_as_text)
    sorted_line = sorted(parts, key=lambda x: x.span())
    line_parts.append(sorted_line)

line_numbers = []
for part in line_parts:
  first_part = convert_to_string_number(part[0].group())
  second_part = convert_to_string_number(part[-1].group())
  number = int(first_part + second_part)
  line_numbers.append(number)

second_puzzle = sum(line_numbers)
print(f'Second puzzle: {second_puzzle}')
