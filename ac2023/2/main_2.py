from functools import reduce
from utils import load_input

reference_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
lines = load_input('2/input.txt')
games_per_color = {}
max_cubes_per_color = {}

for line in lines:
    name, game = line.strip().split(':')
    game_id = int(name.split(' ')[1])
    cubesets = game.split(';')

    games_per_color[game_id] = []
    max_cubes_per_color[game_id] = {}

    for el in cubesets:
        cubes = el.strip().split(',')
        cubes_per_color = {}
        for cube in cubes:
            number, color = cube.strip().split(' ')
            cubes_per_color[color] = int(number)

            if color not in max_cubes_per_color[game_id]:
                max_cubes_per_color[game_id][color] = 0
            max_cubes_per_color[game_id][color] = max(max_cubes_per_color[game_id][color], int(number))

        games_per_color[game_id].append(cubes_per_color)


possible_games = []
for idx, game in games_per_color.items():
    is_possible = True
    for el in game:
        for ref, value in reference_cubes.items():
            try:
                if el[ref] and el[ref] > reference_cubes[ref]:
                    is_possible = False
                    break
            except KeyError as exc:
                continue
    if is_possible:
        possible_games.append(idx)

first_puzzle = sum(possible_games)
print(f'First puzzle: {first_puzzle}')


# ---- SECOND PUZZLE ----

game_power = []
for el in max_cubes_per_color.values():
    set_power = reduce(lambda x, y: x * y, el.values())
    game_power.append(set_power)

second_puzzle = sum(game_power)
print(f'Second puzzle: {second_puzzle}')
