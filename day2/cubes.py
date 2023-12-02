# Constants
cube_pool = {
    'red': 12,
    'green': 13,
    'blue': 14
}
colors = list(cube_pool.keys())


# Part 1
def valid_game(game: str) -> int:
    game_id, game = game.split(':')
    id = game_id.split()[-1]
    rounds = game.split(';')
    
    valid = True
    for round in rounds:
        color_sums = round.split(',')
        for color_sum in color_sums:
            sum, color = color_sum.split()
            if int(sum) > cube_pool[color]:
                valid = False

    return int(id) if valid else 0


def cube_conundrum(input_filepath: str) -> int:
    input = open(input_filepath, 'r')
    games = input.readlines()

    id_sum = 0
    for game in games:
        id = valid_game(game)
        id_sum += id

    return id_sum


# Part 2
def min_cubes(game: str) -> int:
    game_id, game = game.split(':')
    id = game_id.split()[-1]
    rounds = game.split(';')
    
    min_cubes = {colors[i]: 0 for i in range(len(colors))}
    for round in rounds:
        color_sums = round.split(',')
        for color_sum in color_sums:
            sum, color = color_sum.split()
            if int(sum) > min_cubes[color]:
                min_cubes[color] = int(sum)

    power = 1
    for num_cubes in min_cubes.values():
        power *= num_cubes

    return power


def cube_conundrum_2(input_filepath: str) -> int:
    input = open(input_filepath, 'r')
    games = input.readlines()

    power_sum = 0
    for game in games:
        power = min_cubes(game)
        power_sum += power

    return power_sum


if __name__ == '__main__':
    print(f'Part 1: {cube_conundrum("input.txt")}')
    print(f'Part 2: {cube_conundrum_2("input.txt")}')