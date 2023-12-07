from collections import defaultdict

### For part 2 use these card values
# card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
#                '9':9,'T':10,'Q':1,'J':12,'K':13,'A':14}

card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
               '9':9,'T':10,'Q':12,'J':1,'K':13,'A':14}

# Decide game
def decide_game(game):
    cards = defaultdict(int)
    ### For part 2 uncomment the following lines
    # jokers = 0
    # for i in range(5):
    #     if game[i] == 'J':
    #         jokers += 1
    #         continue
    #     cards[game[i]] += 1
    # if jokers == 5:
    #     return 1
    
    # max_value = max(cards.values())
    # max_key = ''
    # max_keys = [key for (key,value) in cards.items() if value == max_value]
    # max_key = max(max_keys,key=lambda x: card_values[x])
            

    # for i in range(jokers):
    #     cards[max_key] += 1
        
    
    for (key,value) in cards.items():
        if value == 5:
            return 1
        if value == 4:
            return 2
        if value == 3:
            if 2 in cards.values():
                return 3
            return 4
    if list(cards.values()).count(2) == 2:
        return 5
    if list(cards.values()).count(2) == 1:
        return 6
    return 7

def compare_equal_games(game1,game2,g):
    for i in range(5):
        if card_values[game1[i]] > card_values[game2[i]]:
            return 1
        if card_values[game1[i]] < card_values[game2[i]]:
            return 2
    return 1

def compare_two_hands(game1,game2):
    g1 = decide_game(game1)
    g2 = decide_game(game2)
    if g1 < g2:
        return 1
    if g1 > g2:
        return 2
    if g1 == g2:
        return compare_equal_games(game1,game2,g1)        
 
def sort_games(games):
    for i in range(len(games)):
        for j in range(i+1,len(games)):
            if compare_two_hands(games[i],games[j]) == 2:
                games[i],games[j] = games[j],games[i] 
    return games

if __name__ == '__main__':
    games = []
    bets = {}
    line = input()
    while line != '':
        game,bet = line.split(' ')
        bets[game] = bet
        games.append(game)
        line = input()
       
    sorted_games = sort_games(games)
    
    earnings = 0
    n = len(sorted_games)
    for i,g in enumerate(sorted_games):
        print(g)
        earnings += (n-i)*int(bets[g])
        
    print(earnings)
    

    
