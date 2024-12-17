# read input file
with open("2024/day 2/input.txt", 'r') as f:
    inp = f.read()

# part 1
def part1():
    reports = []
    unsafe = []

    for line in inp.split("\n"):
        report = [*map(int, line.split(' '))]
        reports.append(report)

        sreport = sorted(report)

        if report == sreport or report == [*reversed(sreport)]:
            for i in range(len(report)-1):
                diff = abs(report[i] - report[i+1])

                if diff <= 0 or diff >= 4:
                    unsafe.append(report)
                    break
        else:
            unsafe.append(report)
    
    for i in unsafe:
        reports.remove(i)

    print(len(reports))