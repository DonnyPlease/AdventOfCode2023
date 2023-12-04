from collections import defaultdict
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
    return count

if __name__ == "__main__":
    cards = defaultdict(int) # This was added later, after the first successful submission
    line = input()
    i = 1
    while (line != ''):
        cards[i] += 1
        numbers = line.split(' ')[2:]
        result = get_points(numbers)
        for j in range(result):
            new_index = j+i+1
            cards[new_index] += cards[i] 
        i+=1
        line = input()
    print(sum(cards.values()))