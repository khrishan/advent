__author__ = 'Khrishan'
__title__ = '2015 - Day 02'

import re

puzzle_input = [line.rstrip('\n') for line in open('input/day02.txt')]

def print_question():
    print('--- Day 2: I Was Told There Would Be No Math ---\n'
          '\n'
          'The elves are running low on wrapping paper, and so they need to submit\n'
          'an order for more. They have a list of the dimensions (length l, width w,\n'
          'and height h) of each present, and only want to order exactly as much as\n'
          'they need.\n'
          '\n'
          'Fortunately, every present is a box (a perfect right rectangular prism),\n'
          'which makes calculating the required wrapping paper for each gift a\n'
          'little easier: find the surface area of the box, which is\n'
          '2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each\n'
          'present: the area of the smallest side.\n'
          '\n'
          'For Example:\n'
          '\n'
          '  - A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square\n'
          '    feet of wrapping paper plus 6 square feet of slack, for a total of 58\n'
          '    square feet.\n'
          '  - A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42\n'
          '    square feet of wrapping paper plus 1 square foot of slack, for a\n'
          '    total of 43 square feet.\n'
          '\n'
          'All numbers in the elves\' list are in feet. How many total square feet of\nwrapping paper should they order?\n'
          '\n'
          '--- Part Two ---\n'
          '\n'
          'The elves are also running low on ribbon. Ribbon is all the same width,\nso they only have to worry about the length they need to order, which\nthey would again like to be exact.\n'
          '\n'
          'The ribbon required to wrap a present is the shortest distance around its\nsides, or the smallest perimeter of any one face. Each present also\nrequires a bow made out of ribbon as well; the feet of ribbon required\nfor the perfect bow is equal to the cubic feet of volume of the present.\nDon\'t ask how they tie the bow, though; they\'ll never tell.\n'
          '\n'
          'For example:\n'
          '\n'
          '  - A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon\n'
          '    to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a\n'
          '    total of 34 feet.\n'
          '  - A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon\n'
          '    to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for\n'
          '    a total of 14 feet.\n'
          '\n'
          'How many total feet of ribbon should they order?\n'
         )


def part_1():
    total = 0
    for line in puzzle_input:
        match = re.match(r'([0-9]+)x([0-9]+)x([0-9]+)', line, re.I)
        length = int(match.group(1))
        width  = int(match.group(2))
        height = int(match.group(3))

        smallest = length * width

        if width * height < smallest:
            smallest = width * height

        if height * length < smallest:
            smallest = height * length

        total += (2 * length * width) + (2 * width * height) + (2 * height * length) + smallest

    print('Part 1 : {}'.format(total))


def part_2():
    total = 0
    for line in puzzle_input:
        match = re.match(r'([0-9]+)x([0-9]+)x([0-9]+)', line, re.I)
        dims = [int(match.group(1)), int(match.group(2)), int(match.group(3))]
        dims.sort()

        total += (2 * dims[0]) + (2 * dims[1]) + (dims[0] * dims[1] * dims[2])

    print('Part 2 : {}'.format(total))



print_question()
part_1()
part_2()
