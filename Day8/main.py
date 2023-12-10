import math
d = input()
l = len(d)

k = {'L':0,'R':1}

print(d)
input()

t = {}
while True:
    line = input()
    if line == "":
        break
    node,_,L,R = line.split(" ")
    L = L[1:-1]
    R = R[0:-1]

    t[node] = [L,R]

def part1():
    cur = "AAA"
    i = 0
    count = 0
    while cur != "ZZZ":
        cur = t[cur][k[d[i]]]
        i += 1
        if i >= l:
            i = 0
        count += 1
        
    return count

def find_smallest_common(visited_zs):
    cycles = []
    for i in range(len(visited_zs)):
        cycles.append(visited_zs[i][0][1])
    
    lcm = cycles[0]
    for i in range(1,len(cycles)):
        lcm = math.lcm(lcm,cycles[i])
    return lcm
        
def part2():
    cur = [n for n in t.keys() if n[2] == "A"]
    visited_zs = [[] for _ in cur]

    for i in range(len(cur)):    
        j = 0
        count = 1
        while True:
            cur[i] = t[cur[i]][k[d[j]]]
            if cur[i][2] == 'Z':
                if cur[i] in [n for (n,_) in visited_zs[i]]:
                    visited_zs[i].append((cur[i],count))
                    break
                else:
                    visited_zs[i].append((cur[i],count))
            j += 1
            if j >= l:
                j = 0
                
            count += 1

    print(visited_zs)
    sc = find_smallest_common(visited_zs)
    return sc     
        
# print(part1())
print(part2())