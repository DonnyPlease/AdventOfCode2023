def read_input():
    lines = []
    with open("Day11/input.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

def get_empty_rows(lines):
    return [i for i, line in enumerate(lines) if all([ch == '.' for ch in line])]

def get_empty_cols(lines):
    empty = []
    for i in range(len(lines[0])):
        em = True
        for j in range(len(lines)):
            if lines[j][i] == '#':
                em = False
                break
        if em:
            empty.append(i)
            
    # Alternative (more consise) solution from hyper-neutrino:        
    # empty = [i for i, col in enumerate(zip(*lines)) if all([ch == '.' for ch in col])]
    return empty
    
def get_galaxies(lines):
    return [(i,j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == '#']

def find_distances(lines, expansion):
    gs = get_galaxies(lines)
    empty_rows = get_empty_rows(lines)
    empty_cols = get_empty_cols(lines)
    
    distances = []
    for i in range(len(gs)):
        for j in range(i+1,len(gs)):
            d = abs(gs[i][0] - gs[j][0]) + abs(gs[i][1] - gs[j][1])
            for k in empty_rows:
                if gs[i][0] < k < gs[j][0] or gs[j][0] < k < gs[i][0]:
                    d += expansion-1
            for k in empty_cols:
                if gs[i][1] < k < gs[j][1] or gs[j][1] < k < gs[i][1]:
                    d += expansion-1
            distances.append(d)
    return distances

if __name__ == "__main__":
    lines = read_input()
    d1 = find_distances(lines, 2)
    d2 = find_distances(lines, 1000000)
    print("Part one result:  ", sum(d1))
    print("Part two result:  ", sum(d2))