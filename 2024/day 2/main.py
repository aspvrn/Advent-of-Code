import numpy as np

# read input file
with open("2024/day 2/input.txt", 'r') as f:
    inp = f.read()

reports = np.array([[*map(int, line.split(" "))] for line in inp.splitlines()], object)



# part 1 (refactored)

def safeCheck(report):
    if len(report) <= 1:
        return 1
    
    diffs = np.diff(report)
    isGradual = (np.all(diffs >= 1) and np.all(diffs <= 3)) or (np.all(diffs <= -1) and np.all(diffs >= -3))

    if isGradual:
        return 1
    else:
        return 0



# part 2 (with numpy)

def safteyDampener(report):
    if safeCheck(report) == 0:
        for level in range(len(report)):
            if safeCheck(np.delete(report, [level])):
                return 1
            
        return 0
    
    return safeCheck(report)



print(np.sum([safeCheck(report) for report in reports]))
print(np.sum([safteyDampener(report) for report in reports]))