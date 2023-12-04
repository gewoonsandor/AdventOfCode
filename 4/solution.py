import math
with open("input.txt", "r") as f:
    cards = f.readlines()

sum = 0

for card in cards:
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
    if correct > 0:
        sum += math.pow(2, (correct - 1))

print(sum)