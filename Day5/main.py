def seed_map(seeds, mapped, dr, sr, l):
    for i,seed in enumerate(seeds):
        if sr <= seed <= sr+l and not mapped[i]:
            seeds[i] += dr-sr
            mapped[i] = True
           
def seed_range_map(seed_ranges, mapped, dr, sr, l):
    for i,(s,e) in enumerate(seed_ranges):
        # Seed range is completely inside the map
        if sr <= s and s+e <= sr+l and not mapped[i]:
            seed_ranges[i] = (s+dr-sr, e)
            mapped[i] = True
        # Map is completely inside the seed range
        elif sr <= s < sr+l and s+e >= sr+l and not mapped[i]:
            seed_ranges[i] = (s+dr-sr, sr+l-s)
            mapped[i] = True
            seed_ranges.append((sr+l, e-(sr+l-s)))
            mapped.append(False)
        # Seed range overlaps start of the map
        elif s < sr < s+e <= sr+l and not mapped[i]:
            seed_ranges.append((s, sr-s))
            mapped.append(False)
            seed_ranges[i] = (dr, e-(sr-s))
            mapped[i] = True
        # Seed range overlaps end of the map
        elif s < sr < sr+l < s+e and not mapped[i]:
            seed_ranges.append((s, sr-s))
            mapped.append(False)
            seed_ranges.append((sr+l, s+e-(sr+l)))
            mapped.append(False)
            seed_ranges[i] = (dr, l)
            mapped[i] = True
           
if __name__ == "__main__": 
    # Read seeds
    seeds = [int(x) for x in input().split(' ')[1:]]
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0,len(seeds)-1,2)]
    input()
    # Read every map and map the previous result to it
    for i in range(7):
        input()
        mapped = [False for _ in seeds]
        ranges_mapped = [False for _ in seed_ranges]
        while True:
            line = input()
            if line == '':
                break
            dr, sr, l = (int(x) for x in line.split(' '))
            seed_map(seeds, mapped, dr, sr, l)
            seed_range_map(seed_ranges, ranges_mapped, dr, sr, l)
            
    # Print the results 
    print(min(seeds))
    print(min([s for (s,_) in seed_ranges]))