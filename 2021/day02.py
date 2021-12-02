"""
Advent of Code 2021: Day 02: Dive!
https://adventofcode.com/2021/day/2
"""

def _read_data(filepath):
    with open(filepath, "r") as input_file:
        data = [i.strip() for i in input_file.readlines()]
        data = [d.split(' ') for d in data]

    return data


def day01(data):
    x = 0
    y = 0
    for instruction in data:
        match instruction[0]:
            case 'forward':
                x += int(instruction[1])
            case 'up':
                y -= int(instruction[1])
            case 'down':
                y += int(instruction[1])
            case _:
                continue

    return x * y


def day02(data):
    x = 0
    y = 0
    aim = 0
    for instruction in data:
        match instruction[0]:
            case 'forward':
                x += int(instruction[1])
                y += aim * int(instruction[1])
            case 'up':
                aim -= int(instruction[1])
            case 'down':
                aim += int(instruction[1])
            case _:
                continue

    return x * y


if __name__ == "__main__":
    FILEPATH = "inputs/day02.txt"
    data = _read_data(FILEPATH)

    print(f"Part 1 : {day01(data)}")    # 1524750
    print(f"Part 2 : {day02(data)}")    # 1592426537
