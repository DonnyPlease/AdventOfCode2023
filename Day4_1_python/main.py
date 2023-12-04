def get_points(numbers):
    correct = set()
    i = 0
    while numbers[i] != '|':
        correct.add(numbers[i])  
        i += 1
    i += 1
    correct.discard('')
    count = 0
    while i < len(numbers):
        if (numbers[i] in correct):
            count += 1
        i += 1

    if count == 0:
        return 0

    result = 1
    for i in range(count-1):
        result *= 2
    return result 

if __name__ == "__main__":
    result = 0
    line = input()
    while line != '':
        numbers = line.split(' ')[2:]
        result += get_points(numbers)
        line = input()
        
    print(result)   