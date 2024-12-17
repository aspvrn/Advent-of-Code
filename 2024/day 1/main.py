# read input file
with open("2024/day 1/input.txt", 'r') as f:
    inp = f.read()


# part 1 
def part1():

    l = []
    r = []

    distance = 0

    for line in inp.split('\n'):
        nums = line.split("   ")
        
        l.append(int(nums[0]))
        r.append(int(nums[1]))
    
    l.sort()
    r.sort()

    for i in range(len(l)):
        distance += abs(l[i] - r[i])
    
    print(distance)


# part 2 
def part2():
    rcount = {}
    llist = []
    score = 0

    for line in inp.split("\n"):
        l, r = line.split("   ")

        llist.append(int(l))

        try:
            rcount[int(r)] += 1
        except:
            rcount[int(r)] = 1
    
    for num in llist:
        try:
            score += num * rcount[num]
        except: pass

    print(score)


part1()
part2()