import re

with open("2024/day 3/input.txt", 'r') as f:
    inp = f.read()



def part1():
    sum = 0

    multis = re.findall('mul\([0-9]+,[0-9]+\)', inp)

    for pair in multis:
        x, y = [int(n) for n in pair[4:-1].split(',')]
        sum += x * y
    
    print(sum)



def part2():
    enabled = True
    sum = 0

    multis = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", inp)

    for entry in multis:
        if not (entry == "don't()" or entry == "do()") and enabled:
            x, y = [int(n) for n in entry[4:-1].split(',')]
            sum += x * y
            
        elif entry == "don't()":
            enabled = False

        elif entry == "do()":
            enabled = True

    print(sum)


part1()
part2()