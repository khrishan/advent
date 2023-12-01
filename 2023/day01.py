# Keeping this here as a reminder
# The pain of this problem was that I didn't realize that we needed just to find numbers - not a string find and replace

# def _convert_words(line):
#     numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
#     count = 0
#     while True:
#         if count >= len(line):
#             break

#         test2 = list(set([x[0] for x in numbers]))

#         if line[count] in test2:
#             test = [len(x) for x in numbers if x[0] == line[count]]
#             for l in test:
#                 try:
#                     if line[count:count+l] in numbers:
#                         number = numbers.index(line[count:count+l]) + 1
#                         newline = line[:count] + str(number)
#                         try:
#                             line = newline + line[count+l:]
#                         except:
#                             pass
#                         break
#                 except IndexError:
#                     continue
        
#         count += 1

#     return line

DIGITS = "0123456789"
DIGITS_AS_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def _remove_letters(string):
    return ''.join([x for x in string if x not in 'abcdefghijklmnopqrstuvwxyz'])


def _clean_input_part_one(line):
    line = _remove_letters(line)

    return int(f'{line[0]}{line[-1]}')

def _clean_input_part_two(line):
    s2 = []
    for i, c in enumerate(line):
        if c in DIGITS:
            s2.append(int(c))
        for index, digit in enumerate(DIGITS_AS_WORDS):
            if line[i:].startswith(digit):
                s2.append(index)
                break
    return int(f"{s2[0]}{s2[-1]}")



def part1(lines):
    return sum([_clean_input_part_one(line) for line in lines])

def part2(lines):
    return sum([_clean_input_part_two(line) for line in lines])

    

if __name__ == '__main__':
    INPUT_FILE = "input/day01.txt"

    with open(INPUT_FILE) as f:
        lines = [x.strip() for x in f.readlines()]
    
    # Part 1
    print(part1(lines))

    # Part 2
    print(part2(lines))
