with open("./input.txt", "r") as f:
    games = f.readlines()

cardToNumber = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
for i in range(2, 10):
    cardToNumber[str(i)] = i

outcomes = {"high": [], "one": [], "two": [], "three": [], "full": [], "four": [], "five": []}
bets = {}

for line in games:
    line.strip()
    game, bet = line.split(" ")
    bets[game] = int(bet)

def findScores(cards):
    cardscopy = cards
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

for cards in bets.keys():
    findScores(cards)

for key in outcomes.keys():
    outcomes[key].sort(key=lambda x: [cardToNumber[c] for c in x])

i = 1
outcome = 0
for key in outcomes.keys():
    print(outcomes[key])
    for card in outcomes[key]:
        outcome += i * bets[card]
        i += 1
print(outcome)