with open("./input.txt", "r") as f:
    games = f.readlines()

cardToNumber = {'A': 14, 'K': 13, 'Q': 12, 'J': float("-inf"), 'T': 10}
for i in range(2, 10):
    cardToNumber[str(i)] = i

outcomes = {"high": [], "one": [], "two": [], "three": [], "full": [], "four": [], "five": []}
bets = {}

for line in games:
    line.strip()
    game, bet = line.split(" ")
    bets[game] = int(bet)

def findScores(cards, cardscopy):
    card = {}
    while (len(cards) > 0):
        card[cards[0]] = cards.count(cards[0])
        cards = cards.replace(cards[0], '') 

    values = list(card.values())
    if max(values) == 5:
        outcomes["five"].append(cardscopy)
    elif max(values) == 4:
        outcomes["four"].append(cardscopy)
    elif max(values) == 3 and 2 in values:
        outcomes["full"].append(cardscopy)
    elif max(values) == 3:
        outcomes["three"].append(cardscopy)
    elif max(values) == 2 and values.count(2) > 1:
        outcomes["two"].append(cardscopy)
    elif max(values) == 2:
        outcomes["one"].append(cardscopy)
    elif max(values) == 1:
        outcomes["high"].append(cardscopy)

def replaceJoker(cards):
    if cards == "JJJJJ":
        return "AAAAA"
    copy = cards
    card = {}
    sortOrder = cardToNumber.copy() 
    sortOrder["J"] = float('inf')
    while (len(cards) > 0):
        card[cards[0]] = cards.count(cards[0])
        cards = cards.replace(cards[0], '') 
    
    if max(card.values()) != 2:
        return copy.replace('J', max(card, key=lambda x: card[x] if x != 'J' else float('-inf')))
    keys = [x for x in card.keys() if card[x] == 2]
    keys.sort(key=lambda x: sortOrder[x])
    if len(keys) == 1 and 'J' in keys:
        return copy.replace('J', max(card, key=lambda x: card[x] if x != 'J' else float('-inf')))
    return copy.replace('J', keys[0])

for cards in bets.keys():
    if 'J' in cards:
        card = replaceJoker(cards)
        findScores(card, cards)
    else:
        findScores(cards, cards)

for key in outcomes.keys():
    outcomes[key].sort(key=lambda x: ([cardToNumber[c] for c in x]))

print(outcomes)

i = 1
outcome = 0
for key in outcomes.keys():
    for card in outcomes[key]:
        outcome += i * bets[card]
        i += 1
print(outcome)