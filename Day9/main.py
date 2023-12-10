import numpy as np
new_elements = []
old_elements = []
line = input()
while line != '':
    numbers = np.array([int(x) for x in line.split(' ')])
    sequences = [numbers]
    while True:
        new_sequence = sequences[-1][1:] - sequences[-1][:-1]
        sequences.append(new_sequence)
        if all(new_sequence == 0):
            break

    l = len(sequences)
    new_element = 0
    for i in range(l-1):
        new_element = sequences[l-i-1][-1] + sequences[l-i-2][-1]
        sequences[l-i-2] = np.append(sequences[l-i-2], new_element)
        
    new_elements.append(new_element)
    
    old_element = 0
    for i in range(l-1):
        old_element = sequences[l-i-2][0] - sequences[l-i-1][0]
        sequences[l-i-2] = np.insert(sequences[l-i-2], 0, old_element)
        
    old_elements.append(old_element)        
    line = input()

print(sum(new_elements))
print(sum(old_elements))