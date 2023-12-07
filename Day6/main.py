ts = [int(x) for x in input().split(' ')[1:] if x != '']
ds = [int(x) for x in input().split(' ')[1:] if x != '']
print(ts)
print(ds)

def ways_to_win(t, d):
    ways = 0
    for i in range(t):
        if i*(t-i) > d:
            ways += 1
    return ways

result = 1
for i in range(len(ts)):
    t = ts[i]
    ways_to_win = 0
    for j in range(t):
        if j*(t-j) > ds[i]:
             ways_to_win += 1
    result *= ways_to_win

print(result)    
