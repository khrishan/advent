import os
from pathlib import Path


def _read_data():
    filename = Path(os.path.basename(__file__))
    filename = filename.with_suffix('.txt')

    with open(f"input/{filename}", 'r') as input_file:
        input_file = [x.strip() for x in input_file.readlines()]

    return input_file


def part01():
    pass


def part02():
    pass


if __name__ == "__main__":
    data = _read_data()
    print(part01(data))
    print(part02(data))
