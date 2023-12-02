from functools import reduce

def _generate_games(lines):
    games = {}

    for l in lines:
        string = l.split(': ') 
        game = string[0]
        game = int(game.replace('Game ', ''))

        sets = []

        set_strings = string[1].split('; ')
        for game_set_string in set_strings:
            game_set = {}
            cubes = game_set_string.split(', ')
            for c in cubes:
                c = c.split(' ')
                game_set[c[1][0]] = int(c[0])
            sets.append(game_set)

        games[game] = sets
    
    return games

def part1(lines):
    cube_rules = {
        "r" : 12,
        "g" : 13,
        "b" : 14,
    }

    games = _generate_games(lines)

    count = 0
    for index, game in games.items():
       valid = True
       for game_set in game:
            for key in cube_rules:
                if key in game_set:
                    if game_set[key] > cube_rules[key]:
                        valid = False
                        continue
       if valid:
           count += index

    return count

def part2(lines):
    games = _generate_games(lines)

    keys = ["r", "g", "b"]

    count = 0
    for game in games.values():
        result = {}

        for game_set in game:
            for key in keys:
                if key in game_set:
                    if key not in result or game_set[key] > result[key]:
                        result[key] = game_set[key] 

        count += reduce((lambda x, y: x * y), result.values())
    
    return count

    

if __name__ == '__main__':
    INPUT_FILE = "input/day02.txt"

    with open(INPUT_FILE) as f:
        lines = [x.strip() for x in f.readlines()]
    
    # Part 1
    print(part1(lines))

    # Part 2
    print(part2(lines))
