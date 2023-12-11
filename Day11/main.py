def read_input():
    lines = []
    with open("Day11/input.txt", "r") as f:
        lines = f.readlines()

    # Remove trailing newline
    lines = [line.strip() for line in lines]
    return lines

def get_empty_rows(lines):
    empty = []
    for i, line in enumerate(lines):
        if line == '.'*len(line):
            empty.append(i)
    return empty

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
    return empty

    
def get_galaxies(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                galaxies.append((i,j))
    return galaxies

def find_distances(lines, expansion):
    galaxies = get_galaxies(lines)
    empty_rows = get_empty_rows(lines)
    empty_cols = get_empty_cols(lines)
    
    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            d = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            for k in empty_rows:
                if galaxies[i][0] < k < galaxies[j][0] or galaxies[j][0] < k < galaxies[i][0]:
                    d += expansion-1
            for k in empty_cols:
                if galaxies[i][1] < k < galaxies[j][1] or galaxies[j][1] < k < galaxies[i][1]:
                    d += expansion-1
            distances.append(d)
    return distances

if __name__ == "__main__":
    lines = read_input()
    d1 = find_distances(lines, 2)
    d2 = find_distances(lines, 1000000)
    print("Part one result:  ",sum(d1))
    print("Part two result:  ",sum(d2))