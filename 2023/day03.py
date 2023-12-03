def _get_grid_shape(lines):
    y = len(lines)
    x = len(lines[0]) # assuming a rectangular grid

    return (x, y)

def _check_adjacent(coords, lines):
    x_max, y_max = _get_grid_shape(lines)

    transformations = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for y, x in coords:
        for y_transform, x_transform in transformations:
            new_y = y + y_transform
            new_x = x + x_transform

            if new_y < 0 or new_y > y_max - 1:
                continue
            if new_x < 0 or new_x > x_max - 1:
                continue

            if lines[new_y][new_x] != '.' and lines[new_y][new_x] not in '0123456789':
                return True
    
    return False

    
def part1(lines):
    count = 0

    for y, line in enumerate(lines):
        number = ''
        coords = []
        for x, char in enumerate(line):
            if char in '0123456789':
                number += char
                coords.append((y, x))

            if char not in '0123456789' or x == len(line) - 1:
                if number == '':
                    continue
                # check around the number co-ords, if symbol, then add to count
                if _check_adjacent(coords, lines):
                    count += int(number)
                number = ''
                coords = []
                continue
    
    return count

def _find_number(x, line):
    number = line[x]
    # Go left
    new_x = x
    while x > 0:
        new_x -= 1
        if new_x < 0 or line[new_x] not in '0123456789':
            break
        number = f"{line[new_x]}{number}"

    # Go right
    new_x = x
    while x < len(line):
        new_x += 1
        if new_x > len(line)-1 or line[new_x] not in '0123456789':
            break
        number += line[new_x]
    
    return number

def _check_gear(coords, lines):
    x_max, y_max = _get_grid_shape(lines)

    transformations = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    numbers = set()

    for y_transform, x_transform in transformations:
        new_y = coords[0] + y_transform
        new_x = coords[1] + x_transform

        if new_y < 0 or new_y > y_max - 1:
            continue
        if new_x < 0 or new_x > x_max - 1:
            continue

        if lines[new_y][new_x] in '0123456789':
            number = _find_number(new_x, lines[new_y])
            numbers.add(int(number))

    print(numbers)

    if len(numbers) == 2:
        return numbers.pop() * numbers.pop()

    return None


def part2(lines):
    # Look for the *
    # Then look around it for the numbers
    # If two numbers, then multiply together
    total = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '*':
                gear_ratio = _check_gear((y, x), lines)
                if gear_ratio is not None:
                    total += gear_ratio
    
    return total

    

if __name__ == '__main__':
    INPUT_FILE = "input/day03.txt"

    with open(INPUT_FILE) as f:
        lines = [x.strip() for x in f.readlines()]
    
    # Part 1
    print(part1(lines))

    # Part 2
    print(part2(lines))
    # 9370460 too low
    # 86619648 too low
    # 87605697 - exact!

# from collections import defaultdict
# from math import prod
# from re import finditer

# parts = defaultdict(list)
# board = list(open('input/day03.txt'))
# chars = {(r, c) for r in range(140)
#                 for c in range(140)
#                 if board[r][c] not in '01234566789.'}

# for r, row in enumerate(board):
#     for m in finditer(r'\d+', row):
#         nexts = {(r+s, c+d) for s in (-1, 0, 1) 
#                             for d in (-1, 0, 1)
#                             for c in range(*m.span())}
#         for c in nexts & chars:
#             parts[c].append(int(m[0]))

# print(sum(sum(p)  for p in parts.values()),
#       sum(prod(p) for p in parts.values() if len(p)==2))