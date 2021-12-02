"""
Advent of Code 2021: Day 01: Sonar Sweep
https://adventofcode.com/2021/day/1
"""


def _read_data(filepath):
    with open(filepath, "r") as input_file:
        data = [int(i.replace("\n", "")) for i in input_file.readlines()]

    return data


def day01(data):
    increase_count = 0
    prev_num = data[0]
    for i in range(1, len(data)):
        if data[i] - prev_num > 0:
            increase_count += 1
        prev_num = data[i]

    return increase_count


def day02(data):
    increase_count = 0
    prev_count = data[0] + data[1] + data[2]
    for i in range(1, len(data) - 2):
        new_count = data[i] + data[i + 1] + data[i + 2]
        if new_count - prev_count > 0:
            increase_count += 1
        prev_count = new_count

    return increase_count


if __name__ == "__main__":
    FILEPATH = "inputs/day01.txt"
    data = _read_data(FILEPATH)

    print(f"Part 1 : {day01(data)}")  # 1451
    print(f"Part 2 : {day02(data)}")  # 1395
