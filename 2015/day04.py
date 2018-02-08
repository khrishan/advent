__author__ = 'Khrishan'
__title__ = '2015 - Day 04'
from hashlib import md5

with open('input/day04.txt', 'r') as my_file:
    puzzle_input = my_file.read()


def print_question():
    print('--- Day 4: The Ideal Stocking Stuffer ---\n\n'
          'Santa needs help mining some AdventCoins (very similar to bitcoins) to\n'
          'use as gifts for all the economically forward-thinking little girls and\n'
          'boys.\n\n'
          'To do this, he needs to find MD5 hashes which, in hexadecimal, start with\n'
          'at least five zeroes. The input to the MD5 hash is some secret key (your \n'
          'puzzle input, given below) followed by a number in decimal. To mine\n'
          'AdventCoins, you must find Santa the lowest positive number (no leading\n'
          'zeroes: 1, 2, 3, ...) that produces such a hash.\n\n'
          'For example:\n\n'
          '  - If your secret key is abcdef, the answer is 609043, because the MD5\n    hash of abcdef609043 starts '
          'with five zeroes (000001dbbfa...), and it\n    is the lowest such number to do so.\n'
          '  - If your secret key is pqrstuv, the lowest number it combines with to\n    make an MD5 hash starting '
          'with five zeroes is 1048970; that is, the\n    MD5 hash of pqrstuv1048970 looks like 000006136ef....\n\n'
          '--- Part Two —--\n\n'
          'Now find one that starts with six zeroes.\n')


def part_1():
    i = 1

    while True:
        m = md5()
        key = puzzle_input + str(i)
        m.update(key.encode('utf-8'))
        md5string = m.hexdigest()
        if md5string[0:5] == '00000':
            break
        else:
            i += 1

    print('Part 1 : {}'.format(i))


def part_2():
    i = 1

    while True:
        m = md5()
        key = puzzle_input + str(i)
        m.update(key.encode('utf-8'))
        md5string = m.hexdigest()
        if md5string[0:6] == '000000':
            break
        else:
            i += 1

    print('Part 2 : {}'.format(i))


print_question()
part_1()
part_2()
