from itertools import pairwise
with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [[int(x) for x in line.strip().split(" ")] for line in lines]
lines = [list(reversed(x)) for x in lines]

def next_prediction(line):
    return [b - a for a, b in pairwise(line)]

output = 0

def check_predictions(predictions):
    for item in predictions:
        if item != 0: return False
    return True

for line in lines:
    preditcion = []
    preditcion.append(line)
    while(not check_predictions(preditcion[-1])):
        preditcion.append(next_prediction(preditcion[-1]))
    outcome = preditcion[-2][-1]
    preditcion = list(reversed(preditcion))
    preditcion.pop(0)
    preditcion.pop(0)
    for line in preditcion:
        outcome = line[-1] + outcome 
    output += outcome
print(output)