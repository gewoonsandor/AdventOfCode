import math
with open("input.txt", "r") as f:
    cards = f.readlines()

correctnum = [0 for i in range(len(cards))]
copies = [1 for i in range(len(cards))]

for i, card in enumerate(cards):
    numbers = card.split(":")[1].strip()
    winning, normal = numbers.split("|")
    winning = winning.strip()
    normal = normal.strip()
    winning = [int(x) for x in winning.split(" ") if x != " " and x != ""]
    normal = [int(x) for x in normal.split(" ") if x != " " and x != ""]

    correct = 0
    for num in normal:
        if num in winning:
            correct += 1
    correctnum[i] = correct 

for i in range(len(cards)):
    for j in range(correctnum[i]):
        if i + j + 1 >= len(cards):
            continue
        copies[i + j + 1] += copies[i]

print(sum(copies))
