def part1(lines):
    pass

def part2(lines):
    pass

    

if __name__ == '__main__':
    INPUT_FILE = "input/test.txt"

    with open(INPUT_FILE) as f:
        lines = [x.strip() for x in f.readlines()]
    
    # Part 1
    print(part1(lines))

    # Part 2
    print(part2(lines))
