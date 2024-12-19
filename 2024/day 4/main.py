import re

with open("2024/day 4/input.txt", 'r') as f:
    inp = f.read()


def part1():
    total = 0
    rows = inp.splitlines()

    zipped = '\n'.join([''.join(a) for a in zip(*rows)])    # vertical version of the input
    backwards = [''.join(reversed(a)) for a in rows]        # flipped version of the input


    # list of L > R diagonals
    lrdiagonals = []
    for i in range(len(rows)-3):
        for j in range(len(rows[i])-3):
            lrdiagonals.append( ''.join([rows[i][j], rows[i+1][j+1], rows[i+2][j+2], rows[i+3][j+3]]) )

    # list of R > L diagonals
    rldiagonals = []
    for i in range(len(backwards)-3):
        for j in range(len(backwards[i])-3):
            rldiagonals.append( ''.join([backwards[i][j], backwards[i+1][j+1], backwards[i+2][j+2], backwards[i+3][j+3]]) )


    # sum up occurances of "XMAS" or "SAMX"
    total += len(re.findall('XMA(?=S)|SAM(?=X)', inp))
    total += len(re.findall('XMA(?=S)|SAM(?=X)', zipped))

    total += len(re.findall('XMA(?=S)|SAM(?=X)', ' '.join(lrdiagonals)))
    total += len(re.findall('XMA(?=S)|SAM(?=X)', ' '.join(rldiagonals)))
    
    print(total)

part1()