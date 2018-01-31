__author__ = 'Khrishan'
__title__ = '2015 - Day 01'

# Read in puzzle input
with open('input/day01.txt', 'r') as my_file:
    puzzle_input = my_file.read().replace('\n', '')


def print_question():
    print('--- Day 1: Not Quite Lisp ---\n'
          '\n'
          'Santa was hoping for a white Christmas, but his weather machine\'s "snow"\n'
          'function is powered by stars, and he\'s fresh out! To save Christmas, he\n'
          'needs you to collect fifty stars by December 25th.\n'
          '\n'
          'Collect stars by helping Santa solve puzzles. Two puzzles will be made\n'
          'available on each day in the advent calendar; the second puzzle is\n'
          'unlocked when you complete the first. Each puzzle grants one star. Good\n'
          'luck!\n'
          '\n'
          'Here\'s an easy puzzle to warm you up.\n'
          '\n'
          'Santa is trying to deliver presents in a large apartment building, but he\n'
          'can\'t find the right floor - the directions he got are a little\n'
          'confusing. He starts on the ground floor (floor 0) and then follows the\n'
          'instructions one character at a time.\n'
          '\n'
          'An opening parenthesis, (, means he should go up one floor, and a closing\n'
          'parenthesis, ), means he should go down one floor.\n'
          '\n'
          'The apartment building is very tall, and the basement is very deep; he\n'
          'will never find the top or bottom floors.\n'
          '\n'
          'For example:\n'
          '\n'
          '  - (()) and ()() both result in floor 0.\n'
          '  - ((( and (()(()( both result in floor 3.\n'
          '  - ))((((( also results in floor 3.\n'
          '  - ()) and ))( both result in floor -1 (the first basement level).\n'
          '  - ))) and )())()) both result in floor -3.\n'
          '\n' 
          'To what floor do the instructions take Santa?\n'
          '\n'
          '--- Part Two ---\n'
          '\n'
          'Now, given the same instructions, find the position of the first\n'
          'character that causes him to enter the basement (floor -1). The first\n'
          'character in the instructions has position 1, the second character has\n'
          'position 2, and so on.\n'
          '\n'
          'For example:\n'
          '\n'
          '  - ) causes him to enter the basement at character position 1.\n'
          '  - ()()) causes him to enter the basement at character position 5.\n'
          '\n'
          'What is the position of the character that causes Santa to first enter\n'
          'the basement?\n'
          '\n'

        )

def part_1():
    floor = 0
    for char in puzzle_input:
        if char == '(':
            floor += 1
        else:
            floor -= 1

    print('Part 1 : {}'.format(floor))


def part_2():
    floor = 0
    for i in range(0, len(puzzle_input)):
        if puzzle_input[i] == '(':
            floor += 1
        else:
            floor -= 1

        if floor < 0:
            break;

    print('Part 2 : {}'.format(i + 1))

#print_question()
part_1()
part_2()
