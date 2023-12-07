rt = int(input().split(':')[1].replace(' ',''))
rd = int(input().split(':')[1].replace(' ',''))
print(rt)
print(rd)

t=0
start = 0
end = 0

while True:
    if t*(rt-t) > rd:
        break
    t += 1
start = t
t= rt
while True:
    if t*(rt-t) > rd:
        break
    t -= 1
end = t

print(end-start+1)
