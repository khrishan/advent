__author__ = 'Khrishan'
__title__ = '2015 - Day 03'

with open('input/day03.txt', 'r') as my_file:
    puzzle_input = my_file.read()

moves = {
            '^': [0, 1],
            '>': [1, 0],
            'v': [0, -1],
            '<': [-1, 0]
        }

def print_question():
    print('--- Day 3: Perfectly Spherical Houses in a Vacuum —--\n\n'
          'Santa is delivering presents to an infinite two-dimensional grid of\nhouses.'
          'He begins by delivering a present to the house at his starting location,\nand then an elf at the North Pole '
          'calls him via radio and tells him where\nto move next. Moves are always exactly one house to the north (^), '
          'south\n(v), east (>), or west (<). After each move, he delivers another present\nto the house at his new '
          'location.\n\n'
          'However, the elf back at the north pole has had a little too much eggnog,\nand so his directions are a '
          'little off, and Santa ends up visiting some\nhouses more than once. How many houses receive at least '
          'one present?\n\n'
          'For example:\n\n'
          '  - > delivers presents to 2 houses: one at the starting location, and\n    one to the east.\n'
          '  - ^>v< delivers presents to 4 houses in a square, including twice to\n    the house at his '
          'starting/ending location.\n'
          '  - ^v^v^v^v^v delivers a bunch of presents to some very lucky children\n    at only 2 houses.\n\n'
          '--- Part Two —--\n\n'
          'The next year, to speed up the process, Santa creates a robot version of\nhimself, Robo-Santa, '
          'to deliver presents with him.\n\n'
          'Santa and Robo-Santa start at the same location (delivering two presents\nto the same starting house), '
          'then take turns moving based on instructions\nfrom the elf, who is eggnoggedly reading from '
          'the same script as the\nprevious year.\n\n'
          'This year, how many houses receive at least one present?\n'
          'For example:\n\n'
          '  - ^v delivers presents to 3 houses, because Santa goes north, and then\n    Robo-Santa goes south.\n'
          '  - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end\n    up back where they started.\n'
          '  - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one\n    direction and '
          'Robo-Santa going the other.\n'
    )

def part_1():
    current_position = [0, 0]

    all_points = []
    all_points.append(current_position)

    for char in puzzle_input:
        current_position = [(x + y) for x, y in zip(current_position, moves.get(char))]
        if current_position not in all_points:
            all_points.append(current_position)

    print('Part 1 : {}'.format(len(all_points)))


def part_2():
    current_position_1 = [0, 0]
    current_position_2 = [0, 0]

    all_points = []
    all_points.append(current_position_1)

    i = 0
    for char in puzzle_input:
        if i % 2 == 0:
            current_position_1 = [(x + y) for x, y in zip(current_position_1, moves.get(char))]
            if current_position_1 not in all_points:
                all_points.append(current_position_1)
        else:
            current_position_2 = [(x + y) for x, y in zip(current_position_2, moves.get(char))]
            if current_position_2 not in all_points:
                all_points.append(current_position_2)
        i += 1

    print('Part 2 : {}'.format(len(all_points)))


print_question()
part_1()
part_2()
