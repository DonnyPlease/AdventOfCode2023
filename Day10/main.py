pipes = {'|': {1:1,3:3}, 
         '-': {2:2,0:0}, 
         'J': {0:1,3:2},
         'L': {3:0,2:1},
         '7': {0:3,1:2},
         'F': {2:3,1:0}
         }
         

lines = []
line = input()
while line != '':
    lines.append(line)
    line = input()
    
def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                return i, j

def move(d,i,j):
    if d == 0:
        return i,j+1
    elif d == 1:
        return i-1,j
    elif d == 2:
        return i,j-1
    else:
        return i+1,j

def find_start_direction(lines,s_i,s_j):
    if lines[s_i][s_j+1] in ('-', 'J', '7'):
        return 0
    if lines[s_i-1][s_j] in ('|', 'F', '7'):
        return 1
    if lines[s_i][s_j-1] in ('-', 'L', 'F'):
        return 2
    if lines[s_i+1][s_j] in ('|', 'J', 'L'):
        return 3
    

def find_loop(lines,s_i,s_j):
    d = find_start_direction(lines,s_i,s_j)
    i,j = s_i,s_j
    loop = []
    length = 0
    while True:
        loop.append((i,j))
        i,j = move(d,i,j)
        length += 1
        if lines[i][j] == 'S':
            break 
        d = pipes[lines[i][j]][d]
    print("Part one result:  ",length//2)
    return loop
    
def is_enclosed(i,j,lines,loop):
    # Check above
    fromLeft = False
    fromRight = False
    cross = 0
    for k in range(i-1,-1,-1):
        if (k,j) in loop:
            if not fromLeft and not fromRight:
                if lines[k][j] == '-':
                    cross += 1
                    continue
                if lines[k][j] == 'J':
                    fromLeft = True
                    continue
                if lines[k][j] == 'L':
                    fromRight = True
                    continue
            if fromLeft:
                if lines[k][j] == 'F':
                    cross += 1
                    fromLeft = False
                    continue
                if lines[k][j] == '7':
                    fromLeft = False
                    continue
            if fromRight:
                if lines[k][j] == 'F':
                    fromRight = False
                    continue
                if lines[k][j] == '7':
                    cross += 1
                    fromRight = False
                    continue
                 
    if cross % 2 == 0:
        return False
    
    # # Check below
    # fromLeft = False
    # fromRight = False
    # cross = 0
    # for k in range(i+1,len(lines)):
    #     if (k,j) in loop:
    #         if not fromLeft and not fromRight:
    #             if lines[k][j] == '-':
    #                 cross += 1
    #                 continue
    #             if lines[k][j] == '7':
    #                 fromLeft = True
    #                 continue
    #             if lines[k][j] == 'F':
    #                 fromRight = True
    #                 continue
    #         if fromLeft:
    #             if lines[k][j] == 'L':
    #                 cross += 1
    #                 fromLeft = False
    #                 continue
    #             if lines[k][j] == 'J':
    #                 fromLeft = False
    #                 continue
    #         if fromRight:
    #             if lines[k][j] == 'L':
    #                 fromRight = False
    #                 continue
    #             if lines[k][j] == 'J':
    #                 cross += 1
    #                 fromRight = False
    #                 continue
                 
    # if cross % 2 == 0:
    #     return False

    # # Check left
    # fromUp = False
    # fromDown = False
    # cross = 0
    # for k in range(j-1,-1,-1):
    #     if (i,k) in loop:
    #         if not fromUp and not fromDown:
    #             if lines[i][k] == '|':
    #                 cross += 1
    #                 continue
    #             if lines[i][k] == '7':
    #                 fromDown = True
    #                 continue
    #             if lines[i][k] == 'J':
    #                 fromUp = True
    #                 continue
    #         if fromUp:
    #             if lines[i][k] == 'F':
    #                 cross += 1
    #                 fromUp = False
    #                 continue
    #             if lines[i][k] == 'L':
    #                 fromUp = False
    #                 continue
    #         if fromDown:
    #             if lines[i][k] == 'F':
    #                 fromDown = False
    #                 continue
    #             if lines[i][k] == 'L':
    #                 cross += 1
    #                 fromDown = False
    #                 continue
    
    # if cross % 2 == 0:
    #     return False
    
    # # Check right
    # fromUp = False
    # fromDown = False
    # cross = 0
    # for k in range(j+1,len(lines[i])):
    #     if (i,k) in loop:
    #         if not fromUp and not fromDown:
    #             if lines[i][k] == '|':
    #                 cross += 1
    #                 continue
    #             if lines[i][k] == 'F':
    #                 fromDown = True
    #                 continue
    #             if lines[i][k] == 'L':
    #                 fromUp = True
    #                 continue
    #         if fromUp:
    #             if lines[i][k] == 'J':
    #                 fromUp = False
    #                 continue
    #             if lines[i][k] == '7':
    #                 cross += 1
    #                 fromUp = False
    #                 continue
    #         if fromDown:
    #             if lines[i][k] == 'J':
    #                 fromDown = False
    #                 cross += 1
    #                 continue
    #             if lines[i][k] == '7':
    #                 fromDown = False
    #                 continue
    # if cross % 2 == 0:
    #     return False
    
    return True

def find_start_symbol(lines,si,sj):
    dirs = []
    if lines[si][sj+1] in ('-', 'J', '7'):
        dirs.append(0)
    if lines[si-1][sj] in ('|', 'F', '7'):
        dirs.append(1)
    if lines[si][sj-1] in ('-', 'L', 'F'):
        dirs.append(2)
    if lines[si+1][sj] in ('|', 'J', 'L'):
        dirs.append(3)
    if dirs == [0,1]:
        return 'L'
    if dirs == [1,2]:
        return 'J'
    if dirs == [2,3]:
        return '7'
    if dirs == [0,3]:
        return 'F'
    if dirs == [0,2]:
        return '-'
    if dirs == [1,3]:
        return '|'
    
    
def count_enclosed(loop,lines):
    si,sj = find_start(lines)
    start_replace = find_start_symbol(lines,si,sj)
    lines[si] = lines[si][:sj] + start_replace + lines[si][sj+1:]
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i,j) in loop:
                continue
            if is_enclosed(i,j,lines,loop):
                count += 1
                # print(i,j)
    return count
        
if __name__ == '__main__':
    s_i, s_j = find_start(lines)
    loop = find_loop(lines,s_i,s_j) # Part one
    en = count_enclosed(loop,lines) # Part two
    print("Part two result:", en)
    