from itertools import combinations
import math

def _read_data(FILEPATH):
    with open(FILEPATH, 'r') as input_file:
        data = [int(i.strip()) for i in input_file.readlines()]
    
    return data

def _balance_calc(data, factor):
    i = 1
    while i < len(data) // 2:
        combs = list(map(list, combinations(data, i)))
        for group1 in combs:
            data_local = data.copy()
            for j in group1:
                data_local.remove(j)
            
            if sum(data_local) == factor*sum(group1):
                return math.prod(group1)

        i += 1

    return 0

def day01(data):
    return _balance_calc(data, 2)

def day02(data):
    return _balance_calc(data, 3)

if __name__ == '__main__':
    FILEPATH = 'input/day24.txt'
    data = _read_data(FILEPATH)

    print(f'Day 01 : {day01(data)}')
    print(f'Day 02 : {day02(data)}')
