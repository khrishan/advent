"""
Advent of Code 2021: Day 03: Binary Diagnostic
https://adventofcode.com/2021/day/3
"""

from collections import Counter

def _read_data(filepath):
    with open(filepath, "r") as input_file:
        data = [i.strip() for i in input_file.readlines()]

    return data

def _counts(data, index):
    chars = [item[index] for item in data]
    counts = dict(Counter(chars))
    return counts

def day01(data):
    bin_len = len(data[0])

    gamma = ''
    epsilon = ''

    for i in range(bin_len):
        counts = _counts(data, i)
        gamma += max(counts, key=counts.get)
        epsilon += min(counts, key=counts.get)
    
    return int(gamma, 2) * int(epsilon, 2)

def day02(data):
    oxygen = data.copy()
    co2 = data.copy()

    bin_len = len(data[0])

    for i in range(bin_len):
        if isinstance(oxygen, list):
            counts_ox = _counts(oxygen, i)
            if counts_ox['0'] == counts_ox['1']:
                max_value = '1'
            else:
                max_value = max(counts_ox, key=counts_ox.get)
            for item in oxygen.copy():
                if item[i] != max_value:
                    oxygen.remove(item)
        if isinstance(co2, list):
            counts_co2 = _counts(co2, i)
            if counts_co2['0'] == counts_co2['1']:
                min_value = '0'
            else:
                min_value = min(counts_co2, key=counts_co2.get)
            for item in co2.copy():
                if item[i] != min_value:
                    co2.remove(item)

        if isinstance(oxygen, list) and len(oxygen) == 1:
            oxygen = oxygen[0]
        if isinstance(co2, list) and len(co2) == 1:
            co2 = co2[0]

    return int(oxygen, 2) * int(co2, 2)



if __name__ == "__main__":
    FILEPATH = "inputs/day03.txt"
    data = _read_data(FILEPATH)

    print(f"Part 1 : {day01(data)}")    # 2498354
    print(f"Part 2 : {day02(data)}")    # 3277956
